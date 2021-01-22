'''
Project: twist.py
Author: Caroline McCormick
Purpose: 
      This program works like the "curl" command. It takes two command line arguments
    1. the DNS name or IP address of the server and 2. the file name you want to
    access. With these arguements, it will create and open a socket and connect to
    the HTTP server. Once connected, it will send a request message to the host for
    the file name provided, and it will receive the data sent back from the server
    until no more data is sent back. Once the stream ends, the data sent back is
    printed to the console.

Usage:
    python3 twist.py hostname filename
'''

from socket import *
import sys


def main():    
    # Read in command line arguments
    args = sys.argv
    num_args = len(args)
    
    # Make sure there are exactly 2 command line arguments
    if num_args < 3:
        print("Not enough arguments.")
        print("Usage: python3 twist.py lecturer-russ.appspot.com /classes/cs346/fall20/")
        sys.exit(2)
    elif num_args > 3:
        print("Too many arguments.")
        print("Usage: python3 twist.py lecturer-russ.appspot.com /classes/cs346/fall20/")
        sys.exit(2)
        
        
    # Create a new socket    
    new_socket = socket(AF_INET, SOCK_STREAM)
    
    # Connect to the socket via command line given host name and port 80
    address = (args[1], 80)
    new_socket.connect(address)
    
    # Create a request message and send to server
    req_msg = "GET " + args[2] + " HTTP/1.1\n"
    host_msg = "Host: " + args[1] + "\n"
    entire_msg = req_msg + host_msg + "\n"
    new_socket.sendall(entire_msg.encode())
    
    
    # Get the response from the server and print it out
    data = new_socket.recv(1024)
    output = data.decode()
    while len(data) == 1024:
        data = new_socket.recv(1024)
        if len(data) != 0:
            output += data.decode() 
    print(output)
    

main()