import socket
import threading

#创建一个socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#获取地址
host = '127.0.0.1'
#端口
port = 12345
#用于添加线程的列表
threads = []
#创建服务器
s.bind((host, port))
#设置最大连接数
s.listen(1)
sock, addr = s.accept()
print('已连接')

#发送消息
def fa():
    while True:
        send_msg = input('我:\n')
        sock.send(send_msg.encode())
        if send_msg == 'exit':
            break

#接收消息
def sou():
    while True:
        info = sock.recv(1024).decode()
        #退出时关闭socket
        if info == 'quit':
            sock.close()
            break
        print('你:' + info)



t1 = threading.Thread(target=fa)
t2 = threading.Thread(target=sou)
threads.append(t1)
threads.append(t2)
for i in range(len(threads)):
    threads[i].start()
threads[0].join()


sock.close()
s.close()