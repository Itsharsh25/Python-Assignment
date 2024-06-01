# port limit 0 to 65536
# ip 192.168.190.69
# port = 8888
import socket      # socket lib hepls communicate without connection 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_addrss = '192.168.190.69'
port = 2222
target = (ip_addrss,port)
s.bind(target)
while True:
        msg = s.recvfrom(120)
        data = msg(0)
        data = '/n'
        data.encode('ascii')    
        

    # when there is any error in code then it will run 
