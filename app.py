import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
users = [
    {'username': 'user1234',
     'password': 'password'},
    {'username': 'user69420',
     'password': 'password'},
    {'username': 'user4321',
     'password': 'password'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>FloppyCoinz User Info Database</h1>
<p>A prototype API for user info grabbing</p>'''


@app.route('/api/v1/resources/users/all', methods=['GET'])
def api_all():
    return jsonify(users)


@app.route('/api/v1/resources/users', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'username' in request.args:
        id = request.args['username']
    else:
        return "Error: No username field provided. Please specify a username."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for user in users:
        if user['username'] == id:
            results.append(user)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()
