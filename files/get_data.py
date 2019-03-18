from pandas_datareader import data
import pandas as pd

#抓資料
df = pd.read_csv('/Users/Kang/Desktop/ETF分組/Developed Europe ETF List (90).csv')
d = df['Symbol'].tolist()

startTime = '2015-12-01'
endTime = '2018-12-31'

df1 = data.DataReader(d, 'yahoo', startTime, endTime)['Adj Close']
###############################################################################
#丟掉月底以外的row
drop_ind = []

for i in range(1,len(df1.index)-1):
    if df1.index[i].month == df1.index[i+1].month:
        drop_ind.append(df1.index[i])
    else:
        pass

df1 = df1.drop(index = drop_ind)
#第一列是11月要拿掉
df1 = df1.drop(df1.index[0])
###############################################################################
#丟掉並非全部月份都有資料的ETF
drop_col = []

t = df1.columns.tolist()
for i in t:
    if df1[i].isnull().any() == True:
        drop_col.append(i)
    else:
        pass

df1 = df1.drop(columns = drop_col)
###############################################################################
#存擋
df1.to_csv('/Users/Kang/Desktop/Result.csv')
