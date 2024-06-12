from typing import Optional, List
from dataclasses import dataclass

'''Die erstellten Produkte orientieren sich grob an der Struktur in dem Digitalen Produktpasst aus der Bachelorarbeit.
Aufgrund der Komplexität des Produktpasses, wurden die Produkte auf die wichtigsten Informationen reduziert.'''

# Emissionsklasse definieren
@dataclass
class Emission:
    id: str
    id_short: str
    category: str
    scope: int
    total_c02_equivalent: int
    measuring_unit: str
    standards_country_code: str
    emissions_data_sheet_file_URL: str

# Produktklasse definieren
@dataclass
class Product:
    id: str
    id_short: str
    description: str
    bill_of_product: List[str]
    bill_of_emissions: List[Emission] 
    bill_of_states: List[str]

# Produkte definieren - Hier können auch direkt die Emissionen definiert werden
products = [
    Product(
        id="Product1",
        id_short="P1",
        description="This is product 1",
        bill_of_product=["Part 1", "Part 2", "Part 3"],
        bill_of_emissions=[
            Emission(
                id="Emission1",
                id_short="E1",
                category="Category1",
                scope=1,
                total_c02_equivalent=100,
                measuring_unit="kg",
                standards_country_code="DE",
                emissions_data_sheet_file_URL="http://example.com/emission1.pdf"
            ),
            Emission(
                id="Emission2",
                id_short="E2",
                category="Category2",
                scope=2,
                total_c02_equivalent=200,
                measuring_unit="kg",
                standards_country_code="DE",
                emissions_data_sheet_file_URL="http://example.com/emission2.pdf"
            )
        ],
        bill_of_states=["State 1", "State 2", "State 3"]
    ),
    # Das neue Produkt hier hinzufügen
    Product(
        id="Product2",
        id_short="P2",
        description="This is product 2",
        bill_of_product=["Part 4", "Part 5", "Part 6"],
        bill_of_emissions=[
            Emission(
                id="Emission3",
                id_short="E3",
                category="Category3",
                scope=1,
                total_c02_equivalent=300,
                measuring_unit="kg",
                standards_country_code="DE",
                emissions_data_sheet_file_URL="http://example.com/emission3.pdf"
            ),
            Emission(
                id="Emission4",
                id_short="E4",
                category="Category4",
                scope=2,
                total_c02_equivalent=400,
                measuring_unit="kg",
                standards_country_code="DE",
                emissions_data_sheet_file_URL="http://example.com/emission4.pdf"
            )
        ],
        bill_of_states=["State 4", "State 5", "State 6"]
    ),
    # Weitere Produkte hier hinzufügen...
]
