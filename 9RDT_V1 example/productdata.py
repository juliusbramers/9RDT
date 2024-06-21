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
    bill_of_product: List[str]
    bill_of_emissions: List[Emission]
    bill_of_states: List[str]

# Einzelne Produktinstanzen
Tesla_Model_3 = Product(
    id="Tesla Model 3",
    id_short="TM3",
    description="This is the Tesla Model 3. It is a fully electric car made by Tesla corp.",
    bill_of_product=[
        "Battery Assembly",
        "Chassis",
        "Interior",
        "Exterior",
        "Wheels",
        "Electronics"
    ],
    bill_of_emissions=[],
    bill_of_states=[
        "Product in concept stage, not yet produced",
        "Product is in the manufacturing or design phase",
        "Product is used and functional but no longer with the original owner",
        "Product is damaged or partially non-functional",
        "Product is at the end of its first life, but components are still usable",
        "Product can no longer be used in its original form",
        "Product is non-functional and cannot be repaired",
        "Product is at the end of its lifecycle and no longer usable"
    ]
)

Battery_Assembly = Product(
    id="Tesla Model 3 Battery Assembly",
    id_short="TM3BA",
    description="This is the Battery Assembly of Tesla Model 3. It is made up of 2170 baterry cells.",
    bill_of_product=[
        "Battery Cells", 
        "Battery Management System", 
        "Cooling System", 
        "Battery Housing"
        ],
    bill_of_emissions=[],
    bill_of_states=[
        "Product is used and functional but no longer with the original owner",
        "Product is damaged or partially non-functional",
        "Product is at the end of its first life, but components are still usable",
        "Product can no longer be used in its original form",
        "Product is non-functional and cannot be repaired",
        "Product is at the end of its lifecycle and no longer usable"
    ]
)

Battery_Cells = Product(
    id="Tesla Model 3 Battery Cells",
    id_short="TM3BC",
    description="This is the Battery Cell of the Tesla Model 3 battery Assembly.",
    bill_of_product=[],
    bill_of_emissions=[
        Emission(
            id="Emission Battery Cells Model 3",
            id_short="EBCM3",
            category="Co2 Equivalent",
            scope=2,
            total_c02_equivalent=3100,
            measuring_unit="kg",
            standards_country_code="DE",
            emissions_data_sheet_file_URL="https://www.iso.org/standard/71206.html"
        )
    ],
    bill_of_states=[
        "Product is damaged or partially non-functional",
        "Product is at the end of its first life, but components are still usable",
        "Product can no longer be used in its original form",
        "Product is non-functional and cannot be repaired",
        "Product is at the end of its lifecycle and no longer usable"
    ]
)

#Hier müssen die Produkte eingetragen werden
products = {
    "Tesla Model 3": Tesla_Model_3,
    "Battery Assembly": Battery_Assembly,
    "Battery Cells": Battery_Cells
}