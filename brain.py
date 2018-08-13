import _globals

import threading
import random
import datetime
from neuron import Neuron
import matplotlib.pyplot as plt
from audio import read
#from video import  get_video
import numpy as np
import network


plt.show()
ax = plt.gca()
ax.set_autoscale_on(True)
line, = ax.plot([], [])

lock = threading.Lock()
cfinished = threading.Event()



def init():
    #global nn
   # nn = Network()
    print("Initiallizing...",end="")
    random.seed(hash(datetime.datetime.now()))
    network.generate_random(2000,20)

    print("OK")
def run_net():
    while True:
        cfinished.clear()
        _globals.nn.on_timer()
        _globals.t += 1
        max = 0.0
        _id = -1
        avg=0
        data=read(exception_on_overflow = False)
        for s in data:
            #print(s)
            _globals.nn.neurons[96+1+s].activate(0,1.0)
            _globals.nn.on_timer()
        cnt=0
        #for c in np.ndarray.flatten(get_video()):
        #    _globals.nn.neurons[96+256+cnt].activate(0,c/255.0)
        #   cnt+=1
        _globals.nn.on_timer()
        for i, n in enumerate(_globals.nn.neurons[:96]):
            if n.out > max:
                max = n.out
                _id = i
                avg=avg+n.cur
        if _id != -1:
            print(chr(_id+ord(' ')), end="")
        avg/=96.0
        line.set_ydata(avg)
        line.set_xdata(_globals.t)
        ax.relim()
        ax.autoscale_view(True, True, True)
        plt.draw()
        cfinished.set()


def hid():
    global t
    while True:
        msg = input("\n[You]:>")
        cfinished.wait()
        lock.acquire()
        for c in msg:
            _globals.nn.neurons[ord(c) - ord(' ')].activate(0, 1.0)
            _globals.t += 1
        _globals.nn.on_timer()
        lock.release()


def run():
    init()
    plt.interactive(True)

    t0 = threading.Thread(target=run_net)
    t1 = threading.Thread(target=hid)
    t0.start()
    t1.start()

if __name__ == '__main__':
    run()
