vowelsDict = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

sentence = input("Write a sentence.\n> ") #input from user

for letter in sentence.lower():
    if letter in vowelsDict:
        vowelsDict[letter] +=1

print ('\n' + 'Your sentence was:   ' + '\n')
print ('Histogram of vowels in the sentence.\n')

for vowel in sorted(vowelsDict):
    histo = 'X' * vowelsDict[vowel]
    print ('{0}: {1}'.format(vowel,histo))

print('\nTotal number of vowels: {}'.format(sum(vowelsDict.values())))
