def find_min_impossible_sum(numbers):
    numbers.sort()
    target_sum = 1
    for number in numbers:
        if number > target_sum:
            break
        target_sum += number
    return target_sum
N = int(input())
numbers = [int(input()) for _ in range(N)]
print(find_min_impossible_sum(numbers))
