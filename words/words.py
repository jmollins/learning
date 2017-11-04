
#!/usr/bin/env python
def histo(label, count): #print the histogram
    print ('%3s :' % label + 'X' * count)
    return 0

wordLength = [0 for i in range(0,15)] #empty list to store letter count
sentence = input('Enter a sentence for the word count: ')

words = sentence.split() #split the sentence into words

for word in words: #get the length of the words
    wordLength[len(word)]+=1

for word, letters in enumerate(wordLength): #Go through the word list and make a histogram
    histo(word, letters) #plot the histogram
    
    

    
