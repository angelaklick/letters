string = input('Enter a word: ')


def vowel(string):
    vowel = "aeiouy"
    number = 0
    for i in (string):
        idx = vowel.find(i)
        if(idx > -1):
            number = number + 1
        
    return number

def consonant(string):
    consonant = "cdfghjklmnpqrstvwxz"
    number = 0
    for i in (string):
        idx = consonant.find(i)
        if(idx > -1):
            number = number + 1
    
    return number

number = vowel(string)
print("The number on vowels are: ", number)


number = consonant(string)
print("The number of consonants are: ", number)



