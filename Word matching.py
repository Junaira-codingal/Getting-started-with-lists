def match_words(words):
    counter = 0
    lst = []
    
    for word in words:
        
        if len(word) > 1 and word[0] == word[-1]:
            
            counter = counter + 1
            lst.append(word)
            
    
    print("List of words with first and last charecter same\n", lst)
    return counter

li = ['abc', 'cfc','xyz','aba','1221']
count = match_words(li)
print(f"Number of words having first and last charecter same:{count}")