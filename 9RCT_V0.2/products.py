from typing import Optional, List
from dataclasses import dataclass

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

@dataclass
class Product:
    id: str
    id_short: str
    description: str
    bill_of_product: List['Product']  # Liste von Produkten statt von Strings
    bill_of_emissions: List[Emission]
    bill_of_states: List[str]

# Definition der Einzelteile
part1 = Product(
    id="Part1",
    id_short="Pa1",
    description="This is Part 1, which product 1 is made of",
    bill_of_product=[],
    bill_of_emissions=[
        Emission(
            id="Emission4",
            id_short="E4",
            category="Category4",
            scope=1,
            total_c02_equivalent=42,
            measuring_unit="kg",
            standards_country_code="DE",
            emissions_data_sheet_file_URL="https://youtu.be/xvFZjo5PgG0?si=ds_vYnnTLCysGrmY"
        ),
        Emission(
            id="Emission5",
            id_short="E5",
            category="Category5",
            scope=2,
            total_c02_equivalent=69,
            measuring_unit="kg",
            standards_country_code="DE",
            emissions_data_sheet_file_URL="http://example.com/emission5.pdf"
        )
    ],
    bill_of_states=["State 1", "State 3", "State 4"]
)

# Weitere Parts könnten hier definiert werden

# Definition der Produkte, die diese Teile verwenden
products = [
    Product(
        id="Product1",
        id_short="P1",
        description="This is product 1",
        bill_of_product=[part1],  # Verwendung des Part-Objekts
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
    Product(
        id="Product2",
        id_short="P2",
        description="This is product 2",
        bill_of_product=[],  # Liste ist leer, wenn keine Parts spezifiziert sind
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
    )
]