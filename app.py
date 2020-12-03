from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_Mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/Mars_app"
mongo = PyMongo(app)

@app.route('/')
def index():
    Mars = mongo.db.Mars.find_one()
    return render_template('index.html', Mars=Mars)


@app.route('/scrape')
def scrape():
    Mars = mongo.db.Mars
    data = scrape_Mars.scrape()
    Mars.update(
        {},
        data,
        upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)