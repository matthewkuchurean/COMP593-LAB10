from tkinter import * 
from tkinter import ttk
import os 
import poke_api

root = Tk()
root.title('Pokemon Viewer')

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
# Set the window icon
icon_path = os.path.join(script_dir, 'poke_ball.ico')
# Print paths to see what they are
print(script_path, script_dir, icon_path, sep='\n')

icon_path = os.path.join(script_dir, 'poke_ball.ico')
root.iconbitmap('C:\poke_ball.ico') 
# create the windows 
# set the window icon 

frm_left = ttk.Frame(root)
frm_left.grid(row=0, column=0, padx=(15), pady=15, sticky=NSEW)
frm_left.columnconfigure(0, weight=1)
frm_left.rowconfigure(0, weight=1)

frm_right = ttk.Frame(root, relief="groove")
frm_right.grid(row=0, column=1, padx=(5,10), pady=10, sticky=NSEW)
frm_right.columnconfigure(0, weight=1)
frm_right.rowconfigure(0, weight=1)


root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=40)
root.columnconfigure(1, weight=60)

root.mainloop()

