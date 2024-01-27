print("Hello World!")

# function lazygit() {
#     git add .
#     git commit -a -m "$1"
#     git push
# }



# sub process
import subprocess
#subprocess.run(["ls", "-l"]) 
#subprocess.run([cmd_str]) 

# os
import os
# os.system('git add .')
# os.system('git commit -m "sync"')
# os.system('git push')

# def lazygit():
# 	cmds = [
# 			'git add .', 
# 			'git commit -m "Sync"', 
# 			'git push'
# 			]
# 	for cmd in cmds:
# 		print(cmd)
# 		os.system(cmd)
#lazygit()

#import sys
# modulename = "CB_Module.py"
# import CB_Module
# if modulename not in sys.modules:
# 	#print(sys.modules)
# 	print(modulename + " NOT LOADED")
# else:
# 	print(modulename + " WAS LOADED")

import sys
output = [module.__name__ for module in sys.modules.values() if module]
output = sorted(output)

for o in output:
	print(o)

import os
import CB_Module as cb

y = "CB_Module"
if y in output:
	print(y + " was found!")
else:
	print(y + " was NOT found!")


cb.lazygit()

#print('The list of imported Python modules are :',output)

# 	subprocess.run(["ls", "-l"]) 
# lazygit()

#git config user.name "chris.brennan"
#git config --global user.email "brennanc@hotmail.com"

#C:\Users\brenn\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts

# https://jupyter.org/install
# pip install jupyterlab
# pip install jupyter