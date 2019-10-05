alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# ask the user for a word and their chosen offset
word = input("Choose a word to decipher: ")
offset = int(input("How many letters is the cipher offset by? "))
split = list(word)
count = 0
newWord = []

# offset each letter in the word using the 'alphabet' array
for eachLetter in split:
    indexNo = alphabet.index(eachLetter)
    newIndex = indexNo - offset
    newWord.append(alphabet[newIndex])

# print each letter on a new line
wordLength = len(newWord)
for i in range(0, wordLength):
    print(newWord[i])
