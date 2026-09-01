from flask import Flask

# creating flask instance
app = Flask(__name__)

# contact route
@app.route("/")
def contact():
    return "This is Contact Page"

# contact route
@app.route("/home")
def contact1():
    return "This is Home Page 1"

# home
@app.route("/home")
def home():
    return "This is Home Page"

# main
if __name__ == "__main__":
    app.run(debug=True)