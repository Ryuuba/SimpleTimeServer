import socket
import datetime

def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def start_server():
    host = '192.168.1.84'  # Use your PC's IP address or 'localhost'
    port = 12345  # Choose an available port number

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for one incoming connection

    print(f"Server is listening on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        try:
            current_time = get_current_time()
            client_socket.send(current_time.encode())
        except Exception as e:
            print(f"Error sending data: {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()
