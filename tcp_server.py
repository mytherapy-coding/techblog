import socket

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Received request:\n{request}")

    # Extract the requested URL from the request
    try:
        url = request.split()[1]
    except IndexError:
        url = '/'

    # Define response content based on requested URL
    if url == '/':
        # Home page content
        response_content = (
            "HTTP/1.1 200 OK\n"
            "Content-Type: text/html\n\n"
            "<html><body>"
            "<h1>Welcome to the Home Page</h1>"
            "<p>This is the home page.</p>"
            "<p><a href='/about'>About</a></p>"
            "</body></html>"
        )
    elif url == '/about':
        # About page content
        response_content = (
            "HTTP/1.1 200 OK\n"
            "Content-Type: text/html\n\n"
            "<html><body>"
            "<h1>About Us</h1>"
            "<p>This is the about page.</p>"
            "<p><a href='/'>Home</a></p>"
            "</body></html>"
        )
    else:
        # Page not found
        response_content = (
            "HTTP/1.1 404 Not Found\n"
            "Content-Type: text/html\n\n"
            "<html><body>"
            "<h1>404 Not Found</h1>"
            "<p>The requested page was not found.</p>"
            "</body></html>"
        )

    # Send the response
    client_socket.send(response_content.encode('utf-8'))

    # Close the connection with the client
    client_socket.close()

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 1235)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print(f"Server is listening on {server_address}")

    while True:
        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        handle_client(client_socket)

if __name__ == "__main__":
    run_server()
