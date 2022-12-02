# Simple Law of Large Numbers Demo by Sean Lewis
# Uses Numpy and Matplotlib

import numpy as np
import matplotlib.pyplot as plt

# We take in the csv file and return the total number of successes, failures, total deals, and the average probability of success for the csv file
def deal_data(csv_file):
    with open(csv_file, 'r') as f:
        data = f.readlines()[1:]
        data = [line.strip().split(',') for line in data]
        data = np.array(data, dtype=int)
        total_success = np.sum(data[:,0])
        total_failure = np.sum(data[:,1])
        total_deals = total_success + total_failure
        prob_success = total_success / total_deals

    return [total_success, total_failure, total_deals, prob_success]

# Deal Data CSV file names
s1 = 'S1deals.csv'
s123 = 'S1toS3deals.csv'
s123456 = 'deals.csv'

print(deal_data(s1))
print(deal_data(s123))
print(deal_data(s123456))

# We take in the csv line (example: 2,2) and return simple success failure array ([1,1,0,0])
def get_array(line):
    line = line.split(',')
    line = [int(i) for i in line]
    array = []
    for i in range(line[0]):
        array.append(1)
    for i in range(line[1]):
        array.append(0)
    return array

# We take in the csv file and return array of simple success failure arrays
def get_arrays(csv_file):
    with open(csv_file, 'r') as f:
        data = f.readlines()[1:]
        data = [line.strip() for line in data]
        data = [get_array(line) for line in data]
        return data

# We take in array of arrays and return the array of the average probability of success at each deal
def get_avg_prob(arrays):
    avg_prob = []
    prev_prob = -1
    items = 0
    for array in arrays:
        for item in array:
            items += 1
            if item == 1:
                prev_prob = (prev_prob * (items - 1) + 1) / items
            else:
                prev_prob = (prev_prob * (items - 1)) / items
            avg_prob.append(prev_prob)
    #print(avg_prob)
    return avg_prob
    
arrays = get_arrays('deals.csv')
avg_prob = get_avg_prob(arrays)

#Showing 0.0 to 1.0 on y-axis
plt.ylim(0,1)

plt.xlabel('Number of Deals')
plt.ylabel('Average Probability of Success')
plt.title('Average Probability of Success Over All Previous Deals')

# Plotting the line graph
plt.plot(avg_prob)
plt.show()