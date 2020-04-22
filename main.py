from os import system, name
import os


def clean_word(x):
  '''Previously, files used to be created as yourname= and it looked very bad. This is just a small cleanup job for making files with names that doesn't have the '=' in it.i.e. just yourname: Refer back to line 5'''
  if "=" in x:
    var = x.split("=")
    return var[0]
  if "+" in x:
    var = x.split("+")
    return var[0]

def list_unpack(x):
  '''This function lets the user print string variable together: Refer back to line 14'''
  list = []
  print(x)
  for i in x:
    try:
      var = open(clean_word(x), "r")
      var_read = var.readlines()
      del var_read[0]
      list.append(var_read)
    except FileNotFoundError:
      print("FileNotFoundError: Variable given to concatenation does not exist")
      console()
  list_clean = " ".join(list)
  print(list_clean)
  console()

      

def clear(): 
  '''Found this on the web, not sure exactly what it is doing, but I am importing OS, so i can clear the console when the user types in clear: Refer back to line 10'''  
    # for windows 
  if name == 'nt': 
    _ = system('cls') 
    console()

  # for mac and linux(here, os.name is 'posix') 
  else: 
    _ = system('clear')
    console()

def exit(): 
  '''I am importing OS, so I can clear the console when the user types in clear: Refer back to line 22''' 
    # for windows 
  if name == 'nt': 
    _ = system('cls') 

  # for mac and linux(here, os.name is 'posix') 
  else: 
    _ = system('clear')


def print_list(x):
	'''This function prints a clean list when requested by the user. By clean, it means all newline's taken out as well as the key word for the file taken out: Refer back to line 33'''
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
  '''Deletes a file, which name will be given by the user: Refer back to line 59'''
  try:
    os.remove(x)
    console()
  except FileNotFoundError:
    print("FileNotFoundError: That variable does not exist")
    console()

def print_string(x):
  '''This function prints a string variable that gets asked by the user: Refer back to line 68'''
  try:
	  var = open(x, "r")
	  var_read = var.readlines()
	  del var_read[0]
	  print(var_read)
  except FileNotFoundError:
    print("FileNotFoundError: String was not found")
    console()

def print_int(x):
  '''Prints an int variable from an int file: Refer back to line 79'''
  try:
    var = open(x, "r")
    var_read = var.readlines()
    del var_read[0]
    print(var_read)
  except FileNotFoundError:
    print("FileNotFoundError: Variable was not found")
    console()

def print_float(x):
  '''Prints a float variable from a float file: Refer back to line 90'''
  try:
    var = open(x, "r")
    var_read = var.readlines()
    del var_read[0]
    print(var_read)
  except FileNotFoundError:
    print("FileNotFoundError: Variable was not found")
    console()

def print_var(varname):
  '''Prints variable to screen depending on variable type: Refer back to line 101'''
  try:
    varfile = open(varname[1], "r")
    var_read = varfile.readline().rstrip()
    if "list" in var_read:
      print_list(varname[1])
    elif "string" in var_read:
      print_string(varname[1])
    elif "int" in var_read:
      print_int(varname[1])
    elif "float" in var_read:
      print_float(varname[1])
    else:
      print("PrintTypeError: The print type given was wrong")
  except FileNotFoundError:
    print("FileNotFoundError: Variable was not found")
  console()

def create_list(varname):
	'''This function will create personalized lists, so you can create an infinite amount of lists with any name. It also opens a custom file with the list name and appends the list contents into that file: Refer back to line 120'''
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
  '''Creates a file that hold a given string: Refer back to line 136'''
  del varname[0]
  varfile = open(clean_word(varname[1]), "w+")
  del varname[0]
  varname = "".join(varname)
  varfile.write("string\n")
  varfile.write(varname)
  varfile.close()
  console()

def create_int(x, y):
  '''Creates integer file, that can only hold a number: Refer back to line 147'''
  varfile = open(clean_word(y), "w+")
  varfile.write("int\n")
  varfile.write(str(x))
  varfile.close()
  console()

def create_float(x, y):
  '''Create float file that can only hold a float: Refer back to line 155'''
  varfile = open(clean_word(y), "w+")
  varfile.write("float\n")
  varfile.write(str(x))
  varfile.close()
  console()


def console():
  '''This is the start of the terminal. This is where the code is led back to after every interaction with the terminal: Refer back to line 164'''
  try:
    write = input("\n>>> ")
    return print_to_console(write)
  except KeyboardInterrupt:
    print("\nKeyboardInterrupt: No function was sent")
    console()


def print_to_console(x):
  '''This is the main function, the will be hadling all the instructions given to the terminal: Refer back to line 174'''
  check = x.split(" ")
  if "print" == check[0]:
    if "%f" == check[1]:
      #This line will be a line that prints all files/variable holders at that point instead passing
      pass
    else:
      del check[0]
      var = " ".join(check)
      print(var)
      console()
  elif "printvar" == check[0]:
    list = []
    if "+" in check:
      for i in check:
        if "+" in i:
          list.append(i)
        elif "+" not in check[-1]:
          list.append(i)
        elif "+" in check[-1]:
          print("ConcatenationError: Concatenation given was wrong")
        else:
          print("ConcatenationError: Concatenation given was wrong")
      list_unpack(list)
    else:
      print_var(check)
      console()
        
#This function is really stright forward. Just type helpin the console to get a gauge of everything you can do in this program
  elif "help" in check[0]:
    print("Here are the list of functions available right now: \nprint ________\nlist ________= ______\nstring _________= ______\nprintvar _________\nint ________= ______\nfloat _________= ______\ndelete _______\nclear\nhelp\nexit")
    console()
#This is the clear function mentioned above.
  elif check[0] == "clear":
    clear()
  elif check[0] == "string":
    create_string(check)
  elif check[0] == "list":
    create_list(check)
  elif check[0] == "int":
    try:
      int(check[2])
      create_int(int(check[2]), check[1])
    except ValueError:
      print("ValueError: Int variable can only hold <class 'int'>")
      console()
  elif check[0] == "float":
    try:
      float(check[2])
      create_float(float(check[2]), check[1])
    except ValueError:
      print("ValueError: Float variable can only hold <class 'float'>")
      console()
  elif check[0] == "delete":
    delete_file(check[1])
  elif check[0] == "exit":
    exit()
  else:
    print("FunctionError: Type help to find typeable functions")
    console()



console()
