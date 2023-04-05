from tkinter import * 
from tkinter import ttk
import os 
import poke_api

root = Tk()
root.title('Pokemon Viewer')

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
image_cache_dir = os.path.join(script_dir, 'images')

#Make the image directory 
if os.path.isdir(image_cache_dir):
    os.makedirs(image_cache_dir) 

# Set the window icon
icon_path = os.path.join(script_dir, 'poke_ball.ico')
# Print paths to see what they are
print(script_path, script_dir, icon_path, sep='\n')

root.iconbitmap('C:\poke_ball.ico') 
# create the windows 
# set the window icon 

frm_left = ttk.Frame(root)
frm_left.grid(row=0, column=0, padx=(10), pady=10, sticky=NSEW)
frm_left.columnconfigure(0, weight=1)
frm_left.rowconfigure(0, weight=1)

img_poke = PhotoImage(file='poke.png')
lbl_poke = ttk.Label(frm_left, image=img_poke)
lbl_poke.grid(padx=10, pady=10)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=40)
root.columnconfigure(1, weight=60)

pokemon_name_list = poke_api.get_pokename_name()
cbox_poke_name = ttk.Combobox(Frame,values=pokemon_name_list, state='readonly')
cbox_poke_name.set("Select a Pokemon")
cbox_poke_name.grid(row=1, column=1, padx=10, pady=10)

def handle_os_sel(event):
    
    pokemon_name = cbox_poke_name.get() 
    image_path = poke_api.download_pokemon_artwork(pokemon_name,image_cache_dir)
    if image_path is not None:
          img_poke['file'] = image_path
          
cbox_poke_name.bind('<<ComboboxSelected>>', handle_os_sel)


btn_set_desktop = ttk.Button(frm_left, text='Set Desktop Image')
btn_set_desktop.grid(row=0, column=2, padx=10, pady=10)



root.mainloop() 

