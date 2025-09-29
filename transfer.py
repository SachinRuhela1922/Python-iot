# server.py
from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
MONGO_URI = "mongodb+srv://iosachinruhela:edith@edith.sgrdglf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client["JarvisAI"]
collection = db["IoTLogs"]

@app.route("/laststatus", methods=["GET"])
def get_last_status():
    try:
        last_doc = collection.find().sort("_id", -1).limit(1)[0]
        return jsonify({
            "assistant": last_doc.get("assistant", "light off")
        })
    except Exception as e:
        return jsonify({"assistant": "light off", "error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
