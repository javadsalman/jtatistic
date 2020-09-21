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


    # BASICS
    # data =   [ random.randint(1, 10)  for i in range(10)]
    # dataset = Dataset(data)
    # print(data)
    # print(dataset)
    # print(f'{dataset.variance=},\n{dataset.deviation=},\n{dataset.coefficient=}')



    #COEFFICIENT
    # l = [1,2,3,4,5,6]
    # v = [i*2 for i in l]
    # dl = Dataset(l)
    # dv = Dataset(v)
    # print(f'{dl.variance=} {dv.variance=}')
    # print(f'{dl.coefficient=} {dv.coefficient=}')




    #SKEW
    # data = [1,2,2,2,3,3,3,4,4,5]
    # dataset = Dataset(data)
    # print(f'{dataset.mean=},\n{dataset.median=}')
    # print(f'{dataset.is_right_skew()=},\n{dataset.is_left_skew()=},\n{dataset.is_skew()=}')

    
    # COVVARIANCE
    # l = [2,4,6,8,10]
    # v = [1,3,5,7,9]
    # # v = [9,7,5,3,1]
    # # v = [9,1,5,3,7]
    # dl = Dataset(l)
    # dv = Dataset(v)

    # print(f'{covariance(dl, dv)=}')
    # print(f'{correlation(dl, dv)=}')
    # print(dl/dv, dl//dv)

   





    #NORMAL DISTRIBUTION
    # data =   [1,2,2,3,3,3,4,4,4,4,5,5,5,6,6,7]
    # dataset = Dataset(data)
    # print(f'{dataset.mean=} {dataset.median=} {dataset.mode}')
    # print(f'{dataset.is_normal_distribution()=}')





    #NORMAL DISTRIBUTION LIVE EXAMPLE
    # times = []
    # for i in range(10000):
    #     times.append(round(timeit.timeit('sum((1,2,3))', number = 1) * 100000, 5))
    #     sleep(0.0001)
    # dataset = Dataset(times)

    # print(dataset.mean, dataset.median, dataset.mode, max(dataset.args), min(dataset.args))



    # STANDART NORMAL DISTRIBUTION 
    # l = [1,2,2,3,3,3,4,4,5]
    # dataset = Dataset(l)
    # standart_dataset = dataset.get_standart()

    # print(f'{dataset.args=}\n{standart_dataset.args=}')
    # print(f'{dataset.mean=} {standart_dataset.mean=}')
    # print(f'{dataset.median=} {standart_dataset.median=}')
    # print(f'{dataset.mode=} {standart_dataset.mode=}')
    # print(f'{dataset.variance=} {standart_dataset.variance=}')




    # CETNRAL LIMIT THEOREM
    # student_heights = [random.randint(150, 195) for i in range(1000)]
    # pop = Dataset(student_heights)
    # sample_distribution = [Dataset(random.sample(pop.args, 100)) for i in range(1000)]
    # sd_dataset = SampleSet(sample_distribution)
    # print(sd_dataset.mean, pop.mean, '\n', sd_dataset.variance, pop.variance)
    # print(sd_dataset, sd_dataset.standart_error)


    
    