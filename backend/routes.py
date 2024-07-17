from . import app
import os
import json
import pymongo
from flask import jsonify, request, make_response, abort, url_for
from pymongo import MongoClient
from bson import json_util
from pymongo.errors import OperationFailure
import sys  # Importa el módulo sys para utilizar sys.exit(1)

# Rutas al archivo JSON local
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "songs.json")

# Cargar los datos desde el archivo JSON
with open(json_url) as f:
    songs_list = json.load(f)

# Configuración de conexión a MongoDB desde variables de entorno
mongodb_service = os.environ.get('MONGODB_SERVICE')
mongodb_username = os.environ.get('MONGODB_USERNAME')
mongodb_password = os.environ.get('MONGODB_PASSWORD')
mongodb_port = os.environ.get('MONGODB_PORT')

# Validar la existencia de la variable de servicio de MongoDB
if not mongodb_service:
    app.logger.error('Missing MongoDB server in the MONGODB_SERVICE variable')
    sys.exit(1)  # Utiliza sys.exit(1) para salir del programa con un código de error

# Construir la URL de conexión a MongoDB
if mongodb_username and mongodb_password:
    url = f"mongodb://{mongodb_username}:{mongodb_password}@{mongodb_service}"
else:
    url = f"mongodb://{mongodb_service}"

# Intentar conectar con MongoDB
try:
    client = MongoClient(url)
    db = client.songs  # Seleccionar la base de datos "songs"
    db.songs.drop()  # Eliminar colección existente (opcional)
    db.songs.insert_many(songs_list)  # Insertar datos desde el archivo JSON en la colección "songs"
    print("Data successfully inserted into MongoDB.")
except OperationFailure as e:
    app.logger.error(f"Error connecting to MongoDB: {str(e)}")
    sys.exit(1)

def parse_json(data):
    return json.loads(json_util.dumps(data))

######################################################################
# INSERTAR CÓDIGO AQUÍ: Definir rutas y lógica adicional de Flask
######################################################################
