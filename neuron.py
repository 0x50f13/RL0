import random
import _globals
import matplotlib.pyplot as plt

class Neuron:
    def __init__(self, lc=0.1, lim=1.0, punish=0.1, diff=4, ind=1.0, rand_act=0.2, defautl_r=16.6):
        '''
        :param lc:Loss coefficent in time how mush activation loss after time pass
        :param lim:Maximum polarized  activation
        :param punish: resistence inc/dec in case of good time diff
        :param diff: time diff to punish/treat
        :param ind: Induction on activation
        :param rand_act:Random activation add coeff
        :param default_r:default synapse resist
        '''
        self.lim = lim
        self.w = []
        self.syn = []  ##Activation in current moent on synapses
        self.lc = lc  ##Loss coeff
        self.last_act = 0
        self.cur = 0.0  ##Current activation
        self.punish = punish
        self.diff = diff
        self.out = 0.0
        self.ind = ind
        self.default_r = defautl_r
        self.rand_act = rand_act

    def add_syn(self):
        self.w.append(self.default_r)
        self.syn.append(0.0)
        return len(self.w)-1

    def activate(self, num, val):
        assert num<len(self.w),"w number out of range:%d miust be 0<=num<%d"%(num,len(self.w))
        self.syn[num] = val / self.w[num]
        delta = _globals.t - self.last_act
        if delta < self.diff and delta > 0:
            self.w[num] += self.punish
        elif delta > -self.diff and delta < 0:
            self.w[num] -= self.punish
        elif delta == 0:
            self.w[num] += self.punish
        else:
            if delta < 0:
                self.w[num] -= 0.1 * self.punish
            else:
                self.w[num] += 0.1 * self.punish
        if self.w[num] < 1.0:
            self.w[num] = 1.0

    def on_timer(self):
        self.cur += sum(self.syn) + abs(
            random.uniform(0, 2 * self.rand_act) - self.rand_act)  ##FIXME:fix lower limit to 0
        self.out = self.cur - self.lim
        if self.out < 0:
            self.out = 0
        elif self.out > 0:
            self.last_act = _globals.t
            self.out += self.ind
        self.cur-=self.lc
        if(self.cur<0):
            self.cur=0

class ResistNeuron:
    def __init__(self,res=1.0,lc=0.5):
        self.res=res
        self.lc=lc
        self.syn=[]
        self.cur=0.0
        self.out=0.0
    def add_syn(self):
        self.syn.append(0.0)
        return len(self.syn)-1
    def activate(self,num,val):
        self.syn[num]=val/self.res
    def on_timer(self):
        self.cur=sum(self.syn)
        self.out=self.cur


