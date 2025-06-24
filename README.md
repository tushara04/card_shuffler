# Card Shuffler Design 1
(not the one with the forks and compartments)

## Simulation 1

### Design
Simulation 1 was planned such that there is no mapping as done in Simulation 2 happens. There it's just either A or B subdeck randomly opening and putting cards into the final_state. E.g. AABAAABBABABBAAAAB... 52 times. So, A opens, a card falls into final_state. A opens, another card falls into final_state. B opens. A opens thrice. And so on. 

This is done over multiple iterations wherein the cards from the final_state after the first iteration is transferred into the initial_state for the second iteration. It is to be tested in this simulation whether carrying out multiple iterations improves the randomness score.

Here the splitting of cards into the two subdecks is essential to the design.

## Simulation 2A

### Design
There is a container *initial_state* with cards put by the user in some random state. Then a process is carried to shuffle the initial_state into a final_state.

### Process
We start with an initial_state. The algorithm generates a final_state. The objective of the process is for the cards to reach from the given initial_state to the generated final_state.

Say, the mapping b/w the initial_state and the final_state is as such: {0:4, 1:3, 2:1, 3:0, 4:2}. This means the 1st card in the initial_state is the 5th card in the final_state. 2nd card is 4th. 3rd is 2nd. 4th is 1st. And, 5th is 3rd.

1. find key for which the value = 0. this means the 4th card in the initial_state has to be chosen first.
2. put initial_state[0,1,2] in storage.
3. put initial_state[3] into final_state.
4. once done, check if storage == empty.
5. if not, empty the storage by putting the cards from storage into initial_state.
6. if storage == empty is true, then find key for which the value = 1.
7. run the entire process as earlier until initial_state == empty.

## Simulation 2B

### Design
In this design, just to add an an extra level of randomization, we split the initial_state into two subdecks A and B. The number of cards in each subdeck is random.

Either the user puts the cards randomly into the two subdecks or the design is such that the user places all the cards into initials_state and they get split into the two subdecks randomly.

## Comments
1. There is no need for the initial_state to be split into two subdecks. It is being done only to add a level of randomization.
2. This is Simulation 2A where there is splitting taking place. In Simulation 2B, there is no splitting of the initial_state.
3. There can be a sensor used in vending machines that determines whether a card was successfully moved.

## Notes
1. Randomness score: initial_state vs final_state -- determine how randomly and well shuffled the cards are. Some algorithm has to be figured out for this.