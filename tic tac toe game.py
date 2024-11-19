from tkinter import *
from tkinter import messagebox


Window=Tk()
Window.title("Tic Tac Toe")
Window.geometry("500x400")

# ************************************
# Window.wm_attributes("-transparentcolor",Window["bg"])

main_frame=Frame(Window,width=500,height=500,bg=Window["bg"])
main_frame.grid(row=0,column=0,padx=20,pady=10)

# label=Label(main_frame,text="Any Text",bg=Window["bg"],fg="white",font=("Algerian",20))
# label.pack(fill=None)

# Window.mainloop()
# ***************************************

global next,counter
next="X"
counter=0
def clicked_func(button):
    global next,counter
    counter+=1
    if button["text"]=="" and next == "X":
        button["fg"]="green"
        button.config(text=next)
        next="O"
    elif button["text"]==""and next =="O":
        button.config(text=next)
        button["fg"]="red"
        next="X"
    else:
        msg=messagebox.showerror("Tic Tac Toe","This button is clicked before.")
    get_winner_func()

def reset_func():
    global buttons_list,counter
    counter=0
    for button in buttons_list:
        button.config(state="normal",text="",bg=main_frame["bg"])
    

def disable_all_buttons():
    global buttons_list
    for button in buttons_list:
        button.config(state="disabled")


def get_winner_func():
    winner_backcolor="magenta"
    winner_forecolor="#111"
    global b1,b2,b3,b4,b5,b6,b7,b8,b9

    if b1["text"]==b2["text"]==b3["text"]!="":
        b1["bg"]=b2["bg"]=b3["bg"]=winner_backcolor
        b1["fg"]=b2["fg"]=b3["fg"]=winner_forecolor
        win_msg=messagebox.showinfo("Tic Tac Toe",f"{b1["text"]} player wins")
        disable_all_buttons()

    elif b4["text"]==b5["text"]==b6["text"]!="":
        b4["bg"]=b5["bg"]=b6["bg"]=winner_backcolor
        b4["fg"]=b5["fg"]=b6["fg"]=winner_forecolor
        disable_all_buttons()
        win_msg=messagebox.showinfo("Tic Tac Toe",f"{b4["text"]} player wins")

    elif b7["text"]==b8["text"]==b9["text"]!="":
        b7["bg"]=b8["bg"]=b9["bg"]=winner_backcolor
        b7["fg"]=b8["fg"]=b9["fg"]=winner_forecolor
        disable_all_buttons()
        win_msg=messagebox.showinfo("Tic Tac Toe",f"{b7["text"]} player wins")

    elif b1["text"]==b4["text"]==b7["text"]!="":
        b1["bg"]=b4["bg"]=b7["bg"]=winner_backcolor
        b1["fg"]=b4["fg"]=b7["fg"]=winner_forecolor
        disable_all_buttons()
        win_msg=messagebox.showinfo("Tic Tac Toe",f"{b1["text"]} player wins")

    elif b2["text"]==b5["text"]==b8["text"]!="":
        b2["bg"]=b5["bg"]=b8["bg"]=winner_backcolor
        b2["fg"]=b5["fg"]=b8["fg"]=winner_forecolor
        disable_all_buttons()
        win_msg=messagebox.showinfo("Tic Tac Toe",f"{b1["text"]} player wins")

    elif b3["text"]==b6["text"]==b9["text"]!="":
        b3["bg"]=b6["bg"]=b9["bg"]=winner_backcolor
        b3["fg"]=b6["fg"]=b9["fg"]=winner_forecolor
        disable_all_buttons()
        win_msg=messagebox.showinfo("Tic Tac Toe",f"{b2["text"]} player wins")

    elif b1["text"]==b5["text"]==b9["text"]!="":
        b1["bg"]=b5["bg"]=b9["bg"]=winner_backcolor
        b1["fg"]=b5["fg"]=b9["fg"]=winner_forecolor
        disable_all_buttons()
        win_msg=messagebox.showinfo("Tic Tac Toe",f"{b1["text"]} player wins")

    elif b3["text"]==b5["text"]==b7["text"]!="":
        b3["bg"]=b5["bg"]=b7["bg"]=winner_backcolor
        b3["fg"]=b5["fg"]=b7["fg"]=winner_forecolor
        disable_all_buttons()
        win_msg=messagebox.showinfo("Tic Tac Toe",f"{b3["text"]} player wins")

    elif counter==9:
        disable_all_buttons()
        tie_msg=messagebox.showinfo("Tic Tac Toe","It's a tie")




b_width=20
b_height=5
b1=Button(main_frame,text="",command=lambda:clicked_func(b1),width=b_width,height=b_height)
b1.grid(row=0,column=0,sticky="news")

b2=Button(main_frame,text="",command=lambda:clicked_func(b2),width=b_width,height=b_height)
b2.grid(row=0,column=1)

b3=Button(main_frame,text="",command=lambda:clicked_func(b3),width=b_width,height=b_height)
b3.grid(row=0,column=2)

b4=Button(main_frame,text="",command=lambda:clicked_func(b4),width=b_width,height=b_height)
b4.grid(row=1,column=0)

b5=Button(main_frame,text="",command=lambda:clicked_func(b5),width=b_width,height=b_height)
b5.grid(row=1,column=1)

b6=Button(main_frame,text="",command=lambda:clicked_func(b6),width=b_width,height=b_height)
b6.grid(row=1,column=2)

b7=Button(main_frame,text="",command=lambda:clicked_func(b7),width=b_width,height=b_height)
b7.grid(row=2,column=0)

b8=Button(main_frame,text="",command=lambda:clicked_func(b8),width=b_width,height=b_height)
b8.grid(row=2,column=1)

b9=Button(main_frame,text="",command=lambda:clicked_func(b9),width=b_width,height=b_height)
b9.grid(row=2,column=2)

buttons_list=[b1,b2,b3,b4,b5,b6,b7,b8,b9]

reset_button=Button(main_frame,text="Reset",width=b_width,height=b_height,command=reset_func)
reset_button.grid(row=3,column=1,pady=10)

for widget in main_frame.winfo_children():
    widget.grid_configure(sticky="news")


Window.mainloop()