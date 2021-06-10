import os
import os.path
import sys
import json
import pandas as pd
import numpy as np
from numpy.random import default_rng
from types import SimpleNamespace

def messages(write,size):
    msg = "\nGerando dados em {}".format(write)
    msg += "\nData size: {}\n".format(int(size))
    return msg

data = {
    'filename':'semiordenado.dat',
    'size':999,
    'min':0,
    'max':1e6,
    'decimals':5,
    'hashsize':8,
    'partition':10,
    'window':20
}
data = json.loads(json.dumps(data), object_hook=lambda item: SimpleNamespace(**item))

try:
    if sys.argv[1] != '':
        data.size = int(sys.argv[1])
except IndexError:
    pass

filename = {
    'name':data.filename.split('.')[0],
    'ext':data.filename.split('.')[1],
    'len':len(data.filename.split('.')[0]),
    'write':None
}
filename = json.loads(json.dumps(filename), object_hook=lambda item: SimpleNamespace(**item))

rng = default_rng()

data_gen = pd.DataFrame(columns=['ID','VALUE','SCORE'])

data_gen['VALUE'] = np.around(rng.random(int(data.size))*rng.choice(int(data.max),size=int(data.size),replace=True),int(data.decimals))
data_gen['ID'] = [hash(str(x))%(10**data.hashsize) for x in data_gen['VALUE']]
data_gen['SCORE'] = np.sort(np.around(np.random.random(int(data.size)),data.decimals))


mudanca =(int ((data.partition * data.size)/100))
index = np.random.randint(0,data.size,mudanca)
print(index)
count = 0
while count < (mudanca-1):
        a = list({data_gen['SCORE'].iloc[index[count]],data_gen['SCORE'].iloc[index[count+1]]})
        b = list(np.copy(a))
        np.random.shuffle(b)
        data_gen['SCORE'] = data_gen['SCORE'].replace(a,b)
        count+=2
count = 0
for files in os.listdir('.'):
    if os.path.isfile(files) and files.split('.')[0][:filename.len] == filename.name:
        count+=1
if count != 0:
    filename.write = "{}{}.{}".format(filename.name,count,filename.ext)
    data_gen.to_csv(filename.write ,sep=" ",index=False)
    print(messages(filename.write,data.size))
else:
    filename.write = "{}.{}".format(filename.name,filename.ext)
    data_gen.to_csv(filename.write,sep=" ",index=False)
    print(messages(filename.write,data.size))
