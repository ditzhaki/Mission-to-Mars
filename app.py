# Import tools
from flask import Flask, render_template
from flask_pymongo import PyMongo
import Scraping

# Set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define our routes
@app.route("/")
def index():
    mars = mongo.db.mars.find()
    return render_template("index.html", mars = mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = Scraping.scrape_all()
   mars.update({}, {"$set":mars_data}, upsert=True)
   return "Successful!"

if __name__ == "__main__":
    app.run(debug=True)