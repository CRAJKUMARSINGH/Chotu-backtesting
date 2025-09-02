#!/usr/bin/env python3
"""
Deployment Script for Backtesting.py Web Application
===================================================

This script provides step-by-step instructions for deploying the web app
to various cloud platforms.
"""

import os
import sys
import subprocess
from datetime import datetime

def check_git_status():
    """Check if this is a git repository"""
    try:
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            return True
        else:
            return False
    except FileNotFoundError:
        return False

def check_required_files():
    """Check that all required files exist"""
    required_files = [
        'streamlit_app.py',
        'requirements_web.txt',
        'vercel.json',
        '.streamlit/config.toml'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    return missing_files

def deploy_to_streamlit_cloud():
    """Instructions for Streamlit Cloud deployment"""
    print("\n" + "="*60)
    print("🚀 DEPLOYMENT TO STREAMLIT CLOUD")
    print("="*60)
    
    print("\n📋 Step-by-Step Instructions:")
    print("1. 📁 Ensure all files are committed to Git")
    print("2. 🌐 Go to https://share.streamlit.io")
    print("3. 🔐 Sign in with your GitHub account")
    print("4. ➕ Click 'New app'")
    print("5. 📂 Select your repository")
    print("6. 📄 Set main file path to: streamlit_app.py")
    print("7. 📦 Set requirements file to: requirements_web.txt")
    print("8. 🚀 Click 'Deploy!'")
    
    print("\n✅ Your app will be available at:")
    print("   https://your-app-name-your-username.streamlit.app")
    
    print("\n💡 Tips:")
    print("   • Free tier available")
    print("   • Automatic deployments on Git push")
    print("   • Custom domain support")
    print("   • Password protection available")

def deploy_to_vercel():
    """Instructions for Vercel deployment"""
    print("\n" + "="*60)
    print("🚀 DEPLOYMENT TO VERCEL")
    print("="*60)
    
    print("\n📋 Step-by-Step Instructions:")
    print("1. 📁 Ensure all files are committed to Git")
    print("2. 🌐 Go to https://vercel.com")
    print("3. 🔐 Sign in with your GitHub account")
    print("4. ➕ Click 'New Project'")
    print("5. 📂 Import your repository")
    print("6. ⚙️ Configure project settings:")
    print("   • Framework Preset: Other")
    print("   • Build Command: pip install -r requirements_web.txt")
    print("   • Output Directory: .")
    print("7. 🚀 Click 'Deploy'")
    
    print("\n✅ Your app will be available at:")
    print("   https://your-app-name.vercel.app")
    
    print("\n💡 Tips:")
    print("   • Free tier available")
    print("   • Automatic deployments on Git push")
    print("   • Custom domain support")
    print("   • Edge functions available")

def deploy_to_heroku():
    """Instructions for Heroku deployment"""
    print("\n" + "="*60)
    print("🚀 DEPLOYMENT TO HEROKU")
    print("="*60)
    
    print("\n📋 Step-by-Step Instructions:")
    print("1. 📁 Ensure all files are committed to Git")
    print("2. 🌐 Go to https://heroku.com")
    print("3. 🔐 Sign up/Sign in")
    print("4. ➕ Click 'Create new app'")
    print("5. 📝 Name your app")
    print("6. 🔗 Connect to GitHub repository")
    print("7. 🚀 Click 'Deploy app'")
    
    print("\n✅ Your app will be available at:")
    print("   https://your-app-name.herokuapp.com")
    
    print("\n💡 Tips:")
    print("   • Free tier discontinued")
    print("   • Paid plans start at $7/month")
    print("   • Automatic deployments available")
    print("   • Custom domain support")

def local_development():
    """Instructions for local development"""
    print("\n" + "="*60)
    print("💻 LOCAL DEVELOPMENT")
    print("="*60)
    
    print("\n📋 Quick Start:")
    print("1. 🐍 Ensure Python 3.9+ is installed")
    print("2. 📦 Install dependencies:")
    print("   pip install -r requirements_web.txt")
    print("3. 🚀 Run the app:")
    print("   python launch_web_app.py")
    print("   # or")
    print("   streamlit run streamlit_app.py")
    
    print("\n✅ Your app will be available at:")
    print("   http://localhost:8501")
    
    print("\n💡 Development Tips:")
    print("   • Auto-reload on file changes")
    print("   • Debug mode available")
    print("   • Hot reload enabled")
    print("   • Local data caching")

def main():
    """Main deployment menu"""
    print("🎉 BACKTESTING.PY WEB APP DEPLOYMENT GUIDE")
    print("="*60)
    print(f"Generated on: {datetime.now()}")
    
    # Check prerequisites
    print("\n🔍 Checking prerequisites...")
    
    missing_files = check_required_files()
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   • {file}")
        print("\n⚠️ Please ensure all files are present before deployment.")
        return
    
    print("✅ All required files present")
    
    is_git_repo = check_git_status()
    if is_git_repo:
        print("✅ Git repository detected")
    else:
        print("⚠️ Not a Git repository (recommended for cloud deployment)")
    
    print("\n🎯 Choose deployment option:")
    print("1. 🌐 Streamlit Cloud (Recommended - Free)")
    print("2. 🚀 Vercel (Free tier available)")
    print("3. ⚡ Heroku (Paid)")
    print("4. 💻 Local Development")
    print("5. 📋 View all options")
    
    while True:
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            deploy_to_streamlit_cloud()
            break
        elif choice == "2":
            deploy_to_vercel()
            break
        elif choice == "3":
            deploy_to_heroku()
            break
        elif choice == "4":
            local_development()
            break
        elif choice == "5":
            deploy_to_streamlit_cloud()
            deploy_to_vercel()
            deploy_to_heroku()
            local_development()
            break
        else:
            print("❌ Invalid choice. Please enter 1-5.")
    
    print("\n" + "="*60)
    print("🎉 DEPLOYMENT GUIDE COMPLETE!")
    print("="*60)
    print("\n📚 Additional Resources:")
    print("   • Streamlit docs: https://docs.streamlit.io")
    print("   • Vercel docs: https://vercel.com/docs")
    print("   • Heroku docs: https://devcenter.heroku.com")
    print("   • Backtesting.py: https://github.com/kernc/backtesting.py")

if __name__ == "__main__":
    main()
