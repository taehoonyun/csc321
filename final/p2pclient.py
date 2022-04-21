import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
while True:
    message = input("enter your message here : ")
    socket.send_string(message)

    #  Get the reply.
    reply = socket.recv()
    print("Received reply %s " % reply)
