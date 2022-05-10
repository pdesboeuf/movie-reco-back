# installation 

pip install -U flask-cors
python -m pip install requests


# LANCEMENT DU SERVEUR
. venv/Scripts/activate
export FLASK_APP=main.py
python -m flask run --host=0.0.0.0


# via Docker
Start
docker-compose -f docker/docker-compose.yml up --build
Stop
docker-compose -f docker/docker-compose.yml down