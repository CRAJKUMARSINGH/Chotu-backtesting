#!/usr/bin/env python3
"""
Web App Launcher for Backtesting.py
====================================

This script launches the Streamlit web application locally.
Perfect for testing before deployment.
"""

import os
import sys
import subprocess
import webbrowser
import time

def main():
    print("🚀 Launching Backtesting.py Web Application")
    print("=" * 50)
    print()
    print("This will start the Streamlit web interface.")
    print("The app will open in your default browser.")
    print()
    
    # Check if streamlit app exists
    app_file = "streamlit_app.py"
    if not os.path.exists(app_file):
        print(f"❌ Error: {app_file} not found!")
        print("Please make sure you're in the correct directory.")
        return 1
    
    # Check if requirements are installed
    try:
        import streamlit
        import plotly
        print("✅ Dependencies found")
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: pip install -r requirements_web.txt")
        return 1
    
    print("🌐 Starting Streamlit server...")
    print("📱 The app will open at: http://localhost:8501")
    print()
    print("💡 To stop the server, press Ctrl+C")
    print("-" * 50)
    
    try:
        # Start Streamlit
        process = subprocess.Popen([
            sys.executable, "-m", "streamlit", "run", app_file,
            "--server.headless", "true",
            "--server.port", "8501"
        ])
        
        # Wait a moment for the server to start
        time.sleep(3)
        
        # Open browser
        try:
            webbrowser.open("http://localhost:8501")
            print("✅ Browser opened automatically")
        except:
            print("💡 Please manually open: http://localhost:8501")
        
        print("\n🎉 Web app is running!")
        print("📊 You can now:")
        print("   • Select different datasets")
        print("   • Adjust strategy parameters")
        print("   • Run backtests interactively")
        print("   • View detailed results and charts")
        
        # Wait for the process to complete
        process.wait()
        
    except KeyboardInterrupt:
        print("\n🛑 Stopping server...")
        process.terminate()
        print("✅ Server stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
