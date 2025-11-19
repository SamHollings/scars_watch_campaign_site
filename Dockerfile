FROM python:3.14
#COPY app.py requirements.txt static/* templates/* ./
COPY . ./app
WORKDIR /app
RUN pip install -r requirements.txt
#CMD ["flask", "run", "--host=0.0.0.0" , "--port=8000"]
CMD ["gunicorn", "--workers=3","--bind", "0.0.0.0:8000", "app:app", "--daemon"]