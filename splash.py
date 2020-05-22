"""
    Splash Screen Demonstration
    Author: Israel Dryer
    Modified: 2020-05-22
"""
import tkinter as tk

# create the main window
root = tk.Tk()

# disable the window bar
root.overrideredirect(1)

# set trasparency and make the window stay on top
root.attributes('-transparentcolor', 'white', '-topmost', True)

# set the background image
psg = tk.PhotoImage(file='splash-logo.png')
tk.Label(root, bg='white', image=psg).pack()

# move the window to center
root.eval('tk::PlaceWindow . Center')

# schedule the window to close after 4 seconds
root.after(4000, root.destroy)

# run the main loop
root.mainloop()
