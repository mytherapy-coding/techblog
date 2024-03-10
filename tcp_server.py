import socket

# Choose the port
port = 1235

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server_socket.bind(('0.0.0.0', port))

print(f"Server is listening on port {port}")

# Start listening for incoming connectionsq
server_socket.listen()

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    try:
        # Receive data from the client
        data_received = client_socket.recv(1024).decode()
        print(f"Received request: {data_received}")

        # Send a response back to the client
        response_message = "I received your message"
        client_socket.sendall(response_message.encode())

    except Exception as e:
        # Print any errors
        print(f"Error: {e}")

    finally:
        # Close the connection with the current client
        client_socket.close()
