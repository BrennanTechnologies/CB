import sys

print("Hello World!")

import CB_Module
module_name = "CB_Module"

if module_name in sys.modules:
    print()
	#print(module_name + " was found!")
else:
    print(module_name + " was NOT found!")

CB_Module.lazygit()
