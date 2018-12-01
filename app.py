from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars



# Create an instance of our Flask app.
app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Set route
@app.route('/')
def index():
     scrapings = mongo.db.scrapings.find_one()
     return render_template("index.html", scrapings = scrapings)


@app.route("/scrape")
def scraper():
     scrapings = mongo.db.scrapings
     scrapings_data = scrape_mars.scrape()
     scrapings.update({}, scrapings_data, upsert=true)
     return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)