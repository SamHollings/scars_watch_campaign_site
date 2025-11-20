# aws_dashboard
Testing out how to deploy a dashboard to AWS





## Build the docker image:
`docker build -t flask-app .`

## Run the docker image:
`docker run -d -p 5000:8000 flask-app`

See the website at: `localhost:5000`

# Dev

To run the flask app on it's inbuilt dev server:
`python -m flask run`

To run the flask app on the gunicorn server:
`python -m gunicorn --workers=3 --bind 0.0.0.0:8000 app:app --daemon`

you can kill the gunicorn server with:
`pkill -f gunicorn`