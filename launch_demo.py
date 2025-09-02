#!/usr/bin/env python3
"""
Simple launcher for the backtesting demo
Run this file to start the demo with a nice welcome message
"""

import os
import sys
import subprocess

def main():
    print("🎉 Welcome to Backtesting.py Demo!")
    print("=" * 50)
    print()
    print("This will run a complete backtesting demonstration")
    print("with Google stock data and an SMA crossover strategy.")
    print()
    print("📊 You'll see:")
    print("   • Trading statistics and performance metrics")
    print("   • Interactive charts (if plotting works)")
    print("   • Complete strategy analysis")
    print()
    
    # Check if demo file exists
    demo_file = "demo_backtesting.py"
    if not os.path.exists(demo_file):
        print(f"❌ Error: {demo_file} not found!")
        print("Please make sure you're in the correct directory.")
        return 1
    
    print("🚀 Starting demo...")
    print("-" * 50)
    print()
    
    try:
        # Run the demo script
        result = subprocess.run([sys.executable, demo_file], 
                              capture_output=False, 
                              text=True)
        return result.returncode
    except Exception as e:
        print(f"❌ Error launching demo: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
