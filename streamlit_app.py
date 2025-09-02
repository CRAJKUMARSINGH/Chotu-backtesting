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
    _plotly_available = True
except Exception as _plotly_error:
    _plotly_available = False
    go = None
    px = None
    make_subplots = None
import sys
import os
import numpy as np
from datetime import datetime

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
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🚀 Backtesting.py Web Demo</h1>', unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.title("⚙️ Configuration")

# Strategy selection
strategy_type = st.sidebar.selectbox(
    "Select Strategy",
    ["SMA Crossover", "Custom Strategy"],
    help="Choose the trading strategy to backtest"
)

# Dataset selection
dataset_options = {
    "Google (GOOG) - 2004-2013": GOOG,
    "Bitcoin (BTCUSD) - 2012-2024": BTCUSD,
    "EUR/USD - 2017-2018": EURUSD
}

selected_dataset = st.sidebar.selectbox(
    "Select Dataset",
    list(dataset_options.keys()),
    help="Choose the financial data to backtest on"
)

@st.cache_data(show_spinner=False)
def _get_dataset(name):
    return dataset_options[name]

@st.cache_data(show_spinner=False)
def _compute_backtest_stats(dataset_key, fast_period, slow_period, commission_pct, starting_cash):
    # Define a local Strategy class bound to parameters for caching correctness
    class _SmaCross(Strategy):
        def init(self):
            price = self.data.Close
            self.ma1 = self.I(SMA, price, fast_period)
            self.ma2 = self.I(SMA, price, slow_period)
        def next(self):
            if crossover(self.ma1, self.ma2):
                self.buy()
            elif crossover(self.ma2, self.ma1):
                self.sell()

    dataset_df = dataset_options[dataset_key]
    bt = Backtest(
        dataset_df,
        _SmaCross,
        commission=commission_pct/100,
        cash=starting_cash,
        exclusive_orders=True,
        finalize_trades=True,
    )
    return bt.run()

data = _get_dataset(selected_dataset)

# Strategy parameters
st.sidebar.subheader("📊 Strategy Parameters")

if strategy_type == "SMA Crossover":
    fast_sma = st.sidebar.slider("Fast SMA Period", 5, 50, 10, help="Period for fast moving average")
    slow_sma = st.sidebar.slider("Slow SMA Period", 10, 100, 20, help="Period for slow moving average")
    
    # Ensure fast SMA is less than slow SMA
    if fast_sma >= slow_sma:
        st.sidebar.warning("⚠️ Fast SMA should be less than Slow SMA")
        slow_sma = fast_sma + 10

# Backtest parameters
st.sidebar.subheader("💰 Trading Parameters")
commission = st.sidebar.slider("Commission (%)", 0.0, 2.0, 0.2, 0.1, help="Commission per trade as percentage")
initial_cash = st.sidebar.number_input("Initial Cash ($)", 1000, 100000, 10000, 1000, help="Starting capital")

# Strategy class
class SmaCross(Strategy):
    """Simple Moving Average Crossover Strategy"""
    
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, fast_sma)  # Fast SMA
        self.ma2 = self.I(SMA, price, slow_sma)  # Slow SMA
    
    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📈 Strategy Overview")
    
    if strategy_type == "SMA Crossover":
        st.markdown("""
        **Simple Moving Average (SMA) Crossover Strategy**
        
        This is a classic trend-following strategy that:
        - **Buys** when the fast SMA crosses above the slow SMA
        - **Sells** when the fast SMA crosses below the slow SMA
        - Works best in trending markets
        """)

with col2:
    st.subheader("📊 Dataset Info")
    st.write(f"**Symbol:** {selected_dataset.split(' - ')[0]}")
    st.write(f"**Period:** {selected_dataset.split(' - ')[1]}")
    st.write(f"**Data Points:** {len(data):,}")
    st.write(f"**Date Range:** {data.index[0].strftime('%Y-%m-%d')} to {data.index[-1].strftime('%Y-%m-%d')}")

# Run backtest button
if st.button("🚀 Run Backtest", type="primary", use_container_width=True):
    with st.spinner("Running backtest..."):
        try:
            # Create and run backtest (cached)
            stats = _compute_backtest_stats(
                selected_dataset,
                fast_sma,
                slow_sma,
                commission,
                initial_cash,
            )
            
            # Display results
            st.success("✅ Backtest completed successfully!")
            
            # Create tabs for different views
            tab1, tab2, tab3, tab4 = st.tabs(["📊 Summary", "📈 Performance", "💰 Trades", "📋 Details"])
            
            with tab1:
                # Key metrics in cards
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric(
                        "Total Return",
                        f"{stats['Return [%]']:.2f}%",
                        f"{stats['Return [%]'] - stats['Buy & Hold Return [%]']:.2f}% vs Buy & Hold"
                    )
                
                with col2:
                    st.metric(
                        "Sharpe Ratio",
                        f"{stats['Sharpe Ratio']:.2f}",
                        "Risk-adjusted return"
                    )
                
                with col3:
                    st.metric(
                        "Max Drawdown",
                        f"{stats['Max. Drawdown [%]']:.2f}%",
                        "Largest peak-to-trough decline"
                    )
                
                with col4:
                    st.metric(
                        "Win Rate",
                        f"{stats['Win Rate [%]']:.2f}%",
                        f"{stats['# Trades']} total trades"
                    )
                
                # Additional metrics
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Final Equity", f"${stats['Equity Final [$]']:,.2f}")
                
                with col2:
                    st.metric("Annual Return", f"{stats['Return (Ann.) [%]']:.2f}%")
                
                with col3:
                    st.metric("Profit Factor", f"{stats['Profit Factor']:.2f}")
                
                with col4:
                    st.metric("CAGR", f"{stats['CAGR [%]']:.2f}%")
            
            with tab2:
                # Performance charts
                st.subheader("📈 Performance Analysis")
                if not _plotly_available:
                    st.warning("Plotly is not available. Install dependencies from requirements_web.txt to see charts.")
                
                if _plotly_available:
                
                # Create performance comparison chart
                fig = make_subplots(
                    rows=2, cols=1,
                    subplot_titles=('Equity Curve', 'Drawdown'),
                    vertical_spacing=0.1
                )
                
                # Equity curve
                equity_curve = stats['_equity_curve']
                fig.add_trace(
                    go.Scatter(
                        x=equity_curve.index,
                        y=equity_curve['Equity'],
                        name='Strategy',
                        line=dict(color='blue')
                    ),
                    row=1, col=1
                )
                
                # Buy & Hold comparison
                buy_hold = initial_cash * (1 + data['Close'].pct_change().cumsum())
                fig.add_trace(
                    go.Scatter(
                        x=buy_hold.index,
                        y=buy_hold,
                        name='Buy & Hold',
                        line=dict(color='red', dash='dash')
                    ),
                    row=1, col=1
                )
                
                # Drawdown
                drawdown = equity_curve['DrawdownPct']
                fig.add_trace(
                    go.Scatter(
                        x=drawdown.index,
                        y=drawdown,
                        name='Drawdown',
                        fill='tonexty',
                        line=dict(color='red')
                    ),
                    row=2, col=1
                )
                
                fig.update_layout(height=600, showlegend=True)
                st.plotly_chart(fig, use_container_width=True)
            
            with tab3:
                # Trade analysis
                st.subheader("💰 Trade Analysis")
                if not _plotly_available:
                    st.warning("Plotly is not available. Install dependencies from requirements_web.txt to see charts.")
                
                trades = stats['_trades']
                if len(trades) > 0:
                    # Trade distribution
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        # Trade returns histogram
                        returns = trades['ReturnPct']
                        if _plotly_available:
                            fig = px.histogram(
                                returns, 
                                nbins=20,
                                title="Trade Returns Distribution",
                                labels={'value': 'Return (%)', 'count': 'Number of Trades'}
                            )
                            st.plotly_chart(fig, use_container_width=True)
                    
                    with col2:
                        # Win/Loss pie chart
                        wins = (returns > 0).sum()
                        losses = (returns <= 0).sum()
                        if _plotly_available:
                            fig = px.pie(
                                values=[wins, losses],
                                names=['Winning Trades', 'Losing Trades'],
                                title="Win/Loss Distribution",
                                color_discrete_sequence=['green', 'red']
                            )
                            st.plotly_chart(fig, use_container_width=True)
                    
                    # Trade table
                    st.subheader("📋 Recent Trades")
                    display_trades = trades.tail(10)[['EntryTime', 'ExitTime', 'Size', 'PnL', 'ReturnPct']]
                    st.dataframe(display_trades, use_container_width=True)
                else:
                    st.info("No trades were executed during the backtest period.")
            
            with tab4:
                # Detailed statistics
                st.subheader("📋 Detailed Statistics")
                
                # Create a comprehensive stats table
                stats_df = pd.DataFrame([
                    ["Start Date", stats['Start']],
                    ["End Date", stats['End']],
                    ["Duration", stats['Duration']],
                    ["Exposure Time", f"{stats['Exposure Time [%]']:.2f}%"],
                    ["Initial Cash", f"${initial_cash:,.2f}"],
                    ["Final Equity", f"${stats['Equity Final [$]']:,.2f}"],
                    ["Total Return", f"{stats['Return [%]']:.2f}%"],
                    ["Buy & Hold Return", f"{stats['Buy & Hold Return [%]']:.2f}%"],
                    ["Annual Return", f"{stats['Return (Ann.) [%]']:.2f}%"],
                    ["Volatility (Ann.)", f"{stats['Volatility (Ann.) [%]']:.2f}%"],
                    ["Sharpe Ratio", f"{stats['Sharpe Ratio']:.2f}"],
                    ["Sortino Ratio", f"{stats['Sortino Ratio']:.2f}"],
                    ["Calmar Ratio", f"{stats['Calmar Ratio']:.2f}"],
                    ["Max Drawdown", f"{stats['Max. Drawdown [%]']:.2f}%"],
                    ["Avg Drawdown", f"{stats['Avg. Drawdown [%]']:.2f}%"],
                    ["Number of Trades", stats['# Trades']],
                    ["Win Rate", f"{stats['Win Rate [%]']:.2f}%"],
                    ["Best Trade", f"{stats['Best Trade [%]']:.2f}%"],
                    ["Worst Trade", f"{stats['Worst Trade [%]']:.2f}%"],
                    ["Avg Trade", f"{stats['Avg. Trade [%]']:.2f}%"],
                    ["Profit Factor", f"{stats['Profit Factor']:.2f}"],
                    ["Expectancy", f"{stats['Expectancy [%]']:.2f}%"],
                    ["SQN", f"{stats['SQN']:.2f}"],
                    ["Kelly Criterion", f"{stats['Kelly Criterion']:.4f}"]
                ], columns=["Metric", "Value"])
                
                st.dataframe(stats_df, use_container_width=True, hide_index=True)
        
        except Exception as e:
            st.error(f"❌ Error running backtest: {e}")
            st.info("Please check your parameters and try again.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Built with ❤️ using <a href='https://github.com/kernc/backtesting.py' target='_blank'>backtesting.py</a> and <a href='https://streamlit.io' target='_blank'>Streamlit</a></p>
    <p>📚 <a href='https://kernc.github.io/backtesting.py/' target='_blank'>Documentation</a> | 🐛 <a href='https://github.com/kernc/backtesting.py/issues' target='_blank'>Issues</a></p>
</div>
""", unsafe_allow_html=True)
