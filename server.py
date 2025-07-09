import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = {}  # conn -> (department, name)
lock = threading.Lock()

def broadcast(message, exclude_conn=None):
    with lock:
        for conn in clients:
            if conn != exclude_conn:
                try:
                    conn.sendall(message.encode())
                except:
                    pass  # Ignore broken pipe errors etc.

def log_message(message):
    with open("chat_log.txt", "a") as f:
        f.write(message + "\n")

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr}")
    try:
        # Step 1: Ask for department and name
        conn.sendall("Enter your department: ".encode())
        department = conn.recv(1024).decode().strip()
        conn.sendall("Enter your name: ".encode())
        name = conn.recv(1024).decode().strip()

        # Register client
        with lock:
            clients[conn] = (department, name)

        join_msg = f"[SERVER] {department}-{name} joined the chat."
        print(join_msg)
        broadcast(join_msg, exclude_conn=conn)
        log_message(join_msg)

        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode().strip()
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

            if message == "/list":
                with lock:
                    user_list = "\n".join([f"- {d}-{n}" for _, (d, n) in clients.items()])
                response = f"[SERVER] Connected users:\n{user_list}\n"
                conn.sendall(response.encode())
            else:
                full_msg = f"[{timestamp}] {department}-{name}: {message}"
                print(full_msg)
                broadcast(full_msg, exclude_conn=conn)
                log_message(full_msg)
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        # Client disconnecting
        with lock:
            if conn in clients:
                left_msg = f"[SERVER] {clients[conn][0]}-{clients[conn][1]} left the chat."
                print(left_msg)
                broadcast(left_msg, exclude_conn=conn)
                log_message(left_msg)
                del clients[conn]
        conn.close()

print(f"[STARTING] Server listening on {HOST}:{PORT}")
while True:
    conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
    thread.start()
