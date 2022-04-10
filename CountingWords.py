from xml.dom.minidom import CharacterData


intro=input("Enter your introduction: ")
wordCount=1
characterCount=0
for i in intro:
    characterCount=characterCount+1
    if(i==" "):
        wordCount=wordCount+1
print("Number of words in the string are:")
print(wordCount)
print("Number of characters in the string are:")
print(characterCount)