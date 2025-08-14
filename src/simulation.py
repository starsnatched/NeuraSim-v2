import math
from .network import Network
from .entities import Neuron


def initialize_network():
    net = Network()
    for i in range(4):
        angle = i * math.pi / 2
        x = math.cos(angle)
        y = math.sin(angle)
        net.add_neuron(Neuron(id=f"n{i}", position=(x, y)))
    return net


def run_development(net: Network, steps: int):
    for _ in range(steps):
        net.develop()


if __name__ == "__main__":
    net = initialize_network()
    run_development(net, 10)
    net.to_json("data/network.json")
