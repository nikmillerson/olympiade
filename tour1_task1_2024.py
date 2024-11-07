import time
letter = input()
text = input()
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def right_iteration(begin_letter, target_letter):
    right_counter = 0
    if begin_letter == target_letter:
        return right_counter
    current_letter = begin_letter
    letter_index = index_getter(current_letter)
    while current_letter != target_letter:
        if (letter_index + right_counter) != 25:
            right_counter += 1
            current_letter = alphabet[letter_index + right_counter]
        else:
            right_counter += 1
            current_letter = alphabet[letter_index + right_counter - 26]
    return right_counter

def index_getter(some_letter):
    for x in range(len(alphabet)):
        if alphabet[x] == some_letter:
            some_letter_index = x
    return some_letter_index


curr_letter = letter
for i in range(len(text)):
    if right_iteration(curr_letter, text[i]) == 0:
        print('P')
    elif right_iteration(curr_letter, text[i]) <= 13:
        counter = right_iteration(curr_letter, text[i])
        curr_letter = text[i]
        print(f"R{counter}")
        print('P')
    elif right_iteration(curr_letter, text[i]) > 13:
        counter = 26 - right_iteration(curr_letter, text[i])
        curr_letter = text[i]
        print(f"L{counter}")
        print("P")

print(time.process_time())