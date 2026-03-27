# Flask-Only Migration Complete

Streamlit has been completely removed from the project. Everything now runs on a single Flask application.

## ✅ What Was Removed

- ❌ `streamlit` from requirements.txt
- ❌ `run.sh` launcher script
- ❌ `run.bat` launcher script
- ❌ `run_all.py` launcher script
- ❌ Streamlit documentation from CODESPACES.md and README.md

## ✅ What Remains

### Single Flask Application
- **Port:** 5000
- **Start:** `python app.py`
- **URL:** http://localhost:5000

### All Features Integrated
- 🗺️ **Interactive Map** - JavaScript canvas with clickable locations
- 📍 **Location Details** - Sidebar with backstory and events
- ⚡ **Fluff Generator** - Inline modal chat interface
- 👥 **Characters Page** - Detailed character and faction information
- 🌍 **World Building** - Rich lore and campaign context

## 📋 Updated Documentation

Files updated to remove Streamlit references:
- `CODESPACES.md` - Removed Streamlit launcher and port info
- `README.md` - Updated to show Flask-only workflow
- `requirements.txt` - Removed streamlit dependency

Files that remain unchanged:
- `.devcontainer/devcontainer.json` - Already Flask-only
- `app.py` - No changes needed
- All HTML templates - No changes needed

## 🚀 Quick Start

### Development
```bash
python app.py
```

### Production
```bash
python -m gunicorn --workers=3 --bind 0.0.0.0:8000 app:app
```

### Docker
```bash
docker build -t scars-watch .
docker run -d -p 5000:8000 -e GEMINI_API_KEY=your_key scars-watch
```

## 🎯 Benefits

✅ **Simpler Setup** - Just Flask, no multiple services
✅ **Easier Deployment** - Single application on one port
✅ **Better Performance** - No IPC between services
✅ **Reduced Dependencies** - Smaller requirements.txt
✅ **GitHub Codespaces Ready** - Works perfectly with one port forward
✅ **Unified Interface** - All features on one website

## 📦 Current Dependencies

Essential packages in requirements.txt:
- `flask` - Web framework
- `langchain` - LLM integration
- `langchain-google-genai` - Google Gemini support
- `google-genai` - Gemini API
- `python-dotenv` - Environment configuration
- `gunicorn` - Production server
- Other data science packages (pandas, numpy, scikit-learn, etc.)

## 🔄 Migration Notes

### If You Had Streamlit Running
Stop Streamlit if it was running on port 8501:
```bash
pkill -f streamlit
```

The project no longer needs it.

### Environment Variables
Still required:
- `GEMINI_API_KEY` - Your Google Gemini API key
- `FLASK_APP` - Usually "app.py" (auto-set)
- `FLASK_ENV` - "development" or "production"
- `PORT` - Optional, defaults to 5000

### Browser Access
Everything is now at: **http://localhost:5000**

No need to manage multiple ports or windows!

## 📚 File Structure

```
scars_watch_campaign_site/
├── app.py                          # Single Flask application
├── requirements.txt                # Dependencies (no Streamlit)
├── templates/
│   ├── red_scar_overview.html     # Map with fluff generator
│   ├── location_detail.html       # Location backstory
│   └── characters.html             # Characters and factions
├── static/
│   ├── css/style.css
│   └── images/
├── src/
│   ├── model_funcs.py             # LLM initialization
│   ├── prompts.py                 # System prompts
│   └── retrieval.py               # Story context
├── data/
│   └── ongoing_story.txt          # Campaign story
└── .devcontainer/
    └── devcontainer.json          # Codespaces config
```

## 🐛 Troubleshooting

### Port 5000 Already in Use
```bash
PORT=8000 python app.py
```

### API Key Issues
```bash
# Create .env file
cp .env_example .env

# Edit and add your GEMINI_API_KEY
nano .env
```

### Module Not Found
```bash
pip install -r requirements.txt
```

## ✨ Next Steps

The application is now simplified and ready for:
- ✅ Production deployment
- ✅ Docker containerization
- ✅ GitHub Codespaces
- ✅ Local development
- ✅ Team collaboration

All with a single, clean Flask application!
