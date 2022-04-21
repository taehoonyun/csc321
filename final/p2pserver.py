import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("From Client: %s" % message)

    #  Send reply back to client
    msg = input("enter your msg here : ")
    socket.send_string(msg)
    print("")
