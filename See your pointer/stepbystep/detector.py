from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import os

window = tk.Tk()
window.geometry("1300x750+10+10")
window.resizable(False,False)

img_num = 0
path = r'DATA'
all_images = []
image_list = os.listdir(path)
for i in range(len(image_list)):
    all_images.append(ImageTk.PhotoImage(Image.open(path+"\\"+image_list[i])))

label = Label(image=all_images[img_num])
label.place(x=0,y=0)

id_l = Label(window,text="",font=("Arial 18"))
id_l.place(x=1120,y=50)

l1 = []
f = open(r'stepbystep\data.txt','a+')

def update_id(e):
    id_l.config(text=f'{((e.y)//25)*44+(e.x//25)}')
label.bind('<Motion>',update_id)

def b1_click(e):
    id_l.config(text=f'{((e.y)//25)*44+(e.x//25)}')
    l1.append(((e.y)//25)*44+(e.x//25))

label.bind('<Button-1>',b1_click)

def b3_click(e):
    global img_num,l1
    f.write(f"{image_list[img_num].split('.')[0]}:{list(set(l1))},\n")
    print("data added...")
    l1 = []
    img_num = img_num + 1
    label.config(image=all_images[img_num])
    print(img_num)

label.bind('<Button-3>',b3_click)
window.mainloop()