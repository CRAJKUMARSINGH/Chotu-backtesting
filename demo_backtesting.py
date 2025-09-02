#!/usr/bin/env python3
"""
One-Click Backtesting Demo
==========================

This script demonstrates the backtesting.py library with a simple SMA crossover strategy.
Just run this file to see the backtesting in action!

Based on: https://github.com/kernc/backtesting.py
"""

import sys
import os

# Add the current directory to Python path so we can import the backtesting module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from backtesting import Backtest, Strategy
    from backtesting.lib import crossover
    from backtesting.test import SMA, GOOG
except ImportError as e:
    print(f"Error importing backtesting module: {e}")
    print("Please make sure you're in the correct directory with the backtesting package.")
    sys.exit(1)


class SmaCross(Strategy):
    """
    Simple Moving Average Crossover Strategy
    
    This strategy buys when the fast SMA crosses above the slow SMA
    and sells when the fast SMA crosses below the slow SMA.
    """
    
    # Define strategy parameters
    n1 = 10  # Fast SMA period
    n2 = 20  # Slow SMA period
    
    def init(self):
        """Initialize the strategy indicators"""
        price = self.data.Close
        self.ma1 = self.I(SMA, price, self.n1)  # Fast SMA
        self.ma2 = self.I(SMA, price, self.n2)  # Slow SMA
    
    def next(self):
        """Execute strategy logic on each bar"""
        if crossover(self.ma1, self.ma2):
            # Fast SMA crosses above slow SMA - BUY signal
            self.buy()
        elif crossover(self.ma2, self.ma1):
            # Fast SMA crosses below slow SMA - SELL signal
            self.sell()


def main():
    """Main function to run the backtest"""
    print("=" * 60)
    print("🚀 BACKTESTING.PY DEMO - SMA CROSSOVER STRATEGY")
    print("=" * 60)
    print()
    print("📊 Using Google (GOOG) stock data from 2004-2013")
    print("📈 Strategy: Simple Moving Average Crossover")
    print("   - Fast SMA: 10 periods")
    print("   - Slow SMA: 20 periods")
    print("   - Commission: 0.2% per trade")
    print()
    
    try:
        # Create and run the backtest
        bt = Backtest(GOOG, SmaCross, 
                     commission=.002,  # 0.2% commission
                     exclusive_orders=True,
                     finalize_trades=True)  # Close any open trades at the end
        
        print("🔄 Running backtest...")
        stats = bt.run()
        
        print("\n" + "=" * 60)
        print("📊 BACKTEST RESULTS")
        print("=" * 60)
        
        # Display key statistics
        print(f"📅 Start Date: {stats['Start']}")
        print(f"📅 End Date: {stats['End']}")
        print(f"⏱️  Duration: {stats['Duration']}")
        print(f"💰 Final Equity: ${stats['Equity Final [$]']:,.2f}")
        print(f"📈 Total Return: {stats['Return [%]']:.2f}%")
        print(f"📉 Buy & Hold Return: {stats['Buy & Hold Return [%]']:.2f}%")
        print(f"📊 Annual Return: {stats['Return (Ann.) [%]']:.2f}%")
        print(f"📊 Sharpe Ratio: {stats['Sharpe Ratio']:.2f}")
        print(f"📊 Max Drawdown: {stats['Max. Drawdown [%]']:.2f}%")
        print(f"🔄 Number of Trades: {stats['# Trades']}")
        print(f"🎯 Win Rate: {stats['Win Rate [%]']:.2f}%")
        print(f"📊 Profit Factor: {stats['Profit Factor']:.2f}")
        
        print("\n" + "=" * 60)
        print("📈 GENERATING INTERACTIVE PLOT...")
        print("=" * 60)
        print("💡 The plot will open in your browser.")
        print("   You can interact with it to zoom, pan, and explore the results.")
        print("   Close the browser tab when you're done.")
        
        # Generate the interactive plot
        try:
            bt.plot()
        except Exception as plot_error:
            print(f"⚠️  Plot generation failed: {plot_error}")
            print("📊 The backtest results above are still valid!")
            print("💡 You can view the results in the console output above.")
        
        print("\n✅ Demo completed successfully!")
        print("🎉 You can now explore the backtesting.py library!")
        
    except Exception as e:
        print(f"\n❌ Error running backtest: {e}")
        print("Please check your installation and try again.")
        return 1
    
    return 0


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
