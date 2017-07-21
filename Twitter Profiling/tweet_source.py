
fhand = open('jeremycorbyntweets.txt')
for line in fhand:
    info = line.split(";;;")
    source = info[5].split(' ')[-1].split('<')[0].split('>')[-1]
    print source
