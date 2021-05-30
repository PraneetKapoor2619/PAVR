30.05.2021

Praneet Kapoor

pavr.py is a crude, dirty program which can be used to automate the process of building (compilation, linking, and hex file generation), and flashing of AVR microcontrollers using avr-gcc and avrdude, respectively. Note that it(pavr.py) is not a replacement for makefile. It has been created just for fun plus with the intention to not scare off people starting with embedded C with all different types of compiler options, linking, etc.

Before using pavr.py, it should be made sure that:
1. The system has the latest version of Python installed
2. pset.txt (configuration file for pavr.py) exists in the same directory as pavr.py   


The algorithm to use pavr.py to successfully to flash an AVR uc are:  
&nbsp;&nbsp;&nbsp;Step 1: Copy paste pavr.py to the directory in which source files are located.  
&nbsp;&nbsp;&nbsp;Step 2: Create a text file named pset.txt which will be acting as our configuration file.  
&nbsp;&nbsp;&nbsp;Step 3: Run pavr.py  
&nbsp;&nbsp;&nbsp;Step 4: Select the required operation from the menu.  

These steps required to use pavr.py are explained below with the help of an example.

EXAMPLE 
Suppose you have directory names "irsensor" in which you have the following files  
&nbsp;&nbsp;&nbsp;1. main.c  
&nbsp;&nbsp;&nbsp;2. USART.c  
&nbsp;&nbsp;&nbsp;3. USART.h  
&nbsp;&nbsp;&nbsp;4. pinDefine.h  
We have to compile our codes, and flash our avr micrcontroller, in this case ATemga328p on Arduino Nano dev. board.

Step 1: Copy paste pavr.py to the dir. irsensor

Step 2: Create a text file named pset.txt(vim command: vim pset.txt). In this file, enter the following rows:  

	part: <name of the slave microcontroller> 
	files: <files to be built. set "all" in case all files with ".c" extension are to be built> 
	port: <com port to which the programmer is connected> 
	programmer: <name of the programmer as per avrdude list of supported programmer> 
	baudrate: <baudrate at which the programmer will communicate with our system> 
	fuse: <fuse value. to be set properly. set "no" if you do not want to change the fuses or if you do not know what you are doing>  
	
	
In our example the pset.txt file has the following contents: 

	part: atmega328p 
	files: all
	port: /dev/ttyUSB0
	programmer: arduino
	baudrate: 57600
	fuse: no

Step 3: Run pavr.py using the following command
		
	python pavr.py

	or 

	python3 pavr.py

Step 4: If the config file has been read correctly the following menu will appear:
		
	1. Compile
	2. Link
	3. Generate Hex
	4. Flash
	5. Exit
	Operation>>
		
This menu is self-explainatory. It should be noted that selecting "Flash" option results in the execution of "Compile", "Link", and "Generate Hex" operations. Then flashing of slave microcontroller is done using avrdude and a programmer. 


