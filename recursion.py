def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def recusrive_Sum(numbers):
    if not numbers:
        return 0
    # print("calling sum(%s)" % numbers[1:])
    remaining_sum = recusrive_Sum(numbers[1:])
    # print("call to sum(%s) returning %d + %d" %
    # (numbers, numbers[0], remaining_sum))
    return numbers[0] + remaining_sum