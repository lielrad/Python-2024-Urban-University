def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if root_word.casefold() in other_words[i].casefold() or other_words[i].casefold() in root_word.casefold():
            same_words.append(other_words[i])
    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))