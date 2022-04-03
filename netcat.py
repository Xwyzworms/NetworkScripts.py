import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading
import NetCat

DEFAULT_IP : str = "YOUR IP"
def execute():
	cmd = cmd.strip()
	if not cmd:
		return
	output = subprocess.check_output(shlex.split(cmd),
									 stderr=subprocess.STDOUT)
	return output

if __name__ == "__main__":
	parser = argparse.ArgumentParser(
		description=" BLOk ",formatter_class=argparse.RawDescriptionHelpFormatter,
		epilog=textwrap.dedent(""" 
			netcat.py -t <target> -p <port> -l -c # Command Shell
			netcat.py -t <target> -p <port> -l -u # Upload File
			netcat.py -t <target> -p <port> -l -e=\"cat /etc/passwd\" # Execute Command
			echo 'ABC' | ./netcat.py - t <target> -p <port> # echo text to server port provided
			netcat.py -t <target> -p <port> -l -c # COnnect to server
		""")
	)

	parser.add_argument("-c", "--command",action="store_true" ,help="Command Shell")
	parser.add_argument("-e", "--execute", help="Execute Command")
	parser.add_argument("-l", "--listen", help="Listen on port", action="store_true")
	parser.add_argument("-u", "--upload", help="Upload File")
	parser.add_argument("-t", "--target", help="Target IP", default=DEFAULT_IP)
	parser.add_argument("-p", "--port", help="Target Port", type=int, default=5555)

	args = parser.parse_args()

	if args.listen:
		buffer = ""
	else:
		buffer = sys.stdin.read() # use CTRL+ D to end input
	print(buffer)
	nc = NetCat(args, buffer.encode())