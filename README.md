# Python-Reverse-Shell

![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

A basic implementation of a reverse shell in Python. This repository provides code for creating a reverse shell connection between two machines, where one machine acts as the listener (server) and the other as the client, allowing remote command execution.

## Features

- **Reverse Shell Communication:** Establish a connection between the client and listener, enabling command execution on the client machine from the listener.

- **File Download:** Download files from the target machine to the listener, allowing retrieval of files remotely.

- **Search by Extension:** Search for files with a specific extension on the target machine, aiding in targeted file retrieval.

- **Network Scanning:** Perform network scanning on the target machine, providing information about open ports, services, and potential vulnerabilities.

- **Basic Security Considerations:** This repository provides a basic example of a reverse shell and additional features for educational purposes. It's important to note that reverse shells can be used for malicious activities. Always use such tools responsibly and only in controlled environments.


## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 2.7 installed on both the listener and client machines.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/7absec/Python-Reverse-Shell.git

   cd Python-Reverse-Shell

2. Send the Client.py to the victim(Target) machine
3. Run the Server on attacker machine
   ```bass
   python2 Server.py
4. Run the Client.py in victim machine
   ```bash
   python2 Client.py


##Commands

1. This shell works on predefind syntax only. Its recommended to use the same syntax in same format

2. Search for files with specific extension:
     ```bash
     Syntax -> search path extenion
  example --> search D:\ txt   [It will search for pdf files in D drive]
      
3. Download files from Traget machine
    ``` bash
    Syntax -> grab source_path destination_path
  example -->> grab*D:/text.png C:/img.png [It will downlaod the text.png file and save it in C drive]
      
4. Internal scan on the target
    ``` bash
    syntax -> scan ip ports [Note: ports should be provided as comma separated value, like 23,80]
  example -->> scan 127.0.0.1 22,80,443
      
5. Take a scaneenshot of target window
    ``` bash
    Syntax -> screencap desitnation_path
  example -->> screencap D:/ss.png [Screenshot will be saved on D drive on attacker machine


6. More featrues will be added in the future.
7. Script regarding persistent will be added in futur commits

**Note: Don't forget to do neccesary changes before executing the sripts.**

**Happy Hacking**

      
      
