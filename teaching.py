import pandas as pd
import numpy as np

data = pd.read_csv('./camcors_claim.csv')
def total(df):
    return sum(sum([df['GS%i' % i]/i for i in range(1,6)]) + df['GS6+ count']/df['GS6+ size'])

data['Paper code'].unique()

maths = ['MATH','MATH/1','MAT0/1','ZZZ!']
physics = ['PSIC']
rac = ['1/RAC']
rel = ['2/REL','2','PTP']
partiii = ['RPR']
maths = data[np.logical_or.reduce([data['Paper code']==i for i in maths])]
physics = data[np.logical_or.reduce([data['Paper code']==i for i in physics])]
rac = data[np.logical_or.reduce([data['Paper code']==i for i in rac])]
rel = data[np.logical_or.reduce([data['Paper code']==i for i in rel])]
partiii = data[np.logical_or.reduce([data['Paper code']==i for i in partiii])]

print('Maths', total(maths[maths['GS6+ count']==0]))
print('Maths Tripos', total(maths[maths['GS6+ count']>0]))
print('Physics', total(physics))
print('RAC', total(rac))
print('Relativity', total(rel))
print(total(data)-total(partiii),total(maths) + total(rac) + total(rel) + total(physics))
