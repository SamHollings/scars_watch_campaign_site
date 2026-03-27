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

### Quick Start (Development)
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