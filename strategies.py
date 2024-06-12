from typing import List
from dataclasses import dataclass

# RStrategy Klasse definieren
@dataclass
class RStrategy:
    id: str
    possible_states: List[str]

# Recycling-Strategien definieren
r_strategies = [
    RStrategy(
        id="R0", 
        possible_states=["State 1", "State 2", "State 3"]
    ),
    RStrategy(
        id="R1", 
        possible_states=["State 4", "State 5", "State 6"]
    ),
    RStrategy(
        id="R2", 
        possible_states=["State 2"]
    ),
    RStrategy(
        id="R3", 
        possible_states=["State 4", "State 5"]
    ),
    RStrategy(
        id="R4", 
        possible_states=["State 3"]
    ),
    RStrategy(
        id="R5", 
        possible_states=["State 1", "State 3", "State 4"]
    ),
    RStrategy(
        id="R6", 
        possible_states=["State 1"]
    ),
    RStrategy(
        id="R7", 
        possible_states=["State 2", "State 4"]
    ),
    RStrategy(
        id="R8", 
        possible_states=["State 1", "State 2", "State 6"]
    ),
    RStrategy(
        id="R9", 
        possible_states=["State 2", "State 5"]
    ),
]