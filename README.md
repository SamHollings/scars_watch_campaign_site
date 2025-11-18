# aws_dashboard
Testing out how to deploy a dashboard to AWS





## Build the docker image:
`docker build -t flask-app .`

## Run the docker image:
`docker run -d -p 5000:8000 flask-app`

See the website at: `localhost:5000`