# Scars Watch Campaign

This is a personal project to make an interactive chat website, which can make background for our ongoing campaign set in the Warhammer 40k universe.

Currently it consists of a few main parts:

- **app.py**: makes the flask app - the website which users interact with.
- **fluff-generator.py**: LLM based tool to write ongoing warhammer fluff based on existing notes and future submissions.
- **model_funcs.py**: Functions to initialise the LLM
- **prompts.py**: Prompts for the LLM

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
### Running the dev app (in streamlit)
- in the terminal run:  python -m streamlit run fluff-generator.py

### Building the docker image:
`docker build -t flask-app .`

### Run the docker image:
`docker run -d -p 5000:8000 flask-app`

See the website at: `localhost:5000`

### Dev

To run the flask app on it's inbuilt dev server:
`python -m flask run`

To run the flask app on the gunicorn server:
`python -m gunicorn --workers=3 --bind 0.0.0.0:8000 app:app --daemon`

you can kill the gunicorn server with:
`pkill -f gunicorn`