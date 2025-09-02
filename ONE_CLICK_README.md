# 🚀 One-Click Backtesting.py Demo

This repository contains a ready-to-run demo of the [backtesting.py](https://github.com/kernc/backtesting.py) library, making it easy to explore algorithmic trading strategies with just one click!

## 📋 What You'll Get

- **Interactive backtesting demo** with Google stock data (2004-2013)
- **SMA Crossover strategy** demonstration
- **Beautiful interactive charts** in your browser
- **Comprehensive trading statistics**
- **One-click execution** for Windows users

## 🎯 Quick Start (One-Click)

### Option 1: Windows Batch File (Easiest)
1. **Double-click** `run_backtesting_demo.bat`
2. Press any key when prompted
3. Watch the magic happen! 🎉

### Option 2: PowerShell Script (Recommended)
1. **Right-click** `run_backtesting_demo.ps1`
2. Select **"Run with PowerShell"**
3. Press any key when prompted
4. Enjoy the interactive demo! 🚀

### Option 3: Direct Python Execution
```bash
python demo_backtesting.py
```

## 📊 What the Demo Shows

The demo runs a **Simple Moving Average (SMA) Crossover** strategy on Google stock data:

- **Fast SMA**: 10-period moving average
- **Slow SMA**: 20-period moving average
- **Buy Signal**: When fast SMA crosses above slow SMA
- **Sell Signal**: When fast SMA crosses below slow SMA
- **Commission**: 0.2% per trade

## 📈 Expected Results

You'll see comprehensive trading statistics including:
- Total return and annualized return
- Sharpe ratio and maximum drawdown
- Number of trades and win rate
- Interactive chart with price, indicators, and trades

## 🔧 Requirements

- **Python 3.9+** (already installed if you're running this)
- **Internet connection** (for the interactive plot)

## 📁 Files Included

- `demo_backtesting.py` - Main demo script
- `run_backtesting_demo.bat` - Windows batch file for one-click execution
- `run_backtesting_demo.ps1` - PowerShell script with better error handling
- `ONE_CLICK_README.md` - This file

## 🛠️ Troubleshooting

### If the batch file doesn't work:
1. Try the PowerShell script instead
2. Make sure Python is installed and in your PATH
3. Run `python --version` to verify Python is available

### If you get import errors:
1. Make sure you're in the correct directory
2. The script automatically adds the current directory to Python path
3. All required dependencies should be installed automatically

### If the plot doesn't open:
1. Check your browser settings
2. The plot should open automatically in your default browser
3. Look for a new browser tab with the interactive chart

## 🎓 Learning More

After running the demo, explore these resources:

- **[Official Documentation](https://kernc.github.io/backtesting.py/)** - Complete guide
- **[GitHub Repository](https://github.com/kernc/backtesting.py)** - Source code
- **[Examples Directory](doc/examples/)** - More strategy examples

## 🔍 Understanding the Strategy

The SMA Crossover strategy is a classic technical analysis approach:

1. **Trend Following**: Identifies and follows market trends
2. **Signal Generation**: Clear buy/sell signals based on moving average crossovers
3. **Risk Management**: Built-in stop-loss through trend reversal signals

## 🚀 Next Steps

Once you've run the demo, try:
1. Modifying the strategy parameters in `demo_backtesting.py`
2. Testing with different datasets (BTCUSD, EURUSD)
3. Creating your own custom strategies
4. Exploring the optimization features

## 📞 Support

If you encounter any issues:
1. Check the [official backtesting.py issues](https://github.com/kernc/backtesting.py/issues)
2. Ensure all dependencies are installed
3. Verify Python version compatibility

---

**Happy Backtesting! 📈💰**
