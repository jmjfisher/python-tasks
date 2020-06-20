from nltk.corpus import words
import itertools

zero = ['O']
two = ['A','B','C']
four = ['G','H','I']
five = ['J','K','L']
six = ['M','N','O']
seven = ['P','Q','R','S']
nine = ['W','X','Y','Z']

english_string = []
not_english_string = []

full_number = [six,four,six,four,five,zero,nine,four,seven,two]
size = 10

def get_all_substrings(string):
    
    length = len(string) + 1
    full_list = [string[x:y] for x, y in itertools.combinations(range(length), r=2)]
    
    for i in full_list:
        if len(i)==1:
            full_list.remove(i)
    return full_list

while len(full_number)>=4:

    gross_list = list(itertools.product(*full_number))
    words_list = []
    
    for i in gross_list:
        
        word = ''
        for letter in i:
            word += letter
        words_list.append(word)

    file_name = 'list_'+str(size)+'.txt'
    with open(file_name, 'w') as file:
        
        for word in words_list:
            if word.lower() in words.words():
                file.write(word+', true\n')
            else:
                check_list = get_all_substrings(word)
                real_words = []
                for i in check_list:
                    if i not in not_english_string:
                        if i in english_string:
                            real_words.append(i)
                        elif i.lower() in words.words():
                            english_string.append(i)
                            real_words.append(i)
                        else:
                            not_english_string.append(i)
                if len(real_words) == 0:
                    file.write(word+', false\n')
                else:
                    file.write(word+', true, '+str(real_words)+'\n')

    file.close()
    print(size)
    full_number.pop(0)
    size-=1
