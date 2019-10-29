import enchant

def check_word(astring)

    dictionary = enchant.Dict("en_US")

    dictionary.check(astring)
