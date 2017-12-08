#!/usr/bin/env python 
#-*- coding: utf8 -*-
#Script by n@gisa
#Usage : python3 calculator_v1

print("This is a program that allows you to do calculations with two numbers. ")

oQ = input("Specifies whether it is an additon (-a), a subtraction (-s), a division (-d) or a multiplication (-m) : ")
oQ = str(oQ)

if oQ == "-a":
	oDem = input("Please give the first number : ")
	oDem2 = input("Please give the second number : ")
	oDem = int(oDem)
	oDem2 = int(oDem2)
	print(oDem+oDem2)
elif oQ == "-s":
	oDem = input("Please give the first number : ")
	oDem2 = input("Please give the second number : ")
	oDem = int(oDem)
	oDem2 = int(oDem2)
	print(oDem-oDem2)
elif oQ == "-d":
	oDem = input("Please give the first number : ")
	oDem2 = input("Please give the second number : ")
	oDem = int(oDem)
	oDem2 = int(oDem2)
	print(oDem/oDem2)
elif oQ == "-m":
	oDem = input("Please give the first number : ")
	oDem2 = input("Please give the second number : ")
	oDem = int(oDem)
	oDem2 = int(oDem2)
	print(oDem*oDem2)
