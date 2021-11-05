from flask import Flask, render_template, redirect
#from pymongo import MongoClient
import scrape_mars
import pymongo

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
#client = MongoClient('mongodb://loccalhost:27017')
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
mars_info = client.mars_db.mars_info
#collection = db.mars_data







# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    mars_data = mars_info.find_one()
    return render_template("index.html", mars_data=mars_data)
    
    
@app.route("/scrape")
def scrape():
    item = scrape_mars.scrape()
    
    mars_info.insert_one(item)
    
    return redirect("/")
    
    
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
