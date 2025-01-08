input_string = input("Enter a string: ")

vowels = 'aeiouAEIOU'
vowel_count = 0
modified_string = ''

for char in input_string:
    if char in vowels:
        vowel_count += 1
        modified_string += '#'
    else:
        modified_string += char

print(f"Number of vowels in the given string: {vowel_count}")
print(f"String after replacing vowels with '#': {modified_string}")
