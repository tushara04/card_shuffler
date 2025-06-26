## Card Shuffler: a visual array manipulation

### Design
1. Initial State Bin: this contains the cards in a certain state the user puts it in. 
2. Storage Bin: this temporarily stores the cards for the desired card to be moved at the bottom for it to be extracted.
3. Final State Bin: this contains the cards in a desired randomized state

### Simulation
The algorithm, as in *simulation_2Aa.py*, assumes a certain state of the cards as put by the user in initial_state bin. Using the random library, it comes up with a random state for the cards to be in. Then, a process is carried out that arranges the cards from the initial state to the final state.

### Process
1. The user puts cards into initial_state bin.
2. The algorithm generates a desired_final_state for the cards to be in: {0:3, 1:2, 2:4, 3:0, 4:2}. The [3] card in the initial_state is supposed to be in the 0th card's place in the final state. And so on.
3. A fork moves the cards [0,1,2] from initial_state bin to storage.
4. The fork moves the card [3] from initial_state bin to final_state bin.
5. Another fork now moves the remaining cards in initial_state [4] to storage [0,1,2,4].
6. The storage now acts as a source. The [2] card in the storage is to be moved to 1st card's place in the final_state. T
7. The fork moves [0,1] from storage to initial_state bin.
8. The fork moves the [2] from storage to the final_state.
9. The storage is left with [4]. So, the fork moves [4] to initial_state bin [0,1,4].
10. The process continues until storage and initial_state bins are empty.
11. The final_state bin now has the cards in the desired_final_state. 

### Comments
1. We could have sensors to check if there are cards left in the storage or initial_state bins.
