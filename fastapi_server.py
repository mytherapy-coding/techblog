from fastapi import FastAPI, Response

# Create an instance of the FastAPI class
app = FastAPI()

# Define response content based on requested URL
@app.get("/")
def read_root():
    # Home page content
    html_content = """
    <html>
        <body>
            <h1>Welcome to the Home Page</h1>
            <p>This is the home page.</p>
            <p><a href='/about'>About</a></p>
        </body>
    </html>
    """
    return Response(content=html_content, media_type="text/html")

@app.get("/about")
def read_about():
    # About page content
    html_content = """
    <html>
        <body>
            <h1>About Us</h1>
            <p>This is the about page.</p>
            <p><a href='/'>Home</a></p>
        </body>
    </html>
    """
    return Response(content=html_content, media_type="text/html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=1235)
