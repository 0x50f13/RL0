from _globals import *
import random

from connection import Axon
from neuron import Neuron, ResistNeuron



class Network:
    neurons = []

    def add_neuron(self, neuron):
        self.neurons.append(neuron)
        self.axons = []
        return len(self.neurons) - 1

    def connect(self, src, dsts):
        self.axons.append(Axon(src, dsts))

    @staticmethod
    def get_rand_neurons(cnt, cur):
        if cur == 0:
            return []
        r = set()
        for i in range(cnt):
            r.add(cur - random.randrange(0, cur - 1) - 1 )
        return list(r)

    def generate_random(self, count, layer_size=3):
        for i in range(count):
            if random.randrange(0, 10) == 5:
                self.connect(
                    self.add_neuron(
                        Neuron(random.uniform(0.1, 0.3), random.uniform(0.6, 1.2), random.uniform(0.2, 0.7))),
                    self.get_rand_neurons(random.randrange(1, layer_size), len(self.neurons)))
            else:
                self.connect(self.add_neuron(ResistNeuron(random.uniform(0.7, 1.1), random.uniform(0.9, 1.5))),
                             self.get_rand_neurons(random.randrange(1, layer_size), len(self.neurons)))
    def on_timer(self):
        for i in range(len(self.axons)):
            self.axons[i].on_timer()
        for i in range(len(self.neurons)):
            self.neurons[i].on_timer()