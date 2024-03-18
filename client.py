import socket

# Define the server's host and port
SERVER_HOST = '127.0.0.1'  # Change this to the server's IP address if necessary
SERVER_PORT = 12345  # Make sure this matches the server's port

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Send a message to the server
message = "Hello, server!"
client_socket.send(message.encode('utf-8'))

# Close the connection
client_socket.close()