import random

## Goal 1: Produce a unreduced random word of length 10, using a given generating set (2 generators)
def rand_rel(generators, length):
    rel = [random.choice(generators) for _ in range(length)]
    return "".join(rel)

# Produce a random (unreduced) relation of length 10
# Here, A=a^{-1}, B=b^{-1}
gens = ['a', 'b', 'A', 'B']
relation = rand_rel(gens, 10)

# Use f-string to print more efficiently
print(f"A random relation of length 10 is: {relation}")


## Goal 2: Same as above, but now a reduced word

def red_word(generators, length):
    # Dictionary to encode generators and their inverses
    inverses = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
    word = [random.choice(list(inverses.keys()))]
    
    while len(word) < length:
        fin_letter = word[-1]
        elim = inverses[fin_letter]
        choices = [g for g in inverses.keys() if g != elim]
        next_letter = random.choice(choices)
        word.append(next_letter)
    return "".join(word)

print(f"A reduced random relation of length 10 is: {red_word(['a', 'b'], 10)}")

## Goal 2: Same as above, but now a cyclically reduced word

def cycred_word(generators, length):
    # Dictionary to encode generators and their inverses
    inverses = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
    word = [random.choice(list(inverses.keys()))]
    
    while len(word) < length-1:
        fin_letter = word[-1]
        elim = inverses[fin_letter] + inverses[word[0]]
        choices = [g for g in inverses.keys() if g != elim]
        next_letter = random.choice(choices)
        word.append(next_letter)

    if len(word) == length-1:
        fin_letter = word[-1]
        init_letter = word[0]
        elim = inverses[fin_letter] + inverses[init_letter]
        choices = [g for g in inverses.keys() if g != elim]
        next_letter = random.choice(choices)
        word.append(next_letter)
    return "".join(word)

print(f"A cyclically reduced random relation of length 10 is: {cycred_word(['a', 'b'], 10)}")

# Goal 4: Adapt this for any number of generators (input number of generators)

# Goal 5: Produce a random presentation with n generators and k relations of length l
