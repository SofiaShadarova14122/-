import tkinter as tk

def on_click_button():
    flag=0
    if flag!=1:
        try:
            a = int(augent_text1.get())
            b = int(augent_text2.get())
            s=a+b
        except ValueError:
            augent.configure(text="Введено не число, проверьте, пожалуста введенные данные")
        else:
            flag = 1
            augent.configure(text="Сумма чисел = " + str(s))

baseWindow=tk.Tk()
baseWindow.title("Сложение двух чисел")
baseWindow.geometry("640x480")
augent=tk.Label(baseWindow, text="Сумма = ", fg="#ff7538", font="candara 18")
augent.pack(side="top")
augent_text1=tk.Entry(baseWindow, fg="#f64a8a", font="candara 18", bg="lightblue", borderwidth="5", width="35", justify="center")
augent_text1.pack()
augent_text2=tk.Entry(baseWindow, fg="#f64a8a", font="candara 18", bg="lightblue", borderwidth="5", width="35", justify="center")
augent_text2.pack()
plus=tk.Button(baseWindow, command=on_click_button, text="Сложить!", fg="#991199", font="candara 18", bg="lightblue", borderwidth="5", width="35", justify="center")
plus.pack()
baseWindow.mainloop()
