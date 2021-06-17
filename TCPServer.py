import socket
import threading

ip = '0.0.0.0'
port = 9998


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((ip, port))
        server.listen(5)
        print(f'[*] listen on {ip} {port}.')

        while True:
            client, address = server.accept()
            print(f'[*] accept connection from {address[0]}:{address[1]}')
            runner = threading.Thread(target=handle_client,args=(client,))
            runner.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(request.decode('utf-8'))
        sock.send(b'ACK')

if __name__ == '__main__':
    main()
