import socket

#创建新的socket对象，使用IPv4地址和TCP协议
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.bind(('localhost', 11451)) #bind绑定ip、端口号
server_socket.listen(5) #启动listen，等待客户端连接，参数5表示最大连接数
print("Start. Server is listening on port 11451...")

client_socket, client_addr = server_socket.accept() #等待client链接
data = client_socket.recv(1024).decode('utf-8') #接收数据，转换成文本，存储到data变量中

while data != 'bye':
    if data: #如果data不为空，打印接收到的数据
        print('[客户端]：', data)
    send_data = input('回复客户端：')
    client_socket.send(send_data.encode('utf-8'))
    if send_data == 'bye':
        break
    data = client_socket.recv(1024).decode('utf-8')

client_socket.close()
server_socket.close()