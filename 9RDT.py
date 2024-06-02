import tkinter as tk
from tkinter import ttk

# Daten für die Demo
products = {
    'Product 1': ['Part 1', 'Part 2', 'Part 3'],
    'Product 2': ['Part 1', 'Part 4'],
    'Product 3': ['Part 5', 'Part 2']
}
states = ['State 1', 'State 2', 'State 3']

def on_product_select(event):
    # Partliste für das ausgewählte Produkt aktualisieren
    product = product_combobox.get()
    parts_combobox['values'] = products[product]
    parts_combobox.current(0)
    on_part_select(None)

def on_part_select(event):
    # Zustandsliste aktualisieren
    state_combobox['values'] = states
    state_combobox.current(0)

root = tk.Tk()
root.title('Circular Economy - Strategy Desicion Tool')

# Produktauswahl
product_label = ttk.Label(root, text="Select Product:")
product_label.pack()
product_combobox = ttk.Combobox(root, values=list(products.keys()))
product_combobox.pack()
product_combobox.bind('<<ComboboxSelected>>', on_product_select)

# Teileauswahl
part_label = ttk.Label(root, text="Select Part:")
part_label.pack()
parts_combobox = ttk.Combobox(root)
parts_combobox.pack()
parts_combobox.bind('<<ComboboxSelected>>', on_part_select)

# Zustandsauswahl
state_label = ttk.Label(root, text="Select State:")
state_label.pack()
state_combobox = ttk.Combobox(root, values=states)
state_combobox.pack()

# Fenster starten
root.mainloop()