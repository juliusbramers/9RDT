from typing import List
from dataclasses import dataclass

# RStrategy Klasse definieren
@dataclass
class RStrategy:
    id: str
    possible_states: List[str]

# Einzelne Recycling-Strategien als Instanzen
r_strategy0 = RStrategy(
    id="Refuse",
    possible_states=["Product in concept stage, not yet produced"]
)

r_strategy1 = RStrategy(
    id="Rethink",
    possible_states=["Product in concept stage, not yet produced"]
)

r_strategy2 = RStrategy(
    id="Reduce",
    possible_states=["Product is in the manufacturing or design phase"]
)

r_strategy3 = RStrategy(
    id="Reuse",
    possible_states=["Product is used and functional but no longer with the original owner"]
)

r_strategy4 = RStrategy(
    id="Repair",
    possible_states=["Product is damaged or partially non-functional"]
)

r_strategy5 = RStrategy(
    id="Refurbish",
    possible_states=["Product is outdated or shows signs of wear"]
)

r_strategy6 = RStrategy(
    id="Remanufacture",
    possible_states=["Product is at the end of its first life, but components are still usable"]
)

r_strategy7 = RStrategy(
    id="Repurpose",
    possible_states=["Product can no longer be used in its original form"]
)

r_strategy8 = RStrategy(
    id="Recycle",
    possible_states=["Product is non-functional and cannot be repaired"]
)

r_strategy9 = RStrategy(
    id="Recover",
    possible_states=["Product is at the end of its lifecycle and no longer usable"]
)

r_strategies = [r_strategy0, r_strategy1, r_strategy2, r_strategy3, r_strategy4, r_strategy5, r_strategy6, r_strategy7, r_strategy8, r_strategy9]