from os import system, name
import os


def clean_word(x):
  #Previously, files used to be created as yourname= and it looked very bad. This is just a small cleanup job for making files with names that doesn't have the '=' in it.i.e. just yourname
  var = x.split("=")
  return var[0]

def clear(): 
  #Found this on the web, not sure exactly what it is doing, but I am importing OS, so i can clear the console when the user types in clear  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
        console()
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
        console()

def exit(): 
  #Found this on the web, not sure exactly what it is doing, but I am importing OS, so i can clear the console when the user types in clear  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


def print_list(x):
	#This function prints a clean list when requested by the user
	try:
		var = open(x, "r")
		var_read = var.readlines()
		if len(var_read) == 1:
			print("PrintError: Can't print variable as a list")
			return 1
		else:
			var_clean = []
			var_delete = []
			var_join = " ".join(var_read)
			var_join2 = var_join.split("\n")
			for i in var_join2:
				if i == "":
					var_delete.append(i)
				elif i == " list":
					var_delete.append(i)
				else:
					var_clean.append(i)
			del var_clean[0]
			print(var_clean)
	except FileNotFoundError:
		print("FileNotFoundError: List was not found")
		console()

def delete_file(x):
  try:
    os.remove(x)
    console()
  except FileNotFoundError:
    print("FileNotFoundError: That variable does not exist")
    console()

def print_string(x):
  #This function prints a certain variable that gets asked by the user
  try:
	  var = open(x, "r")
	  var_read = var.readlines()
	  del var_read[0]
	  print(var_read)
  except FileNotFoundError:
    print("FileNotFoundError: String was not found")
    console()

def print_var(varname):
	'''Prints variable to screen depending on variable type'''
	try:
		varfile = open(varname[1], "r")
		var_read = varfile.readline().rstrip()
		if("list" in var_read):
			print_list(varname[1])
		elif("string" in var_read):
			print_string(varname[1])
		else:
			print("PrintTypeError: The print type given was wrong")
	except FileNotFoundError:
		print("FileNotFoundError: Variable was not found")
		console()

def create_list(varname):
	'''This function will create personalized lists, so u can create an infinite amount of lists with any name. It also opens a custom file with the list name and appends the list contents into that file.'''
	del varname[0]
	varfile = open(clean_word(varname[0]), "w+")
	del varname[0]
	varname = "".join(varname)
	varname = varname.split(",")
	varlist = []
	for elem in varname:
		varlist.append(elem)
	varfile.write("list\n")
	for count in range(len(varlist)):
		varfile.write(varlist[count] + '\n')
	varfile.close()
	console()

def create_string(varname):
	del varname[0]
	varfile = open(clean_word(varname[1]), "w+")
	del varname[0]
	varname = "".join(varname)
	varfile.write("string\n")
	varfile.write(varname)
	varfile.close()
	console()

def console():
  '''This is the start of the terminal. This is where the code is led back to after every interaction with the terminal.'''
  try:
    write = input("\n>>> ")
    return print_to_console(write)
  except KeyboardInterrupt:
    print("\nKeyboardInterrupt: No function was sent")
    console()


def print_to_console(x):
  '''This is the main function, the will be hadling all the instructions given to the terminal'''
  check = x.split(" ")
  if "print" == check[0]:
    del check[0]
    var = " ".join(check)
    print(var)
    console()
  elif "printvar" == check[0]:
    print_var(check)
    console()
#This function is really stright forward. Just type helpin the console to get a gauge of everything you can do in this program
  elif "help" in check[0]:
    print("Here are the list of functions available right now: \nprint ________\nlist ________= ______\nstring _________= ______\nprint var _________\nclear\nhelp\ndelete _______")
    console()
#This is the clear function mentioned above.
  elif check[0] == "clear":
    clear()
  elif check[0] == "string":
    create_string(check)
  elif check[0] == "list":
    create_list(check)
  elif check[0] == "delete":
    delete_file(check[1])
  elif check[0] == "exit":
    exit()
  else:
    print("FunctionError: Type help to find typeable functions")
    console()



console()
