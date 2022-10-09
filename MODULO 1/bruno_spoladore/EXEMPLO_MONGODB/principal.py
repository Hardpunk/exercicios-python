from pymongo import *

con = MongoClient('localhost', 27017)
db = con['pos']
collection = db['veiculo']

# collection.insert_one({'marca':'chevrolet', 'modelo':'chevette', 'cv':85,'cc':1400,'preco':15000})

for v in collection.find({"marca": "vw"}, {"_id": 0, "marca": 1, "modelo": 1}):
    print(v)
