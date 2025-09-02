# 🚀 Deployment Guide - Backtesting.py Web App

This guide will help you deploy the Backtesting.py Streamlit web application to either **Streamlit Cloud** or **Vercel**.

## 📋 Prerequisites

- GitHub account
- Python 3.9+ knowledge
- Basic understanding of web deployment

## 🎯 Option 1: Streamlit Cloud (Recommended)

### Step 1: Prepare Your Repository
1. Make sure your repository contains:
   - `streamlit_app.py` (main app)
   - `requirements_web.txt` (dependencies)
   - `backtesting/` folder (library files)
   - `.streamlit/config.toml` (configuration)

### Step 2: Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository
5. Set the main file path to: `streamlit_app.py`
6. Set the requirements file to: `requirements_web.txt`
7. Click "Deploy"

### Step 3: Access Your App
- Your app will be available at: `https://your-app-name.streamlit.app`
- Share this URL with others!

## 🎯 Option 2: Vercel Deployment

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Deploy
1. Navigate to your project directory
2. Run: `vercel`
3. Follow the prompts
4. Your app will be deployed to Vercel

### Step 3: Access Your App
- Your app will be available at: `https://your-project.vercel.app`

## 🔧 Local Development

### Run Locally
```bash
# Install dependencies
pip install -r requirements_web.txt

# Run the app
streamlit run streamlit_app.py
```

### Access Locally
- Open your browser to: `http://localhost:8501`

## 📁 File Structure

```
your-project/
├── streamlit_app.py          # Main Streamlit application
├── requirements_web.txt      # Python dependencies
├── vercel.json              # Vercel configuration
├── .streamlit/
│   └── config.toml          # Streamlit configuration
├── backtesting/             # Backtesting library
│   ├── __init__.py
│   ├── backtesting.py
│   ├── lib.py
│   └── test/
│       ├── __init__.py
│       ├── GOOG.csv
│       ├── BTCUSD.csv
│       └── EURUSD.csv
└── DEPLOYMENT_GUIDE.md      # This file
```

## 🛠️ Troubleshooting

### Common Issues

#### 1. Import Errors
- **Problem**: `ModuleNotFoundError: No module named 'backtesting'`
- **Solution**: Make sure the `backtesting/` folder is in your repository

#### 2. Missing Dependencies
- **Problem**: `ModuleNotFoundError` for numpy, pandas, etc.
- **Solution**: Check that `requirements_web.txt` contains all dependencies

#### 3. Deployment Fails
- **Problem**: Build fails during deployment
- **Solution**: 
  - Check Python version compatibility
  - Verify all files are committed to GitHub
  - Check the deployment logs

#### 4. App Doesn't Load
- **Problem**: App shows error or doesn't start
- **Solution**:
  - Check the app logs in Streamlit Cloud dashboard
  - Verify the main file path is correct
  - Test locally first

### Performance Tips

1. **Optimize Data Loading**: The app loads data from CSV files
2. **Caching**: Streamlit automatically caches expensive computations
3. **Memory Usage**: Large datasets may require optimization

## 🔄 Updates and Maintenance

### Updating Your App
1. Make changes to `streamlit_app.py`
2. Commit and push to GitHub
3. Streamlit Cloud will automatically redeploy
4. Vercel will also auto-deploy on push

### Monitoring
- **Streamlit Cloud**: Check the dashboard for logs and performance
- **Vercel**: Use the Vercel dashboard for analytics and logs

## 📞 Support

If you encounter issues:

1. **Check the logs** in your deployment platform
2. **Test locally** first to isolate issues
3. **Review the [backtesting.py documentation](https://kernc.github.io/backtesting.py/)**
4. **Check [Streamlit documentation](https://docs.streamlit.io/)**
5. **Review [Vercel documentation](https://vercel.com/docs)**

## 🎉 Success!

Once deployed, your app will provide:
- ✅ Interactive web interface
- ✅ Real-time backtesting
- ✅ Beautiful visualizations
- ✅ Multiple datasets
- ✅ Customizable parameters
- ✅ Professional results display

**Happy Deploying! 🚀📈**
