from dataclasses import dataclass
from typing import Tuple

@dataclass
class Neuron:
    id: str
    position: Tuple[float, float]
    membrane_potential: float = 0.0

@dataclass
class Synapse:
    id: str
    pre: str
    post: str
    weight: float
    neurotransmitter: str

@dataclass
class NeuromuscularJunction:
    id: str
    neuron: str
    muscle: str
    weight: float
