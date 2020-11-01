import time


"""The parameters used for our implementation of the linear congruential generator are the same as the ANSI C implementation."""


class LCG:
    """
    Using this class you can generate list of psudo-random numbers between the range upper and lower (both inclusive).
    Lower limit of lower can be 0 and upper limit of upper can be 2**32 -1.
    I am using a linear congruence generator here.
    """
    def __init__(self, lower=0, upper=100, num_samples=20,seed = None):
        self.lower = lower
        self.upper = upper
        self.num_samples = int(num_samples)
        self.samples = list()
        self.seed = seed
        self.m=2**32
        self.a=1103515245
        self.c=12345

    def generate(self):
        """ Produce samples exclusive of upper and lower limit"""
        self.samples = []
        if self.seed is None:
            x = int(time.time())
        else:
            x = self.seed
        
        bias = self.lower
        length = self.upper - self.lower +1
        x = x % length
        for _ in range(self.num_samples):
            x=(self.a*x+self.c)%self.m
            number = x%length + bias
            self.samples.append(number)
            
        return self.samples
    
    def __call__(self):
        if len(self.samples) != self.num_samples:
            self.generate()
        return self.samples