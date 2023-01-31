#Split the sentence, also think of casing, 
# iterate over the split elements, and 
# count two things: 
# 1) The total number of items and 
# 2) how often the word "I" was used.

sentence = "I will hug you now"
words = sentence.split()
#print(words)

for word in words: 
   numwords = len(words) 
   numI = words.count("I")
print("There are", numwords, " words in our sentence.")
print("The word 'I' shows up",  numI , " time(s) in our sentence.") 

#the xth element/item of the list
print(words[1])