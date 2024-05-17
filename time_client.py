import socket
import time

def get_time_from_server():
    host = "192.168.1.84"  # Replace with the server's IP address
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        server_time = client_socket.recv(1024).decode()
        print(f"{server_time}")
    except Exception as e:
        print(f"Error receiving data: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    get_time_from_server()
