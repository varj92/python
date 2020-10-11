from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

#Conectar A MongoDB 
client = MongoClient(MONGO_URI)

db = client['test'] # crear base de datos
collection = db['productos'] # crear colección

## crear documento en una colección
#collection.insert_one({"name": "Ford Mustang","price":750000})

product_one = {"name": "Ford Focus","price":350000}
product_two = {"name": "Ford Lobo","price":700000}

# crear varios documentos
#collection.insert_many([product_one,product_two])

#mostrar todos los documentos
results = collection.find()
for r in results:
    print(r)
    #print(r['name']) #mostrar solo el nombre

# mostrar solo documentos con precio = 750000
results = collection.find({"price":750000})
for r in results:
    print(r)

result = collection.find_one({"price":750000})
print(result)

# Borrar 1 documento
result = collection.delete_one({"price":750000})
# Borrar varios documentos
result = collection.delete_many({"price":750000})
# Borrar todos los documentos
result = collection.delete_many({})

# Actualizar documentos
collection.update_one({"name": "laptop"}, {"$set": "keyboard", "price": 100})
# Incremetar valor de documento
collection.update_one({"name": "keyboard"}, {"$inc": {"price": 49}})
#Contar documentos de colección
count_prods = collection.count_documents({})
print(count_prods)