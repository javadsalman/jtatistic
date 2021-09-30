# jtatistic is a Python module for solving problems relevant to statistic topics
## BASIC USAGE
```python3
# ------------------- Code ------------------- #
data = [ random.randint(1, 10)  for i in range(10)]
dataset = Dataset(data)
print(data)
print(dataset)
print(f'{dataset.variance=},\n{dataset.deviation=},\n{dataset.coefficient=}')

# ------------------- Output ------------------- #
[5, 9, 5, 6, 10, 4, 6, 10, 2, 8]
<Dataset [N=10 Mean=6.500 Median=6.000 Mode=False]>
dataset.variance=7.166666666666667,
dataset.deviation=2.6770630673681683,
dataset.coefficient=0.41185585651817974
```
## COEFFICIENT
```python3
# ------------------- Code ------------------- #
l = [1,2,3,4,5,6]
v = [i*2 for i in l]
dl = Dataset(l)
dv = Dataset(v)
print(f'{dl.variance=} {dv.variance=}')
print(f'{dl.coefficient=} {dv.coefficient=}')

# ------------------- Output ------------------- #
dl.variance=3.5 dv.variance=14.0
dl.coefficient=0.5345224838248488 dv.coefficient=0.5345224838248488
```

## SKEW
```python3
# ------------------- Code ------------------- #
data = [1,2,2,2,3,3,3,4,4,5]
dataset = Dataset(data)
print(f'{dataset.mean=},\n{dataset.median=}')
print(f'{dataset.is_right_skew()=},\n{dataset.is_left_skew()=},\n{dataset.is_skew()=}')

# ------------------- Output ------------------- #
dataset.mean=2.9,
dataset.median=3.0
dataset.is_right_skew()=False,
dataset.is_left_skew()=True,
dataset.is_skew()=True
```

## COVVARIANCE
```python3
# ------------------- Code ------------------- #
l = [2,4,6,8,10]
v = [1,3,5,7,9]
v = [9,7,5,3,1]
v = [9,1,5,3,7]
dl = Dataset(l)
dv = Dataset(v)

print(f'{covariance(dl, dv)=}')
print(f'{correlation(dl, dv)=}')
print(dl/dv, dl//dv)

# ------------------- Output ------------------- #
covariance(dl, dv)=-1.8
correlation(dl, dv)=-0.060000000000000005
-1.8 -0.060000000000000005
```

## NORMAL DISTRIBUTION
```python3
# ------------------- Code ------------------- #
data =   [1,2,2,3,3,3,4,4,4,4,5,5,5,6,6,7]
dataset = Dataset(data)
print(f'{dataset.mean=} {dataset.median=} {dataset.mode}')
print(f'{dataset.is_normal_distribution()=}')

# ------------------- Output ------------------- #
dataset.mean=4.0 dataset.median=4.0 4
dataset.is_normal_distribution()=True
```

## STANDART NORMAL DISTRIBUTION 
```python3
# ------------------- Code ------------------- #
l = [1,2,2,3,3,3,4,4,5]
dataset = Dataset(l)
standart_dataset = dataset.get_standart()

print(f'{dataset.args=}\n{standart_dataset.args=}')
print(f'{dataset.mean=} {standart_dataset.mean=}')
print(f'{dataset.median=} {standart_dataset.median=}')
print(f'{dataset.mode=} {standart_dataset.mode=}')
print(f'{dataset.variance=} {standart_dataset.variance=}')

# ------------------- Output ------------------- #
dataset.args=[1, 2, 2, 3, 3, 3, 4, 4, 5]
standart_dataset.args=[-1.6329931618554523, -0.8164965809277261, -0.8164965809277261, 0.0, 0.0, 0.0, 0.8164965809277261, 0.8164965809277261, 1.6329931618554523]
dataset.mean=3.0 standart_dataset.mean=0.0
dataset.median=3 standart_dataset.median=0.0
dataset.mode=3 standart_dataset.mode=0.0
dataset.variance=1.5 standart_dataset.variance=1.0
```

## PROVING CETNRAL LIMIT THEOREM WITH JTATISTIC
```python3
# ------------------- Code ------------------- #
student_heights = [random.randint(150, 195) for i in range(10000)]
pop = Dataset(student_heights)
sample_distribution = [Dataset(random.sample(pop.args, 100)) for i in range(10000)]
sd_dataset = SampleSet(sample_distribution)
print(sd_dataset.mean, pop.mean, '\n', sd_dataset.variance, pop.variance)
print(sd_dataset, sd_dataset.standart_error)

# ------------------- Output ------------------- #
172.53898100000046 172.5413
1.783505122151223 178.9789922092179
<SampleSet [N=10000 Mean=172.53898 Standart Error=1.15563]> 1.1556294217595244
```
