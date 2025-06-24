import random

def cards():
    card_suits = ["spade", "club","diamond", "heart"]
    card_deck = ["ace"] + [str(i) for i in range(2, 11)] + ["jack","queen","king"]
    cards_array = [f"{deck}_{suits}" for deck in card_deck for suits in card_suits]
    random.shuffle(cards_array)
    return cards_array

initial_state = cards()

def split():
    x = random.randrange(1, 53)
    subdeck_A = [i for i in initial_state[:x]]
    subdeck_B = [j for j in initial_state[x:]]
    return subdeck_A, subdeck_B


def shuffled_cards(): 
    subdeck_A_shuff, subdeck_B_shuff = split()
    random.shuffle(subdeck_A_shuff)
    random.shuffle(subdeck_B_shuff)
    shuff = subdeck_A_shuff+subdeck_B_shuff
    return shuff

final_state = shuffled_cards()

print(f"initial state: \n{initial_state}\n")
print(f"final state: \n{final_state}")

def cards_shuff_map(): 
    mapping = {}
    for i in initial_state:
        mapping[initial_state.index(i)] = final_state.index(i) 
    return mapping
    
print(cards_shuff_map())