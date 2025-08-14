import json
import random
from typing import Dict
from .entities import Neuron, Synapse, NeuromuscularJunction

class Network:
    def __init__(self):
        self.neurons: Dict[str, Neuron] = {}
        self.synapses: Dict[str, Synapse] = {}
        self.nmjs: Dict[str, NeuromuscularJunction] = {}
    def add_neuron(self, neuron: Neuron):
        self.neurons[neuron.id] = neuron
    def add_synapse(self, synapse: Synapse):
        self.synapses[synapse.id] = synapse
    def add_nmj(self, nmj: NeuromuscularJunction):
        self.nmjs[nmj.id] = nmj
    def develop(self):
        for n in list(self.neurons.values()):
            for m in list(self.neurons.values()):
                if n.id != m.id and f"{n.id}-{m.id}" not in self.synapses:
                    if random.random() < 0.5:
                        sid = f"{n.id}-{m.id}"
                        self.add_synapse(Synapse(id=sid, pre=n.id, post=m.id, weight=random.uniform(0.1,1.0), neurotransmitter="acetylcholine"))
        for n in list(self.neurons.values()):
            if f"{n.id}-muscle" not in self.nmjs and random.random() < 0.25:
                self.add_nmj(NeuromuscularJunction(id=f"{n.id}-muscle", neuron=n.id, muscle="body_wall", weight=random.uniform(0.1,1.0)))
    def to_json(self, path: str):
        data = {
            "neurons":[{"id":n.id,"position":n.position,"membrane_potential":n.membrane_potential} for n in self.neurons.values()],
            "synapses":[{"id":s.id,"pre":s.pre,"post":s.post,"weight":s.weight,"neurotransmitter":s.neurotransmitter} for s in self.synapses.values()],
            "nmjs":[{"id":j.id,"neuron":j.neuron,"muscle":j.muscle,"weight":j.weight} for j in self.nmjs.values()]
        }
        with open(path,"w") as f:
            json.dump(data,f)
