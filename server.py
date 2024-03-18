import socket
import select

# Define the host and port to listen on
HOST = '127.0.0.1'  # Use '0.0.0.0' to listen on all available interfaces
PORT = 12345  # Choose a port number (e.g., 12345)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f"Server is listening on {HOST}:{PORT}")

# List to keep track of connected clients
clients = []

while True:
    # Use select to wait for incoming data or connections
    ready_to_read, _, _ = select.select([server_socket] + clients, [], [])

    for sock in ready_to_read:
        if sock is server_socket:
            # Accept new connection
            client_socket, client_address = server_socket.accept()
            clients.append(client_socket)
            print(f"Connection established from {client_address}")
        else:
            # Handle incoming data from client
            data = sock.recv(1024).decode('utf-8')
            if not data:
                # Client disconnected
                print(f"Client {sock.getpeername()} disconnected")
                sock.close()
                clients.remove(sock)
            else:
                print(f"Received message from {sock.getpeername()}: {data}")

# Close the server socket (not reached in this example)
server_socket.close()