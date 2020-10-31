class UniformGenerator:
    def __init__(self, lower, upper, num_samples=50):
        self.lower = lower
        self.upper = upper
        self.num_samples = num_samples
        self.samples = list()

    def produce_samples_exclusive(self):
        ''' Produce samples exclusive of upper and lower limit'''
        gaps = (self.upper - self.lower)/(self.num_samples+1)
        
        for i in range(1, self.num_samples+1):
            self.samples.append(self.lower + i*gaps)
        
        return self.samples

