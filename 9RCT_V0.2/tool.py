import tkinter as tk
from tkinter import ttk
from products import products
from strategies import r_strategies

class ProductSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Circular Economy - Strategy Decision Tool')  # Titel des Fensters setzen

        # Globale Schriftgröße festlegen
        self.root.option_add('*Font', 'Helvetica 22')

        # Fenstergröße und Position
        window_width = 500
        window_height = 500

        # Bildschirmbreite und -höhe ermitteln
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Position für das Fenster berechnen
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Fenstergröße und Position festlegen
        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        self.product_var = tk.StringVar()
        self.emission_var = tk.StringVar()
        self.state_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Wähle ein Produkt:").pack(pady=10)
        self.product_dropdown = ttk.Combobox(self.root, textvariable=self.product_var, state="readonly")
        self.product_dropdown.pack()
        self.product_dropdown['values'] = [product.id_short for product in products]
        self.product_dropdown.bind('<<ComboboxSelected>>', self.update_subproducts)

    def update_subproducts(self, event):
        selected_product = next((product for product in products if product.id_short == self.product_var.get()), None)
        if selected_product and selected_product.bill_of_product:
            self.subproduct_var = tk.StringVar()
            ttk.Label(self.root, text="Wähle ein Unterprodukt:").pack(pady=10)
            self.subproduct_dropdown = ttk.Combobox(self.root, textvariable=self.subproduct_var, state="readonly")
            self.subproduct_dropdown.pack()
            self.subproduct_dropdown['values'] = [subproduct.id_short for subproduct in selected_product.bill_of_product]
            self.subproduct_dropdown.bind('<<ComboboxSelected>>', self.update_emissions)
        else:
            self.update_emissions(None)

    def update_emissions(self, event):
        selected_product = next((product for product in products if product.id_short == self.product_var.get()), None)
        if selected_product and selected_product.bill_of_emissions:
            ttk.Label(self.root, text="Emissionen:").pack(pady=10)
            for emission in selected_product.bill_of_emissions:
                ttk.Label(self.root, text=f"{emission.id_short}: {emission.category}").pack()
            self.update_states()
        else:
            ttk.Label(self.root, text="Keine Emissionen gefunden!").pack()
            self.update_states()

    def update_states(self):
        selected_product = next((product for product in products if product.id_short == self.product_var.get()), None)
        if selected_product and selected_product.bill_of_states:
            ttk.Label(self.root, text="Wähle einen Zustand:").pack(pady=10)
            self.state_dropdown = ttk.Combobox(self.root, textvariable=self.state_var, state="readonly")
            self.state_dropdown.pack()
            self.state_dropdown['values'] = selected_product.bill_of_states
            self.state_dropdown.bind('<<ComboboxSelected>>', self.update_strategies)
        else:
            ttk.Label(self.root, text="Keine Zustände gefunden!").pack()

    def update_strategies(self, event):
        selected_state = self.state_var.get()
        matching_strategies = [strategy for strategy in r_strategies if selected_state in strategy.possible_states]
        ttk.Label(self.root, text="Mögliche R-Strategien:").pack(pady=10)
        if matching_strategies:
            for strategy in matching_strategies:
                ttk.Label(self.root, text=strategy.id).pack()
        else:
            ttk.Label(self.root, text="Keine Strategien gefunden!").pack()

def main():
    root = tk.Tk()
    app = ProductSelectorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()