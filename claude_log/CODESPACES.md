# Running in GitHub Codespaces

This project is fully configured to run in GitHub Codespaces with a single Flask application. Follow these steps:

## Quick Start

1. **Open in Codespaces**
   - Go to the repository on GitHub
   - Click `Code` → `Codespaces` → `Create codespace on main`
   - Wait for the environment to initialize (this will take a minute or two)

2. **Start the Flask App**
   - In the terminal, run:
     ```bash
     python app.py
     ```
   - Wait for output showing the Flask server has started on port 5000

3. **Access the App**
   - Click the "Ports" tab at the bottom of the screen
   - You should see port 5000 forwarded
   - Click on port 5000 to open the map interface
   - All features (fluff generator, locations, characters) are accessible directly

## Features

### Map Interface
- **JavaScript-based interactive map** with clickable regions
- **Responsive design** that works on desktop and mobile
- **Golden-themed UI** matching the Warhammer 40k aesthetic

### Location System
- **Click locations to view details** in a side panel
- **Backstory and event timeline** for each region
- **5 major locations** with full lore

### Characters Page
- **Named characters and factions** from the story
- **Imperial, Chaos, and Xenos** faction pages
- **Detailed character backgrounds** and roles

### Fluff Generator
- **Inline modal interface** for battle report submission
- **AI-generated narrative** using Claude Gemini API
- **Chat-based conversation** with story context
- **Session history** maintained during play

## Troubleshooting

### Flask App Won't Start
If you see connection errors, the port might be in use:
```bash
PORT=8000 python app.py
```

### Fluff Generator Shows Error
This means the API key is missing or invalid:

1. **Check your `.env` file:**
   ```bash
   cat .env
   ```

2. **Set up `.env` from template:**
   ```bash
   cp .env_example .env
   # Edit .env with your GEMINI_API_KEY
   ```

3. **Verify the key works** by trying a fluff generator message

### Dependencies Missing
The devcontainer automatically installs dependencies. If you need to manually install:
```bash
pip install -e .
pip install -r requirements.txt
```

### Environment Variables
Create a `.env` file with required API keys:
```bash
cp .env_example .env
# Edit .env with your GEMINI_API_KEY
```

### Sidebar Won't Open
- Clear browser cache (Ctrl+Shift+Delete)
- Refresh the page (Ctrl+F5)
- Check browser console for JavaScript errors (F12)

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
