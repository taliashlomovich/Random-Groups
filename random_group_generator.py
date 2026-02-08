import random

## Random Group Generator!

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

def cycred_word_improved(n, l):
    inverses = {}
    for i in range(1,n+1):
        elt = f"a_{i}"
        elt_inv = f"A_{i}"
        inverses[elt] = elt_inv
        inverses[elt_inv] = elt
    word = [random.choice(list(inverses.keys()))]

    while len(word) < l-1:
        fin_letter = word[-1]
        elim = inverses[fin_letter] + inverses[word[0]]
        choices = [g for g in inverses.keys() if g != elim]
        next_letter = random.choice(choices)
        word.append(next_letter)

    if len(word) == l-1:
        fin_letter = word[-1]
        init_letter = word[0]
        elim = inverses[fin_letter] + inverses[init_letter]
        choices = [g for g in inverses.keys() if g != elim]
        next_letter = random.choice(choices)
        word.append(next_letter)
    return "".join(word)

print(f"A cyclically reduced random relation of length 10, from 5 generators, is: {cycred_word_improved(5, 10)}")


# Goal 5: Produce a random presentation with n generators and k relations of length l
def generators(n):
    gens = []
    for i in range(1,n+1):
            elt = f"a_{i}"
    gens.append(elt)
    return gens


def random_pres(n,k,l):
    rels = []
    for i in range(1,k+1):
        rels.append(cycred_word_improved(n,l))
    presentation = {
        'S' : gens,
        'R' : rels
    }
    return presentation

print(f"Given n,k,l, a random group presentation is: , {random_pres(3,2,4)}")