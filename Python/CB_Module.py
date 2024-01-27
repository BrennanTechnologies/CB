import sys
import random
import array as arr
import CB_Module as cb
from datetime import date
from datetime import datetime

### Function Template:
### -----------------------------------
def function_template(a,b):
	try:
		print("Try")
	except NameError:
		print ("Name Error")
	except TypeError: 
		print("Error: cannot add an int and a str")
	except ZeroDivisionError:
		print("Div by Zero")
	except:
		error_type, error_instance, traceback = sys.exc_info()
		print(sys.exc_info())
		print("Other Error")
	else:
		print("Else")
	finally:
		print("Finally")


### Write Log:
### -----------------------------------
def write_log(msg, cat="INFO"):
	# Print Msg
	print(msg)
	
	# Open Log File
	log_file = "logfile.log"
	file = open(log_file, 'a+')
	
	# Date/Time
	today = date.today()
	time = datetime.now()
	time = time.strftime("%H:%M:%S")
	
	# Build Msg String
	msg = str(time) + "\t" +str(today) + "\t" + cat + "\t" + msg + "\n"

	# Write File / Close File
	file.write(msg)
	file.close()
	
### Read File:
### -----------------------------------
def read_file(file_name):
	file = open(file_name, 'r')
	print(file.read())
	file.close()

# Create random array
### -----------------------------------
def make_random_array(num_elements, min_val, max_val):
	#a = arr.array("i")
	a = []
	for i in range(0,num_elements):
		a.append(random.randint(min_val,max_val))
	return a