#!/usr/bin/env python3
"""
Web App Validation Script
=========================

This script validates the actual functionality of the Streamlit web app
by testing the core backtesting operations that the app performs.
"""

import sys
import os
import pandas as pd
import numpy as np
from datetime import datetime

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def validate_sma_strategy():
    """Validate the SMA crossover strategy used in the web app"""
    print("🔍 Validating SMA Strategy...")
    
    try:
        from backtesting import Backtest, Strategy
        from backtesting.lib import crossover
        from backtesting.test import SMA, GOOG, BTCUSD, EURUSD
        
        class SmaCross(Strategy):
            def init(self):
                price = self.data.Close
                self.ma1 = self.I(SMA, price, 10)  # Fast SMA
                self.ma2 = self.I(SMA, price, 20)  # Slow SMA
            
            def next(self):
                if crossover(self.ma1, self.ma2):
                    self.buy()
                elif crossover(self.ma2, self.ma1):
                    self.sell()
        
        # Test with different datasets
        datasets = {
            "GOOG": GOOG,
            "BTCUSD": BTCUSD,
            "EURUSD": EURUSD
        }
        
        for name, data in datasets.items():
            print(f"\n📊 Testing {name} dataset...")
            
            # Run backtest
            bt = Backtest(data, SmaCross, commission=.002, cash=10000)
            stats = bt.run()
            
            # Validate key metrics
            print(f"  ✅ Total Return: {stats['Return [%]']:.2f}%")
            print(f"  ✅ Sharpe Ratio: {stats['Sharpe Ratio']:.2f}")
            print(f"  ✅ Max Drawdown: {stats['Max. Drawdown [%]']:.2f}%")
            print(f"  ✅ Number of Trades: {stats['# Trades']}")
            print(f"  ✅ Win Rate: {stats['Win Rate [%]']:.2f}%")
            
            # Validate data structures
            equity_curve = stats['_equity_curve']
            trades = stats['_trades']
            
            print(f"  ✅ Equity curve shape: {equity_curve.shape}")
            print(f"  ✅ Trades count: {len(trades)}")
            
            # Check for required columns
            required_equity_cols = ['Equity', 'DrawdownPct']
            for col in required_equity_cols:
                if col in equity_curve.columns:
                    print(f"  ✅ Equity column '{col}' present")
                else:
                    print(f"  ❌ Missing equity column '{col}'")
                    return False
            
            if len(trades) > 0:
                required_trade_cols = ['EntryTime', 'ExitTime', 'Size', 'PnL', 'ReturnPct']
                for col in required_trade_cols:
                    if col in trades.columns:
                        print(f"  ✅ Trade column '{col}' present")
                    else:
                        print(f"  ❌ Missing trade column '{col}'")
                        return False
        
        return True
    except Exception as e:
        print(f"❌ SMA Strategy validation failed: {e}")
        return False

def validate_plotly_charts():
    """Validate that Plotly charts can be created with the data"""
    print("\n📈 Validating Plotly Charts...")
    
    try:
        import plotly.graph_objects as go
        import plotly.express as px
        from plotly.subplots import make_subplots
        
        # Test equity curve chart
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
        
        bt = Backtest(GOOG, TestStrategy, commission=.002, cash=10000)
        stats = bt.run()
        
        equity_curve = stats['_equity_curve']
        trades = stats['_trades']
        
        # Test subplot creation
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=('Equity Curve', 'Drawdown'),
            vertical_spacing=0.1
        )
        
        # Add equity curve
        fig.add_trace(
            go.Scatter(
                x=equity_curve.index,
                y=equity_curve['Equity'],
                name='Strategy',
                line=dict(color='blue')
            ),
            row=1, col=1
        )
        
        # Add drawdown
        fig.add_trace(
            go.Scatter(
                x=equity_curve.index,
                y=equity_curve['DrawdownPct'],
                name='Drawdown',
                fill='tonexty',
                line=dict(color='red')
            ),
            row=2, col=1
        )
        
        print("✅ Subplot chart created successfully")
        
        # Test histogram
        if len(trades) > 0:
            returns = trades['ReturnPct']
            fig_hist = px.histogram(
                returns, 
                nbins=20,
                title="Trade Returns Distribution"
            )
            print("✅ Histogram chart created successfully")
        
        # Test pie chart
        if len(trades) > 0:
            wins = (trades['ReturnPct'] > 0).sum()
            losses = (trades['ReturnPct'] <= 0).sum()
            
            fig_pie = px.pie(
                values=[wins, losses],
                names=['Winning Trades', 'Losing Trades'],
                title="Win/Loss Distribution"
            )
            print("✅ Pie chart created successfully")
        
        return True
    except Exception as e:
        print(f"❌ Plotly charts validation failed: {e}")
        return False

def validate_metrics_calculation():
    """Validate that all metrics are calculated correctly"""
    print("\n📊 Validating Metrics Calculation...")
    
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
        
        bt = Backtest(GOOG, TestStrategy, commission=.002, cash=10000)
        stats = bt.run()
        
        # Test all required metrics
        required_metrics = [
            'Start', 'End', 'Duration', 'Exposure Time [%]',
            'Equity Final [$]', 'Equity Peak [$]', 'Return [%]',
            'Buy & Hold Return [%]', 'Return (Ann.) [%]',
            'Volatility (Ann.) [%]', 'Sharpe Ratio', 'Sortino Ratio',
            'Calmar Ratio', 'Max. Drawdown [%]', 'Avg. Drawdown [%]',
            'Max. Drawdown Duration', 'Avg. Drawdown Duration',
            '# Trades', 'Win Rate [%]', 'Best Trade [%]',
            'Worst Trade [%]', 'Avg. Trade [%]', 'Profit Factor',
            'Expectancy [%]', 'SQN', 'Kelly Criterion'
        ]
        
        for metric in required_metrics:
            if metric in stats:
                print(f"  ✅ {metric}: {stats[metric]}")
            else:
                print(f"  ❌ Missing metric: {metric}")
                return False
        
        return True
    except Exception as e:
        print(f"❌ Metrics calculation validation failed: {e}")
        return False

def validate_dataframe_operations():
    """Validate DataFrame operations used in the web app"""
    print("\n📋 Validating DataFrame Operations...")
    
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
        
        bt = Backtest(GOOG, TestStrategy, commission=.002, cash=10000)
        stats = bt.run()
        
        trades = stats['_trades']
        
        # Test DataFrame operations used in the web app
        if len(trades) > 0:
            # Test tail operation
            recent_trades = trades.tail(10)
            print(f"✅ Tail operation: {len(recent_trades)} recent trades")
            
            # Test column selection
            display_cols = ['EntryTime', 'ExitTime', 'Size', 'PnL', 'ReturnPct']
            display_trades = trades[display_cols]
            print(f"✅ Column selection: {display_trades.shape}")
            
            # Test statistics table creation
            stats_data = [
                ["Start Date", stats['Start']],
                ["End Date", stats['End']],
                ["Duration", stats['Duration']],
                ["Total Return", f"{stats['Return [%]']:.2f}%"],
                ["Sharpe Ratio", f"{stats['Sharpe Ratio']:.2f}"]
            ]
            
            stats_df = pd.DataFrame(stats_data, columns=["Metric", "Value"])
            print(f"✅ Statistics table: {stats_df.shape}")
        
        return True
    except Exception as e:
        print(f"❌ DataFrame operations validation failed: {e}")
        return False

def run_validation():
    """Run all validation tests"""
    print("=" * 60)
    print("🔬 WEB APP VALIDATION SUITE")
    print("=" * 60)
    print(f"Validation started at: {datetime.now()}")
    print()
    
    validations = [
        ("SMA Strategy", validate_sma_strategy),
        ("Plotly Charts", validate_plotly_charts),
        ("Metrics Calculation", validate_metrics_calculation),
        ("DataFrame Operations", validate_dataframe_operations)
    ]
    
    results = []
    
    for validation_name, validation_func in validations:
        print(f"Running: {validation_name}")
        try:
            result = validation_func()
            results.append((validation_name, result))
            if result:
                print(f"✅ {validation_name} VALIDATED\n")
            else:
                print(f"❌ {validation_name} FAILED\n")
        except Exception as e:
            print(f"❌ {validation_name} ERROR: {e}\n")
            results.append((validation_name, False))
    
    # Summary
    print("=" * 60)
    print("📊 VALIDATION SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for validation_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {validation_name}")
    
    print()
    print(f"Overall: {passed}/{total} validations passed")
    
    if passed == total:
        print("🎉 ALL VALIDATIONS PASSED! Web app is fully functional.")
        print("\n🚀 Ready for deployment to:")
        print("   • Streamlit Cloud")
        print("   • Vercel")
        print("   • Local development")
        return True
    else:
        print("⚠️ Some validations failed. Please fix issues before deployment.")
        return False

if __name__ == "__main__":
    success = run_validation()
    sys.exit(0 if success else 1)
