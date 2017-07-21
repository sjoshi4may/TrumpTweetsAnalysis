from operator import itemgetter
import nltk
# import matplotlib.pyplot as plt
fhand = open('donaldtrumptweets.txt')
count_android={}
count_iphone={}
count_client ={}
count_tweetdeck={}
total_count={}
for line in fhand:
    info = line.split(";;;")
    source = info[5].split(' ')[-1].split('<')[0].split('>')[-1]
    tweet = info[0].replace(',','').replace("u'",'').replace('u"','')
    tweet= tweet[1:].strip('"')

    token = nltk.word_tokenize(tweet)
    tagged = nltk.pos_tag(token)
    # words=tweet.split(' ')
    for tup in tagged:
        if tup[1]=='JJ' or tup[1]=='JJR' or tup[1]=='JJS':# or tup[1]=='UH' or tup[1]=='RB'or tup[1]=='RBS'or tup[1]=='RBR':
            word=tup[0]
            word=word.lower()
            total_count[word]=total_count.get(word,0)+1
            if source=='Android':
                count_android[word]=count_android.get(word,0)+1
            elif source=='iPhone':
                count_iphone[word]=count_iphone.get(word,0)+1
            elif source=='TweetDeck':
                count_tweetdeck[word]=count_tweetdeck.get(word,0)+1
            else:
                count_client[word]=count_client.get(word,0)+1


count_android=sorted(count_android.items(), key=itemgetter(1))
count_iphone=sorted(count_iphone.items(), key=itemgetter(1))
count_client=sorted(count_client.items(), key=itemgetter(1))
total_count=sorted(total_count.items(), key=itemgetter(1))
count_tweetdeck=sorted(count_tweetdeck.items(),key = itemgetter(1))

andro_iphon_ratio = {}
for tup1 in count_android:
    for tup2 in count_iphone:
        if tup1[0]==tup2[0]:
            andro_iphon_ratio[tup1[0]]=float(tup1[1])/tup2[1]

# for tup in sorted(andro_iphon_ratio.items(), key=itemgetter(1)):
#     print tup[0],tup[1]
counts=andro_iphon_ratio

words = sorted(counts, key=counts.get, reverse=True)
highest = None
lowest = None
for w in words[:100]:
    if highest is None or highest < counts[w] :
        highest = counts[w]
    if lowest is None or lowest > counts[w] :
        lowest = counts[w]
print 'Range of counts:',highest,lowest

# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

fhand = open('gword.js','w')
fhand.write("gword = [")
first = True
for k in words[:100]:
    if not first : fhand.write( ",\n")
    first = False
    size = counts[k]
    size = (size - lowest) / float(highest - lowest)
    size = int((size * bigsize) + smallsize)
    fhand.write("{text: '"+k+"', size: "+str(size)+"}")
fhand.write( "\n];\n")

print "Output written to gword.js"
print "Open gword.htm in a browser to view"

#
# plt.bar(range(len(D)), D.values(), align='center')
# plt.xticks(range(len(D)), D.keys())
# plt.xticks(rotation=45)
# plt.show()
