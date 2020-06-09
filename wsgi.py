
import os
import sys
from app.main import app 

path = os.getcwd()
#print("path ",path)
base_path = os.path.dirname(__file__)
#print("base path",base_path)
static_p = os.path.join(path, "static")
sys.path.insert(0, base_path)
sys.path.insert(1,static_p)
#print("static_p ",static_p)
app.template_folder=static_p
app.static_folder=static_p




if __name__ == "__main__": 
        app.run() 
