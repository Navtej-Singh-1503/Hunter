'''
CREATED BY Navtej-Singh-1503
© 2025 Navtej Singh Saggar
Educational use only

13/02/2026


mail - navtejsingh15032011@gmail.com

'''

import os
import time


print("INSTALLING PACKAGES")
print("IT WILL START IN 3 SECONDS")

time.sleep(3)

os.system("sudo apt update")
os.system("pip install google-generativeai")
os.system("pip install --upgrade google-generativeai")


print("NEED GOOGLE GEMINI API KEY IF YOU DON'T HAVE YOU CAN GET IT ON https://aistudio.google.com/api-keys")
print("ENTER YOUR GOOGLE GEMINI API KEY ")
api = input("..>> ")

with open("FILES/api.py" , "w") as f:
    f.write("apikey = '"+api+"'")

with open("modify/api.py", "w") as w:
    w.write("apikey = '"+api+"'")


