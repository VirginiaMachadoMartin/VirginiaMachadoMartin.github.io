#read the lorem.txt file and count character frequency in text

#send in file
text = open('lorem.txt', 'r')

#file to str
text_read = text.read()

#declare empty list to fill with frequency count
text_as_list = list()


#for loop over str
for char in text_read:

   #count characters in str file 
    character_count = text_read.count(char)

   #fill empty list by testing if character is there & appending it if it's not
    if text_as_list.count(char) == 0: 
        text_as_list.append(char)
        text_as_list.append(character_count)

#print awesome results
print(text_as_list)