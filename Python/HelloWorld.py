import sys

print("Hello World!")

#import CB_Module
import CB_Module as cb

module_name = "CB_Module"
if module_name in sys.modules:
    print("Found ME!!!")
	#print(module_name + " was found!")
else:
    print(module_name + " was NOT found!")

cb.write_log("New Log")

cb.lazygit()
