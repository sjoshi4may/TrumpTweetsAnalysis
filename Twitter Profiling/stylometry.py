import nltk
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.utils import shuffle

""" Android = 1
    iphone = 0 """


# base = {'NN':0,'NNP':0,'IN':0,'JJ':0,'DT':0,'VB':0,'PRP':0,'NNS':0,'RB':0,
#         'VBZ':0,'VBP':0,'CC':0,'PRP$':0,'VBG':0,'VBD':0,'MD':0,'CD':0,'VBN':0,
#         'POS':0,'WP':0,'WRB':0,'JJR':0,'RP':0,'NNPS':0,'JJS':0,'WDT':0,'FW':0,
#         'EX':0,'RBR':0,'PDT':0,'RBS':0,'SYM':0,'UH':0,'WP$':0,'LS':0}

fhand = open('donaldtrumptweets.txt')
android_set=[]
iphone_set=[]
client_set=[]
for line in fhand:
    base = {'NN':0,'NNP':0,'IN':0,'JJ':0,'DT':0,'VB':0,'PRP':0,'NNS':0,'RB':0,
            'VBZ':0,'VBP':0,'CC':0,'PRP$':0,'VBG':0,'VBD':0,'MD':0,'CD':0,'VBN':0,
            'POS':0,'WP':0,'WRB':0,'JJR':0,'RP':0,'NNPS':0,'JJS':0,'WDT':0,'FW':0,
            'EX':0,'RBR':0,'PDT':0,'RBS':0,'SYM':0,'UH':0,'WP$':0,'LS':0,'.':0,
            "''":0,'TO':0,'``':0,':':0,'#':0}
    info = line.split(";;;")
    source = info[5].split(' ')[-1].split('<')[0]
    tweet = info[0].replace(',','').replace("u'",'').replace('u"','')
    tweet= tweet[1:].strip('"')

    token = nltk.word_tokenize(tweet)
    tagged = nltk.pos_tag(token)
    for words,key in tagged:
        if key!='(' and key!=')' and  key!='$':
            base[key]=base.get(key,0)+1

    if source=='Android':
        android_set.append(base.values())
    elif source=='iPhone':
        iphone_set.append(base.values())
    else:
        client_set.append(base)


training_android  = np.asarray(android_set[:int(0.9*len(android_set))])
res_train_android = np.ones(len(training_android))

training_iphone  = np.asarray(iphone_set[:int(0.9*len(android_set))])
res_train_iphone = np.zeros(len(training_iphone))

test_android = np.asarray(android_set[int(0.9*len(android_set)):])
res_test_android = np.ones(len(test_android))

test_iphone = np.asarray(iphone_set[int(0.9*len(android_set)):])
res_test_iphone = np.zeros(len(test_iphone))


training_set = np.concatenate((training_iphone,training_android),axis=0)
res_training = np.concatenate((res_train_iphone,res_train_android),axis=0)

test_Set=np.concatenate((test_iphone,test_android),axis=0)
res_test_Set=np.concatenate((res_test_iphone,res_test_android),axis=0)

# test_Set, res_test_Set = shuffle(test_Set, res_test_Set, random_state=0)


clf = MLPClassifier(activation='logistic',solver='adam', hidden_layer_sizes=(5,33),alpha=1e-4,max_iter=500)
clf.fit(training_set, res_training)
pred =clf.predict(test_Set)
prob=np.sum(pred==res_test_Set)/float(len(pred))
print prob
# print style
# base=sorted(base.items(),key = lambda x: x[1])
# x,y=zip(*base)
# plt.bar(range(len(x)), y, align='center')
# plt.xticks(range(len(x)), x)
# plt.xticks(rotation=60)
# plt.show()
