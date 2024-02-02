import tkinter as tk
from tkinter import Menu, ttk
from tkinter.messagebox import showinfo

root = tk.Tk()

root.title('Tkinter Window Demo')
root.geometry('1200x800')
root.resizable(False, False)



# progress label text
def update_progress_label():
    return f"Current Progress: {progressbar['value']}%"



# btn function
def submit_btn_clicked():
    """ callback when the login button clicked
    """
    msg = 'The button was clicked!'
    showinfo(
        title='Information',
        message=msg
    )
    if progressbar['value'] < 100:
        progressbar['value'] += 20
        value_label['text'] = update_progress_label()
    else:
        showinfo(message='The progress completed!')



# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

# add a submenu
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Keyboard Shortcuts')
sub_menu.add_command(label='Color Themes')

# add the File menu to the menubar
file_menu.add_cascade(
    label="Preferences",
    menu=sub_menu
)

# add Exit menu item
file_menu.add_separator()
file_menu.add_command(
    label='Exit',
    command=root.destroy
)


menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)
# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu,
    underline=0
)



# button
submit_btn = ttk.Button(root, text='Next', command=submit_btn_clicked)
submit_btn.pack(ipadx=5, ipady=5, expand=True)


progressbar = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=280)
# place the progressbar
progressbar.pack(ipadx=10, ipady=20, expand=True)


value_label = ttk.Label(root, text=update_progress_label())
value_label.pack()



root.mainloop()
