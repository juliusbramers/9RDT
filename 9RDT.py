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

# Globale Schriftgröße festlegen
root.option_add('*Font', 'Helvetica 22')

# Hintergrundfarbe festlegen
root.configure(bg='#1B9783')

# Globale Hintergrundfarbe festlegen
root.option_add('*Background', 'grey') 

# Fenstergröße und Position
window_width = 500
window_height = 500

# Bildschirmbreite und -höhe ermitteln
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Position für das Fenster berechnen
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Fenstergröße und Position festlegen
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")


# Produktauswahl
product_label = tk.Label(root, text="Select Product:", font=("Helvetica", 16), bg='#1B9783')
product_label.pack()
product_combobox = ttk.Combobox(root, values=list(products.keys()))
product_combobox.pack()
product_combobox.bind('<<ComboboxSelected>>', on_product_select)

# Teileauswahl
part_label = tk.Label(root, text="Select Part:", font=("Helvetica", 16), bg='#1B9783')
part_label.pack()
parts_combobox = ttk.Combobox(root)
parts_combobox.pack()
parts_combobox.bind('<<ComboboxSelected>>', on_part_select)

# Zustandsauswahl
state_label = tk.Label(root, text="Select State:", font=("Helvetica", 16), bg='#1B9783')
state_label.pack()
state_combobox = ttk.Combobox(root, values=states)
state_combobox.pack()

# Fenster starten
root.mainloop()