vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

vowel_count = consonant_count = space_count = other_count = 0

s = input("Enter a string: ")

for char in s:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1
    elif char == " ":
        space_count += 1
    else:
        other_count += 1

print("Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
print(f"Spaces: {space_count}")
print(f"Other Characters: {other_count}")


