from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to the Home Page</h1>
    <p>This is the home page.</p>
    <p><a href='/about'>About</a></p>
    """

@app.route('/about')
def about():
    return """
    <h1>About Us</h1>
    <p>This is the about page.</p>
    <p><a href='/'>Home</a></p>
    """

@app.errorhandler(404)
def page_not_found(e):
    return """
    <h1>404 Not Found</h1>
    <p>The requested page was not found.</p>
    """, 404

if __name__ == '__main__':
    app.run(debug=True)
