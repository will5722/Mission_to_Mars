from flask import Flask, render_template, redirect
from pymongo import MongoClient
import scrape_costa

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
client = MongoClient('mongodb://loccalhost:27017')
temps = client.costa_rica.temps

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
