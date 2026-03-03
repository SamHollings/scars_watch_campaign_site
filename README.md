# Scars Watch Campaign

This is a personal project to make an interactive chat website, which can make background for our ongoing campaign set in the Warhammer 40k universe.

Currently it consists of a few main parts:

- **app.py**: makes the flask app - the website which users interact with.
- **fluff-generator.py**: LLM based tool to write ongoing warhammer fluff based on existing notes and future submissions.
- **model_funcs.py**: Functions to initialise the LLM
- **prompts.py**: Prompts for the LLM

## Requirements

- The repository dependencies are described in **pyproject.toml**.
- You will needs a local .env file with appropriate keys - see **.env_example**

## Instructions
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