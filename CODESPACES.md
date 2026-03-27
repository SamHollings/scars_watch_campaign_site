# Running in GitHub Codespaces

This project is fully configured to run in GitHub Codespaces. Follow these steps to get started:

## Quick Start - Option 1: Both Services (Recommended)

1. **Open in Codespaces**
   - Go to the repository on GitHub
   - Click `Code` → `Codespaces` → `Create codespace on main`
   - Wait for the environment to initialize (this will take a minute or two)

2. **Start Both Services**
   - In the terminal, run:
     ```bash
     python run_all.py
     ```
   - Wait for output showing both services have started

3. **Access the App**
   - Click the "Ports" tab at the bottom of the screen
   - You should see ports 5000 and 8501 forwarded
   - Click on port 5000 to open the map interface
   - Click the "Launch Streamlit Fluff Generator" button to access Streamlit

## Quick Start - Option 2: Flask Only

1. **Start Flask**
   - In the terminal, run:
     ```bash
     python app.py
     ```

2. **Access the Map**
   - Click the "Ports" tab and open port 5000
   - The map interface will load

## Quick Start - Option 3: Run Services Separately

If you prefer to manage services in separate terminals:

**Terminal 1 - Flask:**
```bash
python app.py
```

**Terminal 2 - Streamlit:**
```bash
streamlit run fluff_generator.py --server.port 8501
```

Both will be accessible via the Ports tab (5000 for Flask, 8501 for Streamlit).

## Features

### Map Interface
- **JavaScript-based interactive map** with clickable regions
- **Responsive design** that works on desktop and mobile
- **Golden-themed UI** matching the Warhammer 40k aesthetic

### Navigation
- **"Launch Streamlit Fluff Generator"** button on the fluff generator page
- **"← Back to Map"** button on all pages
- Smooth transitions between pages
- Automatic Streamlit detection and status messages

### Fluff Generator
- **Streamlit-powered interface** for battle report submission
- **AI-generated narrative** using LLM integration
- **Session management** for multi-turn conversations
- **Integration with ongoing story** for campaign continuity

## Alternative: Streamlit Dev Mode

If you prefer to use Streamlit for development:

```bash
python -m streamlit run fluff-generator.py --server.port 5000
```

## Troubleshooting

### Streamlit Button Shows "Not Running"
This means Streamlit is not accessible on port 8501. Solutions:

1. **Start Streamlit in a separate terminal:**
   ```bash
   streamlit run fluff_generator.py --server.port 8501
   ```

2. **Or use the combined launcher:**
   ```bash
   python run_all.py
   ```

3. **Check if Streamlit is running:**
   - Open the Ports tab
   - Look for port 8501
   - If not visible, Streamlit hasn't started

### Port Already in Use
If port 5000 is already in use, specify a different port:
```bash
PORT=8000 python app.py
```

For Streamlit, use:
```bash
streamlit run fluff_generator.py --server.port 8000
```

### Dependencies Missing
The devcontainer automatically installs dependencies. If you need to manually install:
```bash
pip install -e .
pip install -r requirements.txt
```

### Streamlit Errors
If you see "ModuleNotFoundError" for streamlit components:
```bash
pip install streamlit
pip install langchain langchain-google-genai google-genai
```

### Environment Variables
Set environment variables in the Codespaces environment or create a `.env` file (copy from `.env_example`):
```bash
cp .env_example .env
# Edit .env with your API keys (especially GEMINI_API_KEY)
```

## Development Tips

- **Hot Reload**: The Flask dev server automatically reloads when you modify files
- **Debug Mode**: Debug mode is enabled by default in Codespaces
- **View Console**: Check the terminal for any errors or debug output

## File Structure
- `app.py` - Flask application with route definitions
- `templates/` - HTML templates with embedded JavaScript
  - `red_scar_overview.html` - Interactive map interface
  - `scars_watch.html` - Fluff generator page
- `static/` - Static assets (images, CSS)
- `.devcontainer/devcontainer.json` - Codespaces configuration
