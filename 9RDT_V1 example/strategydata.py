from typing import List
from dataclasses import dataclass

# RStrategy Klasse definieren
@dataclass
class RStrategy:
    id: str
    possible_states: List[str]

# Einzelne Recycling-Strategien als Instanzen
r_strategy0 = RStrategy(
    id="R0",
    possible_states=["State 1", "State 2", "State 3"]
)

r_strategy1 = RStrategy(
    id="R1",
    possible_states=["State 4", "State 5", "State 6"]
)

r_strategy2 = RStrategy(
    id="R2",
    possible_states=["State 2"]
)

r_strategy3 = RStrategy(
    id="R3",
    possible_states=["State 4", "State 5"]
)

r_strategy4 = RStrategy(
    id="R4",
    possible_states=["State 3"]
)

r_strategy5 = RStrategy(
    id="R5",
    possible_states=["State 1", "State 3", "State 4"]
)

r_strategy6 = RStrategy(
    id="R6",
    possible_states=["State 1"]
)

r_strategy7 = RStrategy(
    id="R7",
    possible_states=["State 2", "State 4"]
)

r_strategy8 = RStrategy(
    id="R8",
    possible_states=["State 1", "State 2", "State 6"]
)

r_strategy9 = RStrategy(
    id="R9",
    possible_states=["State 2", "State 5"]
)

r_strategies = [r_strategy0, r_strategy1, r_strategy2, r_strategy3, r_strategy4, r_strategy5, r_strategy6, r_strategy7, r_strategy8, r_strategy9]