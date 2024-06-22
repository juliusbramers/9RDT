import tkinter as tk
from tkinter import ttk
from productdata import products
from strategydata import r_strategies

class ProductApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('R-Strategy Decision Tool')

        style = ttk.Style(self)
        font = ('Helvetica', 18)
        style.configure('.', font=font)
        style.configure('TCombobox', font=font)
        self.option_add('*TCombobox*Listbox*Font', font)

        window_width = 600
        window_height = 1000
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        start_x = int((screen_width - window_width) / 2)
        start_y = int((screen_height - window_height) / 2)
        self.geometry(f'{window_width}x{window_height}+{start_x}+{start_y}')

        self.resizable(True, True)
        self.create_widgets()

    def create_widgets(self):
        self.dropdown_frames = []
        self.emissions_label = None
        self.states_menu = None
        self.rstrategy_label = None
        self.no_data_label = None
        self.new_emissions_label = None
        self.last_selected_product_id = None  # Neues Attribut für die zuletzt ausgewählte Produkt-ID

        ttk.Label(self, text="Select Product:").pack(pady=(20, 10))
        self.initial_menu = ttk.Combobox(self, state="readonly", font=('Arial', 18))
        self.initial_menu.pack()
        self.initial_menu.bind('<<ComboboxSelected>>', self.handle_product_selection)
        self.update_dropdown(self.initial_menu, list(products.keys()))

    def handle_product_selection(self, event):
        self.clear_dynamic_widgets()
        product_id = event.widget.get()
        self.last_selected_product_id = product_id  # Aktualisieren der zuletzt ausgewählten Produkt-ID
        if product_id in products:
            self.handle_selection(product_id, self)
        else:
            self.display_no_data()

    def handle_selection(self, product_id, parent_frame):
        self.product_id_last = product_id  # Aktualisieren der product_id_last mit der aktuellen Auswahl
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
        self.emissions_label = ttk.Label(self, text="Emissions of new Product:\n\n" + emissions_text)
        self.emissions_label.pack(pady=(10, 5))

        if product.bill_of_states:
            if self.states_menu:
                self.states_menu.destroy()
            ttk.Label(self, text="Select current State of Product:").pack(pady=(10, 0))
            self.states_menu = ttk.Combobox(self, values=product.bill_of_states, state="readonly", font=('Arial', 18), width=50)
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

        self.display_new_emissions(strategies)

    def display_new_emissions(self, strategies):
        if self.new_emissions_label:
            self.new_emissions_label.destroy()

        product_id = self.product_id_last  # Verwendung der zuletzt ausgewählten Produkt-ID
        product = products.get(product_id, None)
        if product and hasattr(product, 'bill_of_emissions_new_r'):
            applicable_emissions = [e for e in product.bill_of_emissions_new_r if e.r_strategy in strategies]
            if applicable_emissions:
                new_emissions_text = "\n\n".join([
                    f"R-Strategy: {e.r_strategy}\nCO2 eq: {e.total_c02_equivalent}kg\nUnit: {e.measuring_unit}\nEmissions Difference: {e.r_strategy_emissions_difference_percent}%\nCost Difference: {e.r_strategy_cost_difference_percent}%"
                    for e in applicable_emissions])
                # Finde die Strategie mit dem größten Wert in r_strategy_emissions_difference_percent
                max_emission_strategy = max(applicable_emissions, key=lambda e: e.r_strategy_emissions_difference_percent)
                strategy_advice = f"\n\nUse Strategy {max_emission_strategy.r_strategy} to minimize the Carbon Impact."
                new_emissions_text += strategy_advice
            else:
                new_emissions_text = "No new emissions data found for selected R-Strategies."
        else:
            new_emissions_text = "No new emissions data available."

        self.new_emissions_label = ttk.Label(self, text="New Emissions Data:\n\n" + new_emissions_text)
        self.new_emissions_label.pack(pady=(10, 5))

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
        if self.new_emissions_label:
            self.new_emissions_label.destroy()
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