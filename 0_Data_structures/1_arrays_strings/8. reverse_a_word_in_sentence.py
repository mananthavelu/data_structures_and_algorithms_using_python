# Given an input sentences, reverse the words in it and return

def reverse_the_words(input_sentence):
    reversed_list_of_words = []
    split_sentence = input_sentence.split(' ')
    for word in split_sentence:
        reversed_list_of_words.append(word[::-1])
    print(reversed_list_of_words)
    result= " ".join(reversed_list_of_words)
    print(result)
    return result


print ("Pass" if ('retaw' == reverse_the_words('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == reverse_the_words('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == reverse_the_words('This is one small step for ...')) else "Fail")