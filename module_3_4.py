# Задача "Однокоренные"

def single_root_words(root_word, *other_words):
    same_words=[]
    for i in range(len(other_words)):
        word_tmp = str(other_words[i])
        if (root_word.upper() in word_tmp.upper()) or (word_tmp.upper() in root_word.upper()):
             same_words.append(other_words[i])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

