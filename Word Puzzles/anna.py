words = []
file = open("words.txt", "rt")
for line in file:
    line = line.lower()
    word = ''
    isValid = True
    for character in line:
        if (character >= 'a' and character <= 'z'):
            word += character
            continue
        if character == '\n':
            continue
        isValid = False
    if isValid:
        words.append(word)

max = 0
for i in words:
   if len(i) > max:
       max = len(i)


shortToLong = []
for i in range(0, max + 1):
    shortToLong.append([])

x = 0
for word in words:
    length = len(word) 
    shortToLong[length].append(word)
    #print(word)
#find the lenght of the word
#and put the word in the appropriate shortToLong position

palindromes = []
for word in words:
    bword = None
    for c in word:
        if bword == None:
            bword = c
        else:
            bword = c + bword 
    if bword == word:
        palindromes.append(word)
#print(palindromes)

letters = input("Give a list of letters ")
length = len(letters)

posiblepalind = []
posiblewords = shortToLong[0:length + 1]
for sect in posiblewords:
    for w in sect:
        #print(w)
        if w in palindromes:
            posiblepalind.append(w)
        
#print(posiblewords) 
#print(posiblepalind)
anna = []
for i in range(length):
    for w in posiblewords[i]:
        part = letters[0:i]
        if w == part:
            #print(w)
            anna.append(w)
print(anna)