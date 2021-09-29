import tkinter as tk
import subprocess as sub
import os
import tkmacosx as tkm
from tkinter import *


root = tk.Tk()
root.title("Search and Replace")

#set read write permissions for search-replace.sh
os.system("chmod 755 search-replace.sh")

#container frame for all elements
container = Frame(root)
container.pack()

wrapper = Frame(container)
wrapper.pack(side=LEFT)

wrapper2 = Frame(container)

text_box = Text(wrapper2, height=10, width=60, font=12, background="gray")
text_box.pack(side=LEFT, expand=True)

sb_ver = Scrollbar(wrapper2,orient=VERTICAL)
sb_ver.pack(side=RIGHT, fill=Y)

text_box.config(yscrollcommand=sb_ver.set)
sb_ver.config(command=text_box.yview)

wrapper2.pack(side=LEFT)

#frame for first line of elements
line1 = Frame(wrapper)
line1.pack(anchor="w")
# Prompt to ask for dry run 
dry_run_label = tk.Label(line1, text="Would you like to run a dry run first?")
dry_run_label.pack(side=tk.LEFT)
#variables
dry_var = IntVar()
dry_var.set(1)
dry_script_var = ""

def dry_checker():
    global dry_script_var
    if dry_var.get():
        dry_script_var = "yes"
    else:
        dry_script_var = "no"

#yes checkbox
yes_button = Radiobutton(line1, text="Yes", value=1, variable=dry_var)
yes_button.pack(side=tk.LEFT)

#no checkbox
no_button = Radiobutton(line1, text="No", value=0, variable=dry_var)
no_button.pack(side=tk.LEFT)



#frame for second line of elements
line2 = Frame(wrapper)
line2.pack(anchor="w")
#enter site name prompt
name_label = Label(line2, text="Enter the Site Name")
name_label.pack(side=tk.LEFT)
#field to enter site name
site_name_var = StringVar()
site_name_field = Entry(line2)
site_name_field.pack(side=LEFT)



#frame for third line of elements
line3 = Frame(wrapper)
line3.pack(anchor="w")
#site environment prompt
env_prompt_label = Label(line3, text="Site Environment")
env_prompt_label.pack(side=LEFT)
#environment checkboxes
#Dev
env_check_var = IntVar()
env_check_var.set(0)
env_script_var = ""

def env_check():
    global env_script_var
    if env_check_var.get() == 0:
        env_script_var = "dev"
    elif env_check_var.get() == 1:
        env_script_var = "test"
    elif env_check_var.get() == 2:
        env_script_var = "live"
    else:
        env_script_var = "invalid"

dev_check = Radiobutton(line3, text="Dev", value=0, variable=env_check_var)
dev_check.pack(side=LEFT)
#test
test_check = Radiobutton(line3, text="Test", value=1, variable=env_check_var)
test_check.pack(side=LEFT)
#live
live_check = Radiobutton(line3, text="Live", value=2, variable=env_check_var)
live_check.pack(side=LEFT)




#frame for fourth line of elements
line4 = Frame(wrapper)
line4.pack(anchor="w")
#prompt for entering the string to search
search_string_label = Label(line4, text="Enter the String to Search")
search_string_label.pack(side=LEFT)
#field to enter search string
search_string_field = Entry(line4)
search_string_field.pack(side=LEFT)



#frame for fifth line of elements
line5 = Frame(wrapper)
line5.pack(anchor="w")
#prompt to enter replacment string
replace_string_label = Label(line5, text="Enter the Replacment String")
replace_string_label.pack(side=LEFT)
#field to enter replacment string 
replace_string_field = Entry(line5)
replace_string_field.pack(side=LEFT)

# clear entry fields function
def clear_pressed():
    site_name_field.delete(0, END)
    search_string_field.delete(0, END)
    replace_string_field.delete(0, END)
    text_box.delete("1.0", "end")

def run_pressed():
    global return_code
    global result_btn_state
    global results
    dry_checker()
    env_check()

    sub.call(['sh', './search-replace.sh', dry_script_var, str(site_name_field.get()), env_script_var, str(search_string_field.get()), str(replace_string_field.get())])
    results = tkm.Button(wrapper, text="Results", command=view_results, padx=10, pady=5)
    results.pack()


def view_results():
    print("view results pressed")
    with open("terminal-output.txt") as f:
        for line in f:
            print(line)
            text_box.insert(END, line)
    results.pack_forget()
  
#control buttons
run = tkm.Button(wrapper, text="Run", command=run_pressed, padx=10, pady=5)
run.pack()
clear = tkm.Button(wrapper, text="Clear", command=clear_pressed, padx=10, pady=5)
clear.pack()


root.mainloop()