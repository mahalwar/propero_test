def reverse_word(word):
    new_word=""
    for i in word:
        new_word=i+new_word
    
    return new_word

def reverse_letters(sentence):
    ans=""
    word=""
    for i in sentence:
        if i==' ':
            ans=ans+reverse_word(word)+" "
            word=""
        else:
            word=word+i

    ans=ans+reverse_word(word)
    return ans

        

sentence=input("Enter the sentence: ")
ans=reverse_letters(sentence)
print(ans)
