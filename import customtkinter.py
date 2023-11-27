import customtkinter
from tkinter import *

from customtkinter import CTkFrame, CTkLabel, Font

app = customtkinter.CTk()
app.title('Aeshi Shop')
app.geometry("1000x400")
app.config(bg="#25283b")
app.resizable(False, False)

font1 = Font(family="Arial", size=25, weight="bold")
font2 = Font(family="Arial", size=15, weight="bold")
font3 = Font(family="Arial", size=12, weight="bold")
price_list = [20, 25]
total_price = 0

bill_frame = CTkFrame(app, width=300, height=400, fg_color="#545457")
bill_frame.place(x=700, y=0)

menu_label = CTkFrame(app, bg_color="#25283b")
menu_label.set_text("Aeshi Shop")
menu_label.set_font(font1)
menu_label.set_text_color("#FFFFFF")
menu_label.place(x=230, y=5)

img1 = PhotoImage(file=r"1.png")
img2 = PhotoImage(file=r"2.png")

img1_label = CTkLabel(app, image=img1, text="Orange\nPrice: 25", text_font=font2, text_color="#FFFFFF",
                      fg_color="#090b17", width=200, height=200, corner_radius=20, compound=TOP, anchor=N)
img2_label = CTkLabel(app, image=img2, text="Apple\nPrice: 20", text_font=font2, text_color="#FFFFFF",
                      fg_color="#090b17", width=200, height=200, corner_radius=20, compound=TOP, anchor=N)

img1_label.place(x=100, y=100)
img2_label.place(x=400, y=100)

app.mainloop()
