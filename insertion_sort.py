def insertionSort(Array):
    for i in range(1, len(Array)):
        key = Array[i]
        j = i - 1

        # Compare key with each element on the left of it until an element
        #  smaller than it is found
        # For descending order, change key<Array[j] to key>Array[j].
        while j >= 0 and key < Array[j]:
            Array[j + 1] = Array[j]
            j -= 1
        Array[j + 1] = key
    return Array

