from day1_data import data
import heapq

left = []
right = []

# process data into pairs
def process_data():
    data_array = data.split("\n")
    for i, row in enumerate(data_array):
        pair = list(map(int, row.split("   ")))
        heapq.heappush(left, pair[0])
        heapq.heappush(right, pair[1])
    return left, right

def calculate_distance(num1, num2):
    return abs(num1 - num2)

def add_distances():
    sum = 0
    for i in range(len(left)):
        left_item = heapq.heappop(left)
        right_item = heapq.heappop(right)
        sum += calculate_distance(left_item, right_item)

    return sum

def calculate_frequency():
    freq = {}
    for i, num in enumerate(right):
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

def calculate_similarity(freq):
    similarity = 0
    for num in left:
        if num in freq:
            similarity += num * freq[num]
    return similarity

if __name__ == '__main__':
    process_data()
    # Part 1
    result = add_distances()
    print(result)
    # Part 2
    frequency = calculate_frequency()
    similarity = calculate_similarity(frequency)
    print(similarity)