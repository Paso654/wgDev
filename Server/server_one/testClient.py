#
# testClient for ServerOne
# Team: Sandro Gallo
# last-updated: 10/04/2020 by Sandro
#

import socket
import mylib as ml

# Create a socket object (client)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Request a message to user
msg = input("Enter a message to send to the server: ")

# Try to connect to the server
clientSocket.connect((ml.HOST, ml.PORT))
print("Connected to server", ml.HOST, ":", ml.PORT)

# Send a message to the server
ml.strSend(clientSocket, msg)
print("Message sent")

# Close the socket when done
clientSocket.close()
print("Connection closed.")
input("press RETURN to terminate")
