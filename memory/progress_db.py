from tinydb import TinyDB
from datetime import datetime

db = TinyDB("learning_progress.json")

def save_progress(topic, score):

    db.insert({
        "topic": topic,
        "score": score,
        "timestamp": str(datetime.now())
    })


def get_progress():

    return db.all()