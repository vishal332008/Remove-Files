import time
import os
from datetime import datetime


time.time()

path = input("Enter The Path : ")
source = input("Enter The Source : ")

if os.path.exists(path):
    os.walk(path)
    path = os.path.join(path+"/"+source)
    date1 = time.time()
    
    if date1 - os.stat(path)[9]>259200:
        os.remove(path)
else:
    print("Path Not Found")