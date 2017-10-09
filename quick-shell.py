#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quick-shell.py
#  
#  Copyright 2017 zottel <z0ttelz@err0r-dev>
#  This is an open source program! You can modify it as you like!
#  But it's not made to harm any one! 
#  
#  
#  
#  
#  
# 

 
# Imports
import sys
import os

# def

def bash(command):
	os.system(command)
def clear():
	bash("clear")
def menu_error():
	raw_input("\033[1;37m")
	bash("./quick-shell.py")
def menu():
	print("\n" *5  + "\033[1;30mPress enter continue...\033[1;m")
	menu_error()
	





	
# Main menu
clear()
print("\033[1;3mYou may have to start this script as root. Or just type 'root'.\033[1;m\033[1;m\n")
print("\033[1;31mSelect:\033[1;m\n")
print("\033[1;32m1. Put Wificard in Monitormode\033[1;m")
print("\033[1;33m2. Stop Monitormode\033[1;m")






print("\033[1;32m99. Requirements\033[1;m")
print("\n\n\033[1;31mType exit to exit...\033[1;m")
cmd = raw_input("\n\033[1;32m")
print("\033[1;m")


# modules

# Put in mon mode
if (cmd == "1"):
	clear()
	print("\33[1;31mSelect interface:\33[1;m")
	bash("iwconfig")
	interface =raw_input("\33[1;36mInterface name:\33[1;m")
	bash("airmon-ng start " + interface + ">quickshell-airmon-ng.log")
	if interface == "" :
		print("\033[1;31mErr0r\033[1m")
	else :
		print("\033[1;33mWlan-card should now be called: \033[1;m\033[1;32m" + interface + "mon\033[1;m")
	menu()
# Put out of mon mode
elif (cmd == "2"):
	clear()
	print("\33[1;31mSelect interface:\33[1;m")
	bash("iwconfig")
	interface =raw_input("\33[1;36mInterface name:\33[1;m")
	bash("airmon-ng stop " + interface + ">quickshell-airmon-ng.log")
	if interface == "" :
		print("\033[1;31mErr0r\033[1m")
	else :
		print("\033[1;33mDone! If there are anny err0rs please look in the quickshell-airmon-ng.log \033[1;m")
	menu()
#exit
elif (cmd == "exit") :
	clear()
	print("\033[1;33mThanks for using quick-shell. \nWe hope u like it and we see u soon!\033[1;m")
	print("\033[1;30m Copyright Err0r Dev Software 2017\033[1;m")
	






		

# Requirements
elif (cmd == "99"):
	clear()
	print("\033[1;31mRequirements:\033[1;m\n")
	print("\033[1;33m1. Airmon-ng")
	print("2. Iwconfig")
	
	
	
	
	
	
	
	print("\033[1;m")
	menu()
# Bash
elif (cmd == "bash"):
	clear()
	bash("bash")
	menu()
# root
elif (cmd == "root"):
	clear()
	print("\033[1;35mYou have to enter your UNIX password:\033[1;m")
	bash("sudo python ./quick-shell.py")	
#err0r	
else :
	clear()
	print("\033[1;31mErr0r the command '" + cmd +"' was not found! \n Please contact the admins for support!\033[1;m")
	print("\n" *2  + "\033[1;30mPress enter continue...\033[1;m")
	menu_error()
