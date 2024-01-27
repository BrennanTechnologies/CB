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

cmd_str = 'git add .'
os.system(cmd_str)
cmd_str = 'git commit -m "sync"'
os.system(cmd_str)
cmd_str = 'git push'
os.system(cmd_str)


cmd_str += 'git add .'
cmd_str += 'git commit -m "sync"'
cmd_str += 'git push'
print(cmd_str)
#os.system(cmd_str)



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