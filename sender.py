# port limit 0 to 65536
# ip 192.168.190.69
# port = 8888
import socket      # socket lib hepls communicate without connection 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_addrss = '192.168.190.236'
port = 2233
target = (ip_addrss,port)
msg = input('enter the msg')
encript_msg = msg.encode('ascii')
s.sendto(encript_msg,target)
print('msg sent')

# except Exception as e:        # when there is any error in code then it will run 
#     print('msg not sent')