import socket

target_host = '127.0.0.1'
target_port = 9998

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as client:
    client.sendto(b'ABCDE',(target_host,target_port))
    data, addr = client.recvfrom(4096)
    print(data.decode())
