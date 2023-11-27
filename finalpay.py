import customtkinter
from tkinter import *
from tkinter import messagebox
from datetime import datetime, date

app = customtkinter.CTk()
app.title('Fruit Shop')
app.config(bg="#023020")
app.geometry("1000x550")
app.resizable(False, False)

font1 = ('Arial', 25, 'bold')
font2 = ('Arial', 15, 'bold')
font3 = ('Arial', 12, 'bold')
font4 = ('Impact', 35, 'italic')
font5 = ('Arial', 20, 'bold')
font6 = ('Impact', 25, 'bold')
font7 = ('Impact', 35, 'bold')

price_list = [25, 20]
total_price = 0
balance_price= 0

bill_frame = customtkinter.CTkFrame(app, width=500, height=800, fg_color="#5F8575")
bill_frame.place(x=700, y=-5)

name_label=customtkinter.CTkLabel(bill_frame,text=f'\n      ORDER DETAILS  ', text_color="#FFFFFF", fg_color="#023020", width=600, height=115, compound=TOP,anchor=W)
name_label.configure(font=font4)
name_label.place(x=-3,y=-35)

menu_label = customtkinter.CTkLabel(app, text="A E S H I  S H O P",text_color="#FFFFFF", fg_color="#023020", width=200, height=50, compound=TOP,anchor=W)
menu_label.configure(font=font7)
menu_label.place(x=245, y=7)

img1 = PhotoImage(file="1.png")
img2 = PhotoImage(file="2.png")

apple_price_label = customtkinter.CTkLabel(app, text="Price of Apple:", text_color="#FFFFFF", fg_color="#023020")
apple_price_label.configure(font=font2)
apple_price_label.place(x=150, y=460)

apple_price_entry = customtkinter.CTkEntry(app, fg_color="#FFFFFF", text_color="#000000", border_color="#FFFFFF", width=230)
apple_price_entry.configure(font=font2)
apple_price_entry.place(x=300, y=460)


def pay():
    global total_price, balance_price
    
    if customer_entry.get() == '' or apple_price_entry.get() == '':
        messagebox.showerror(title="Error", message="Please enter a valid amount and apple price.")
    else:
        amount_money = float(customer_entry.get()) if customer_entry.get() else 0.0
        apple_price = float(apple_price_entry.get()) if apple_price_entry.get() else 0.0

        # Calculate total price including the apple price
        total_price = int(quntity1_combobox.get()) * price_list[0] + int(quntity2_combobox.get()) * apple_price

        amount_money = float(customer_entry.get()) if customer_entry.get() else 0.0
        total_price = int(quntity1_combobox.get()) * price_list[0] + int(quntity2_combobox.get()) * price_list[1]

        if total_price == 0:
            messagebox.showwarning(title="Error", message="Please select some fruits.")
        elif amount_money < total_price:
            messagebox.showwarning(title="Insufficient Funds", message="The amount of money is not enough to pay.")
        else:
            balance_price = amount_money - total_price 

            date_label = customtkinter.CTkLabel(bill_frame, text=f'     Date: {date.today()}', text_color="#FFFFFF", fg_color="#355E3B", width=600, anchor=W)
            date_label.configure(font=font5)
            date_label.place(x=0, y=100)

            time_label = customtkinter.CTkLabel(bill_frame, text=f'     Time: {datetime.now().strftime("%H:%M")}', text_color="#FFFFFF", fg_color="#355E3B", width=600, anchor=W)
            time_label.configure(font=font5)
            time_label.pack()
            time_label.place(x=0, y=140)
 
            name_label = customtkinter.CTkLabel(bill_frame, text=f'    Amount of money: ₱{amount_money:.2f}')
            name_label.configure(font=font5)
            name_label.place(x=0, y=220)

            price_label = customtkinter.CTkLabel(bill_frame, text=f'    Total Price: ₱{total_price}.00')
            price_label.configure(font=font5)
            price_label.place(x=0, y=250)

            balance_label = customtkinter.CTkLabel(bill_frame, text=f'    Balance: ₱{balance_price:.2f}', text_color="#FFFFFF")
            balance_label.configure(font=font5)
            balance_label.place(x=0, y=300)

            remaining_label = customtkinter.CTkLabel(bill_frame, text=f'        YOUR BALANCE IS NOW \n       ONLY ₱{balance_price:.2f}')
            remaining_label.configure(font=font6)
            remaining_label.place(x=0, y=400)



def new():
    customer_entry.delete(0,END)
    apple_price_entry.delete(0, END)
    quntity1_combobox.set(0)
    quntity2_combobox.set(0)

def save():
   f = open(f'{customer_entry.get()} Bill', "w", encoding="utf-8")
   f.write(f'Total Price: ₱{total_price}.00\n')
   f.write(f'Balance: ₱{balance_price:.2f}\n')
   f.write(f'Date: {date.today()}\n')
   f.write(f'Time: {datetime.now().strftime("%H:%M")}\n')
   messagebox.showinfo(title="Saved", message="Bill has been saved.")


img1_label = customtkinter.CTkLabel(app, image=img1, text="Orange\nCost: ₱25.00\n\n", font=font2, text_color="#FFFFFF", fg_color="#4F7942", width=250, height=330, corner_radius=0, compound=TOP, anchor=N)
img1_label.place(x=50, y=70)

img2_label = customtkinter.CTkLabel(app, image=img2, text="Apple\nCost: ₱20.00\n\n", font=font2, text_color="#FFFFFF", fg_color="#4F7942", width=250, height=330, corner_radius=0, compound=TOP, anchor=N)
img2_label.place(x=365, y=70)

quntity1_combobox=customtkinter.CTkComboBox(app, text_color="#000000",fg_color="#FFFFFF",values=('0','1','2','3','4','5'),state="readonly")
quntity1_combobox.configure(font=font3) 
quntity1_combobox.place(x=105,y=360)
quntity1_combobox.set(0)

quntity2_combobox=customtkinter.CTkComboBox(app, text_color="#000000",fg_color="#FFFFFF",values=('0','1','2','3','4','5'),state="readonly")
quntity2_combobox.configure(font=font3) 
quntity2_combobox.place(x=420,y=360)
quntity2_combobox.set(0)

customer_label=customtkinter.CTkLabel(app,text="Amount of Money:",text_color="#FFFFFF",fg_color="#023020")
customer_label.configure(font=font2) 
customer_label.place(x=150,y=430)

customer_entry=customtkinter.CTkEntry(app,fg_color="#FFFFFF",text_color="#000000",border_color="#FFFFFF",width=230)
customer_entry.configure(font=font2) 
customer_entry.place(x=300,y=430)

pay_button=customtkinter.CTkButton(app, command=pay, text="Pay Bill",fg_color="#CF0107",hover_color="#CF0107",corner_radius=0,cursor="hand2")
pay_button.configure(font=font2) 
pay_button.place(x=120,y=505)

save_button=customtkinter.CTkButton(app, command=save, text="Save Bill",fg_color="#EC6D10",hover_color="#EC6D10",corner_radius=0,cursor="hand2")
save_button.configure(font=font2) 
save_button.place(x=276,y=505)

new_button=customtkinter.CTkButton(app, command=new, text="New Bill",fg_color="#c26406",hover_color="#c26406",corner_radius=0,cursor="hand2")
new_button.configure(font=font2) 
new_button.place(x=430,y=505)


app.mainloop()