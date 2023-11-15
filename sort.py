
def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: avg O(n+k) worst O(n^2) Why and under what conditions?
    TODO: Memory usage: O(n+k) Why and under what conditions?
    creating a new output list and a list of counts k is the size of the counts list"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

    output = []

    low = min(numbers)
    high = max(numbers)


    counts = []
    for i in range(low, high + 1):
      counts.append(0)
    for i in range(len(numbers)):
      counts[numbers[i] - low] += 1
    
    for i in range(len(counts)):
      for j in range(counts[i]):
        output.append(i + low)

    return output



def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: O(n^2)worst  avg O(n+k) Why and under what conditions?
    TODO: Memory usage: O(n+k) Why and under what conditions?
    k is the size of the buckets list"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    output = []

    low = min(numbers)
    high = max(numbers)

    buckets = []

    for i in range(10):
        buckets.append([])

    for i in range(len(numbers)):
      bucket = numbers[i] % 10 - 1
      if bucket == -1:
        bucket = 9
      buckets[bucket].append(numbers[i])

    
    for i in range(len(buckets)):
        sorted_bucket = buckets[i]
       
        output = output + sorted_bucket

    return output
    
# print(counting_sort([4, 7, 3, 4, 2]))
print(bucket_sort([4, 7, 3, 4, 2, -10]))