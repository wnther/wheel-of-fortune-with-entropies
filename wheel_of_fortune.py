from math import log2

LETTER_FREQUENCIES: dict = {'a': .082, 'b': .015, 'c': .028, 'd': .043, 'e': .127, 'f': .022, 'g': .020, 'h': .061, 'i': .070, 
                            'j': .002, 'k': .008, 'l': .040, 'm': .024, 'n': .067, 'o': .075, 'p': .019, 'q': .001, 'r': .060, 
                            's': .063, 't': .091, 'u': .028, 'v': .010, 'w': .023, 'x': .001, 'y': .020, 'z': .001}

def entropy(p: float) -> float:
    return p * log2(1 / p) + (1 - p) * log2(1 / (1 - p))

entropies: dict = {i: entropy(LETTER_FREQUENCIES[i]) for i in LETTER_FREQUENCIES}
sorted_entropies: dict = dict(sorted(entropies.items(), key=lambda x:x[1], reverse=True))

print(sorted_entropies)