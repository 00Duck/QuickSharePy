# QuickSharePy
A (very) simple Python server for sharing files between computers.

## Setup

- Make sure python, pip, and git are all installed. From a PowerShell or Bash shell:

`git --version; python3 --version; pip3 --version`

- Clone down the respository to the computer that will be hosting the server.

`git clone https://github.com/00Duck/QuickSharePy`

- Inside the directory you just cloned down, run the following to install dependencies:

`pip3 install -r requirements.txt`

- Open the srv.py file. Modify the following:

`HOST = '0.0.0.0'`  This can be kept as-is, and will default to your computer's private IP address

`PORT = 8000` The default port to use

`SHARED_DIR = r'/path/to/shared/folder'` Make sure to change this to the correct full folder path you would like to share

- Save and close the file
- Type `python3 srv.py` to start the server.

## Usage

On another computer or virtual machine (connected locally via the network), you can do the following:

### File Retrieval from Shared Directory (Host > Client)

`wget 192.168.1.123:8000/myfilename.txt`

### File Send to Shared Directory (Client > Host)

`curl -F file=@myfilename.txt 192.168.1.123:8000`
