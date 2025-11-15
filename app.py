# Import the Flask class from the flask module
from flask import Flask, jsonify

# 1. Create an "instance" of the Flask application
# __name__ tells Flask where to look for resources
app = Flask(__name__)

# --- DEFINE YOUR API ROUTES ---

# 2. Define a "route" for the home page ("/")
# This @app.route() decorator binds a URL to a function.
@app.route('/')
def home():
    """This function runs when someone visits the root URL."""
    # Return a simple string
    return "Welcome to the Minimal Flask API!"

# 3. Define a route for a JSON data endpoint
# This is what most modern APIs do.
@app.route('/api/hello')
def api_hello():
    """This function runs when someone visits '/api/hello'."""
    # Create a Python dictionary
    data = {
        "message": "Hello, world!",
        "status": "ok"
    }
    # jsonify() converts the dictionary to a proper JSON response
    return jsonify(data)

# 4. Define a dynamic route that accepts a name
@app.route('/api/greet/<name>')
def api_greet(name):
    """This function runs for '/api/greet/John', '/api/greet/Jane', etc."""
    data = {
        "greeting": f"Hello, {name}!",
        "message": "This is a dynamic route."
    }
    return jsonify(data)

# --- RUN THE APPLICATION ---

# 5. This 'if' block ensures the server only runs
#    when the script is executed directly (not imported)
if __name__ == '__main__':
    # app.run() starts the development server
    # debug=True will auto-reload the server on code changes
    app.run(debug=True, host='0.0.0.0', port=5000)
