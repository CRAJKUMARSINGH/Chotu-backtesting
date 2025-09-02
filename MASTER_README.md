# 🚀 Backtesting.py - Complete Demo Suite

A comprehensive demonstration of the [backtesting.py](https://github.com/kernc/backtesting.py) library with multiple deployment options and user interfaces.

## 📋 What's Included

This repository provides **4 different ways** to run the backtesting.py demo:

1. **🌐 Web Application** - Interactive Streamlit web app
2. **💻 Command Line** - Simple Python scripts
3. **🖥️ Windows GUI** - One-click batch files
4. **📱 Cloud Deployment** - Ready for Vercel/Streamlit Cloud

## 🎯 Quick Start Guide

### Option 1: Web Application (Recommended)
```bash
# Install dependencies
pip install -r requirements_web.txt

# Launch web app
python launch_web_app.py
```
**Features:** Interactive interface, multiple datasets, real-time parameter adjustment

### Option 2: Command Line Demo
```bash
# Run the basic demo
python demo_backtesting.py

# Or use the launcher
python launch_demo.py
```
**Features:** Quick results, console output, simple execution

### Option 3: Windows One-Click
- **Double-click:** `run_backtesting_demo.bat`
- **Right-click:** `run_backtesting_demo.ps1` → "Run with PowerShell"
**Features:** No command line needed, perfect for beginners

### Option 4: Cloud Deployment
- **Streamlit Cloud:** Follow `DEPLOYMENT_GUIDE.md`
- **Vercel:** Use the included `vercel.json`
**Features:** Shareable URL, no local setup required

## 📊 Demo Strategy

All demos showcase a **Simple Moving Average (SMA) Crossover** strategy:

- **Fast SMA:** 10-period moving average
- **Slow SMA:** 20-period moving average
- **Buy Signal:** Fast SMA crosses above slow SMA
- **Sell Signal:** Fast SMA crosses below slow SMA
- **Datasets:** Google (GOOG), Bitcoin (BTCUSD), EUR/USD

## 📁 File Structure

```
backtesting/
├── 🌐 Web Application
│   ├── streamlit_app.py          # Main web app
│   ├── launch_web_app.py         # Web app launcher
│   ├── requirements_web.txt      # Web dependencies
│   ├── vercel.json               # Vercel config
│   └── .streamlit/config.toml    # Streamlit config
│
├── 💻 Command Line
│   ├── demo_backtesting.py       # Basic demo script
│   ├── launch_demo.py            # Demo launcher
│   └── QUICK_START.txt           # Quick reference
│
├── 🖥️ Windows GUI
│   ├── run_backtesting_demo.bat  # Batch file
│   └── run_backtesting_demo.ps1  # PowerShell script
│
├── 📚 Documentation
│   ├── MASTER_README.md          # This file
│   ├── ONE_CLICK_README.md       # One-click guide
│   └── DEPLOYMENT_GUIDE.md       # Deployment guide
│
└── 📦 Backtesting Library
    └── backtesting/              # Core library files
```

## 🚀 Detailed Usage

### Web Application Features

The Streamlit web app provides:

- **📊 Multiple Datasets:** Google, Bitcoin, EUR/USD
- **⚙️ Interactive Parameters:** Adjust SMA periods, commission, initial cash
- **📈 Rich Visualizations:** Equity curves, drawdown charts, trade analysis
- **📋 Comprehensive Results:** 20+ performance metrics
- **💾 Export Capabilities:** Results can be saved and shared

### Command Line Features

The command line demos provide:

- **⚡ Fast Execution:** Quick backtest results
- **📊 Key Metrics:** Essential performance statistics
- **🎯 Simple Interface:** Easy to understand output
- **🔧 Customizable:** Easy to modify strategy parameters

### Windows GUI Features

The Windows launchers provide:

- **🖱️ One-Click:** No command line knowledge required
- **🎨 User-Friendly:** Clear instructions and feedback
- **🛠️ Error Handling:** Helpful error messages
- **📱 Browser Integration:** Automatic plot opening

## 🔧 Requirements

### System Requirements
- **Python:** 3.9 or higher
- **OS:** Windows, macOS, or Linux
- **Browser:** For web application (Chrome, Firefox, Safari, Edge)

### Dependencies
- **Core:** numpy, pandas, bokeh
- **Web:** streamlit, plotly
- **Optional:** matplotlib, scikit-learn

## 📈 Expected Results

All demos will show comprehensive trading statistics:

- **Total Return:** Strategy performance vs buy & hold
- **Risk Metrics:** Sharpe ratio, maximum drawdown
- **Trade Analysis:** Number of trades, win rate, profit factor
- **Visualizations:** Equity curves, trade distributions

## 🛠️ Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   pip install -r requirements_web.txt
   ```

2. **Port Already in Use**
   ```bash
   # Change port in launch_web_app.py
   streamlit run streamlit_app.py --server.port 8502
   ```

3. **Missing Dependencies**
   ```bash
   pip install streamlit plotly numpy pandas bokeh
   ```

4. **Windows Execution Policy**
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

### Getting Help

1. **Check Logs:** Look for error messages in the output
2. **Test Locally:** Try the command line version first
3. **Verify Dependencies:** Ensure all packages are installed
4. **Check Python Version:** Must be 3.9+

## 🎓 Learning Resources

### Official Documentation
- **[Backtesting.py Docs](https://kernc.github.io/backtesting.py/)**
- **[Streamlit Docs](https://docs.streamlit.io/)**
- **[GitHub Repository](https://github.com/kernc/backtesting.py)**

### Examples and Tutorials
- **Strategy Examples:** Check `doc/examples/` folder
- **Web App Customization:** Modify `streamlit_app.py`
- **Strategy Development:** Create your own strategies

## 🔄 Updates and Maintenance

### Keeping Updated
1. **Pull Latest Changes:** `git pull origin main`
2. **Update Dependencies:** `pip install -r requirements_web.txt --upgrade`
3. **Test All Methods:** Verify each deployment option works

### Contributing
1. **Fork the Repository:** Create your own copy
2. **Make Changes:** Add features or fix bugs
3. **Test Thoroughly:** Ensure all methods still work
4. **Submit Pull Request:** Share your improvements

## 📞 Support and Community

### Getting Help
- **Issues:** [GitHub Issues](https://github.com/kernc/backtesting.py/issues)
- **Discussions:** [GitHub Discussions](https://github.com/kernc/backtesting.py/discussions)
- **Documentation:** [Official Docs](https://kernc.github.io/backtesting.py/)

### Community Resources
- **Examples:** Browse the examples folder
- **Tutorials:** Follow the quick start guides
- **Forums:** Join the community discussions

## 🎉 Success Stories

Once you've mastered the demos, you can:

- ✅ **Create Custom Strategies:** Build your own trading algorithms
- ✅ **Analyze Real Data:** Test on your own financial datasets
- ✅ **Optimize Parameters:** Find the best strategy settings
- ✅ **Share Results:** Deploy your own web applications
- ✅ **Build Portfolios:** Combine multiple strategies

## 📄 License

This demo suite is based on the [backtesting.py](https://github.com/kernc/backtesting.py) library, which is licensed under AGPL-3.0.

---

**Happy Backtesting! 📈💰**

*Built with ❤️ using [backtesting.py](https://github.com/kernc/backtesting.py) and [Streamlit](https://streamlit.io)*
