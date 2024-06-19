import tkinter as tk
from tkinter import ttk
from product_data import products  # Importieren Sie die Daten aus der product_data.py Datei
from strategies import RStrategy, r_strategies  # Importieren Sie die RStrategy Klasse und die r_strategies Liste aus der strategies.py Datei

# Erstes Dropdownmenü
def on_product_select(event):
    selected_product_id = product_combobox.get()
    selected_product = next(p for p in products if p.id == selected_product_id)
    
    # Teile für das ausgewählte Produkt holen
    parts = selected_product.bill_of_product
    
    # Ändern Sie den Text des Labels
    parts_label.config(text=f"Select Part of {selected_product_id}:")
    
    if parts:
        # "Show for all" als ersten Eintrag hinzufügen und dann die Teile in der Combobox anzeigen
        parts_combobox['values'] = ["Show for all"] + parts
        parts_combobox.set(parts[0])  # Setzen Sie den Text der Combobox auf das erste Teil
        on_part_select(None)  # Aktualisieren Sie die Zustandscombobox
    else:
        # Wenn keine Teile vorhanden sind, "Product not found" anzeigen
        parts_combobox['values'] = ["Product not found"]
        parts_combobox.set("Product not found")  # Setzen Sie den Text der Combobox auf "Product not found"
        state_combobox['values'] = selected_product.bill_of_states
        state_combobox.set(selected_product.bill_of_states[0] if selected_product.bill_of_states else "Product not found")

# Zweites Dropdownmenü
def on_part_select(event):
    selected_part_id = parts_combobox.get()

    if selected_part_id == "Show for all":
        # Suche alle Produkte, die das ausgewählte Teil enthalten
        products_with_part = [p for p in products if any(part.id == selected_part_id for part in p.bill_of_products)]
        # Kombiniere alle Emissionen der gefundenen Produkte
        combined_emissions = [e for product in products_with_part for e in product.bill_of_emissions]
        if combined_emissions:
            emissions_combobox['values'] = [e.id for e in combined_emissions]
            emissions_combobox.set(combined_emissions[0].id)
        else:
            emissions_combobox['values'] = ["No Emission found!"]
            emissions_combobox.set("No Emission found!")
    else:
        # Suche das Produkt, das das ausgewählte Teil enthält
        product_with_part = next((p for p in products if any(part.id == selected_part_id for part in p.bill_of_products)), None)
        if product_with_part:
            # Finde das ausgewählte Teil im Produkt
            selected_part = next((part for part in product_with_part.bill_of_products if part.id == selected_part_id), None)
            if selected_part and selected_part.bill_of_emissions:
                # Emissionen des ausgewählten Teils anzeigen
                emissions_combobox['values'] = [e.id for e in selected_part.bill_of_emissions]
                emissions_combobox.set(selected_part.bill_of_emissions[0].id)
            else:
                # Keine Emissionen gefunden
                emissions_combobox['values'] = ["No Emission found!"]
                emissions_combobox.set("No Emission found!")
        else:
            emissions_combobox['values'] = ["No Emission found!"]
            emissions_combobox.set("No Emission found!")

    on_emission_select(None)  # Aktualisiere die Anzeige der Emissionsdaten basierend auf der neuen Auswahl

# Globale Variable für die Strategie-Labels
strategy_labels = []

# Neue Funktion für die Auswahl von Emissionsdaten
def on_emission_select(event):
    selected_emission_id = emissions_combobox.get()
    selected_product_id = product_combobox.get()
    selected_product = next(p for p in products if p.id == selected_product_id)
    selected_emission = next(e for e in selected_product.bill_of_emissions if e.id == selected_emission_id)
    
    # Aktualisieren Sie das Label mit den Details der ausgewählten Emissionsdaten
    emissions_data_label.config(text=f"ID: {selected_emission.id}\n"
                                     f"Short ID: {selected_emission.id_short}\n"
                                     f"Category: {selected_emission.category}\n"
                                     f"Scope: {selected_emission.scope}\n"
                                     f"Total CO2 Equivalent: {selected_emission.total_c02_equivalent} {selected_emission.measuring_unit}\n"
                                     f"Standards Country Code: {selected_emission.standards_country_code}\n"
                                     f"Emissions Data Sheet: {selected_emission.emissions_data_sheet_file_URL}")

# Änderungen in `on_part_select` um die Emissionsdaten-Combobox zu aktualisieren
def on_part_select(event):
    selected_product_id = product_combobox.get()
    selected_product = next(p for p in products if p.id == selected_product_id)
    emissions_combobox['values'] = [e.id for e in selected_product.bill_of_emissions]
    emissions_combobox.set(selected_product.bill_of_emissions[0].id if selected_product.bill_of_emissions else "Emissions not found")
    on_emission_select(None)  # Aktualisieren Sie das Emissionsdaten-Label

# Globale Variable für das Emissionsdaten-Label
emissions_data_label = None

# Drittes Dropdownmenü
def on_state_select(event):
    global strategy_labels

    selected_state = state_combobox.get()
    
    # Finden Sie alle Strategien, die den ausgewählten Zustand in ihrem possible_state Attribut haben
    suited_strategies = [s.id for s in r_strategies if selected_state in s.possible_states]
    
    # Entfernen Sie alle alten Strategie-Labels
    for label in strategy_labels:
        label.destroy()
    strategy_labels = []

    if suited_strategies:
        # Wenn es passende Strategien gibt, erstellen Sie für jede Strategie ein Label und fügen Sie es zur Liste hinzu
        for strategy_id in suited_strategies:
            label = ttk.Label(root, text=strategy_id)
            label.pack()
            strategy_labels.append(label)
    else:
        # Wenn es keine passenden Strategien gibt, zeigen Sie eine Nachricht an
        label = ttk.Label(root, text="No suited R-Strategy found!")
        label.pack()
        strategy_labels.append(label)

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
parts_label = ttk.Label(root, text="Select Part of Product:") #Default Text für das Dropdown Menü, sobald Produkt ausgewählt wurde, wird "...Product" zur id des Produkts
parts_label.pack()
parts_combobox = ttk.Combobox(root)
parts_combobox.bind('<<ComboboxSelected>>', on_part_select)
parts_combobox.pack()

# Emissionsdaten-Combobox und Label hinzufügen
emissions_label = ttk.Label(root, text="Select Emissions Data:")
emissions_label.pack()
emissions_combobox = ttk.Combobox(root)
emissions_combobox.bind('<<ComboboxSelected>>', on_emission_select)
emissions_combobox.pack()

emissions_data_label = ttk.Label(root, text="Emissions Details:")
emissions_data_label.pack()

# Zustandsauswahl
state_label = ttk.Label(root, text="Select State:")
state_label.pack()
state_combobox = ttk.Combobox(root)
state_combobox.bind('<<ComboboxSelected>>', on_state_select)
state_combobox.pack()

# Textbox für die Strategien
strategy_label = ttk.Label(root, text="Possible R-Strategies:")
strategy_label.pack()

root.mainloop()