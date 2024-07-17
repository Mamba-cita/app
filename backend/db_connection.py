import pymongo

url = "mongodb+srv://gigi:tomi@ter.kskf9ol.mongodb.net/t-truck?retryWrites=true&w=majority&appName=ter"
client = pymongo.MongoClient(url)


db = client['t-truck']