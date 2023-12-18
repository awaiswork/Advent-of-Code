def calculateHash(step):
    current_value = 0
    for char in step:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    
    return current_value


with open('data.txt', 'r') as f:
    data = f.read()
    steps = data.split(',')

    sum_of_hashes = 0
    for step in steps:
        hashValue = calculateHash(step)
        sum_of_hashes += hashValue
    
    print(sum_of_hashes)