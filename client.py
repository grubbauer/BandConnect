import socket
import threading

usrname = input("Enter Username: ")

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"{data.decode('utf-8')}")

        except Exception as e:
            print(f"Error: {e}")
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:
        message = input("Your message: ")
        client.send(f'{usrname.encode('utf-8')}: {message.encode('utf-8')}')

if __name__ == "__main__":
    start_client()
