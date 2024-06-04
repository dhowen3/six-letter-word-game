from string import ascii_lowercase

input_filename = input("enter name of input file: ")
f = open("six_letter_words.txt", 'w')
print("making word list...")
words = open(input_filename, 'r')
for line in words:
    new_line = line.lower()
    if len(new_line) != 7:
        continue
    all_letters = True
    for char in new_line[:-1]:
        if char not in ascii_lowercase:
            all_letters = False
            break
    if all_letters:
        f.write(new_line)
f.close()
print("done")
