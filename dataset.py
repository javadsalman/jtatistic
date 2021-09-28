import math
import random

def covariance(d1, d2):
    d1_mean, d2_mean = d1.mean, d2.mean
    return sum([(d1.args[i] - d1.mean)*(d2.args[i] - d2.mean) for i in range(d1.n)]) / d1.n - 1

def correlation(d1, d2):
    return covariance(d1, d2) / (d1.mean * d2.mean)



class BasicDataset:
    def __init__(self, args, sample = True):
        self.args = args
        self.sample = sample

    @property
    def n(self):
        return len(self.args)

    @property
    def mean(self):
        return round(sum(self.args)/self.n, 15)

    @property
    def median(self):
        middle = (self.n+1)/2
        args = sorted(self.args)
        if middle.is_integer():
            return args[int(middle)-1]
        else:
            return (args[int(middle)] + args[int(middle)-1]) / 2
            
    @property
    def mode(self):
        _dict = {}
        item, count = '', 0
        for i in self.args:
            _dict[i] = _dict.get(i, 0) + 1
            if _dict[i] >= count:
                last_count = count
                item, count = i, _dict[i]
        return item if count > last_count else False

    @property
    def variance(self):
        mean = self.mean
        alg_sum = sum([pow(arg-mean, 2) for arg in self.args])
        return round(alg_sum / (self.n - (1 if self.sample else 0)), 15)

    @property
    def deviation(self):
        return self.variance ** 0.5

    

    
    
class Dataset(BasicDataset):
    def __str__(self):
        mode = self.mode
        return f'<Dataset [N={self.n} Mean={self.mean:.3f} Median={self.median:.3f} Mode={mode if mode!=False else False}]>' 
    
    def __add__(self, other):
        return Dataset(self.args + other.args)

    def __sub__(self, other):
        copy_args = self.args[:]
        for i in other.args:
            if i in copy_args:
                copy_args.remove(i)
        return Dataset(copy_args)

    def __truediv__(self, other):
        return covariance(self, other)
    
    def __floordiv__(self, other):
        return correlation(self, other)

    def __getitem__(self, key):
        return self.args[key]

    def __setitem__(self, key, value):
        self.args[key] = value
        
    def shuffle(self):
        random.shuffle(self.args)

    def sort(self):
        self.args.sort()

    def get_standart(self):
        mean = self.mean
        deviation = self.deviation
        return Dataset([(i-mean)/deviation for i in self.args])

    
    
    @property
    def skewness(self):
        mean = self.mean
        alg_sum_pw3 = sum([(i - mean)**3 for i in self.args])
        alg_sum_pw2 = sum([(i - mean)**2 for i in self.args])
        return ((1/self.n)*alg_sum_pw3) / pow((1/(self.n-1)) * alg_sum_pw2, 1/3)
        
    def is_right_skew(self):
        return self.mean > self.median

    def is_left_skew(self):
        return self.mean < self.median

    def is_skew(self):
        return self.mean != self.median

    
    
    @property
    def coefficient(self):
        return self.deviation / self.mean
 
    def is_normal_distribution(self):
        return self.mean == self.median == self.mode

    def is_standart_normal_distribution(self):
        return self.mean == self.median == self.mode and self.variance == 1





class SampleSet(BasicDataset):
    def __init__(self, sampledata):
        self.sampledata = sampledata
        self.args = [sample.mean for sample in sampledata]
        self.sample = True
    
    def __str__(self):
        return f'<SampleSet [N={self.n} Mean={self.mean:.5f} Standart Error={self.standart_error:.5f}]>'
    
    @property
    def standart_error(self):
        return self.deviation / pow(self.deviation, 0.5)


if __name__ == "__main__":
    import timeit
    from time import sleep