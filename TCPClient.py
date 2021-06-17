import socket

# host
target_host = '127.0.0.1'
# port
target_port = 9998
# use socket without close
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    # create connect
    client.connect((target_host, target_port))
    # send data as byte
    client.send(b'ABCDEF')
    # receive data
    response = client.recv(4096)
    # print it
    print(response)
