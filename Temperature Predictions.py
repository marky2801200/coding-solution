# question link: https://www.hackerrank.com/challenges/temperature-predictions/problem

# Enter your code here. Read input from STDIN. Print output to 
import pandas as pd

N = int(input())

columns = input().split()

df = pd.DataFrame(columns=columns)

for i in range(N):
    df.loc[i, :] = input().split()
    
df.tmax = pd.to_numeric(df.tmax, errors='coerce')
df.tmin = pd.to_numeric(df.tmin, errors='coerce')

tmax_missing = df.tmax.isna()
tmin_missing = df.tmin.isna()

tmax_interp = df.tmax.interpolate(method='cubic')
tmin_interp = df.tmin.interpolate(method='cubic')

for i in range(df.shape[0]):
    if tmax_missing[i]:
        print(tmax_interp[i])
    if tmin_missing[i]:
        print(tmin_interp[i])


