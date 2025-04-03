# Define the model parameters at the top, like setting up the problem on paper
H = {'A': 0.2, 'C': 0.3, 'G': 0.3, 'T': 0.2}  # Emission probabilities for state H
L = {'A': 0.3, 'C': 0.2, 'G': 0.2, 'T': 0.3}  # Emission probabilities for state L
trProb = {  # Transition probabilities between states
    ('S', 'H'): 0.5, ('S', 'L'): 0.5, 
    ('H', 'H'): 0.5, ('L', 'L'): 0.6, 
    ('L', 'H'): 0.4, ('H', 'L'): 0.5
}

# Viterbi parameters (log probabilities)
emission_probs = {"H": {"A": -2.322, "C": -1.737, "G": -1.737, "T": -2.322}, 
                  "L": {"A": -1.737, "C": -2.322, "G": -2.322, "T": -1.737}}
transition_probs = {"H": {"H": -1, "L": -1}, "L": {"H": -1.322, "L": -0.737}}
states = ["H", "L"]
start_probs = {"H": -1, "L": -1}

# Step 1: Forward Algorithm - Compute probability of observing the sequence
def forward_algorithm(sequence, H, L, trProb):
    P = []  # Probability table to store results for each position
    
    for i in sequence:
        if len(P) == 0:  # Initial step: From start state S to H or L
            p = [trProb[('S', 'H')] * H[i], trProb[('S', 'L')] * L[i]]
        else:  # Subsequent steps: Combine previous probs with transitions
            p = []
            # H: Probability from H->H and L->H
            p.append(P[-1][0] * trProb[('H', 'H')] * H[i] + P[-1][1] * trProb[('L', 'H')] * H[i])
            # L: Probability from L->L and H->L
            p.append(P[-1][1] * trProb[('L', 'L')] * L[i] + P[-1][0] * trProb[('H', 'L')] * L[i])
        P.append(p)
    
    return P

# Step 2: Initialize Viterbi - Set up the first column of the table
def initialize_viterbi(sequence, start_probs, emission_probs):
    vit_res = {}
    # First position: Start prob + emission prob for the first character
    v_init_H = start_probs["H"] + emission_probs["H"][sequence[0]]
    v_init_L = start_probs["L"] + emission_probs["L"][sequence[0]]
    vit_res[0] = {"H": v_init_H, "L": v_init_L}
    return vit_res

# Step 3: Fill Viterbi Table - Compute probabilities for each position
def fill_viterbi_table(sequence, vit_res, states, emission_probs, transition_probs):
    # Pre-allocate the dictionary for all positions
    for i in range(1, len(sequence)):
        vit_res[i] = {state: 0 for state in states}
    
    # Fill the table, position by position
    for i in range(1, len(sequence)):
        for j in range(len(states)):
            # Emission probability for current state and character
            term1 = emission_probs[states[j]][sequence[i]]
            # Find max probability from previous states
            prev_probs = [vit_res[i-1][states[k]] + transition_probs[states[k]][states[j]] 
                           for k in range(len(states))]
            maximum = max(prev_probs)
            # Final probability for this state at this position
            vit_res[i][states[j]] = round(term1 + maximum, 6)
    
    return vit_res

# Step 4: Extract Results - Separate H and L probabilities for display
def extract_probabilities(vit_res):
    h_lis, l_lis = [], []
    for key in vit_res:
        h_lis.append(vit_res[key]["H"])
        l_lis.append(vit_res[key]["L"])
    return h_lis, l_lis

# Step 5: Display Results - Print the table and path
def display_results(sequence, h_lis, l_lis):
    # Print header with sequence characters
    print("States", end="\t\t")
    for char in sequence:
        print(char, end="\t\t")
    print("\n")
    
    # Print H probabilities
    print("H", end="\t\t")
    for h in h_lis:
        print(h, end="\t\t")
    print("\n\n")
    
    # Print L probabilities
    print("L", end="\t\t")
    for l in l_lis:
        print(l, end="\t\t")
    print("\n")

# Step 6: Trace Path - Determine the most likely state sequence
def trace_path(h_lis, l_lis):
    max_path = []
    for i in range(len(h_lis)):
        max_path.append('H' if h_lis[i] > l_lis[i] else 'L')
    return max_path

# Main execution flow - Solving the problem step-by-step
def main():
    # Forward Algorithm for "GGCA"
    seq = "GGCA"
    P = forward_algorithm(seq, H, L, trProb)
    print("Forward Algorithm Results:")
    print("Probability table:", P)
    print("Total probability:", P[-1][0] + P[-1][1])
    print("\n")

    # Viterbi Algorithm for "GGCACTGAA"
    input_str = "GGCACTGAA"
    
    # Step-by-step Viterbi calculation
    vit_res = initialize_viterbi(input_str, start_probs, emission_probs)
    vit_res = fill_viterbi_table(input_str, vit_res, states, emission_probs, transition_probs)
    h_lis, l_lis = extract_probabilities(vit_res)
    
    # Display results
    print("Viterbi Algorithm Results:")
    display_results(input_str, h_lis, l_lis)
    
    # Trace and print the path
    max_path = trace_path(h_lis, l_lis)
    print("PATH SEQUENCE")
    print(max_path)

# Run the program
if __name__ == "__main__":
    main()