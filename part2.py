import enchant

def check_word(astring)

    dictionary = enchant.Dict("en_US")

    dictionary.check(astring)
    
#source of import https://stackoverflow.com/questions/3788870/how-to-check-if-a-word-is-an-english-word-with-python
