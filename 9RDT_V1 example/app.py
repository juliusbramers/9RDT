import tkinter as tk
from tkinter import ttk
from productdata import products
from strategydata import r_strategies

class ProductApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('R-Strategy Decision Tool')

        # Stilobjekt erstellen
        style = ttk.Style(self)
        
        # Globalen Stil für alle Widgets setzen
        font = ('Helvetica', 18)
        style.configure('.', font=font)
        style.configure('TCombobox', font=font)  # Schriftart für Combobox setzen
        
        # Alternative Methode zur Anwendung der Schriftart auf alle Widgets
        self.option_add('*TCombobox*Listbox*Font', font)

        # Fenstergröße
        window_width = 600
        window_height = 700

        # Bildschirmauflösung abfragen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Startposition berechnen
        start_x = int((screen_width - window_width) / 2)
        start_y = int((screen_height - window_height) / 2)

        # Fensterposition und -größe einstellen
        self.geometry(f'{window_width}x{window_height}+{start_x}+{start_y}')

        self.resizable(True, True)
        self.create_widgets()

    def create_widgets(self):
        self.dropdown_frames = []
        self.emissions_label = None
        self.states_menu = None
        self.rstrategy_label = None
        self.no_data_label = None

        ttk.Label(self, text="Select Product:").pack(pady=(20, 10))
        self.initial_menu = ttk.Combobox(self, state="readonly", font=('Arial', 18))
        self.initial_menu.pack()
        self.initial_menu.bind('<<ComboboxSelected>>', self.handle_product_selection)
        self.update_dropdown(self.initial_menu, list(products.keys()))

    def handle_product_selection(self, event):
        self.clear_dynamic_widgets()
        product_id = event.widget.get()
        if product_id in products:
            self.handle_selection(product_id, self)
        else:
            self.display_no_data()

    def handle_selection(self, product_id, parent_frame):
        current_frame_index = self.dropdown_frames.index(parent_frame) if parent_frame in self.dropdown_frames else -1
        for frame in self.dropdown_frames[current_frame_index+1:]:
            frame.destroy()
            self.dropdown_frames.remove(frame)

        product = products.get(product_id, None)
        if product:
            if product.bill_of_product:
                frame = ttk.Frame(parent_frame)
                frame.pack(pady=10)
                self.dropdown_frames.append(frame)
                label = ttk.Label(frame, text=f"Select Component of {product.id_short}:")
                label.pack()

                dropdown = ttk.Combobox(frame, state="readonly", font=('Arial', 18))
                dropdown.pack()
                dropdown.bind('<<ComboboxSelected>>', lambda e: self.handle_selection(dropdown.get(), frame))
                self.update_dropdown(dropdown, product.bill_of_product)
            else:
                self.display_emissions_and_states(product)
        else:
            self.display_no_data()

    def display_emissions_and_states(self, product):
        if self.no_data_label:
            self.no_data_label.destroy()
            self.no_data_label = None

        if product.bill_of_emissions:
            emissions_text = "\n\n".join([
                f"ID: {e.id}\nCategory: {e.category}\nScope: {e.scope}\nCO2 eq: {e.total_c02_equivalent}kg\nUnit: {e.measuring_unit}\nStandards: {e.standards_country_code}\nInfo: {e.emissions_data_sheet_file_URL}"
                for e in product.bill_of_emissions])
        
        else:
            emissions_text = "No Emissions found!"

        if self.emissions_label:
            self.emissions_label.destroy()
        self.emissions_label = ttk.Label(self, text="Emissions:\n\n" + emissions_text)
        self.emissions_label.pack(pady=(10, 5))

        if product.bill_of_states:
            if self.states_menu:
                self.states_menu.destroy()
            self.states_menu = ttk.Combobox(self, values=product.bill_of_states, state="readonly", font=('Arial', 18))
            self.states_menu.pack()
            self.states_menu.bind('<<ComboboxSelected>>', self.handle_state_selection)
        else:
            if self.states_menu:
                self.states_menu.destroy()
            ttk.Label(self, text="No States found!").pack()

    def handle_state_selection(self, event):
        state = event.widget.get()
        matching_strategies = [rs.id for rs in r_strategies if state in rs.possible_states]
        self.display_rstrategies(matching_strategies)

    def display_rstrategies(self, strategies):
        if self.rstrategy_label:
            self.rstrategy_label.destroy()

        if strategies:
            strategy_text = "Possible R-Strategies: " + ", ".join(strategies)
        else:
            strategy_text = "No R-Strategies found! Select another state."
        
        self.rstrategy_label = ttk.Label(self, text=strategy_text)
        self.rstrategy_label.pack(pady=(10, 0))

    def update_dropdown(self, dropdown, values):
        dropdown['values'] = values
        if values:
            dropdown.set(values[0])

    def clear_dynamic_widgets(self):
        for frame in self.dropdown_frames:
            frame.destroy()
        self.dropdown_frames.clear()
        if self.emissions_label:
            self.emissions_label.destroy()
        if self.states_menu:
            self.states_menu.destroy()
        if self.rstrategy_label:
            self.rstrategy_label.destroy()
        if self.no_data_label:
            self.no_data_label.destroy()
            self.no_data_label = None

    def display_no_data(self):
        self.clear_dynamic_widgets()
        if not self.no_data_label:
            self.no_data_label = ttk.Label(self, text="No Data found! Please try again.")
            self.no_data_label.pack(pady=(10, 0))

if __name__ == "__main__":
    app = ProductApp()
    app.mainloop()