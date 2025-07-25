from flask import Flask, #request

app = Flask(__name__) # creates a Flask app instance (object)

tasks = [] # initializes an empty list to store tasks

#@app.route('/', methods=['GET', 'POST']) # defines route for home page (GET= to retrieve the data, POST= to handle submission)
