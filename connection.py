import _globals
class Axon:
    def __init__(self, input_id, out_ids):  # ids of neurons in tuple (<id_neuron>,<id_synapse>)
        self.input = input_id
        self.out = []
        for i in out_ids:
            self.out.append((i, _globals.nn.neurons[i].add_syn()))

    def on_timer(self):
        out = _globals.nn.neurons[self.input]
        for c in self.out:
            (i, syn) = c
            _globals.nn.neurons[i].activate(syn, out.cur)