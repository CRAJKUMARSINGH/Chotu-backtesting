#!/usr/bin/env python3
"""
Streamlit Web Application for Backtesting.py
============================================

A comprehensive web interface for the backtesting.py library.
This app can be deployed to Vercel or Streamlit Cloud.

Based on: https://github.com/kernc/backtesting.py
"""

import streamlit as st
import pandas as pd
try:
    import plotly.graph_objects as go
    import plotly.express as px
    from plotly.subplots import make_subplots
except Exception as e:
    st.error("Plotly is required but not installed. Please install 'plotly' and restart the app.")
    st.stop()
import sys
import os
import numpy as np
from datetime import datetime
import gc
import psutil

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from backtesting import Backtest, Strategy
    from backtesting.lib import crossover
    from backtesting.test import SMA, GOOG, BTCUSD, EURUSD
except ImportError as e:
    st.error(f"Error importing backtesting module: {e}")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="Backtesting.py Demo",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .strategy-info {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #1f77b4;
    }
    .performance-info {
        background-color: #fff3cd;
        padding: 0.5rem;
        border-radius: 0.25rem;
        border: 1px solid #ffeaa7;
        font-size: 0.8rem;
        color: #856404;
    }
</style>
""", unsafe_allow_html=True)

# Memory optimization function
@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_dataset_info():
    """Get dataset information with caching"""
    return {
        "Google (GOOG) - 2004-2013": {"data": GOOG, "points": len(GOOG)},
        "Bitcoin (BTCUSD) - 2012-2024": {"data": BTCUSD, "points": len(BTCUSD)},
        "EUR/USD - 2017-2018": {"data": EURUSD, "points": len(EURUSD)}
    }

@st.cache_data(ttl=1800)  # Cache for 30 minutes
def run_backtest_cached(data, strategy_class, **params):
    """Run backtest with caching for performance"""
    try:
        bt = Backtest(data, strategy_class, **params)
        stats = bt.run()
        return stats
    except Exception as e:
        st.error(f"Backtest error: {e}")
        return None

@st.cache_data(ttl=900)  # Cache for 15 minutes
def create_charts_cached(equity_curve, trades):
    """Create charts with caching"""
    try:
        # Create subplots
        fig = make_subplots(
            rows=3, cols=1,
            subplot_titles=('Equity Curve', 'Drawdown', 'Trade Returns Distribution'),
            vertical_spacing=0.1,
            specs=[[{"secondary_y": False}],
                   [{"secondary_y": False}],
                   [{"secondary_y": False}]]
        )
        
        # Equity curve
        fig.add_trace(
            go.Scatter(
                x=equity_curve.index,
                y=equity_curve['Equity'],
                name='Strategy',
                line=dict(color='blue', width=2)
            ),
            row=1, col=1
        )
        
        # Drawdown
        drawdown = equity_curve['DrawdownPct']
        fig.add_trace(
            go.Scatter(
                x=equity_curve.index,
                y=drawdown,
                name='Drawdown',
                fill='tonexty',
                line=dict(color='red', width=1)
            ),
            row=2, col=1
        )
        
        # Trade returns histogram
        if len(trades) > 0:
            returns = trades['ReturnPct'].dropna()
            if len(returns) > 0:
                fig.add_trace(
                    go.Histogram(
                        x=returns,
                        name='Trade Returns',
                        nbinsx=20,
                        marker_color='green',
                        opacity=0.7
                    ),
                    row=3, col=1
                )
        
        # Update layout
        fig.update_layout(
            height=800,
            showlegend=True,
            title_text="Backtest Results",
            title_x=0.5
        )
        
        return fig
    except Exception as e:
        st.error(f"Chart creation error: {e}")
        return None

def optimize_memory():
    """Optimize memory usage"""
    gc.collect()
    if hasattr(psutil, 'Process'):
        process = psutil.Process()
        memory_info = process.memory_info()
        memory_mb = memory_info.rss / 1024 / 1024
        return memory_mb
    return None

# Header
st.markdown('<h1 class="main-header">🚀 Backtesting.py Web Demo</h1>', unsafe_allow_html=True)

# Performance monitoring
memory_usage = optimize_memory()
if memory_usage:
    st.sidebar.markdown(f"""
    <div class="performance-info">
    💾 Memory Usage: {memory_usage:.1f} MB
    </div>
    """, unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.title("⚙️ Configuration")

# Strategy selection
strategy_type = st.sidebar.selectbox(
    "Select Strategy",
    ["SMA Crossover", "Custom Strategy"],
    help="Choose the trading strategy to backtest"
)

# Dataset selection with caching
dataset_info = get_dataset_info()
selected_dataset = st.sidebar.selectbox(
    "Select Dataset",
    list(dataset_info.keys()),
    help="Choose the financial data to backtest on"
)

data = dataset_info[selected_dataset]["data"]
data_points = dataset_info[selected_dataset]["points"]

# Display dataset info
st.sidebar.markdown(f"📊 **Data Points:** {data_points:,}")

# Strategy parameters
st.sidebar.subheader("📊 Strategy Parameters")

if strategy_type == "SMA Crossover":
    fast_sma = st.sidebar.slider("Fast SMA Period", 5, 50, 10, help="Period for fast moving average")
    slow_sma = st.sidebar.slider("Slow SMA Period", 10, 100, 20, help="Period for slow moving average")
    
    # Ensure fast_sma < slow_sma
    if fast_sma >= slow_sma:
        st.sidebar.warning("⚠️ Fast SMA should be less than Slow SMA")
        slow_sma = fast_sma + 10
    
    # SMA Crossover Strategy
    class SmaCross(Strategy):
        def init(self):
            price = self.data.Close
            self.ma1 = self.I(SMA, price, fast_sma)
            self.ma2 = self.I(SMA, price, slow_sma)
        
        def next(self):
            if crossover(self.ma1, self.ma2):
                self.buy()
            elif crossover(self.ma2, self.ma1):
                self.sell()
    
    strategy_class = SmaCross

# Backtest parameters
st.sidebar.subheader("💰 Backtest Parameters")
commission = st.sidebar.slider("Commission (%)", 0.0, 2.0, 0.2, 0.1, help="Trading commission as percentage")
cash = st.sidebar.number_input("Initial Cash ($)", 1000, 100000, 10000, 1000, help="Starting capital")

# Run backtest button
if st.sidebar.button("🚀 Run Backtest", type="primary"):
    with st.spinner("Running backtest..."):
        # Run backtest with caching
        stats = run_backtest_cached(
            data, 
            strategy_class, 
            commission=commission/100, 
            cash=cash,
            exclusive_orders=True
        )
        
        if stats is not None:
            # Store results in session state for caching
            st.session_state['backtest_stats'] = stats
            st.session_state['backtest_data'] = data
            st.session_state['backtest_params'] = {
                'fast_sma': fast_sma if strategy_type == "SMA Crossover" else None,
                'slow_sma': slow_sma if strategy_type == "SMA Crossover" else None,
                'commission': commission,
                'cash': cash
            }
            st.success("✅ Backtest completed successfully!")

# Display results if available
if 'backtest_stats' in st.session_state:
    stats = st.session_state['backtest_stats']
    
    # Create tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Summary", "📈 Performance", "💰 Trades", "📋 Details"])
    
    with tab1:
        st.subheader("📊 Performance Summary")
        
        # Key metrics in columns
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Return", f"{stats['Return [%]']:.2f}%")
        
        with col2:
            st.metric("Sharpe Ratio", f"{stats['Sharpe Ratio']:.2f}")
        
        with col3:
            st.metric("Max Drawdown", f"{stats['Max. Drawdown [%]']:.2f}%")
        
        with col4:
            st.metric("Number of Trades", f"{stats['# Trades']}")
        
        # Additional metrics
        col5, col6, col7, col8 = st.columns(4)
        
        with col5:
            st.metric("Win Rate", f"{stats['Win Rate [%]']:.1f}%")
        
        with col6:
            st.metric("Avg Trade Duration", f"{stats['Avg. Trade Duration']}")
        
        with col7:
            st.metric("Best Trade", f"{stats['Best Trade [%]']:.2f}%")
        
        with col8:
            st.metric("Worst Trade", f"{stats['Worst Trade [%]']:.2f}%")
    
    with tab2:
        st.subheader("📈 Performance Charts")
        
        # Get data for charts
        equity_curve = stats['_equity_curve']
        trades = stats['_trades']
        
        # Create charts with caching
        fig = create_charts_cached(equity_curve, trades)
        
        if fig:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Failed to create charts")
    
    with tab3:
        st.subheader("💰 Trade Analysis")
        
        trades = stats['_trades']
        
        if len(trades) > 0:
            # Trade distribution
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Trade Returns Distribution")
                returns = trades['ReturnPct'].dropna()
                if len(returns) > 0:
                    fig = px.histogram(
                        returns, 
                        nbins=20,
                        title="Distribution of Trade Returns",
                        labels={'value': 'Return (%)', 'count': 'Number of Trades'}
                    )
                    st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.subheader("Trade Duration Analysis")
                durations = trades['Duration'].dropna()
                if len(durations) > 0:
                    fig = px.histogram(
                        durations,
                        nbins=15,
                        title="Distribution of Trade Durations",
                        labels={'value': 'Duration', 'count': 'Number of Trades'}
                    )
                    st.plotly_chart(fig, use_container_width=True)
            
            # Recent trades table
            st.subheader("📋 Recent Trades")
            display_trades = trades.tail(10)[['EntryTime', 'ExitTime', 'Size', 'PnL', 'ReturnPct']]
            st.dataframe(display_trades, use_container_width=True)
        else:
            st.info("No trades were executed during the backtest period.")
    
    with tab4:
        st.subheader("📋 Detailed Statistics")
        
        # Convert stats to DataFrame for better display
        stats_df = pd.DataFrame(list(stats.items()), columns=['Metric', 'Value'])
        st.dataframe(stats_df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p>🚀 Powered by <a href="https://github.com/kernc/backtesting.py" target="_blank">backtesting.py</a> | 
    📊 Built with <a href="https://streamlit.io" target="_blank">Streamlit</a></p>
</div>
""", unsafe_allow_html=True)

# Memory cleanup at the end
optimize_memory()
