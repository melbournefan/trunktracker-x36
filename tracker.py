import tkinter as tk
from tkinter import ttk
import serial
import csv
import xml.etree.ElementTree as XD
import datetime

#window init
master = tk.Tk()
master.geometry('1020x600')
master.title("TrunkTracker x36 v0.1")

#launch settings
def open_settings():
    setngs = tk.Toplevel()
    setngs.title("TrunkTracker - Settings")
    setngs.geometry("600x600")

#menubar init
menubr = tk.Menu(master)
menubr.add_command(label="File")
menubr.add_command(label="Settings", command=open_settings)
menubr.add_command(label="About")
menubr.add_command(label="Quit", command=master.quit)
master.config(menu=menubr)

#portslect frame
mainfr = ttk.Frame(master, borderwidth=5, relief="sunken", width=1020, height=50)
mainfr.grid(column=1, row=1, sticky="w,e", rowspan=3)
master.rowconfigure(0, weight=1)
master.columnconfigure(1, weight=1)
comptlbl = ttk.Label(master, text="COM Port:",).grid(column=1, row=1, pady=2, padx=4, sticky='W')
combox = ttk.Combobox(master, textvariable='comvar').grid(column=1, pady=2, padx=4, row=3, sticky='SW')
#COM Port selection

def select_com():
    listpts = serial.tools.list_ports.comports()
    
    comvar = StringVar(listpts)
    


#gridparameters


master.mainloop()
