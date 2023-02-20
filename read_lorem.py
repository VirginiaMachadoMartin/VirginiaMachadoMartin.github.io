#read the lorem.txt file and count characters in text
#send in file
text = open('lorem.txt', 'r')

text_read = text.read()
#file to str

text_as_list = list()

#print(text_as_list)

#for loop over str

for char in text_read:
   c = text_read.count(char)
    
   if text_as_list.count(char) == 0: 
    text_as_list.append(char)
    text_as_list.append(c)
       #text_as_list[char] +=1
   #else: 
       #text_as_list[char] = 1
    #   pass

print(text_as_list)
#current count = (chart + " " + str((text.count(char))))