#!/usr/bin/env python3
"""
One-Click Launcher for Unified Investment Learning Platform
"""

import subprocess
import sys
import os
import webbrowser
import time

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import streamlit
        import pandas
        import plotly
        import yfinance
        return True
    except ImportError:
        return False

def install_dependencies():
    """Install required packages"""
    print("📦 Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements_unified.txt"])
    print("✅ Dependencies installed!")

def launch_app():
    """Launch the Streamlit app"""
    print("🚀 Launching Investment Learning Platform...")
    print("📊 Opening browser...")
    
    # Open browser after a short delay
    def open_browser():
        time.sleep(2)
        webbrowser.open('http://localhost:8501')
    
    import threading
    threading.Thread(target=open_browser, daemon=True).start()
    
    # Launch Streamlit
    subprocess.run([sys.executable, "-m", "streamlit", "run", "unified_investment_app.py"])

if __name__ == "__main__":
    print("=" * 60)
    print("🎓 UNIFIED INVESTMENT LEARNING PLATFORM")
    print("=" * 60)
    print()
    
    # Check dependencies
    if not check_dependencies():
        print("⚠️  Dependencies not found")
        response = input("Install dependencies now? (y/n): ")
        if response.lower() == 'y':
            install_dependencies()
        else:
            print("❌ Cannot launch without dependencies")
            sys.exit(1)
    
    # Launch app
    try:
        launch_app()
    except KeyboardInterrupt:
        print("\n👋 Shutting down...")
    except Exception as e:
        print(f"❌ Error: {e}")
        input("Press Enter to exit...")
