import pandas as pd
import numpy as np
import collections
import matplotlib.pyplot as plt

users = pd.read_csv('./dt_small/ratings.csv')
users = users[users["rating"]>=3.5]
counter=collections.Counter(users['userId'])
users['count_r']=0
print(users.shape)
for x in users.index:
		users.loc[x,'count_r'] = counter[users.loc[x,'userId']]
counter=collections.Counter(users['userId'])

users = users[users["count_r"]>=100]
print(users.shape)
counter=collections.Counter(users['userId'])
plt.hist(counter.values())
plt.show()