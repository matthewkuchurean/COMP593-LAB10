from tkinter import * 
import os 
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# create the windows 
root = Tk()
root.title('')
root.iconbitmap('')

# set the window icon 

icon_path = os.path.join(script_dir, 'poo.ico')
root.iconbitmap(icon_path)