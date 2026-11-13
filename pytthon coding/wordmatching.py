def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr +=1
            lst.append(word)
    print("list of words with same first and last charecter name\n",lst)
    return ctr
count=match_words(["abc","cbc","xyz","aba","edamame","5005","hoszbb"])
print("number of words having same first and last letter name:",count)