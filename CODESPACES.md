# Running in GitHub Codespaces

This project is fully configured to run in GitHub Codespaces. Follow these steps to get started:

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
   - You should see output indicating the server is running on `0.0.0.0:5000`

3. **Access the App**
   - Click the "Ports" tab at the bottom of the screen
   - You should see port 5000 forwarded
   - Click on the "Open in Browser" icon (or click the port number link)
   - The map interface will load in a new browser tab

## Features

### Map Interface
- **JavaScript-based interactive map** with clickable regions
- **Responsive design** that works on desktop and mobile
- **Golden-themed UI** matching the Warhammer 40k aesthetic

### Navigation
- **"Launch Fluff Generator"** button on the map page
- **"← Back to Map"** button on the fluff generator page
- Smooth transitions between pages

## Alternative: Streamlit Dev Mode

If you prefer to use Streamlit for development:

```bash
python -m streamlit run fluff-generator.py --server.port 5000
```

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, specify a different port:
```bash
PORT=8000 python app.py
```

### Dependencies Missing
The devcontainer automatically installs dependencies. If you need to manually install:
```bash
pip install -e .
pip install -r requirements.txt
```

### Environment Variables
Set environment variables in the Codespaces environment or create a `.env` file (copy from `.env_example`):
```bash
cp .env_example .env
# Edit .env with your API keys
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
