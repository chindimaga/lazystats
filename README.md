This library has basic mathematical implementations which can increase your working pace

## To install 
> pip install lazystats
## How to use 

### to genarate 30 numbers between 10 and 100 (BOTH inclusive) 
```
import lazystats
a = lazystats.Randnums.LCG(10,100,30)
print(a.generate())
```

### you may even set the seed to reproduce the results
```
import lazystats
seed = 20
a = lazystats.Randnums.LCG(10,100,30,seed)
print(a.generate())
```