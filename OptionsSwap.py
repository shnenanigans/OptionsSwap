import os
import tkinter as tk
import instgroups
from tkinter import messagebox

def get_txt():
    txts = os.listdir(os.getcwd() + "\\data")
    i=0
    for elem in txts:
        elem = elem[:-4]
        txts[i]=elem
        i+=1
    return txts

def get_configs(insts):
    config_paths = []

    i=0
    while i<len(insts):
        config_path = mcpath + "\\instances\\" + insts[i] + "\\.minecraft\\config\\standardoptions.txt"
        config_paths.append(config_path)
        i += 1
    return config_paths

def create_group_widget():
    labelframe = tk.Frame(frame2, bg="#fee5b5", height=30, width=150)
    listframe = tk.Frame(frame2, bg="#fee5b5", height=170, width=125)
    grouplist = instgroups.find_groups(mcpath)
    groups = tk.Listbox(listframe, selectmode = "single", height=len(grouplist), bg="#FFF3DC")
    if len(grouplist)>10:
        groups.config(height=10)
    else:
        groups.config(height=len(grouplist))
    for each_item in range(len(grouplist)):
        groups.insert(tk.END, grouplist[each_item])
        groups.itemconfig(each_item)
    grouplabel = tk.Label(labelframe, text="Select a MultiMC group", background="#fee5b5")
    labelframe.place(relx=0.5, rely=0.35, anchor="n")
    listframe.place(relx=0.5, rely=0.45, anchor="n")
    groups.place(relx=0.5, rely=0, anchor="n")
    grouplabel.place(relx=0.5, rely=0.5, anchor="center")

    swap_button = tk.Button(frame3, text="Swap", command=lambda: find_instances(groups), bg="#fecca8", activebackground="#feedcc")
    swap_button.place(relx=0.5, rely=0.5, anchor="center")

def create_instance_widget():
    labelframe = tk.Frame(frame2, bg="#fee5b5", height=30, width=150)
    listframe = tk.Frame(frame2, bg="#fee5b5", height=170, width=125)
    instlist = instgroups.find_instances(mcpath)
    instances = tk.Listbox(listframe, selectmode = "multiple", height=len(instlist), bg="#FFF3DC")
    if len(instlist)>10:
        instances.config(height=10)
    else:
        instances.config(height=len(instlist))
    for each_item in range(len(instlist)):
        instances.insert(tk.END, instlist[each_item])
        instances.itemconfig(each_item)
    instlabel = tk.Label(labelframe, text="Select instances", background="#fee5b5")
    labelframe.place(relx=0.5, rely=0.35, anchor="n")
    listframe.place(relx=0.5, rely=0.45, anchor="n")
    instances.place(relx=0.5, rely=0, anchor="n")
    instlabel.place(relx=0.5, rely=0.5, anchor="center")

    swap_button = tk.Button(frame3, text="Swap", command=lambda: find_instances(instances), bg="#fecca8")
    swap_button.place(relx=0.5, rely=0.5, anchor="center")

#figure out if inst or groups is selected, and then get which instances to sync from the dropdown menues
def find_instances(select):
    #if groups is selected
    if method.get()==0:
        selected = select.curselection()
        if len(selected)==0:
            messagebox.showerror(title=None, message="Please select a group")
        for i in selected:
            group = select.get(i)
        insts = instgroups.find_instances_from_groups(group, mcpath)

    #if instances is selected
    if method.get()==1:
        selected = select.curselection()
        if len(selected)==0:
            messagebox.showerror(title=None, message="Please select instances")
        insts = []
        for i in selected:
            inst = select.get(i)
            insts.append(inst)
    swap(insts)

def swap(insts):
    try:
        configs = get_configs(insts)
        for file in txt_list.curselection():
            options = txt_list.get(file)
        options_path = os.getcwd() + "\\data\\" + options + ".txt"
        for i in range(len(configs)):
            with open(configs[i], "w+") as f:
                f.write(options_path)
    except Exception as e:
        messagebox.showerror(title=None, message="Make sure standardoptions.txt exists in this instance's config folder.")
        print(e)
    else:
        messagebox.showinfo(title=None, message="Success!")

try:
    with open("mcpath.txt") as f:
        mcpath = f.read()
        if "\\user\\" in mcpath:
            messagebox.showerror(message="Make sure mcpath.txt contains the path to your MultiMC path.")
except FileNotFoundError:
    messagebox.showerror(message="Create a file called mcpath.txt and put the path to your MultiMC in it.")

txts = get_txt()
root = tk.Tk()
root.geometry("450x400")

frame1 = tk.Frame(root, height=400, width=130, bg="#fee5b5")
frame2 = tk.Frame(root, height=400, width=220, bg="#fee5b5")
frame3 = tk.Frame(root, height=400, width=100, bg="#fee5b5")
frame1.place(x=0, y=0)
frame2.place(x=130, y=0)
frame3.place(x=350, y=0)


txt_label = tk.Label(frame1, text="Select options file", bg="#fee5b5")
txtlistframe = tk.Frame(frame1, bg="#fee5b5")
txt_list = tk.Listbox(txtlistframe, selectmode="single", height=len(txts), exportselection=0, bg="#FFF3DC")
if len(txts)>20:
    txt_list.config(height=20)
else:
    txt_list.config(height=len(txts))
for item in txts:
    txt_list.insert(tk.END, item)
txtlistframe.place(relx=0.5, rely=0.2, anchor="n")
txt_label.place(relx=0.5, rely=0.1, anchor="n")
txt_list.pack()


method = tk.IntVar()
radioframe = tk.Frame(frame2, bg="#fee5b5", height=100, width=200)
radioframe.place(relx=0.5, rely=0.03, anchor="n")
radio_label = tk.Label(radioframe, text="Select groups if you have multimc\ngroups, instances otherwise.", background="#fee5b5")
bygroups = tk.Radiobutton(radioframe, background="#fee5b5", activebackground="#fee5b5", text="groups", variable=method, value=0, command=create_group_widget)
byinst = tk.Radiobutton(radioframe, background="#fee5b5", activebackground="#fee5b5", text="instances", variable=method, value=1, command=create_instance_widget)
radio_label.place(relx=0.5, rely=0, anchor="n")
bygroups.place(relx=0, rely=0.4, anchor="nw")
byinst.place(relx=0, rely=0.7, anchor="nw")


create_group_widget()
root.mainloop()
