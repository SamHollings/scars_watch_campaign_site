# Streamlit Integration Summary

The fluff generator page now includes a button to launch the Streamlit-powered battle fluff generator. This document explains the changes and how to use them.

## Changes Made

### 1. **Updated Fluff Generator Page** (`templates/scars_watch.html`)

**New Features:**
- ⚡ **"Launch Streamlit Fluff Generator" button** - Opens Streamlit in a new tab
- 📋 **Feature descriptions** - Information about the fluff generation process
- ⚠️ **Automatic status detection** - Shows if Streamlit is running
- 💡 **Helpful error messages** - Instructions on how to start Streamlit if not running

**Visual Improvements:**
- Orange action section for the button (distinct from gold theme)
- Clear descriptions of how the system works
- Better organized content layout

### 2. **New Launcher Scripts**

Three options for starting both Flask and Streamlit together:

#### **Option A: Python Launcher (Recommended)**
```bash
python run_all.py
```
- Cross-platform (Windows, macOS, Linux)
- Colored terminal output
- Automatic dependency checking
- Clean shutdown on Ctrl+C
- Best for development

#### **Option B: Shell Script (Linux/macOS)**
```bash
bash run.sh
```
- Native bash implementation
- Colored output
- Same functionality as Python launcher

#### **Option C: Batch Script (Windows)**
```bash
run.bat
```
- Windows-native batch file
- Opens services in separate command windows
- Configurable via environment variables

### 3. **JavaScript Service Detection**

The launch button includes automatic service detection:

```javascript
// Checks if Streamlit is running on port 8501
// Shows appropriate message if not found
// Offers to retry or shows instructions
```

**User Experience:**
- If Streamlit is running: Opens in a new tab immediately
- If Streamlit is not running: Shows helpful error message with startup instructions
- Option to retry after starting Streamlit

## Usage

### Quick Start - All Services
```bash
python run_all.py
```

Then navigate to:
- 🗺️ Map: http://localhost:5000
- ⚡ Streamlit: http://localhost:8501 (or use the button on the map page)

### Quick Start - Separate Terminals
```bash
# Terminal 1
python app.py

# Terminal 2
streamlit run fluff_generator.py --server.port 8501
```

### In GitHub Codespaces
```bash
python run_all.py
```

Ports will be automatically forwarded. Click on port 5000 to open the map, then use the button to launch Streamlit.

## Navigation Flow

```
Map (/)
    ↓
Fluff Generator Page (/scars_watch)
    ├─→ [⚡ Launch Streamlit Fluff Generator]
    │   └─→ Streamlit App (http://localhost:8501)
    │       └─→ Battle Report & Story Generation
    │
    └─→ [← Back to Map]
        └─→ Map (/)
```

## Technical Details

### Port Configuration
- **Flask**: Port 5000 (configurable via `FLASK_PORT` env var)
- **Streamlit**: Port 8501 (configurable via command line)

### Service Detection
- JavaScript makes a CORS request to detect Streamlit
- Falls back gracefully if Streamlit is not running
- Provides clear instructions for starting

### Environment Variables
```bash
# Flask configuration
FLASK_PORT=5000          # Change Flask port
FLASK_HOST=0.0.0.0       # Bind to all interfaces
FLASK_DEBUG=1            # Enable debug mode

# Streamlit runs with defaults
# Can override with command line: --server.port 8501
```

## Troubleshooting

### Button Shows "Streamlit is not running"
1. Open a new terminal
2. Run: `streamlit run fluff_generator.py --server.port 8501`
3. Refresh the page and try again

### Services Won't Start
```bash
# Check if ports are already in use
lsof -i :5000      # Flask port
lsof -i :8501      # Streamlit port

# Use different ports if needed
PORT=8000 python app.py
streamlit run fluff_generator.py --server.port 8000
```

### Port Forwarding in Codespaces Not Working
- Ports should auto-forward
- Check "Ports" tab at bottom of screen
- If not visible, run commands again
- May need to refresh the page

## Files Modified/Created

**Modified:**
- `templates/scars_watch.html` - Added Streamlit button and styling

**New Files:**
- `run_all.py` - Python launcher (cross-platform)
- `run.sh` - Shell launcher (Linux/macOS)
- `run.bat` - Batch launcher (Windows)
- `STREAMLIT_INTEGRATION.md` - This file

## Future Enhancements

Possible improvements:
- [ ] Embed Streamlit in iframe instead of new window
- [ ] Add status indicator showing which services are running
- [ ] Create REST API for service control
- [ ] Add service restart button
- [ ] Create Docker Compose setup for all services

## Dependencies

The integration requires:
- Flask (already in requirements.txt)
- Streamlit (already in requirements.txt)
- Python 3.6+ (for app.py launcher)

All dependencies are automatically installed with:
```bash
pip install -e .
pip install -r requirements.txt
```
