# Overview

This is a simple demonstration of what a server to client model would look like if both were running on the same network. This uses ports to connect from one computer to the other to send messages that return demonstation data for the user.

With this demo, it is designed in a way that will allow the user to modify and scale the server and client side to their wishes. Additionally, the server side has a simple bash file that the user can use to begin the run process of the server. While this may be useless due to the small nature of the server, a more complex program with multiple moving parts may need a similar file to get everything running

[Software Demo Video]([http://youtube.link.goes.here](https://youtu.be/2DYttLCXo-U))

# Network Communication

This is a client to server program. The client attempts to contact the server via a port and IP address. The server then waits for a password or "handshake" to ensure that the user is authorize to access the data and then returns info based upon the users entry.

This program used UDP to send messages back and forth between the server and the client. The server takes specific messages from the client and then returns a message dependent upon the users input.

Data is sent via bianary and then uncoded along each end.

# Development Environment

The tools that where used was python and basic networking.

# Useful Websites
* [Python Networking](https://www.tutorialspoint.com/python/python_networking.htm)
* [Network Programming](https://www.youtube.com/watch?v=FGdiSJakIS4&ab_channel=freeCodeCamp.org)

# Future Work

* Encode the handshake using a hashing algorithm so if it gets intercepted, the hacker will still be unable to connect
* Have the server modify data and then return it. (Something like a calculator
