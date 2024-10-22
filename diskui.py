from tkinter import *
from tkinter import ttk



def percent_calculate():
  total_storage = float(entry_total_storage.get())
  used_storage = float(entry_used_storage.get())
  calculate_percentage = (used_storage / total_storage) * 100
  if used_storage < total_storage:
    percentage.set( f'{str(calculate_percentage)}% utilisés.' )
  else:
    percentage.set("Error: used_storage can't be larger than total !")

root = Tk()
root.title("Calculateur du taux d'utilisation d'un disque")

label_total_storage = ttk.Label(root, text="Total capacity (Gb)")
label_total_storage.grid(row=0, column=0,padx=2, pady=2)
entry_total_storage = ttk.Entry(root)
entry_total_storage.grid(row=0, column=1, padx=2, pady=2)

label_used_storage = ttk.Label(root, text="Used capacity (Gb)")
label_used_storage.grid(row=1, column=0, padx=2, pady=2)
entry_used_storage = ttk.Entry(root)
entry_used_storage.grid(row=1, column=1, padx=2, pady=2)

calculate_button = ttk.Button(root, text="Percent usage", command=percent_calculate)
calculate_button.grid(row=2, column=1, columnspan=2, padx=2, pady=2)

percentage = StringVar(value=0)

label_result = ttk.Label(root, textvariable=percentage)
label_result.grid(row=3, column=0, columnspan=3, padx=2, pady=2)

root.mainloop()