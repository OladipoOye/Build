# plot showing message passing performance on BEC
import numpy as np
import matplotlib.pyplot as plt

def bec_msg_passing(erasure_prob, num_iterations, code_length):
    # Implementation of BEC message passing simulation
    pe = erasure_prob
    pe_list = [pe]
    while num_iterations > 0:
        pe = erasure_prob * (1 - (1 - pe) ** (code_length - 1))
        num_iterations -= 1
        pe_list.append(pe)
    return pe_list

erasure_prob = 0.429
num_iterations = 50
code_length = 6


pe_list = bec_msg_passing(erasure_prob, num_iterations, code_length)

plt.plot(pe_list, marker='o')
plt.ylabel('Probability of Erasure')
plt.xlabel('Iteration')
plt.title('BEC Message Passing Performance')
plt.grid()
plt.show()
# yes]