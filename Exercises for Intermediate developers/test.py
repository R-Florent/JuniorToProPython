def reverse_world(Sentence):
    list_sentence = Sentence.split()

    list_sentence_reversed =  [i[::-1] for i in list_sentence]

    res_str = " ".join(list_sentence_reversed)

    return res_str

str = "My Name is Jessa"
print(reverse_world(str))
