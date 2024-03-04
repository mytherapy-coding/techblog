import socket

# Choose the port number
port = 1235

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(('0.0.0.0', port))

# Start listening for incoming connections
server_socket.listen()

print(f"Server is listening on port {port}")

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive data from the client
    data_received = client_socket.recv(1024).decode()
    print(f"Received data: {data_received}")

    # Send a response back to the client
    response_message = f"Hello, Client at {client_address}!"
    client_socket.sendall(response_message.encode())

    # Close the connection with the current client
    client_socket.close()
