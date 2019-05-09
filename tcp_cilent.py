import socket
import threading

#创建一个socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#获取本机地址
host = '127.0.0.1'
#端口
port = 12345
#创建一个用于添加线程的列表
threads = []
#连接服务器
s.connect((host, port))
print('客户端已连接')

#发送消息
def fa():
    while True:
        #获取发送内容
        send_msg = input('我:\n')
        #将发送内容进行编码发送
        s.send(send_msg.encode())
        #判断发送内容是否为exit，是则退出并关闭客户端
        if send_msg == 'exit':
            break
#接收消息
def shou():
    while True:
        #将接收到的内容进行解码
        info = s.recv(1024).decode()
        #退出时关闭socket
        if info == 'quit':
            s.close()
            print('客户端已关闭')
            break
        print('你:' + info)

info = ''
t2 = threading.Thread(target=fa)#创建一个用于发的线程
t1 = threading.Thread(target=shou)#创建一个用于收的线程
#将创建的线程添加到列表
threads.append(t2)
threads.append(t1)
for i in range(len(threads)):
    threads[i].start()#启动线程

# 阻塞线程，直到子线程执行结束，主线程才能结束。
threads[0].join()
s.close()

