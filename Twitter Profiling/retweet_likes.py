import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
filename='donaldtrumptweets.txt'
fhand = open(filename)
likes=[]
retweets=[]
tweet=[]
for line in fhand:
    info = line.split(';;;')
    likes.append(int(info[1].split('\'')[-1]))
    retweets.append(int(info[2].split('\'')[-1]))
i=likes.index(max(likes))
j= retweets.index(max(retweets))
print i,j
print likes[i],likes[j]
print retweets[i],retweets[j]
# print retweets,j
# plt.plot(range(0,l),likes,'b', range(0,l), retweets,'r')
# plt.show()
