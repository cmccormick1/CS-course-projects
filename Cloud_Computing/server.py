'''
AUTHOR: Caroline McCormick
FILE: server.py
ASSIGNMENT: Project 2
COURSE: CSC 346, Fall 2020 
PURPOSE: This program acts as a multi-threaded, HTTP server for an HTTP client.
         It takes two command line parameters: "port" and "dir_path." "port" is 
         the port number you want it to serve on, and "dir_path" is the directory
         in which the file you want to serve resides.

USAGE:
    python3 server.py port dir_path
'''

from socket import *
from threading import *
from os import path
import sys


def main():
    # Read in command line arguments
    args = sys.argv
    port = args[1]
    dir_path = args[2]
    
    # Create listening socket
    server_sock = socket()
    server_addr = ('0.0.0.0', int(port))
    server_sock.bind(server_addr)
    server_sock.listen(5)
    
    while True:
        # Accept incoming connection and create connected socket
        (con_sock, con_addr) = server_sock.accept()
        
        # Create thread
        thread = Thread(target=handle_requests, args=(con_sock, dir_path)).start()
        
        
def handle_requests(con_sock, dir_path):
    # Read request from client
    request = con_sock.recv(1024).decode()
    filename = request.split()[1]
    if not dir_path.endswith('/'):
        dir_path += '/'
    if filename.startswith('/'):
        filename = filename[1:]
    
    # Send error if file doesn't exist
    if not path.exists(dir_path + filename):
        err_msg = 'HTTP/1.1 404 Not Found\n\n'
        con_sock.sendall(err_msg.encode())
    else:
        # Open file
        file = open(dir_path + filename, 'rb')
        file_contents = file.read()    
        
        # Send good status message and file contents
        msg = 'HTTP/1.1 200 OK\nContent-Length: ' + str(len(file_contents)) + '\n\n'
        con_sock.sendall(msg.encode() + file_contents)
        
        
        
main()
        
        
        
        
        