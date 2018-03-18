with open("hb.txt",'r') as fp:
    content=fp.read()

words=content.split()
set_words = set(words)
new_words_list = list(set_words)
d={}
count=0
for word in new_words_list:
    d[word]=0
    for word_boss in words:
        if word_boss==word:
            count=count+1
    d[word] = count
    count=0

f= sorted(d,key=d.get,reverse = True)
top = f[0:9]
print("Top 10 most frequent words are-")
for w in top:
    print("'" +str(w)+ "'"+" with a frequency of- "+str(d[w]))
