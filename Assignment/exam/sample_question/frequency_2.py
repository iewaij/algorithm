def wordfrequency(sentence):
    word_list2 = sentence
    for i in word_list2:
        if i not in word_list2:
            word_list2.append(i)
    for k in word_list2:
        print("frequency for {} is {}".format(k,word_list2.count(k)))
