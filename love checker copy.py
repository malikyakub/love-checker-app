import random
import customtkinter as ctk
from tkinter import messagebox

window = ctk.CTk()
window.geometry('380x600')
window.config(background='#163744')

def result(event):
    random_result = random.randint(0,100)
    if len(b_name_var.get()) == 0 or len(g_name_var.get()) == 0:
        messagebox.showerror('Error', 'no name were inserted')
    else:
        if len(b_name_var.get()) == 0 or len(g_name_var.get()) == 0:
            messagebox.showerror('ERROR', 'no couple name inserted')
        else:
            mk = ['mk', 'malik', 'maalik', 'malik yakub', 'maalik yacquub']
            fm = ['faam', 'faay', 'fatma', 'fatima', 'faaduma', 'faadumo', 'fatima abdukadir', 'faadumo cabduqaadir']

            if b_name_var.get() in mk and g_name_var.get() in fm:
                love_result.configure(text='🤍', text_color='#00ff00')
            elif b_name_var.get() in mk and g_name_var.get() not in fm:
                g_name_var.set('')
                love_result.configure(text='0%', text_color='red')
            elif g_name_var.get() in fm and b_name_var.get() not in mk:
                b_name_var.set('')
                love_result.configure(text='0%', text_color='red')
            else:
                if random_result < 35:
                    love_result.configure(text_color='red')
                    b_name_var.set('')
                    g_name_var.set('')
                elif random_result > 75:
                    love_result.configure(text_color='#00ff00')
                    b_name_var.set('')
                    g_name_var.set('')
                else:
                    love_result.configure(text_color='white')
                    b_name_var.set('')
                    g_name_var.set('')
                love_result.configure(text=f'{random_result}%') 

fonsize = ctk.CTkFont('Lemon',120,'bold')
love_result = ctk.CTkLabel(window, text='', font=fonsize, bg_color='#163744', text_color='white')
love_result.pack(expand=True, fill='both')
color = (1, 1, 1, 0.8)
love_frame = ctk.CTkFrame(window, bg_color='#163744', fg_color='#164B60')
love_frame.pack(pady=10)

b_name_var = ctk.StringVar()
g_name_var = ctk.StringVar()

normal = ctk.CTkFont('Lemon', 17, 'bold')

b_name = ctk.CTkLabel(love_frame, text='boy\'s name', font=normal, text_color='white')
b_name.grid(row=0, column=0, pady=15, padx=(30,10))
b_name_en = ctk.CTkEntry(love_frame, textvariable=b_name_var, border_width=1, font=normal)
b_name_en.grid(row=0, column=1, padx=(0,30))
g_name = ctk.CTkLabel(love_frame, text='girls\'s name', font=normal, text_color='white')
g_name.grid(row=1, column=0, pady=5, padx=(30,10))
g_name_en = ctk.CTkEntry(love_frame, textvariable=g_name_var, border_width=1, font=normal)
g_name_en.grid(row=1, column=1, padx=(0,30))

btn_font = ctk.CTkFont('Lemon',20,'bold')
check_love = ctk.CTkButton(love_frame, text='Check love', border_color='#00ff00',border_width=2, fg_color='transparent' ,hover_color='#00ff00', font=btn_font, command=lambda:result())
check_love.grid(row=2, column=0, columnspan=2, pady=(25, 10), sticky='we', padx=30)
window.bind('<Return>', result)

window.mainloop()