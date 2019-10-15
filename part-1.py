import random
def part1(x):
  vowels = int(x)
  consonants = 9-int(x)
  character = 0
  word = []
  for i in range(vowels):
    character = random.choice(['a','e','i','o','u',])
    word.append(character)
  for i in range(consonants):
    character = random.choice(['b', 'c', 'd','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'])
    word.append(character)
  print(word)
part1(6)
