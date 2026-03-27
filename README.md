# Scars Watch Campaign
[![CI](https://github.com/samhollings/scars_watch_campaign_site/actions/workflows/ci.yml/badge.svg)](https://github.com/samhollings/scars_watch_campaign_site/actions/workflows/ci.yml) 
![Static Badge](https://img.shields.io/badge/status-development-blue) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This is a personal project to make an interactive chat website, which can make background for our ongoing campaign set in the Warhammer 40k universe.

Currently it consists of a few main parts:

- **app.py**: Flask application serving the interactive web interface
- **templates/**: HTML templates with JavaScript for interactive features
  - `red_scar_overview.html`: Interactive map interface with fluff generator
  - `location_detail.html`: Location backstory and events
  - `characters.html`: Characters and factions in the Red Scar region
- **src/model_funcs.py**: Functions to initialize the Gemini LLM
- **src/prompts.py**: System prompts for narrative generation
- **src/retrieval.py**: Story context retrieval

The intention is that this will generate post battle fluff based on the ongoing story and sides 
invovled in our battles.

Rough process:
- access to ongoing story google docs document
    - intially contents of this could simply be put into a text file, but eventually we want to be able to read and write to a something hosted on the web
- use this as background context then, take in battle info and generate post battle fluff
    - intially the whole document could be dumped into the prompt, 
    - but eventually will want to bring only the relevant sections of the story into the prompt - e.g. RAG
- save this fluff back into the ongoing story document / database
- some sort of front end, to display the ongoing story
- a trigger mechanism - such that when a battle report is submitted, the fluff is generated, added to the story document and displauyued on the front end

Assets:
- txt file to store the story
- battle report submission file
- model pipeline to generate fluff
- prompt template
- front end to display story and receive submissions
- trigger mechanism to run the model pipeline when a battle report is submitted

## Requirements

- The repository dependencies are described in **pyproject.toml**.
- You will needs a local .env file with appropriate keys - see **.env_example**

## Instructions

### GitHub Codespaces (Recommended)

Launch in the cloud instantly - no local setup required!

1. **Click "Code" → "Codespaces" → "Create codespace on main"** on the GitHub repo
2. Wait for the environment to initialize (1-2 minutes)
3. In the terminal, run:
   ```bash
   python app.py
   ```
4. When you see "Running on http://0.0.0.0:5000", click the **Ports** tab
5. Click the link or the globe icon next to port 5000
6. The map interface loads instantly!

**All features work in Codespaces:**
- 🗺️ Interactive map with clickable locations
- ⚡ Inline fluff generator modal
- 📍 Location sidebar with backstory and events
- 👥 Characters page
- 🌍 Full campaign interface

**Note:** First request may take 5-10 seconds (API initialization)

### Quick Start (Local Development)
```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env_example .env
# Edit .env with your GEMINI_API_KEY

# Run the Flask app
python app.py
```

Then open http://localhost:5000 in your browser.

### Production (Gunicorn)
```bash
python -m gunicorn --workers=3 --bind 0.0.0.0:8000 app:app
```

To stop gunicorn: `pkill -f gunicorn`

### Docker

Build:
```bash
docker build -t scars-watch .
```

Run:
```bash
docker run -d -p 5000:8000 -e GEMINI_API_KEY=your_key scars-watch
```

Visit http://localhost:5000

## Troubleshooting

### Map tooltips or sidebar not working
1. Press `F12` to open browser DevTools
2. Go to the **Console** tab
3. Look for error messages
4. Try reloading the page (`Ctrl+Shift+R`)
5. See `DEBUGGING_GUIDE.md` for detailed debugging steps

### API errors when generating fluff
- Make sure `.env` file exists with valid `GEMINI_API_KEY`
- Run: `cat .env` to verify the key is set
- Copy `.env_example` and add your key: `cp .env_example .env`

### Port already in use
```bash
PORT=8000 python app.py
```

## Project Structure

```
scars_watch_campaign_site/
├── app.py                          # Flask web application
├── templates/                      # HTML templates
│   ├── red_scar_overview.html     # Interactive map
│   ├── characters.html             # Characters page
│   └── location_detail.html        # Location details
├── static/                         # Images and CSS
├── src/                            # Python modules
│   ├── fluff_generator.py         # LLM interface
│   ├── model_funcs.py             # Model initialization
│   ├── prompts.py                 # System prompts
│   └── retrieval.py               # Story context
├── data/                           # Story files
│   └── ongoing_story.txt          # Campaign narrative
└── .devcontainer/                 # Codespaces config
    └── devcontainer.json
```

## Features

- **Interactive Map** - Click locations for backstory and events
- **Fluff Generator** - AI-powered narrative generation for battles
- **Characters Page** - Named characters and factions from the story
- **Location Details** - Sidebar with full backstory and event timelines
- **Responsive Design** - Works on desktop, tablet, and mobile
- **GitHub Codespaces** - Fully configured for cloud development

## Technologies

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript Canvas
- **LLM:** Google Gemini API via LangChain
- **Story Context:** RAG-ready with local story file

## Documentation

- `DEBUGGING_GUIDE.md` - Troubleshooting map and UI issues
- `FLUFF_GENERATOR_MODULE.md` - Fluff generator API documentation
- `MAP_CUSTOMIZATION.md` - Adding new locations to the map
- `claude_log/` - Claude-created documentation