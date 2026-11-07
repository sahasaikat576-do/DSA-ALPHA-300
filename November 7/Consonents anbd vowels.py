def count_vowels_consonants(s):

    vowels = 0
    consonants = 0

    for ch in s:

        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):

            ch = ch.lower()

            if ch in "aeiou":
                vowels += 1

            else:
                consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)


s = "Hello World"
count_vowels_consonants(s)
