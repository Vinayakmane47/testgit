import pymongo

import dns


client = pymongo.MongoClient("mongodb+srv://Vinayak:Sak$103138@cluster0.j3xloau.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Vinayak",
    "email":"manevinayak",
    "surname":"mane"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
