import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

# maximum number of backlog connections set to 5
# start listening
server.listen(5)

print"[*] Listening on %s:%d" % (bind_ip, bind_port)

#performs recv and then sends message back to client
def handle_client(client_socket):
    request = client_socket.recv(1024)
    
    print"[*] Recieved: %s" % request
    
    # send back packet
    client_socket.send("ACK!")
    
    client_socket.close()
    
    while True:
        # when client connects, return val of server.accept() is (conn, addr) 
        # passed into client, addr
        # conn is new socket object
        client,addr = server.accept()
        
        print "[*] Accepted connection from %s:%d " % (addr[0], addr[1])
        
        # create new thread that points to handle_client func
        client_handler = threading.Thread(target = handle_client, args = (client,))
        
        # start thread to handle client
        client_handler.start()
