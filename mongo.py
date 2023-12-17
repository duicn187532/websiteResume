# import pymongo 
#連線雲端資料庫
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pymongo

uri = "mongodb+srv://root:21airr01@mycluster.wk4zgas.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db=client.員工#選擇操作test資料庫
collection=db.users#選擇操作users集合
def SearchOne(string):
    target=collection.find_one({'enum':string})
    return target['uname']
def insertdata(uname,enum,pwd,sex,email,email2,bir,licenses):
    data={
            "uname": uname,
            "enum": enum,
            "pwd": pwd,
            "sex": sex,
            "email": email,
            "email2": email2,
            "bir": bir,
            "licenses": licenses
        }
        # 如果需要插入多個不同的記錄，可以在這裡繼續添加
        # 但如果只插入一條記錄，則只需要一個字典
    collection.insert_one(data)
data=collection.find({},sort=[
    ('enum',pymongo.ASCENDING)
])
dnta=collection.find_one({
    'sex':'男'
})
dbcount=collection.count_documents({})
list_data=list(data)
# print(list_data)
#print(dnta['uname'])
# for i in data:
#     print(i)
# for i in data:
#     print(i['uname'])
# result=collection.update_many({
#     "sex":"男"
# },{
#     "$set":{
#         "enum":"58882"
#     }
# })
# print(result.matched_count)
# print(result.modified_count)
