import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("\n[SERVER CLOSED]")
                break
            print(data.decode())
        except:
            print("\n[ERROR receiving data]")
            break

# Prompt for department
data = client_socket.recv(1024).decode()
print(data, end='')
dept = input()
client_socket.sendall(dept.encode())

# Prompt for name
data = client_socket.recv(1024).decode()
print(data, end='')
name = input()
client_socket.sendall(name.encode())

# Start receiver thread
thread = threading.Thread(target=receive_messages, daemon=True)
thread.start()

# Main loop for sending messages
try:
    while True:
        msg = input()
        if msg.strip() == "":
            continue
        client_socket.sendall(msg.encode())
except KeyboardInterrupt:
    print("\n[CLIENT EXIT]")
finally:
    client_socket.close()
