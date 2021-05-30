import os
from subprocess import check_output
import re

#global variables
part = ''
files = ''
filenames = list()
port = ''
programmer = ''
baudrate = ''
fuse = ''

def pset_check():
	global part, files, filenames, port, programmer, baudrate, fuse

	fhandle = open("pset.txt", 'r')
	for line in fhandle:
		if(line.startswith("part:")):
			part = line.lstrip("part:")
			part = part.strip("\n\r\t ")
		elif(line.startswith("files:")):
			files = line.lstrip("files:")
			files = files.strip("\n\r\t ")
		elif(line.startswith("port:")):
			port = line.lstrip("port:")
			port = port.strip("\n\r\t ")
		elif(line.startswith("programmer:")):
			programmer = line.lstrip("programmer:")
			programmer = programmer.strip("\n\r\t ")
		elif(line.startswith("baudrate:")):
			baudrate = line.lstrip("baudrate:")
			baudrate = baudrate.strip("\n\r\t ")
		elif(line.startswith("fuse:")):
			fuse = line.lstrip("fuse:")
			fuse = fuse.strip("\n\r\t ")
		else: continue

	if(len(part)):
		print("Part:", part)
	else:
		invalid_exit("part")
	
	if(len(files)):
		if(files == "all"): file_extr("all")
		else: file_extr(files)
		print("Files:", files)
	else: 
		invalid_exit("files")
	
	if(len(port)):
		print("Port:", port)
	else:
		invalid_exit("port")
	
	if(len(programmer)):
		print("Programmer:", programmer)
	else:
		invalid_exit("programmer")

	if(len(baudrate)):
		print("Baudrate:", baudrate)
	else:
		invalid_exit("baudrate")
	
	if(len(fuse)):
		print("Fuse:", fuse)
	else: 
		invalid_exit("fuse")
	
def invalid_exit(string):
	print("Invalid", string)
	exit(0)

def file_extr(fn):
	global files, filenames
	if(fn == "all"):
		files = check_output(['dir'], shell = True).decode("utf-8")	
	output = re.findall("[^\n\t\r ]+", files)
	files = ''
	for fname in output:
		if(fname.find(".c") != -1):
			files = files + fname + " "
			filenames.append(fname[:len(fname) - 2])
	return 0

def menu():
	while(True):
		print("1. Compile\n2. Link\n3. Generate Hex\n4. Flash\n5. Exit")
		choice = int(input("Operation>> "))
		if(choice == 1): compile()
		elif(choice == 2): link()
		elif(choice == 3): hexgen()
		elif(choice == 4): flash()
		elif(choice == 5): exit(0)
		else: print(choice + " operation not defined!\a")
		print("\n")
	return 0

def compile():
	global filenames, part
	print(filenames)
	for name in filenames:
		command = "avr-gcc -g -Os -mmcu=" + part + " -c " +  name + ".c -o " + name + ".o"
		print(command)
		os.system(command)
	return 0

def link():
	global filenames, part
	print(filenames)
	command = "avr-gcc -g -mmcu=" + part
	for name in filenames:
		command = command + " " + name + ".o"
	command = command + " -o prgrm.elf"
	os.system(command)
	return 0

def hexgen():
	command = "avr-objcopy -j .text -j .data -O ihex prgrm.elf prgrm.hex"
	os.system(command)
	return 0

def flash():
	global part, port, programmer, baudrate, fuse
	command = "avrdude -c" + programmer + " -p" + part + " -P" + port + " -b" + baudrate + " -v -U flash:w:prgrm.hex:i"
	if(fuse != "no"):
		command = command + " " + fuse
	compile()
	link()
	hexgen()
	os.system(command)
	return 0
	
if __name__ == "__main__" :
	pset_check()
	menu()
