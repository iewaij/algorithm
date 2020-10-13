def palindrome_2(word2):
    for i in range(0,len(word2)):
        for j in range(1,len(word2)+1):
            word_subset = word2[i:j]
            inverse2 = word_subset[::-1]
            if word_subset == inverse2:
                if len(word_subset)>1:
                    print(word_subset, "is palindrome")

palindrome_2("int​elle​ct")
