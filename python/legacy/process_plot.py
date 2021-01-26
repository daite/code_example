#!/usr/bin/env python
# tasklist > sample.txt for windows 7
# chrome sucks!!!!

import pandas as pd

df = pd.read_fwf('sample.txt', skiprows=[0, 1])
df.columns = ['Process name', 'PID',  'Session name',  'Session #',  'Memory usage']
data = [int(x.strip('K').replace(',', '')) for x in df['Memory usage']]
df['Memory usage'] = data
df1 = df.groupby('Process name').sum()
ax = df1['Memory usage'].order()[-8:].plot(kind='barh', grid=True, color='g')
ax.set_title("My process")
ax.set_xlabel("Memory KBytes")
ax.set_ylabel('Process name')
