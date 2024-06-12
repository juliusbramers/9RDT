import tkinter as tk
from tkinter import ttk
from product_data import products  # Importieren Sie die Daten aus der product_data.py Datei

def on_product_select(event):
    # Partliste für das ausgewählte Produkt aktualisieren
    product_id = product_combobox.get()
    product = next((p for p in products if p.id == product_id), None)
    if product:
        parts_combobox['values'] = product.bill_of_product
        parts_combobox.current(0)
        on_part_select(None)

def on_part_select(event):
    # Zustandsliste aktualisieren
    product_id = product_combobox.get()
    product = next((p for p in products if p.id == product_id), None)
    if product:
        state_combobox['values'] = product.bill_of_states
        state_combobox.current(0)

root = tk.Tk()
root.title('Circular Economy - Strategy Desicion Tool')

# Globale Schriftgröße festlegen
root.option_add('*Font', 'Helvetica 22')

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
product_label = ttk.Label(root, text="Select Product:")
product_label.pack()
product_combobox = ttk.Combobox(root, values=[p.id for p in products])
product_combobox.bind('<<ComboboxSelected>>', on_product_select)
product_combobox.pack()

# Teileauswahl
parts_label = ttk.Label(root, text="Select Part:")
parts_label.pack()
parts_combobox = ttk.Combobox(root)
parts_combobox.bind('<<ComboboxSelected>>', on_part_select)
parts_combobox.pack()

# Zustandsauswahl
state_label = ttk.Label(root, text="Select State:")
state_label.pack()
state_combobox = ttk.Combobox(root)
state_combobox.pack()

root.mainloop()