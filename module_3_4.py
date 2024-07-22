#def single_root_words(root_word, *other_words):
def single_root_words(root_word,other_words):
    same_words = []
    for i in range(len(other_words)):
        #if root_word.lower() == other_words[i]:
        if (root_word.lower() in other_words[i] != True):
            same_words.append(other_words[i])

    return  print(same_words)


single_root_words("rich", ["pich", "richiest", 'orichalcum', 'cheers', 'richies'])