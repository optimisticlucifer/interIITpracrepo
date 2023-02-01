#%%%
import pandas as pd
import math
tranData=pd.read_csv("fake_data.csv");
tranData
# %%
enter = [] 
exit = []
for i in range(tranData.shape[0]):
    temp=tranData['amount'].iloc[i]
    if(temp >0):
        enter.append(tranData['price'].iloc[i])
    else:
        exit.append(tranData['price'].iloc[i])
# %%
returns=0
indiReturns=[]
for i in zip(exit, enter):
    tempReturns = (math.log(i[0],math.e) - math.log(i[1],math.e))
    indiReturns.append(tempReturns)
    returns+=tempReturns

# %%
print("the return in MYR is {}".format(returns))
print("the individual return in MYR is {}".format(indiReturns))
