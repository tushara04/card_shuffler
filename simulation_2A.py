import random

def given_cards():
    card_suits = ["spade", "club","diamond", "heart"]
    card_deck = ["ace"] + [str(i) for i in range(2, 11)] + ["jack","queen","king"]
    cards_array = [f"{deck}_{suits}" for deck in card_deck for suits in card_suits]
    #random.shuffle(cards_array)
    return cards_array

initial_state = given_cards()

def shuffled_cards(): 
    shuff = given_cards()
    random.shuffle(shuff)
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