from typing import Optional, List
from dataclasses import dataclass
from strategydata import r_strategy0, r_strategy1, r_strategy2, r_strategy3, r_strategy4, r_strategy5, r_strategy6, r_strategy7, r_strategy8, r_strategy9
from strategydata import RStrategy

@dataclass
class Emission:
    id: str
    id_short: str
    category: Optional[str]
    scope: Optional[int]
    total_c02_equivalent: Optional[int]
    measuring_unit: Optional[str]
    standards_country_code: Optional[str]
    emissions_data_sheet_file_URL: Optional[str]

@dataclass
class EmissionNewR:
    id: str
    id_short: str
    description: Optional[str]
    category: Optional[str]
    scope: Optional[int]
    total_c02_equivalent: Optional[int]
    measuring_unit: Optional[str]
    standards_country_code: Optional[str]
    emissions_data_sheet_file_URL: Optional[str]
    r_strategy: RStrategy
    r_strategy_emissions_difference_percent: Optional[int]
    r_strategy_cost_difference_percent: Optional[int]

@dataclass
class Product:
    id: str
    id_short: str
    description: Optional[str]
    bill_of_product: Optional[List[str]]
    bill_of_emissions: Optional[List[Emission]]
    bill_of_emissions_new_r: Optional[List[EmissionNewR]]
    bill_of_states: Optional[List[str]]

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
    bill_of_emissions_new_r=[],
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
    bill_of_emissions_new_r=[],
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
    bill_of_emissions_new_r=[
        EmissionNewR(
            id="Emission New R Strategy 6 Battery Cells Model 3",
            id_short="ENR6BCM3",
            description="These are the new Emissons for the R-Strategies for Battery Cell of the Tesla Model 3 battery Assembly.",
            category="Co2 Equivalent",
            scope=2,
            total_c02_equivalent=2400,
            measuring_unit="kg",
            standards_country_code="DE",
            emissions_data_sheet_file_URL="https://www.iso.org/standard/71206.html",
            r_strategy=r_strategy6,
            r_strategy_emissions_difference_percent=24,
            r_strategy_cost_difference_percent=13
        ),
        EmissionNewR(
            id="Emission New R Strategy 4 Battery Cells Model 3",
            id_short="ENR4BCM3",
            description="These are the new Emissons for the R-Strategies for Battery Cell of the Tesla Model 3 battery Assembly.",
            category="Co2 Equivalent",
            scope=2,
            total_c02_equivalent=400,
            measuring_unit="kg",
            standards_country_code="DE",
            emissions_data_sheet_file_URL="https://www.iso.org/standard/71206.html",
            r_strategy=r_strategy4,
            r_strategy_emissions_difference_percent=83,
            r_strategy_cost_difference_percent=64
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