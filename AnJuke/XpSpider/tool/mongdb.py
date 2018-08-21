import pymongo
client = pymongo.MongoClient('localhost')
db = client['AnJuKeSp']
collection = db['anhui']
results = collection.find({},{'url':1,'_id':0})
print(len(results))
# print(results)
for result in results:
    print(result['url'])