data = ''
with open('data.txt', 'r') as f:
    data = f.read()

histories = data.split('\n')
num_histories = []

for history in histories:
    int_array = [int(x) for x in history.split(' ')]
    num_histories.append(int_array)

# to check if all elements in an array is 0
def if_all_zero(arr):
    return all([x == 0 for x in arr])

def recursive_func(arr, sum):
    if if_all_zero(arr):
        return arr[len(arr) - 1]
    else:
        new_arr = []
        for i in range(len(arr) - 1):
            difference = arr[i + 1] - arr[i]
            new_arr.append(difference)
        
        # storing the extrapolated value
        sum = arr[len(arr) - 1] + recursive_func(new_arr, sum)
        return sum
    
sum_of_extrapolated_value = 0
for history in num_histories:
    sum_of_extrapolated_value += recursive_func(history, 0)

print(f"P1: {sum_of_extrapolated_value}")