# 1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it
NAME = "name.txt"
out_file = open(NAME, 'w')
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# 2. Write code that opens "name.txt" and reads the name (as above) then prints, "Your name is Bob"
NAME = "name.txt"
in_file = open(NAME)
text = in_file.read()
in_file.close()
print(f"your name is {text}")

# 3. Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the  result
FILENAME = "numbers.txt"
in_file = open(FILENAME)
numbers = in_file.readlines()
first_line = numbers[0].strip()
second_line = numbers[1].strip()
print(int(first_line)+int(second_line))
in_file.close()


# 4. write a fourth block of code that prints the total for all lines in numbers.txt
FILENAME = "numbers.txt"
in_file = open(FILENAME)
numbers = in_file.readlines()
total = 0
for i in numbers:
    total += int(i)
print(total)
