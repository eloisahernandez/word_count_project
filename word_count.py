import re
from nltk.stem import PorterStemmer 


ps = PorterStemmer()

#read book .read() is a method and requires ()
text = open("Frankenstein.txt","r").read()

#print(len(text))

#find all the different words
##split text into words
#count how many times each word appears in text

#delete punctuation 
#text = text.replace(","," ")

text = re.sub("[^a-zA-Z]", " ", text)
text = text.lower()

words = text.split(" ")


def not_empty_str(word):
    return word != ""
    
#

def elo_filter(should_keep_word,words):
    words2 = []
    for word in words:
        if should_keep_word(word):
            words2.append(word)
    return words2        
        

words2 = filter(not_empty_str,words)
        
        
#example: {"the": 20} 
word_count = {}


for word in words2:
    #word = ps.stem(word)
    if word in word_count:
        count = word_count[word]
        word_count[word] = count + 1
    else:
        word_count[word] = 1
        
sorted_count = []

for word, count in word_count.items():
    sorted_count.append([word,count])
 
#wordcount example ["the", 20] 

def get_count(wordcount):
    return wordcount[1]
    

#sorted_count.sort(reverse = True, key = lambda wordcount: wordcount[1])

sorted_count.sort(reverse = True, key = get_count)
    
print (len(word_count))
print(sorted_count[0:200])

#print(text[2400:3500])


