import string

# IF COUNT OF A LETTER IN THE WORD IS MORE THAN
# COUNT OF THAT LETTER IN LIST, IT WON'T BE COUNT
def count_of(word, me_list):
    for i in word:
        if word.count(i) > me_list.count(i):
            return False
    return True

#SORT WORDS DESCENDING
def Sorting(lst):
    lst2 = sorted(lst, key=len)
    return lst2

#NO UPPERCASE WORD
def no_upper_case(words, new_words):
    for word in words:
        if not word[0].isupper():
            new_words.append(word)

with open("words") as f:
    words = f.readlines()

new_words = []

no_upper_case(words, new_words)

letters = input("Enter the letters: ").split()

alph_m = list(string.ascii_lowercase)

alph = []

final_words = []

for i in alph_m:
    if i not in letters:
        alph.append(i)

for word in new_words:
    check = True
    for lt in alph:
        if lt in word:
            check = False
            break
    if (check):
        final_words.append(word)

final_words = [w.strip() for w in final_words]

final_words_2 = []

for word in final_words:
    if count_of(word, letters):
        final_words_2.append(word)

final_words_2 = Sorting(final_words_2)

our_word = final_words_2[len(final_words_2) - 1]

print("\nTHE BEST WORD: {}".format(our_word))
    
