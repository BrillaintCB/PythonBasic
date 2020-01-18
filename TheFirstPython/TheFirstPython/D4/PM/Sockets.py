"""
Python provides two levels of access to network service. at a low level, you can access the basic socket support in the underlying operating system,
which allows you to implement clients and severs for both connection-oriented and connectionsless protocols.


Python aslo has libraries that provide higher-level access to specific applciation-level network
protocols, such as FTP, HTTP, and so on.
This chapter gives you understanding of most famous concept in Networking - Socket Programming.


What is Sockets?

Sockets are the endpoints of brdirectional communications channel.
Sockets may communicate within a process, betwen processes on the same machine, or between processes on different countinents.

Sockets may be implemented over a number of different channel types: Unix domain sockets, TCP, UDP, and so on.
The socket library provides specific classes for handling the common transports as well as a generic interface for handling the rest

"""

#Domain
"""
The family of protocols that is used as the transport mechanism.
These values are constants such as AF_INET, PF_INET, PF_UNIX< PF_X25, and so on.\
"""
#Type
"""
The type of communications between the two endpoints, typically SOCK_STREAM for connection-oriented protocols and SOCK_DGRAM for connectionless protocols
"""
#protocol
"""
Typically zero, this may be used to identify a variant of a protocol within a domain and type.
"""
#hostname
"""
This identifier of a network interface-
A string, which can be a hostname, a dotted-quad address, or an IPV6 address in colon(not possibly dot)notation

A string <broadcast>, which specifies an INADDR_BROADCAST address

A-zero-length string, which specifies INADDR_ANY, or

An integer, interpreted as a binary address in host byte order.
"""
#port
"""
 Each server listens for clients calling on one or more ports. A port may be a Fixnum port number, a string 
 constrains a port number, or the name of a service.

"""


import socket #Import socket module

s = socket.socket() # Create a socket object
host = "192.168.200.205"
port = 54321
s.bind((host, port)) # Bind to the host and port as Tuple

s.listen(15)
while True:
    c, addr = s.accept() # Establish connection with client.
    print("Got connection from", addr)

    output = "Thank you for connecting"
    #c.sendall(output.encode('utf-16'))
    c.sendall(output.encode('utf-8'))
    #c.send(output.encode('utf-8'))
    #c.send(output)
    c.close() # close the coneection

# https://recipes4dev.tistory.com/153