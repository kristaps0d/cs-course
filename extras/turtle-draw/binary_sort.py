import string, time

def to_number(text):
    dict = string.ascii_letters
    value = 0

    # cycle trough every letter in text
    for i in text:

        # # find number for letter from dict
        for n, j in enumerate(dict):
            if i == j:
               value += n + 1

    return value

def to_numbers(text, index=0, value=0):
    dict = string.ascii_letters

    # check if all letters have been accounted for
    if len(text) < index + 1:
        return value
        
    # cycle trough every letter from dict
    for n, i in enumerate(dict):
        if i == text[index]:
            return to_numbers(
                text, 
                index + 1, 
                value + n + 1
            )

vards = "tastur"

tim1 = time.time()
data1 = to_number(vards)
tim2 = tim1 - time.time()

tim3 = time.time()
data2 = to_numbers(vards)
tim4 = tim3 - time.time()

print("\nstandart for loop:", data1, " ", tim2)
print("function based loop:", data2, " ", tim4, "\n")