# Importar la biblioteca PyMongo
import pymongo
# Crear una conexión con la base de datos
cliente = pymongo.MongoClient(
    'mongodb+srv://admin:12345@od1.jiahqis.mongodb.net')
db = cliente['DBprueba']
# Obtener la colección en la que se agregarán los campos
coleccion = db['COLprueba']
# Crear un diccionario con los campos a agregar
campos = {'campo1': 'valor1', 'campo2': 'valor2'}
# Agregar los campos a la colección
coleccion.insert_one(campos)
print(campos)
