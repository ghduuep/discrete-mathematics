from itertools import permutations
from collections import defaultdict
from math import factorial

def how_many_permutations(text: str) -> int:
    letters = defaultdict()
    for letter in text:
        letters[letter] += 1
    numerator = factorial(len(text))
    factors = [factorial(count) for count in letters.values()]
    denominator = 1
    for factor in factors:
        denominator *= factor

    return numerator // denominator
    
print(how_many_permutations("paralelepipedo"))

