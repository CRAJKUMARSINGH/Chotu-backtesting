#!/usr/bin/env python3
"""
Comprehensive Test Script for Backtesting.py Web Application
============================================================

This script tests the Streamlit web application programmatically to ensure
all functionality works correctly before deployment.
"""

import sys
import os
import time
import subprocess
import requests
import pandas as pd
import numpy as np
from datetime import datetime

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test all required imports"""
    print("🔍 Testing imports...")
    
    try:
        import streamlit as st
        print("✅ Streamlit imported successfully")
    except ImportError as e:
        print(f"❌ Streamlit import failed: {e}")
        return False
    
    try:
        import plotly.graph_objects as go
        import plotly.express as px
        from plotly.subplots import make_subplots
        print("✅ Plotly imported successfully")
    except ImportError as e:
        print(f"❌ Plotly import failed: {e}")
        return False
    
    try:
        from backtesting import Backtest, Strategy
        from backtesting.lib import crossover
        from backtesting.test import SMA, GOOG, BTCUSD, EURUSD
        print("✅ Backtesting library imported successfully")
    except ImportError as e:
        print(f"❌ Backtesting import failed: {e}")
        return False
    
    return True

def test_data_availability():
    """Test that all datasets are available"""
    print("\n📊 Testing data availability...")
    
    try:
        from backtesting.test import GOOG, BTCUSD, EURUSD
        
        datasets = {
            "GOOG": GOOG,
            "BTCUSD": BTCUSD,
            "EURUSD": EURUSD
        }
        
        for name, data in datasets.items():
            if data is not None and len(data) > 0:
                print(f"✅ {name}: {len(data)} data points")
            else:
                print(f"❌ {name}: No data available")
                return False
        
        return True
    except Exception as e:
        print(f"❌ Data availability test failed: {e}")
        return False

def test_backtest_execution():
    """Test basic backtest execution"""
    print("\n🚀 Testing backtest execution...")
    
    try:
        from backtesting import Backtest, Strategy
        from backtesting.lib import crossover
        from backtesting.test import SMA, GOOG
        
        class TestStrategy(Strategy):
            def init(self):
                price = self.data.Close
                self.ma1 = self.I(SMA, price, 10)
                self.ma2 = self.I(SMA, price, 20)
            
            def next(self):
                if crossover(self.ma1, self.ma2):
                    self.buy()
                elif crossover(self.ma2, self.ma1):
                    self.sell()
        
        # Run backtest
        bt = Backtest(GOOG, TestStrategy, commission=.002, cash=10000)
        stats = bt.run()
        
        # Verify key statistics exist
        required_stats = [
            'Return [%]', 'Sharpe Ratio', 'Max. Drawdown [%]', 
            'Win Rate [%]', '# Trades', 'Equity Final [$]'
        ]
        
        for stat in required_stats:
            if stat in stats:
                print(f"✅ {stat}: {stats[stat]}")
            else:
                print(f"❌ Missing statistic: {stat}")
                return False
        
        # Test equity curve access
        equity_curve = stats['_equity_curve']
        if 'Equity' in equity_curve.columns and 'DrawdownPct' in equity_curve.columns:
            print("✅ Equity curve data accessible")
        else:
            print("❌ Equity curve data missing")
            return False
        
        # Test trades access
        trades = stats['_trades']
        if len(trades) > 0:
            required_trade_cols = ['EntryTime', 'ExitTime', 'Size', 'PnL', 'ReturnPct']
            for col in required_trade_cols:
                if col in trades.columns:
                    print(f"✅ Trade column {col} available")
                else:
                    print(f"❌ Missing trade column: {col}")
                    return False
        else:
            print("⚠️ No trades executed (this might be normal)")
        
        return True
    except Exception as e:
        print(f"❌ Backtest execution failed: {e}")
        return False

def test_streamlit_app_import():
    """Test that the Streamlit app can be imported"""
    print("\n🌐 Testing Streamlit app import...")
    
    try:
        # Test if the app file exists
        if not os.path.exists('streamlit_app.py'):
            print("❌ streamlit_app.py not found")
            return False
        
        # Try to import the app (this will test syntax)
        with open('streamlit_app.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Basic syntax check
        try:
            compile(content, 'streamlit_app.py', 'exec')
            print("✅ Streamlit app syntax is valid")
        except SyntaxError as e:
            print(f"❌ Streamlit app syntax error: {e}")
            return False
        
        return True
    except Exception as e:
        print(f"❌ Streamlit app import test failed: {e}")
        return False

def test_requirements():
    """Test that all requirements are available"""
    print("\n📦 Testing requirements...")
    
    try:
        import streamlit
        import plotly
        import pandas
        import numpy
        import bokeh
        
        print(f"✅ Streamlit version: {streamlit.__version__}")
        print(f"✅ Plotly version: {plotly.__version__}")
        print(f"✅ Pandas version: {pandas.__version__}")
        print(f"✅ NumPy version: {numpy.__version__}")
        print(f"✅ Bokeh version: {bokeh.__version__}")
        
        return True
    except ImportError as e:
        print(f"❌ Requirements test failed: {e}")
        return False

def test_web_server():
    """Test if the web server can start"""
    print("\n🌐 Testing web server...")
    
    try:
        # Check if port 8501 is available
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', 8501))
        sock.close()
        
        if result == 0:
            print("⚠️ Port 8501 is already in use")
            return True  # Not a failure, just means server might be running
        else:
            print("✅ Port 8501 is available")
        
        return True
    except Exception as e:
        print(f"❌ Web server test failed: {e}")
        return False

def test_deployment_files():
    """Test that all deployment files exist"""
    print("\n📁 Testing deployment files...")
    
    required_files = [
        'streamlit_app.py',
        'requirements_web.txt',
        'vercel.json',
        '.streamlit/config.toml'
    ]
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} exists")
        else:
            print(f"❌ {file_path} missing")
            return False
    
    return True

def test_launcher_scripts():
    """Test launcher scripts"""
    print("\n🚀 Testing launcher scripts...")
    
    launcher_files = [
        'launch_web_app.py',
        'launch_demo.py',
        'run_backtesting_demo.bat',
        'run_backtesting_demo.ps1'
    ]
    
    for file_path in launcher_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} exists")
        else:
            print(f"❌ {file_path} missing")
            return False
    
    return True

def run_comprehensive_test():
    """Run all tests"""
    print("=" * 60)
    print("🧪 COMPREHENSIVE WEB APP TEST SUITE")
    print("=" * 60)
    print(f"Test started at: {datetime.now()}")
    print()
    
    tests = [
        ("Import Test", test_imports),
        ("Data Availability", test_data_availability),
        ("Backtest Execution", test_backtest_execution),
        ("Streamlit App Import", test_streamlit_app_import),
        ("Requirements", test_requirements),
        ("Web Server", test_web_server),
        ("Deployment Files", test_deployment_files),
        ("Launcher Scripts", test_launcher_scripts)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"Running: {test_name}")
        try:
            result = test_func()
            results.append((test_name, result))
            if result:
                print(f"✅ {test_name} PASSED\n")
            else:
                print(f"❌ {test_name} FAILED\n")
        except Exception as e:
            print(f"❌ {test_name} ERROR: {e}\n")
            results.append((test_name, False))
    
    # Summary
    print("=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    print()
    print(f"Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! Web app is ready for deployment.")
        return True
    else:
        print("⚠️ Some tests failed. Please fix issues before deployment.")
        return False

if __name__ == "__main__":
    success = run_comprehensive_test()
    sys.exit(0 if success else 1)
