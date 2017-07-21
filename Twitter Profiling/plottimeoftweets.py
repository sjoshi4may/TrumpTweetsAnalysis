# Also number of tweets per day
import matplotlib.pyplot as plt
import collections
import pandas as pd

filename = 'donaldtrumptweets.txt'
fhand  = open(filename)
time_iphone=[]
time_android=[]
time_rest=[]
time=[]
date=[]
date_android=[]
date_iphone=[]
date_rest=[]
for line in fhand:
    info = line.split(';;;')
    source = info[5].split(' ')[-1].split('<')[0]
    date_time_day = info[3].split(' ')
    t= date_time_day[4]
    date = date_time_day[2]+' '+ date_time_day[-1]
    time.append(t)
    if source=='Android':
        time_android.append(int(t[:2]))
        date_android.append(date)
    elif source=='iPhone':
        time_iphone.append(int(t[:2]))
        date_iphone.append(date)
    else:
        time_rest.append(int(t[:2]))
        date_rest.append(date)
counter1=collections.Counter(date_iphone)
counter2=collections.Counter(date_android)
counter3=collections.Counter(date_rest)

df1=pd.DataFrame(counter1,index=['iphone'],columns=['Jun 2016','Jul 2016','Aug 2016','Sep 2016','Oct 2016',
                                                    'Nov 2016','Dec 2016','Jan 2017','Feb 2017','Mar 2017',
                                                    'Apr 2017','May 2017','Jun 2017','Jul 2017'])
df2=pd.DataFrame(counter2,index=['android'],columns=['Jun 2016','Jul 2016','Aug 2016','Sep 2016','Oct 2016',
                                                    'Nov 2016','Dec 2016','Jan 2017','Feb 2017','Mar 2017',
                                                    'Apr 2017','May 2017','Jun 2017','Jul 2017'])
df3=pd.DataFrame(counter3,index=['Web Client'],columns=['Jun 2016','Jul 2016','Aug 2016','Sep 2016','Oct 2016',
                                                    'Nov 2016','Dec 2016','Jan 2017','Feb 2017','Mar 2017',
                                                    'Apr 2017','May 2017','Jun 2017','Jul 2017'])
df1=df1.fillna(0)
df2=df2.fillna(0)
df3=df3.fillna(0)
df=pd.concat([df1,df2,df3])
df=df.T
df.plot.bar()
plt.show()
#
# plt.bar(range(len(counter1)), counter1.values(), align="center")
# plt.xticks(range(len(counter1)), list(counter1.keys()))
# plt.bar(range(len(counter2)), counter2.values(), align="center")
# plt.xticks(range(len(counter2)), list(counter2.keys()))
# plt.show()
