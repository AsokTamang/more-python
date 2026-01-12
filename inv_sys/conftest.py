import os
import sys

pathdir = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))
print(pathdir)
sys.path.insert(0,pathdir)  #here we are inserting the parent dir of this file in our system path