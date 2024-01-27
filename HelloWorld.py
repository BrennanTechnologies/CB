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

cmds = [
		'git add .', 
		'git commit -m "Sync"', 
		'git push'
		]
for cmd in cmds:
	print(cmd)
	os.system(cmd)

# def lazygit():
#     # git add .
#     # git commit -a -m "$1"
#     # git push

# 	subprocess.run(["ls", "-l"]) 
# lazygit()

#git config user.name "chris.brennan"
#git config --global user.email "brennanc@hotmail.com"

#C:\Users\brenn\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts

# https://jupyter.org/install
# pip install jupyterlab
# pip install jupyter