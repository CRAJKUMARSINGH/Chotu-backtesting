#!/usr/bin/env python3
"""
🎓 UNIFIED INVESTMENT LEARNING PLATFORM
======================================
Educational trading & investment app combining:
- FinRL (Reinforcement Learning)
- Backtesting.py (Strategy Testing)
- Lumibot (Live Trading Simulation)
- VectorBT (Portfolio Analysis)

Built for learning stock investment fundamentals
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import yfinance as yf

# Page config
st.set_page_config(
    page_title="Investment Learning Platform",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #1f77b4, #2ca02c);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    .lesson-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 1rem;
        color: white;
        margin: 1rem 0;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin: 0.5rem 0;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        color: #856404;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'portfolio' not in st.session_state:
    st.session_state.portfolio = {'cash': 100000, 'holdings': {}}
if 'trade_history' not in st.session_state:
    st.session_state.trade_history = []

# Header
st.markdown('<h1 class="main-header">🎓 Investment Learning Platform</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Learn Stock Investment Through Interactive Simulations</p>', unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📚 Learning Modules")
module = st.sidebar.radio(
    "Choose a module:",
    ["🏠 Home", "📖 User Manual", "📚 Basics", "📊 Market Analysis", "🤖 Strategy Builder", 
     "💼 Portfolio Simulator", "📈 Backtest Lab", "🎯 Quiz & Practice",
     "🔬 Advanced: Walk-Forward", "📊 Advanced: Portfolio Optimization"]
)

# Module 1: Home
if module == "🏠 Home":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="lesson-card">
            <h3>📖 User Manual</h3>
            <p>Complete guide on how to use this app</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="lesson-card">
            <h3>📚 Learn Basics</h3>
            <p>Understand stocks, markets, and investment fundamentals</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="lesson-card">
            <h3>📊 Analyze Markets</h3>
            <p>Explore real market data and technical indicators</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick stats
    st.subheader("📊 Market Overview")
    
    # Fetch real market data
    tickers = ['SPY', 'AAPL', 'MSFT', 'GOOGL']
    cols = st.columns(len(tickers))
    
    for idx, ticker in enumerate(tickers):
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            current_price = info.get('currentPrice', info.get('regularMarketPrice', 0))
            prev_close = info.get('previousClose', current_price)
            change = ((current_price - prev_close) / prev_close * 100) if prev_close else 0
            
            with cols[idx]:
                st.metric(
                    label=ticker,
                    value=f"${current_price:.2f}",
                    delta=f"{change:.2f}%"
                )
        except:
            with cols[idx]:
                st.metric(label=ticker, value="N/A", delta="0%")

# Module 2: User Manual
elif module == "📖 User Manual":
    st.header("📖 Complete User Manual")
    
    st.markdown("""
    ## 🎓 Welcome to Investment Learning Platform!
    
    This app teaches you about stock investment through interactive simulations.
    
    ### 🚀 Quick Start (3 Steps)
    
    1. **Start with Basics** - Click "📚 Basics" in sidebar
    2. **Analyze Stocks** - Try "📊 Market Analysis" with AAPL
    3. **Practice Trading** - Use "💼 Portfolio Simulator" with $100,000 virtual money
    
    ---
    
    ## 📚 All Modules Explained
    
    ### 1. 🏠 Home
    - Market overview with real-time prices
    - Quick navigation to all modules
    - Current market status
    
    ### 2. 📚 Basics (START HERE!)
    **6 Interactive Lessons:**
    - What is a Stock? (Ownership in companies)
    - How Markets Work (Supply & demand)
    - Risk & Return (Higher risk = higher potential return)
    - Diversification (Don't put all eggs in one basket)
    - Technical Analysis (Reading charts)
    - Fundamental Analysis (Company value)
    
    **Time:** 15-20 minutes  
    **Difficulty:** Beginner
    
    ### 3. 📊 Market Analysis
    **Analyze Real Stocks:**
    - Enter any ticker (AAPL, MSFT, GOOGL, TSLA)
    - View candlestick charts
    - See technical indicators (SMA, Bollinger Bands)
    - Analyze volume and returns
    
    **How to use:**
    1. Enter stock ticker (e.g., "AAPL")
    2. Select time period (1mo, 3mo, 6mo, 1y, 2y, 5y)
    3. Click "Analyze Stock"
    4. Explore interactive charts
    
    **Time:** 5-10 minutes per stock  
    **Difficulty:** Beginner
    
    ### 4. 🤖 Strategy Builder
    **Build Trading Strategies:**
    - Create SMA Crossover strategy
    - Customize parameters (fast/slow periods)
    - See buy/sell signals on chart
    - Compare to Buy & Hold
    
    **How to use:**
    1. Enter stock ticker
    2. Adjust Fast SMA (5-50) and Slow SMA (20-200)
    3. Click "Test Strategy"
    4. Review performance metrics
    
    **Strategy Logic:**
    - Buy when Fast SMA crosses above Slow SMA
    - Sell when Fast SMA crosses below Slow SMA
    
    **Time:** 10-15 minutes  
    **Difficulty:** Intermediate
    
    ### 5. 💼 Portfolio Simulator
    **Practice Virtual Trading:**
    - Start with $100,000 virtual money
    - Buy and sell real stocks
    - Track profit/loss
    - View trade history
    
    **How to use:**
    1. Go to "Trade" tab
    2. Enter stock ticker
    3. Choose Buy or Sell
    4. Enter number of shares
    5. Click "Execute Trade"
    
    **Features:**
    - Real market prices
    - Portfolio tracking
    - Trade history log
    - No real money risk!
    
    **Time:** Unlimited practice  
    **Difficulty:** Beginner
    
    ### 6. 📈 Backtest Lab
    **Compare 5 Strategies:**
    - Buy & Hold (baseline)
    - SMA Crossover (trend following)
    - RSI Mean Reversion (oversold/overbought)
    - Bollinger Bands (volatility)
    - MACD (momentum)
    
    **How to use:**
    1. Enter stock ticker
    2. Select strategies to compare
    3. Adjust commission and slippage
    4. Click "Run Comprehensive Backtest"
    5. Compare results
    
    **Time:** 5-10 minutes  
    **Difficulty:** Intermediate
    
    ### 7. 🎯 Quiz & Practice
    **Test Your Knowledge:**
    - Stock Basics Quiz
    - Technical Analysis Quiz
    - Risk Management Quiz
    - Portfolio Theory Quiz
    
    **How to use:**
    1. Select quiz topic
    2. Answer questions
    3. Click "Submit Quiz"
    4. See your score
    
    **Time:** 5 minutes per quiz  
    **Difficulty:** Beginner
    
    ### 8. 🔬 Walk-Forward Optimization
    **Advanced Strategy Testing:**
    - Train on historical data
    - Test on future data
    - Avoid overfitting
    - See strategy robustness
    
    **How to use:**
    1. Enter stock ticker
    2. Set training window (3-12 months)
    3. Set testing window (1-6 months)
    4. Click "Run Walk-Forward Analysis"
    5. Review out-of-sample results
    
    **Time:** 10-15 minutes  
    **Difficulty:** Advanced
    
    ### 9. 📊 Portfolio Optimization
    **Build Optimal Portfolios:**
    - Multiple stocks
    - Efficient Frontier
    - Maximum Sharpe Ratio
    - Minimum Volatility
    - Correlation analysis
    
    **How to use:**
    1. Enter multiple tickers (one per line)
    2. Select historical period
    3. Click "Optimize Portfolio"
    4. See optimal allocations
    
    **Time:** 10-15 minutes  
    **Difficulty:** Advanced
    
    ---
    
    ## 💡 Learning Path
    
    ### Week 1: Foundations
    1. Complete all Basics lessons
    2. Analyze 5 different stocks
    3. Take Stock Basics quiz
    4. Score 100% on quiz
    
    ### Week 2: Technical Analysis
    1. Learn chart reading
    2. Build first strategy
    3. Run backtests
    4. Compare strategies
    
    ### Week 3: Practice Trading
    1. Start virtual portfolio
    2. Make 10 trades
    3. Track performance
    4. Learn from mistakes
    
    ### Week 4: Advanced Concepts
    1. Try walk-forward optimization
    2. Build multi-stock portfolio
    3. Master all quizzes
    4. Optimize strategies
    
    ---
    
    ## 🎯 Tips for Success
    
    ### For Beginners
    - Start with Basics module
    - Take your time
    - Try interactive examples
    - Don't skip lessons
    
    ### For Practice
    - Use virtual money freely
    - Make mistakes safely
    - Track your decisions
    - Learn from results
    
    ### For Advanced Users
    - Test multiple strategies
    - Optimize parameters
    - Build diverse portfolios
    - Use walk-forward testing
    
    ---
    
    ## 🤔 Frequently Asked Questions
    
    ### Q: Is this real money?
    **A:** No! 100% virtual. You start with $100,000 fake money.
    
    ### Q: Can I lose real money?
    **A:** No! Zero risk. It's all for learning.
    
    ### Q: What stocks can I analyze?
    **A:** Any stock! Try: AAPL, MSFT, GOOGL, TSLA, AMZN, etc.
    
    ### Q: How do I know if my strategy is good?
    **A:** Test it in Backtest Lab and compare to Buy & Hold.
    
    ### Q: What if I make mistakes?
    **A:** Perfect! Mistakes are how you learn. No real money at risk.
    
    ### Q: Can I reset my portfolio?
    **A:** Yes! Just refresh the page.
    
    ### Q: How long to learn everything?
    **A:** Basics in 1 day, mastery in 1 month with daily practice.
    
    ### Q: Is this financial advice?
    **A:** No! This is for education only. Always consult professionals.
    
    ---
    
    ## 🔧 Troubleshooting
    
    ### Data Not Loading
    - Check internet connection
    - Try different stock ticker
    - Refresh the page
    
    ### App Running Slow
    - Close other browser tabs
    - Refresh the page
    - Try simpler analysis
    
    ### Charts Not Showing
    - Wait for data to load
    - Check ticker is valid
    - Try different time period
    
    ---
    
    ## ⚠️ Important Disclaimer
    
    This app is for **educational purposes only**.
    
    - ✅ Use virtual money to learn
    - ✅ Practice strategies safely
    - ✅ Understand concepts
    - ❌ Not financial advice
    - ❌ Not a recommendation to trade
    - ❌ Always consult professionals before investing real money
    
    ---
    
    ## 🎓 Ready to Start?
    
    Click "📚 Basics" in the sidebar to begin your learning journey!
    
    **Remember:** Every expert was once a beginner. You're taking the first step! 🚀
    """)

# Module 3: Basics
elif module == "📚 Basics":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="lesson-card">
            <h3>📖 Learn Basics</h3>
            <p>Understand stocks, markets, and investment fundamentals</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="lesson-card">
            <h3>📊 Analyze Markets</h3>
            <p>Explore real market data and technical indicators</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="lesson-card">
            <h3>🤖 Build Strategies</h3>
            <p>Create and test your own trading strategies</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick stats
    st.subheader("📊 Market Overview")
    
    # Fetch real market data
    tickers = ['SPY', 'AAPL', 'MSFT', 'GOOGL']
    cols = st.columns(len(tickers))
    
    for idx, ticker in enumerate(tickers):
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            current_price = info.get('currentPrice', info.get('regularMarketPrice', 0))
            prev_close = info.get('previousClose', current_price)
            change = ((current_price - prev_close) / prev_close * 100) if prev_close else 0
            
            with cols[idx]:
                st.metric(
                    label=ticker,
                    value=f"${current_price:.2f}",
                    delta=f"{change:.2f}%"
                )
        except:
            with cols[idx]:
                st.metric(label=ticker, value="N/A", delta="0%")

# Module 3: Basics
elif module == "📚 Basics":
    st.header("📚 Investment Basics")
    
    lesson = st.selectbox(
        "Choose a lesson:",
        ["What is a Stock?", "How Markets Work", "Risk & Return", 
         "Diversification", "Technical Analysis", "Fundamental Analysis"]
    )
    
    if lesson == "What is a Stock?":
        st.markdown("""
        ### 📈 What is a Stock?
        
        A **stock** represents ownership in a company. When you buy a stock, you become a shareholder.
        
        **Key Concepts:**
        - **Share**: A unit of ownership
        - **Price**: What people pay for one share
        - **Market Cap**: Total value of all shares (Price × Shares)
        - **Dividend**: Profit shared with shareholders
        
        **Example:**
        If Apple has 16 billion shares at $180 each:
        - Market Cap = 16B × $180 = $2.88 Trillion
        """)
        
        # Interactive example
        st.subheader("🎮 Interactive Example")
        shares = st.slider("Number of shares you want to buy:", 1, 100, 10)
        price = st.number_input("Price per share ($):", value=180.0, step=1.0)
        total = shares * price
        
        st.success(f"💰 Total Investment: ${total:,.2f}")
        st.info(f"📊 You would own {shares} shares worth ${total:,.2f}")
    
    elif lesson == "Risk & Return":
        st.markdown("""
        ### ⚖️ Risk & Return
        
        **The Golden Rule**: Higher potential returns come with higher risk.
        
        **Risk Types:**
        1. **Market Risk**: Overall market movements
        2. **Company Risk**: Specific to one company
        3. **Liquidity Risk**: Difficulty selling
        
        **Return Measures:**
        - **Total Return**: Price change + dividends
        - **Annualized Return**: Average yearly return
        - **Risk-Adjusted Return**: Return per unit of risk (Sharpe Ratio)
        """)
        
        # Risk-Return visualization
        st.subheader("📊 Risk-Return Tradeoff")
        
        assets = pd.DataFrame({
            'Asset': ['Savings', 'Bonds', 'Stocks', 'Crypto'],
            'Return': [2, 5, 10, 25],
            'Risk': [1, 3, 8, 20]
        })
        
        fig = px.scatter(
            assets, x='Risk', y='Return', text='Asset',
            size='Return', color='Asset',
            title="Risk vs Return by Asset Class"
        )
        fig.update_traces(textposition='top center')
        st.plotly_chart(fig, use_container_width=True)

# Module 3: Market Analysis
elif module == "📊 Market Analysis":
    st.header("📊 Real-Time Market Analysis")
    
    # Stock selector
    ticker = st.text_input("Enter Stock Ticker:", value="AAPL").upper()
    period = st.selectbox("Time Period:", ["1mo", "3mo", "6mo", "1y", "2y", "5y"])
    
    if st.button("📈 Analyze Stock"):
        with st.spinner(f"Fetching data for {ticker}..."):
            try:
                stock = yf.Ticker(ticker)
                df = stock.history(period=period)
                
                if df.empty:
                    st.error(f"No data found for {ticker}")
                else:
                    # Stock info
                    info = stock.info
                    
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Current Price", f"${info.get('currentPrice', 'N/A')}")
                    with col2:
                        st.metric("Market Cap", f"${info.get('marketCap', 0)/1e9:.2f}B")
                    with col3:
                        st.metric("P/E Ratio", f"{info.get('trailingPE', 'N/A')}")
                    with col4:
                        st.metric("52W High", f"${info.get('fiftyTwoWeekHigh', 'N/A')}")
                    
                    # Price chart with indicators
                    st.subheader("📈 Price Chart with Technical Indicators")
                    
                    # Calculate indicators
                    df['SMA_20'] = df['Close'].rolling(window=20).mean()
                    df['SMA_50'] = df['Close'].rolling(window=50).mean()
                    df['Upper_BB'] = df['SMA_20'] + (df['Close'].rolling(window=20).std() * 2)
                    df['Lower_BB'] = df['SMA_20'] - (df['Close'].rolling(window=20).std() * 2)
                    
                    fig = go.Figure()
                    
                    # Candlestick
                    fig.add_trace(go.Candlestick(
                        x=df.index,
                        open=df['Open'],
                        high=df['High'],
                        low=df['Low'],
                        close=df['Close'],
                        name='Price'
                    ))
                    
                    # Moving averages
                    fig.add_trace(go.Scatter(x=df.index, y=df['SMA_20'], name='SMA 20', line=dict(color='orange')))
                    fig.add_trace(go.Scatter(x=df.index, y=df['SMA_50'], name='SMA 50', line=dict(color='blue')))
                    
                    # Bollinger Bands
                    fig.add_trace(go.Scatter(x=df.index, y=df['Upper_BB'], name='Upper BB', line=dict(dash='dash', color='gray')))
                    fig.add_trace(go.Scatter(x=df.index, y=df['Lower_BB'], name='Lower BB', line=dict(dash='dash', color='gray')))
                    
                    fig.update_layout(
                        title=f"{ticker} Price Chart",
                        yaxis_title="Price ($)",
                        xaxis_title="Date",
                        height=600
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Volume chart
                    st.subheader("📊 Trading Volume")
                    fig_vol = go.Figure()
                    fig_vol.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volume'))
                    fig_vol.update_layout(height=300)
                    st.plotly_chart(fig_vol, use_container_width=True)
                    
                    # Returns analysis
                    st.subheader("📈 Returns Analysis")
                    df['Daily_Return'] = df['Close'].pct_change() * 100
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Total Return", f"{((df['Close'].iloc[-1] / df['Close'].iloc[0] - 1) * 100):.2f}%")
                        st.metric("Avg Daily Return", f"{df['Daily_Return'].mean():.2f}%")
                    with col2:
                        st.metric("Volatility (Std Dev)", f"{df['Daily_Return'].std():.2f}%")
                        st.metric("Best Day", f"{df['Daily_Return'].max():.2f}%")
                    
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Module 4: Strategy Builder
elif module == "🤖 Strategy Builder":
    st.header("🤖 Build Your Trading Strategy")
    
    st.markdown("""
    ### Create a Simple Moving Average (SMA) Crossover Strategy
    
    **Strategy Logic:**
    - **Buy Signal**: When fast SMA crosses above slow SMA
    - **Sell Signal**: When fast SMA crosses below slow SMA
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        ticker = st.text_input("Stock Ticker:", value="AAPL")
        fast_period = st.slider("Fast SMA Period:", 5, 50, 10)
    with col2:
        period = st.selectbox("Data Period:", ["6mo", "1y", "2y", "5y"])
        slow_period = st.slider("Slow SMA Period:", 20, 200, 50)
    
    if st.button("🚀 Test Strategy"):
        with st.spinner("Running backtest..."):
            try:
                # Fetch data
                stock = yf.Ticker(ticker)
                df = stock.history(period=period)
                
                # Calculate SMAs
                df['Fast_SMA'] = df['Close'].rolling(window=fast_period).mean()
                df['Slow_SMA'] = df['Close'].rolling(window=slow_period).mean()
                
                # Generate signals
                df['Signal'] = 0
                df.loc[df['Fast_SMA'] > df['Slow_SMA'], 'Signal'] = 1
                df['Position'] = df['Signal'].diff()
                
                # Calculate returns
                df['Strategy_Return'] = df['Signal'].shift(1) * df['Close'].pct_change()
                df['Buy_Hold_Return'] = df['Close'].pct_change()
                
                # Plot
                fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                                   subplot_titles=('Price & Signals', 'Cumulative Returns'))
                
                # Price chart
                fig.add_trace(go.Scatter(x=df.index, y=df['Close'], name='Price'), row=1, col=1)
                fig.add_trace(go.Scatter(x=df.index, y=df['Fast_SMA'], name=f'Fast SMA ({fast_period})'), row=1, col=1)
                fig.add_trace(go.Scatter(x=df.index, y=df['Slow_SMA'], name=f'Slow SMA ({slow_period})'), row=1, col=1)
                
                # Buy/Sell signals
                buy_signals = df[df['Position'] == 1]
                sell_signals = df[df['Position'] == -1]
                fig.add_trace(go.Scatter(x=buy_signals.index, y=buy_signals['Close'], 
                                        mode='markers', name='Buy', marker=dict(color='green', size=10, symbol='triangle-up')), row=1, col=1)
                fig.add_trace(go.Scatter(x=sell_signals.index, y=sell_signals['Close'], 
                                        mode='markers', name='Sell', marker=dict(color='red', size=10, symbol='triangle-down')), row=1, col=1)
                
                # Cumulative returns
                df['Cum_Strategy'] = (1 + df['Strategy_Return']).cumprod()
                df['Cum_BuyHold'] = (1 + df['Buy_Hold_Return']).cumprod()
                
                fig.add_trace(go.Scatter(x=df.index, y=df['Cum_Strategy'], name='Strategy'), row=2, col=1)
                fig.add_trace(go.Scatter(x=df.index, y=df['Cum_BuyHold'], name='Buy & Hold'), row=2, col=1)
                
                fig.update_layout(height=800)
                st.plotly_chart(fig, use_container_width=True)
                
                # Performance metrics
                st.subheader("📊 Performance Metrics")
                
                strategy_return = (df['Cum_Strategy'].iloc[-1] - 1) * 100
                buyhold_return = (df['Cum_BuyHold'].iloc[-1] - 1) * 100
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Strategy Return", f"{strategy_return:.2f}%")
                with col2:
                    st.metric("Buy & Hold Return", f"{buyhold_return:.2f}%")
                with col3:
                    st.metric("Outperformance", f"{(strategy_return - buyhold_return):.2f}%")
                
                if strategy_return > buyhold_return:
                    st.success("🎉 Your strategy outperformed buy & hold!")
                else:
                    st.warning("📉 Buy & hold performed better. Try adjusting parameters!")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Module 5: Portfolio Simulator
elif module == "💼 Portfolio Simulator":
    st.header("💼 Virtual Portfolio Simulator")
    
    st.markdown(f"""
    <div class="success-box">
    💰 <strong>Current Cash:</strong> ${st.session_state.portfolio['cash']:,.2f}
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🛒 Trade", "📊 Portfolio", "📜 History"])
    
    with tab1:
        st.subheader("🛒 Place a Trade")
        
        col1, col2 = st.columns(2)
        with col1:
            ticker = st.text_input("Stock Ticker:", value="AAPL").upper()
            action = st.radio("Action:", ["Buy", "Sell"])
        with col2:
            shares = st.number_input("Number of Shares:", min_value=1, value=10)
            
        if st.button("Execute Trade"):
            try:
                stock = yf.Ticker(ticker)
                price = stock.info.get('currentPrice', stock.info.get('regularMarketPrice', 0))
                
                if price == 0:
                    st.error("Could not fetch price")
                else:
                    total_cost = shares * price
                    
                    if action == "Buy":
                        if total_cost > st.session_state.portfolio['cash']:
                            st.error("Insufficient funds!")
                        else:
                            st.session_state.portfolio['cash'] -= total_cost
                            if ticker in st.session_state.portfolio['holdings']:
                                st.session_state.portfolio['holdings'][ticker] += shares
                            else:
                                st.session_state.portfolio['holdings'][ticker] = shares
                            
                            st.session_state.trade_history.append({
                                'Date': datetime.now(),
                                'Ticker': ticker,
                                'Action': 'Buy',
                                'Shares': shares,
                                'Price': price,
                                'Total': total_cost
                            })
                            
                            st.success(f"✅ Bought {shares} shares of {ticker} at ${price:.2f}")
                    
                    else:  # Sell
                        if ticker not in st.session_state.portfolio['holdings'] or st.session_state.portfolio['holdings'][ticker] < shares:
                            st.error("Insufficient shares!")
                        else:
                            st.session_state.portfolio['cash'] += total_cost
                            st.session_state.portfolio['holdings'][ticker] -= shares
                            if st.session_state.portfolio['holdings'][ticker] == 0:
                                del st.session_state.portfolio['holdings'][ticker]
                            
                            st.session_state.trade_history.append({
                                'Date': datetime.now(),
                                'Ticker': ticker,
                                'Action': 'Sell',
                                'Shares': shares,
                                'Price': price,
                                'Total': total_cost
                            })
                            
                            st.success(f"✅ Sold {shares} shares of {ticker} at ${price:.2f}")
            
            except Exception as e:
                st.error(f"Error: {str(e)}")
    
    with tab2:
        st.subheader("📊 Current Holdings")
        
        if st.session_state.portfolio['holdings']:
            holdings_data = []
            total_value = st.session_state.portfolio['cash']
            
            for ticker, shares in st.session_state.portfolio['holdings'].items():
                try:
                    stock = yf.Ticker(ticker)
                    price = stock.info.get('currentPrice', stock.info.get('regularMarketPrice', 0))
                    value = shares * price
                    total_value += value
                    
                    holdings_data.append({
                        'Ticker': ticker,
                        'Shares': shares,
                        'Price': f"${price:.2f}",
                        'Value': f"${value:,.2f}"
                    })
                except:
                    pass
            
            df_holdings = pd.DataFrame(holdings_data)
            st.dataframe(df_holdings, use_container_width=True)
            
            st.markdown(f"""
            <div class="metric-card">
            <h3>Portfolio Summary</h3>
            <p>💰 Cash: ${st.session_state.portfolio['cash']:,.2f}</p>
            <p>📊 Total Portfolio Value: ${total_value:,.2f}</p>
            <p>📈 Total Return: ${(total_value - 100000):,.2f} ({((total_value/100000 - 1) * 100):.2f}%)</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("No holdings yet. Start trading!")
    
    with tab3:
        st.subheader("📜 Trade History")
        
        if st.session_state.trade_history:
            df_history = pd.DataFrame(st.session_state.trade_history)
            st.dataframe(df_history, use_container_width=True)
        else:
            st.info("No trades yet")

# Module 6: Backtest Lab
elif module == "📈 Backtest Lab":
    st.header("📈 Advanced Backtesting Lab")
    
    st.markdown("""
    ### Test Multiple Strategies
    Compare different trading strategies side-by-side
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        ticker = st.text_input("Stock Ticker:", value="AAPL")
        period = st.selectbox("Period:", ["1y", "2y", "3y", "5y"])
        initial_capital = st.number_input("Initial Capital ($):", value=10000, step=1000)
    
    with col2:
        # Advanced options
        st.subheader("Advanced Options")
        commission = st.slider("Commission (%)", 0.0, 1.0, 0.1, 0.05)
        slippage = st.slider("Slippage (%)", 0.0, 0.5, 0.05, 0.01)
        
        # Strategy selection
        strategies_to_test = st.multiselect(
            "Select Strategies to Compare:",
            ["Buy & Hold", "SMA Crossover", "RSI Mean Reversion", "Bollinger Bands", "MACD"],
            default=["Buy & Hold", "SMA Crossover", "RSI Mean Reversion"]
        )
    
    if st.button("🔬 Run Comprehensive Backtest"):
        with st.spinner("Running multiple strategies..."):
            try:
                stock = yf.Ticker(ticker)
                df = stock.history(period=period)
                
                results_data = []
                
                # Strategy 1: Buy & Hold
                if "Buy & Hold" in strategies_to_test:
                    df['BuyHold'] = (df['Close'] / df['Close'].iloc[0]) * initial_capital
                    final_value = df['BuyHold'].iloc[-1]
                    results_data.append({
                        'Strategy': 'Buy & Hold',
                        'Final Value': final_value,
                        'Total Return (%)': ((final_value / initial_capital - 1) * 100)
                    })
                
                # Strategy 2: SMA Crossover
                if "SMA Crossover" in strategies_to_test:
                    df['SMA_10'] = df['Close'].rolling(10).mean()
                    df['SMA_30'] = df['Close'].rolling(30).mean()
                    df['SMA_Signal'] = 0
                    df.loc[df['SMA_10'] > df['SMA_30'], 'SMA_Signal'] = 1
                    df['SMA_Return'] = df['SMA_Signal'].shift(1) * df['Close'].pct_change()
                    # Apply commission
                    df['SMA_Return'] = df['SMA_Return'] - (commission/100) * abs(df['SMA_Signal'].diff())
                    df['SMA_Portfolio'] = initial_capital * (1 + df['SMA_Return']).cumprod()
                    final_value = df['SMA_Portfolio'].iloc[-1]
                    results_data.append({
                        'Strategy': 'SMA Crossover',
                        'Final Value': final_value,
                        'Total Return (%)': ((final_value / initial_capital - 1) * 100)
                    })
                
                # Strategy 3: RSI Mean Reversion
                if "RSI Mean Reversion" in strategies_to_test:
                    delta = df['Close'].diff()
                    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
                    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
                    rs = gain / loss
                    df['RSI'] = 100 - (100 / (1 + rs))
                    df['RSI_Signal'] = 0
                    df.loc[df['RSI'] < 30, 'RSI_Signal'] = 1  # Oversold - Buy
                    df.loc[df['RSI'] > 70, 'RSI_Signal'] = -1  # Overbought - Sell
                    df['RSI_Return'] = df['RSI_Signal'].shift(1) * df['Close'].pct_change()
                    df['RSI_Return'] = df['RSI_Return'] - (commission/100) * abs(df['RSI_Signal'].diff())
                    df['RSI_Portfolio'] = initial_capital * (1 + df['RSI_Return']).cumprod()
                    final_value = df['RSI_Portfolio'].iloc[-1]
                    results_data.append({
                        'Strategy': 'RSI Mean Reversion',
                        'Final Value': final_value,
                        'Total Return (%)': ((final_value / initial_capital - 1) * 100)
                    })
                
                # Strategy 4: Bollinger Bands
                if "Bollinger Bands" in strategies_to_test:
                    df['BB_Middle'] = df['Close'].rolling(20).mean()
                    df['BB_Std'] = df['Close'].rolling(20).std()
                    df['BB_Upper'] = df['BB_Middle'] + (df['BB_Std'] * 2)
                    df['BB_Lower'] = df['BB_Middle'] - (df['BB_Std'] * 2)
                    df['BB_Signal'] = 0
                    df.loc[df['Close'] < df['BB_Lower'], 'BB_Signal'] = 1  # Buy at lower band
                    df.loc[df['Close'] > df['BB_Upper'], 'BB_Signal'] = -1  # Sell at upper band
                    df['BB_Return'] = df['BB_Signal'].shift(1) * df['Close'].pct_change()
                    df['BB_Return'] = df['BB_Return'] - (commission/100) * abs(df['BB_Signal'].diff())
                    df['BB_Portfolio'] = initial_capital * (1 + df['BB_Return']).cumprod()
                    final_value = df['BB_Portfolio'].iloc[-1]
                    results_data.append({
                        'Strategy': 'Bollinger Bands',
                        'Final Value': final_value,
                        'Total Return (%)': ((final_value / initial_capital - 1) * 100)
                    })
                
                # Strategy 5: MACD
                if "MACD" in strategies_to_test:
                    exp1 = df['Close'].ewm(span=12, adjust=False).mean()
                    exp2 = df['Close'].ewm(span=26, adjust=False).mean()
                    df['MACD'] = exp1 - exp2
                    df['MACD_Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()
                    df['MACD_Hist'] = df['MACD'] - df['MACD_Signal_Line']
                    df['MACD_Trade_Signal'] = 0
                    df.loc[df['MACD'] > df['MACD_Signal_Line'], 'MACD_Trade_Signal'] = 1
                    df['MACD_Return'] = df['MACD_Trade_Signal'].shift(1) * df['Close'].pct_change()
                    df['MACD_Return'] = df['MACD_Return'] - (commission/100) * abs(df['MACD_Trade_Signal'].diff())
                    df['MACD_Portfolio'] = initial_capital * (1 + df['MACD_Return']).cumprod()
                    final_value = df['MACD_Portfolio'].iloc[-1]
                    results_data.append({
                        'Strategy': 'MACD',
                        'Final Value': final_value,
                        'Total Return (%)': ((final_value / initial_capital - 1) * 100)
                    })
                
                # Plot comparison
                fig = go.Figure()
                
                for strategy in strategies_to_test:
                    if strategy == "Buy & Hold" and 'BuyHold' in df.columns:
                        fig.add_trace(go.Scatter(x=df.index, y=df['BuyHold'], name='Buy & Hold'))
                    elif strategy == "SMA Crossover" and 'SMA_Portfolio' in df.columns:
                        fig.add_trace(go.Scatter(x=df.index, y=df['SMA_Portfolio'], name='SMA Crossover'))
                    elif strategy == "RSI Mean Reversion" and 'RSI_Portfolio' in df.columns:
                        fig.add_trace(go.Scatter(x=df.index, y=df['RSI_Portfolio'], name='RSI Mean Reversion'))
                    elif strategy == "Bollinger Bands" and 'BB_Portfolio' in df.columns:
                        fig.add_trace(go.Scatter(x=df.index, y=df['BB_Portfolio'], name='Bollinger Bands'))
                    elif strategy == "MACD" and 'MACD_Portfolio' in df.columns:
                        fig.add_trace(go.Scatter(x=df.index, y=df['MACD_Portfolio'], name='MACD'))
                
                fig.update_layout(
                    title=f"Strategy Comparison - {ticker}",
                    yaxis_title="Portfolio Value ($)",
                    xaxis_title="Date",
                    height=600,
                    hovermode='x unified'
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # Performance table
                st.subheader("📊 Performance Comparison")
                
                results = pd.DataFrame(results_data)
                results = results.sort_values('Total Return (%)', ascending=False)
                
                # Add risk metrics
                st.dataframe(results.style.format({
                    'Final Value': '${:,.2f}',
                    'Total Return (%)': '{:.2f}%'
                }), use_container_width=True)
                
                best_strategy = results.iloc[0]['Strategy']
                best_return = results.iloc[0]['Total Return (%)']
                st.success(f"🏆 Best Strategy: {best_strategy} with {best_return:.2f}% return")
                
                # Additional metrics
                st.subheader("📈 Risk-Adjusted Metrics")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Commission Applied", f"{commission}%")
                with col2:
                    st.metric("Slippage Applied", f"{slippage}%")
                with col3:
                    st.metric("Strategies Tested", len(strategies_to_test))
                
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Module 7: Quiz
elif module == "🎯 Quiz & Practice":
    st.header("🎯 Test Your Knowledge")
    
    quiz_topic = st.selectbox(
        "Choose a topic:",
        ["Stock Basics", "Technical Analysis", "Risk Management", "Portfolio Theory"]
    )
    
    if quiz_topic == "Stock Basics":
        st.subheader("📝 Stock Basics Quiz")
        
        q1 = st.radio(
            "1. What does a stock represent?",
            ["A loan to a company", "Ownership in a company", "A bond", "A commodity"]
        )
        
        q2 = st.radio(
            "2. What is market capitalization?",
            ["Total revenue", "Share price × Number of shares", "Total assets", "Annual profit"]
        )
        
        q3 = st.radio(
            "3. What is a dividend?",
            ["Stock price increase", "Profit shared with shareholders", "Trading fee", "Market index"]
        )
        
        if st.button("Submit Quiz"):
            score = 0
            if q1 == "Ownership in a company":
                score += 1
            if q2 == "Share price × Number of shares":
                score += 1
            if q3 == "Profit shared with shareholders":
                score += 1
            
            st.markdown(f"""
            <div class="{'success-box' if score == 3 else 'warning-box'}">
            <h3>Your Score: {score}/3</h3>
            <p>{'🎉 Perfect! You understand the basics!' if score == 3 else '📚 Keep learning! Review the basics module.'}</p>
            </div>
            """, unsafe_allow_html=True)

# Module 8: Walk-Forward Optimization
elif module == "🔬 Advanced: Walk-Forward":
    st.header("🔬 Walk-Forward Optimization")
    
    st.markdown("""
    ### What is Walk-Forward Optimization?
    
    Walk-forward optimization is a technique to test strategy robustness by:
    1. **Training** on a period of data
    2. **Testing** on the next period
    3. **Rolling forward** and repeating
    
    This simulates real-world trading where you optimize on past data and trade on future data.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        ticker = st.text_input("Stock Ticker:", value="AAPL")
        total_period = st.selectbox("Total Period:", ["2y", "3y", "5y"])
        
    with col2:
        train_window = st.slider("Training Window (months):", 3, 12, 6)
        test_window = st.slider("Testing Window (months):", 1, 6, 3)
    
    if st.button("🚀 Run Walk-Forward Analysis"):
        with st.spinner("Running walk-forward optimization..."):
            try:
                stock = yf.Ticker(ticker)
                df = stock.history(period=total_period)
                
                st.info(f"📊 Total data points: {len(df)}")
                st.info(f"🔄 Training window: {train_window} months, Testing window: {test_window} months")
                
                # Simple walk-forward simulation
                train_days = train_window * 21  # Approximate trading days
                test_days = test_window * 21
                
                results = []
                
                for i in range(0, len(df) - train_days - test_days, test_days):
                    train_data = df.iloc[i:i+train_days]
                    test_data = df.iloc[i+train_days:i+train_days+test_days]
                    
                    if len(test_data) < test_days // 2:
                        break
                    
                    # Optimize on training data (find best SMA periods)
                    best_return = -np.inf
                    best_fast = 10
                    best_slow = 20
                    
                    for fast in range(5, 20, 5):
                        for slow in range(20, 60, 10):
                            train_data['Fast_SMA'] = train_data['Close'].rolling(fast).mean()
                            train_data['Slow_SMA'] = train_data['Close'].rolling(slow).mean()
                            train_data['Signal'] = 0
                            train_data.loc[train_data['Fast_SMA'] > train_data['Slow_SMA'], 'Signal'] = 1
                            train_data['Return'] = train_data['Signal'].shift(1) * train_data['Close'].pct_change()
                            total_return = train_data['Return'].sum()
                            
                            if total_return > best_return:
                                best_return = total_return
                                best_fast = fast
                                best_slow = slow
                    
                    # Test on out-of-sample data
                    test_data['Fast_SMA'] = test_data['Close'].rolling(best_fast).mean()
                    test_data['Slow_SMA'] = test_data['Close'].rolling(best_slow).mean()
                    test_data['Signal'] = 0
                    test_data.loc[test_data['Fast_SMA'] > test_data['Slow_SMA'], 'Signal'] = 1
                    test_data['Return'] = test_data['Signal'].shift(1) * test_data['Close'].pct_change()
                    test_return = test_data['Return'].sum() * 100
                    
                    results.append({
                        'Period': f"{test_data.index[0].strftime('%Y-%m-%d')} to {test_data.index[-1].strftime('%Y-%m-%d')}",
                        'Best Fast SMA': best_fast,
                        'Best Slow SMA': best_slow,
                        'Test Return (%)': test_return
                    })
                
                # Display results
                st.subheader("📊 Walk-Forward Results")
                
                results_df = pd.DataFrame(results)
                st.dataframe(results_df.style.format({
                    'Test Return (%)': '{:.2f}%'
                }), use_container_width=True)
                
                # Summary statistics
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    avg_return = results_df['Test Return (%)'].mean()
                    st.metric("Average Return", f"{avg_return:.2f}%")
                
                with col2:
                    win_rate = (results_df['Test Return (%)'] > 0).sum() / len(results_df) * 100
                    st.metric("Win Rate", f"{win_rate:.1f}%")
                
                with col3:
                    best_period = results_df.loc[results_df['Test Return (%)'].idxmax(), 'Period']
                    st.metric("Best Period", best_period[:10])
                
                st.success("✅ Walk-forward analysis complete! This shows how the strategy performs on unseen data.")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Module 9: Portfolio Optimization
elif module == "📊 Advanced: Portfolio Optimization":
    st.header("📊 Portfolio Optimization")
    
    st.markdown("""
    ### Modern Portfolio Theory
    
    Build an optimal portfolio by balancing risk and return across multiple assets.
    
    **Key Concepts:**
    - **Diversification**: Don't put all eggs in one basket
    - **Efficient Frontier**: Best risk/return combinations
    - **Sharpe Ratio**: Return per unit of risk
    """)
    
    # Stock selection
    st.subheader("Select Your Portfolio")
    
    col1, col2 = st.columns(2)
    
    with col1:
        tickers_input = st.text_area(
            "Stock Tickers (one per line):",
            value="AAPL\nMSFT\nGOOGL\nAMZN\nTSLA"
        )
        tickers = [t.strip() for t in tickers_input.split("\n") if t.strip()]
    
    with col2:
        period = st.selectbox("Historical Period:", ["1y", "2y", "3y", "5y"])
        num_portfolios = st.slider("Number of Random Portfolios:", 1000, 10000, 5000, 1000)
    
    if st.button("🎯 Optimize Portfolio"):
        with st.spinner("Optimizing portfolio..."):
            try:
                # Download data for all tickers
                data = yf.download(tickers, period=period, progress=False)['Close']
                
                if isinstance(data, pd.Series):
                    data = data.to_frame()
                
                st.success(f"✅ Downloaded data for {len(tickers)} stocks")
                
                # Calculate returns
                returns = data.pct_change().dropna()
                
                # Calculate mean returns and covariance
                mean_returns = returns.mean() * 252  # Annualized
                cov_matrix = returns.cov() * 252  # Annualized
                
                # Generate random portfolios
                results = np.zeros((4, num_portfolios))
                weights_record = []
                
                for i in range(num_portfolios):
                    weights = np.random.random(len(tickers))
                    weights /= np.sum(weights)
                    weights_record.append(weights)
                    
                    portfolio_return = np.sum(weights * mean_returns)
                    portfolio_std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
                    sharpe_ratio = portfolio_return / portfolio_std
                    
                    results[0,i] = portfolio_return
                    results[1,i] = portfolio_std
                    results[2,i] = sharpe_ratio
                
                # Find optimal portfolios
                max_sharpe_idx = np.argmax(results[2])
                min_vol_idx = np.argmin(results[1])
                
                max_sharpe_return = results[0, max_sharpe_idx]
                max_sharpe_std = results[1, max_sharpe_idx]
                max_sharpe_weights = weights_record[max_sharpe_idx]
                
                min_vol_return = results[0, min_vol_idx]
                min_vol_std = results[1, min_vol_idx]
                min_vol_weights = weights_record[min_vol_idx]
                
                # Plot efficient frontier
                st.subheader("📈 Efficient Frontier")
                
                fig = go.Figure()
                
                # All portfolios
                fig.add_trace(go.Scatter(
                    x=results[1,:],
                    y=results[0,:],
                    mode='markers',
                    marker=dict(
                        size=3,
                        color=results[2,:],
                        colorscale='Viridis',
                        showscale=True,
                        colorbar=dict(title="Sharpe Ratio")
                    ),
                    name='Portfolios',
                    text=[f"Return: {r:.2%}<br>Risk: {s:.2%}<br>Sharpe: {sh:.2f}" 
                          for r, s, sh in zip(results[0,:], results[1,:], results[2,:])],
                    hovertemplate='%{text}<extra></extra>'
                ))
                
                # Max Sharpe portfolio
                fig.add_trace(go.Scatter(
                    x=[max_sharpe_std],
                    y=[max_sharpe_return],
                    mode='markers',
                    marker=dict(size=15, color='red', symbol='star'),
                    name='Max Sharpe Ratio'
                ))
                
                # Min Volatility portfolio
                fig.add_trace(go.Scatter(
                    x=[min_vol_std],
                    y=[min_vol_return],
                    mode='markers',
                    marker=dict(size=15, color='green', symbol='star'),
                    name='Min Volatility'
                ))
                
                fig.update_layout(
                    title="Efficient Frontier",
                    xaxis_title="Risk (Standard Deviation)",
                    yaxis_title="Expected Return",
                    height=600,
                    hovermode='closest'
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Display optimal portfolios
                st.subheader("🎯 Optimal Portfolios")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("### 🔴 Maximum Sharpe Ratio")
                    st.metric("Expected Return", f"{max_sharpe_return:.2%}")
                    st.metric("Risk (Std Dev)", f"{max_sharpe_std:.2%}")
                    st.metric("Sharpe Ratio", f"{max_sharpe_return/max_sharpe_std:.2f}")
                    
                    st.markdown("**Allocation:**")
                    for ticker, weight in zip(tickers, max_sharpe_weights):
                        st.write(f"- {ticker}: {weight:.1%}")
                
                with col2:
                    st.markdown("### 🟢 Minimum Volatility")
                    st.metric("Expected Return", f"{min_vol_return:.2%}")
                    st.metric("Risk (Std Dev)", f"{min_vol_std:.2%}")
                    st.metric("Sharpe Ratio", f"{min_vol_return/min_vol_std:.2f}")
                    
                    st.markdown("**Allocation:**")
                    for ticker, weight in zip(tickers, min_vol_weights):
                        st.write(f"- {ticker}: {weight:.1%}")
                
                # Correlation matrix
                st.subheader("📊 Correlation Matrix")
                
                corr_matrix = returns.corr()
                
                fig_corr = go.Figure(data=go.Heatmap(
                    z=corr_matrix.values,
                    x=corr_matrix.columns,
                    y=corr_matrix.columns,
                    colorscale='RdBu',
                    zmid=0,
                    text=corr_matrix.values,
                    texttemplate='%{text:.2f}',
                    textfont={"size": 10}
                ))
                
                fig_corr.update_layout(
                    title="Asset Correlation Matrix",
                    height=500
                )
                
                st.plotly_chart(fig_corr, use_container_width=True)
                
                st.info("💡 Lower correlation between assets means better diversification!")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Footer
# Module 10: User Manual
elif module == "📖 User Manual":
    st.header("📖 Complete User Manual")
    
    # Table of Contents
    st.markdown("""
    ## 📑 Table of Contents
    
    1. [Getting Started](#getting-started)
    2. [Module Guide](#module-guide)
    3. [Features Overview](#features-overview)
    4. [Tips & Best Practices](#tips-best-practices)
    5. [Troubleshooting](#troubleshooting)
    6. [FAQ](#faq)
    """)
    
    # Getting Started
    st.markdown("---")
    st.subheader("🚀 Getting Started")
    
    with st.expander("Installation", expanded=False):
        st.markdown("""
        ### Installation Steps
        
        1. **Install Dependencies:**
        ```bash
        pip install -r requirements_unified.txt
        ```
        
        2. **Launch the App:**
        ```bash
        python launch_unified_app.py
        ```
        
        3. **Access in Browser:**
        - Local: http://localhost:8501
        - The app opens automatically
        
        ### System Requirements
        - Python 3.8 or higher
        - 4GB RAM minimum
        - Internet connection (for market data)
        - Modern web browser
        """)
    
    with st.expander("First Steps", expanded=False):
        st.markdown("""
        ### Your First 30 Minutes
        
        **Minutes 1-10: Learn Basics**
        1. Click "📚 Basics" in sidebar
        2. Read "What is a Stock?"
        3. Try the interactive example
        4. Complete the lesson
        
        **Minutes 11-20: Analyze a Stock**
        1. Click "📊 Market Analysis"
        2. Enter "AAPL" (Apple)
        3. Click "Analyze Stock"
        4. Explore the charts
        
        **Minutes 21-30: Build a Strategy**
        1. Click "🤖 Strategy Builder"
        2. Keep default settings
        3. Click "Test Strategy"
        4. Review the results
        """)
    
    # Module Guide
    st.markdown("---")
    st.subheader("📚 Module Guide")
    
    modules_info = {
        "🏠 Home": {
            "Purpose": "Overview and navigation hub",
            "Features": ["Market overview", "Quick stats", "Module previews"],
            "Time": "2 minutes",
            "Difficulty": "Easy"
        },
        "📚 Basics": {
            "Purpose": "Learn investment fundamentals",
            "Features": ["6 interactive lessons", "Visual examples", "Concept explanations"],
            "Time": "15 minutes",
            "Difficulty": "Easy"
        },
        "📊 Market Analysis": {
            "Purpose": "Analyze real stocks",
            "Features": ["Real-time data", "Technical indicators", "Charts", "Volume analysis"],
            "Time": "10 minutes per stock",
            "Difficulty": "Medium"
        },
        "🤖 Strategy Builder": {
            "Purpose": "Create trading strategies",
            "Features": ["SMA Crossover", "Backtesting", "Performance comparison", "Visual signals"],
            "Time": "15 minutes",
            "Difficulty": "Medium"
        },
        "💼 Portfolio Simulator": {
            "Purpose": "Practice virtual trading",
            "Features": ["$100,000 virtual money", "Buy/sell execution", "Portfolio tracking", "Trade history"],
            "Time": "20 minutes",
            "Difficulty": "Medium"
        },
        "📈 Backtest Lab": {
            "Purpose": "Compare multiple strategies",
            "Features": ["5 strategies", "Commission/slippage", "Performance metrics", "Risk analysis"],
            "Time": "15 minutes",
            "Difficulty": "Hard"
        },
        "🎯 Quiz & Practice": {
            "Purpose": "Test your knowledge",
            "Features": ["Multiple topics", "Instant scoring", "Learning feedback"],
            "Time": "10 minutes",
            "Difficulty": "Easy"
        },
        "🔬 Walk-Forward": {
            "Purpose": "Test strategy robustness",
            "Features": ["Training/testing windows", "Parameter optimization", "Out-of-sample testing"],
            "Time": "15 minutes",
            "Difficulty": "Hard"
        },
        "📊 Portfolio Optimization": {
            "Purpose": "Build optimal portfolios",
            "Features": ["Efficient Frontier", "Sharpe ratio optimization", "Correlation analysis"],
            "Time": "15 minutes",
            "Difficulty": "Hard"
        }
    }
    
    for module_name, info in modules_info.items():
        with st.expander(f"{module_name} - {info['Purpose']}", expanded=False):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Time Required:** {info['Time']}")
                st.markdown(f"**Difficulty:** {info['Difficulty']}")
            with col2:
                st.markdown("**Features:**")
                for feature in info['Features']:
                    st.markdown(f"- {feature}")
    
    # Features Overview
    st.markdown("---")
    st.subheader("✨ Features Overview")
    
    with st.expander("Real Market Data", expanded=False):
        st.markdown("""
        ### 📊 Live Data from Yahoo Finance
        
        - **Real-time prices** for any stock
        - **Historical data** up to 5 years
        - **Company information** (market cap, P/E ratio, etc.)
        - **Technical indicators** (SMA, Bollinger Bands, RSI, MACD)
        - **Volume analysis**
        
        **Supported Tickers:**
        - US Stocks: AAPL, MSFT, GOOGL, TSLA, etc.
        - ETFs: SPY, QQQ, IWM, etc.
        - Indices: ^GSPC (S&P 500), ^DJI (Dow Jones)
        """)
    
    with st.expander("Virtual Trading", expanded=False):
        st.markdown("""
        ### 💼 Risk-Free Practice
        
        - **$100,000 starting capital** (virtual money)
        - **Real market prices** for accurate simulation
        - **Buy and sell** any stock
        - **Portfolio tracking** in real-time
        - **Trade history** log
        - **Profit/loss** calculation
        
        **How to Trade:**
        1. Enter stock ticker
        2. Choose Buy or Sell
        3. Enter number of shares
        4. Click "Execute Trade"
        5. View updated portfolio
        """)
    
    with st.expander("Strategy Building", expanded=False):
        st.markdown("""
        ### 🤖 Create & Test Strategies
        
        **Available Strategies:**
        1. **SMA Crossover** - Moving average signals
        2. **RSI Mean Reversion** - Overbought/oversold
        3. **Bollinger Bands** - Volatility breakouts
        4. **MACD** - Momentum indicator
        5. **Buy & Hold** - Baseline comparison
        
        **Features:**
        - Adjustable parameters
        - Visual buy/sell signals
        - Performance vs Buy & Hold
        - Commission & slippage modeling
        - Risk-adjusted metrics
        """)
    
    with st.expander("Advanced Features", expanded=False):
        st.markdown("""
        ### 🔬 Professional Tools
        
        **Walk-Forward Optimization:**
        - Train on historical data
        - Test on future data
        - Rolling window analysis
        - Robustness testing
        
        **Portfolio Optimization:**
        - Modern Portfolio Theory
        - Efficient Frontier
        - Maximum Sharpe Ratio
        - Minimum Volatility
        - Correlation analysis
        - Optimal asset allocation
        """)
    
    # Tips & Best Practices
    st.markdown("---")
    st.subheader("💡 Tips & Best Practices")
    
    with st.expander("Learning Path", expanded=False):
        st.markdown("""
        ### 📚 Recommended Learning Path
        
        **Week 1: Foundations**
        - [ ] Complete all Basics lessons
        - [ ] Analyze 5 different stocks
        - [ ] Take Stock Basics quiz
        - [ ] Understand key concepts
        
        **Week 2: Technical Analysis**
        - [ ] Learn chart reading
        - [ ] Understand indicators
        - [ ] Build first strategy
        - [ ] Run backtests
        
        **Week 3: Practice Trading**
        - [ ] Start virtual portfolio
        - [ ] Make 10 trades
        - [ ] Track performance
        - [ ] Learn from results
        
        **Week 4: Advanced Strategies**
        - [ ] Compare multiple strategies
        - [ ] Optimize parameters
        - [ ] Analyze risk metrics
        - [ ] Master concepts
        """)
    
    with st.expander("Trading Tips", expanded=False):
        st.markdown("""
        ### 🎯 Key Principles
        
        1. **Start Simple**
           - Master basics before advanced features
           - One strategy at a time
           - Small positions initially
        
        2. **Practice Daily**
           - 15-30 minutes per day
           - Consistency is key
           - Review your trades
        
        3. **Diversify**
           - Don't put all eggs in one basket
           - Multiple stocks
           - Different sectors
        
        4. **Manage Risk**
           - Set stop losses
           - Position sizing
           - Never risk more than you can afford
        
        5. **Learn Continuously**
           - Read lessons
           - Take quizzes
           - Experiment safely
           - Ask questions
        
        6. **Be Patient**
           - Good investing takes time
           - Don't chase quick profits
           - Stick to your strategy
        
        7. **Track Performance**
           - Review your trades
           - Learn from mistakes
           - Celebrate successes
           - Adjust strategies
        """)
    
    with st.expander("Common Mistakes to Avoid", expanded=False):
        st.markdown("""
        ### ⚠️ What NOT to Do
        
        1. **Don't overtrade**
           - Too many trades = high costs
           - Quality over quantity
        
        2. **Don't ignore risk**
           - Always consider downside
           - Use stop losses
        
        3. **Don't chase performance**
           - Past returns ≠ future returns
           - Stick to your plan
        
        4. **Don't invest without research**
           - Always analyze first
           - Understand what you buy
        
        5. **Don't let emotions decide**
           - Fear and greed are bad advisors
           - Follow your strategy
        
        6. **Don't skip the basics**
           - Foundation is crucial
           - Master fundamentals first
        
        7. **Don't use real money yet**
           - Practice with virtual money
           - Build confidence first
           - Learn from mistakes safely
        """)
    
    # Troubleshooting
    st.markdown("---")
    st.subheader("🔧 Troubleshooting")
    
    with st.expander("Common Issues", expanded=False):
        st.markdown("""
        ### Problem: App won't start
        **Solution:**
        ```bash
        pip install --upgrade streamlit
        python launch_unified_app.py
        ```
        
        ### Problem: Dependencies missing
        **Solution:**
        ```bash
        pip install -r requirements_unified.txt
        ```
        
        ### Problem: Port already in use
        **Solution:**
        ```bash
        streamlit run unified_investment_app.py --server.port 8502
        ```
        
        ### Problem: Data not loading
        **Solution:**
        - Check internet connection
        - Try different stock ticker
        - Refresh the page
        - Wait a moment and try again
        
        ### Problem: Charts not displaying
        **Solution:**
        - Update your browser
        - Clear browser cache
        - Try different browser
        - Check JavaScript is enabled
        
        ### Problem: Slow performance
        **Solution:**
        - Close other browser tabs
        - Restart the app
        - Use shorter time periods
        - Reduce number of strategies
        """)
    
    # FAQ
    st.markdown("---")
    st.subheader("❓ Frequently Asked Questions")
    
    faqs = {
        "Is this real money?": "No! All trading is with virtual money ($100,000). There's zero risk.",
        "Can I lose real money?": "No! This is a simulation for learning. No real money is involved.",
        "What stocks can I analyze?": "Any stock with a valid ticker symbol (AAPL, MSFT, GOOGL, TSLA, etc.).",
        "How do I save my progress?": "Portfolio and trades save in your session. They reset when you refresh the page.",
        "Can I use this for real trading?": "This is for education only. Always consult professionals before real trading.",
        "Is the data real?": "Yes! We use real market data from Yahoo Finance.",
        "How accurate are the strategies?": "Backtests use historical data. Past performance doesn't guarantee future results.",
        "Can I create my own strategies?": "Yes! Use the Strategy Builder to create and test custom strategies.",
        "What's the best strategy?": "There's no 'best' strategy. It depends on market conditions and your goals.",
        "How long to learn?": "Basics: 1 week. Intermediate: 1 month. Advanced: 2-3 months with practice.",
        "Do I need coding knowledge?": "No! The app is designed for beginners with no coding required.",
        "Can I deploy this online?": "Yes! Deploy to Streamlit Cloud, Vercel, or Heroku.",
        "Is this suitable for kids?": "Yes! Check FOR_YOUR_SON.md for a kid-friendly guide.",
        "What if I make mistakes?": "Perfect! Mistakes are how you learn. No real money is at risk.",
        "Can I share my portfolio?": "Currently, portfolios are session-based. Export features coming soon!",
        "How often is data updated?": "Market data updates in real-time when you analyze stocks.",
        "What's the difference between modules?": "Each module teaches different aspects. Start with Basics and progress.",
        "Can I test multiple stocks?": "Yes! Portfolio Optimization module supports multiple stocks.",
        "Are there video tutorials?": "Yes! Check the Video Tutorials module for complete guides.",
        "Where can I get help?": "Check documentation files: START_HERE.md, QUICK_START_UNIFIED.md, etc."
    }
    
    for question, answer in faqs.items():
        with st.expander(f"Q: {question}", expanded=False):
            st.markdown(f"**A:** {answer}")
    
    # Quick Reference
    st.markdown("---")
    st.subheader("📋 Quick Reference")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🚀 Quick Commands
        
        **Launch App:**
        ```bash
        python launch_unified_app.py
        ```
        
        **Install Dependencies:**
        ```bash
        pip install -r requirements_unified.txt
        ```
        
        **Direct Streamlit:**
        ```bash
        streamlit run unified_investment_app.py
        ```
        """)
    
    with col2:
        st.markdown("""
        ### 📖 Documentation Files
        
        - **START_HERE.md** - Entry point
        - **FOR_YOUR_SON.md** - Kid-friendly
        - **QUICK_START_UNIFIED.md** - Quick ref
        - **UNIFIED_APP_GUIDE.md** - Complete guide
        - **VIDEO_TUTORIAL_SCRIPT.md** - Video guide
        """)
    
    # Contact & Support
    st.markdown("---")
    st.subheader("📞 Contact & Support")
    
    st.markdown("""
    ### Need More Help?
    
    1. **Check Documentation** - All guides included with app
    2. **Review Examples** - Try the sample strategies
    3. **Watch Videos** - See Video Tutorials module
    4. **Experiment** - Safe to try anything with virtual money
    
    ### Remember
    
    - This is for **education only**
    - **Not financial advice**
    - Always **consult professionals** before real trading
    - **Practice safely** with virtual money
    
    ### Happy Learning! 🎓📈
    """)

# Module 11: Video Tutorials
elif module == "🎥 Video Tutorials":
    st.header("🎥 Video Tutorial Guide")
    
    st.markdown("""
    ## Complete Video Tutorial Series
    
    Professional video tutorials to help you master the platform.
    """)
    
    # Video Series Overview
    st.subheader("📺 Video Series (8 Videos, ~57 minutes total)")
    
    videos = [
        {
            "title": "Video 1: Introduction & Setup",
            "duration": "5 minutes",
            "topics": ["Installation", "First launch", "Interface overview"],
            "difficulty": "Easy"
        },
        {
            "title": "Video 2: Learning the Basics",
            "duration": "8 minutes",
            "topics": ["What is a stock?", "Risk & return", "Taking quizzes"],
            "difficulty": "Easy"
        },
        {
            "title": "Video 3: Market Analysis",
            "duration": "7 minutes",
            "topics": ["Analyzing stocks", "Reading charts", "Technical indicators"],
            "difficulty": "Medium"
        },
        {
            "title": "Video 4: Building Your First Strategy",
            "duration": "10 minutes",
            "topics": ["Strategy basics", "Setting parameters", "Analyzing results"],
            "difficulty": "Medium"
        },
        {
            "title": "Video 5: Virtual Trading",
            "duration": "8 minutes",
            "topics": ["Starting portfolio", "Placing trades", "Managing positions"],
            "difficulty": "Medium"
        },
        {
            "title": "Video 6: Advanced Features",
            "duration": "12 minutes",
            "topics": ["Backtest Lab", "Walk-Forward", "Portfolio Optimization"],
            "difficulty": "Hard"
        },
        {
            "title": "Video 7: Tips & Best Practices",
            "duration": "5 minutes",
            "topics": ["Learning path", "Best practices", "Getting help"],
            "difficulty": "Easy"
        },
        {
            "title": "Video 8: Conclusion",
            "duration": "2 minutes",
            "topics": ["Recap", "Next steps", "Resources"],
            "difficulty": "Easy"
        }
    ]
    
    for i, video in enumerate(videos, 1):
        with st.expander(f"{video['title']} ({video['duration']})", expanded=False):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**Duration:** {video['duration']}")
                st.markdown(f"**Difficulty:** {video['difficulty']}")
                st.markdown("**Topics Covered:**")
                for topic in video['topics']:
                    st.markdown(f"- {topic}")
            
            with col2:
                st.info(f"📹 Video {i} of 8")
                st.markdown("*Video coming soon!*")
    
    # Quick Start Video
    st.markdown("---")
    st.subheader("⚡ Quick Start Video (10 minutes)")
    
    st.markdown("""
    For users who want a faster introduction:
    
    - **Installation** (1 min)
    - **Interface overview** (2 min)
    - **First stock analysis** (2 min)
    - **First strategy** (3 min)
    - **First trade** (2 min)
    
    *Perfect for getting started quickly!*
    """)
    
    # Video Production Info
    st.markdown("---")
    st.subheader("🎬 Video Production Information")
    
    with st.expander("For Content Creators", expanded=False):
        st.markdown("""
        ### Creating Your Own Tutorials
        
        Want to create video tutorials? Here's what you need:
        
        **Equipment:**
        - Screen recording software (OBS Studio, Camtasia)
        - Good microphone for narration
        - Video editing software (DaVinci Resolve, Adobe Premiere)
        
        **Recording Tips:**
        - Record in 1080p or 4K
        - Use 60 FPS for smooth animations
        - Record audio separately
        - Use cursor highlighting
        - Add zoom effects for details
        
        **Complete Script:**
        Check `VIDEO_TUTORIAL_SCRIPT.md` for the complete narration script,
        scene descriptions, and production notes.
        
        **Publishing:**
        - Upload to YouTube
        - Create playlist
        - Add timestamps
        - Include links to documentation
        - Enable captions
        """)
    
    # Interactive Demo
    st.markdown("---")
    st.subheader("🎮 Interactive Demo")
    
    st.markdown("""
    ### Try It Yourself!
    
    The best way to learn is by doing. Here's a quick interactive demo:
    """)
    
    demo_step = st.selectbox(
        "Choose a demo:",
        ["Select a demo...", "Analyze a Stock", "Build a Strategy", "Place a Trade"]
    )
    
    if demo_step == "Analyze a Stock":
        st.markdown("""
        ### 📊 Stock Analysis Demo
        
        **Step 1:** Go to "📊 Market Analysis" in the sidebar
        
        **Step 2:** Enter a stock ticker (try "AAPL")
        
        **Step 3:** Select time period (try "1y")
        
        **Step 4:** Click "Analyze Stock"
        
        **Step 5:** Explore the charts and metrics!
        
        *Try it now by clicking "📊 Market Analysis" in the sidebar!*
        """)
    
    elif demo_step == "Build a Strategy":
        st.markdown("""
        ### 🤖 Strategy Building Demo
        
        **Step 1:** Go to "🤖 Strategy Builder" in the sidebar
        
        **Step 2:** Enter a stock ticker (try "MSFT")
        
        **Step 3:** Adjust SMA periods (try 10 and 50)
        
        **Step 4:** Click "Test Strategy"
        
        **Step 5:** Review performance vs Buy & Hold!
        
        *Try it now by clicking "🤖 Strategy Builder" in the sidebar!*
        """)
    
    elif demo_step == "Place a Trade":
        st.markdown("""
        ### 💼 Virtual Trading Demo
        
        **Step 1:** Go to "💼 Portfolio Simulator" in the sidebar
        
        **Step 2:** Click the "Trade" tab
        
        **Step 3:** Enter a stock ticker (try "GOOGL")
        
        **Step 4:** Select "Buy" and enter 5 shares
        
        **Step 5:** Click "Execute Trade"
        
        **Step 6:** View your portfolio in the "Portfolio" tab!
        
        *Try it now by clicking "💼 Portfolio Simulator" in the sidebar!*
        """)
    
    # Additional Resources
    st.markdown("---")
    st.subheader("📚 Additional Resources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📖 Documentation
        
        - START_HERE.md
        - QUICK_START_UNIFIED.md
        - UNIFIED_APP_GUIDE.md
        - FOR_YOUR_SON.md
        - VIDEO_TUTORIAL_SCRIPT.md
        """)
    
    with col2:
        st.markdown("""
        ### 🔗 External Resources
        
        - Investopedia.com
        - Yahoo Finance
        - TradingView
        - Khan Academy (Finance)
        - Coursera (Investment courses)
        """)
    
    st.success("🎥 Video tutorials help you learn faster! Check back for updates.")

# Keep the original footer
# (Footer code remains at the very end)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>🎓 <strong>Investment Learning Platform</strong></p>
    <p>Combining FinRL, Backtesting.py, Lumibot, and VectorBT</p>
    <p>Built for educational purposes • Not financial advice</p>
</div>
""", unsafe_allow_html=True)
