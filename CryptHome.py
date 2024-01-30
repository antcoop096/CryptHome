#import libraries
import os
import turtle
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
import tkinter as tk
import webbrowser
import shutil

def button(img, x2, y2, comm, window):
 button = Button(window,
                command = comm,
                bg="#063763",
                bd=0,
                activebackground="#063763",
                state=ACTIVE,
                image = img)               
 button.place(x=x2, y=y2)    


def get_file_name(file_path): #this captures the file name by...
    file_path_components = file_path.split('/') #splits the filepath string into multiple parts, seperating the things between "/" into different strings, and putting all those strings in a list
    file_name_and_extension = file_path_components[-1] #gets and returns the last string in the list, which is the file name
    return file_name_and_extension

def openFile(): #opens the crypto storage connected to software
    filepath = filedialog.askopenfilename(initialdir = "/Users/AnthonyCooper/Desktop/CryptoProject 2/CryptoStorage") #looks for the user to choose and item in the software storage, this whole method with return the filepath of that item


def openFile2(): #opens the drive
    filepath = filedialog.askopenfilename(initialdir = "/Volumes/SONI") #looks for the user to choose an item in the drive storage, this whole method will return the filepath of that item
    shutil.move(src = filepath, dst = "/Users/AnthonyCooper/Desktop/CryptoProject 2/CryptoStorage")


def openFile3(): #opens the drive
    filepath = filedialog.askopenfilename(initialdir = "/Users/AnthonyCooper/Desktop/CryptoProject 2/CryptoStorage") #looks for the user to choose an item in the drive storage, this whole method will return the filepath of that item
    shutil.move(src = filepath, dst = "/Volumes/SONI")


window = Tk() #displays screen
icon = PhotoImage(file = "crypthomeicon.png")
window.iconphoto(True,icon)

def manage():
    window.title("Crypt Home - Manager")

    manage_bg = PhotoImage(file = "manage(PROTO).png")
    Label(window, image = manage_bg).place(x=0,y=0)

    view_b_i = PhotoImage(file='view_b_i.png')
    button(view_b_i, 825, 632, openFile, window)

    drive_b_i = PhotoImage(file='drive_b_i.png')
    button(drive_b_i, 829, 845, openFile2, window)

    software_b_i = PhotoImage(file='software_b_i.png')
    button(software_b_i, 1310, 845, openFile3, window)

    back_b_i = PhotoImage(file='back_b_i.png')
    button(back_b_i, 37, 37, main, window)

    window.mainloop()

def safety(): #
    window.title("Crypt Home - Crypto Safety 101")

    safety_bg = PhotoImage(file = "safety(PROTO).png")
    Label(window, image = safety_bg).place(x=0,y=0)

    back_b_i = PhotoImage(file='back_b_i.png')
    button(back_b_i, 37, 37, main, window)

    window.mainloop()

def review():
   
   webbrowser.open("https://sites.google.com/epsstudents.org/cryptositereviewmockup/home") #goes to the review site via webbrowser
   window.mainloop()

def info():
    window.title("Crypt Home - Software Info/Usage Guide")

    info_bg = PhotoImage(file = "info(PROTO).png")
    Label(window, image = info_bg).place(x=0,y=0)

    back_b_i = PhotoImage(file='back_b_i.png')
    button(back_b_i, 37, 37, main, window)

    window.mainloop()

def main():
    window.title("Crypt Home - Home Menu")

    main_menu_bg = PhotoImage(file = "main_menu(PROTO).png")
    Label(window, image = main_menu_bg).place(x=0,y=0)

    logo = PhotoImage(file = "crypthomelogo.png")
    Label(window, image = logo).place(x=841,y=203)
     
    manage_b_i = PhotoImage(file='manage_b_i.png')
    button(manage_b_i, 1040, 555, manage, window)

    safety_b_i = PhotoImage(file='safety_b_i.png')
    button(safety_b_i, 1039, 692, safety, window)

    review_b_i = PhotoImage(file='review_b_i.png')
    button(review_b_i, 883, 830, review, window)

    
    info_b_i = PhotoImage(file='info_b_i.png')
    button(info_b_i, 890, 970, info, window)

    
    exit_b_i = PhotoImage(file='exit_b_i.png')
    button(exit_b_i, 1228, 1110, exit, window)
    
    window.mainloop()


main()

###
