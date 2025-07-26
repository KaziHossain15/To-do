from flask import Flask, redirect, request, render_template # imports necessary modules from Flask

app = Flask(__name__) # creates a Flask app instance (object)

tasks = [] # initializes an empty list to store tasks

@app.route('/', methods=['GET', 'POST']) # defines route for home page (GET= to retrieve the data, POST= to handle submission)
def index():
    if request.method == 'POST': # checks if the form is submitted
        task = request.form.get('task') # retrieves the task from the form data
        if task: # checks if the task is not empty
            tasks.append(task) # adds the task to the list
        return redirect('/') # redirects to the home page after submission
    return render_template('index.html', tasks=tasks) # renders the index.html template with the list of tasks

