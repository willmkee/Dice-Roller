import random
import tkinter as tk

def roll_dice():
    try:
        num_dice = int(num_entry.get())
        dice_type = int(dice_entry.get())

        if(num_dice > 0 and dice_type > 0):
            result = []
            for roll in range(num_dice):
                result.append(random.randint(1, dice_type))
            result_label.config(text=result)
        else:
            result_label.config(text="Enter INTEGERS greater than zero")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

#Create the main app window
app = tk.Tk()
app.title('Dice Roller')

app.geometry("300x200")
app.configure(padx=10, pady=10)

num_label = tk.Label(app, text='Enter Number of Dice:')
num_label.pack()

num_entry = tk.Entry(app)
num_entry.pack()

dice_label = tk.Label(app, text='Enter Number of Sides on Dice:')
dice_label.pack()

dice_entry = tk.Entry(app)
dice_entry.pack()

roll_button = tk.Button(app, text='Roll Dice', command=roll_dice)
roll_button.pack()

result_label = tk.Label(app, text='', wraplength=200)
result_label.pack()

app.mainloop()
