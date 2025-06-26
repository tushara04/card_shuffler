import random

def given_cards():

    card_suits = ["spade", "club","diamond", "heart"]
    card_deck = ["ace"] + [str(i) for i in range(2, 11)] + ["jack","queen","king"]
    cards_array = [f"{deck}_{suits}" for deck in card_deck for suits in card_suits]
    #random.shuffle(cards_array)
    
    return cards_array

initial_state = given_cards()

print(f"initial state:\n{initial_state}\n")

def desired_shuffle(): 
    
    shuff = given_cards()
    random.shuffle(shuff)
    
    return shuff

desired_final_state = desired_shuffle()

def cards_shuff_map():
    # this function tells what card (value) comes to the position (key); e.g. {0:2}. So, the third card in initial state comes to the first position in the desired final state
    
    mapping = {}
    for i in range(len(desired_final_state)):
        card = desired_final_state[i]
        target_position = initial_state.index(card)
        mapping[i] = target_position
    
    return mapping

mapped = cards_shuff_map()

def process():
    
    initial_arrangement = [i for i in range(0, 52)]
    
    desired_arrangement = []
    for i in range(0,52):
        desired_arrangement += [new for old, new in mapped.items() if old == i]

    storage = []
    final_arrangement = []

    initial_arrangement_as_source = True

    while len(final_arrangement) < 52:

        target = desired_arrangement[len(final_arrangement)]

        if initial_arrangement_as_source:
            source = initial_arrangement
            temp = storage
        else: 
            source = storage
            temp = initial_arrangement
        
        while source and source[0] != target:
            moved = source.pop(0)
            temp.append(moved)
        
        if source and source[0] == target: 
            found = source.pop(0)
            final_arrangement.append(found)

        while source: 
            moved = source.pop(0)
            temp.append(moved)
        
        initial_arrangement_as_source = not initial_arrangement_as_source

    return final_arrangement
    

shuffling = process()


def shuffled_cards(): 
 
    final_state = []
    for i in shuffling:
        final_state.append(initial_state[i])
        
    return final_state


print(f"final state:\n{shuffled_cards()}")

