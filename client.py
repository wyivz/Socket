import socket

client_socket = socket.socket() # 创建socket对象
client_socket.connect(('127.0.0.1', 11451))             # 连接服务器
print('连接成功')

info = ''
while info != 'bye':
    msg = input('发送给服务器：')
    client_socket.send(msg.encode('utf-8'))
    if msg == 'bye':
        break
    info = client_socket.recv(1024).decode('utf-8')
    print('[服务器]：', info)
client_socket.close()

