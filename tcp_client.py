import socket

# Replace with the server's IP address and port
server_ip = "127.0.0.1"
server_port = 1235

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))
print(f"Connected to {server_ip}:{server_port}")

# Greeting message
message_to_send = "hello server!"

try:
    # Send the message to the server
    client_socket.sendall(message_to_send.encode())

    # Wait for a response from the server
    response_message = client_socket.recv(1024).decode()

    # Print the response
    print(f"I received your message: {response_message}")

except Exception as e:
    # Print any errors
    print(f"Error: {e}")

finally:
    # Close the connection
    client_socket.close()
