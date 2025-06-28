fileName = input("Enter filename: ")
with open(fileName, 'r') as file:
    lines = file.readlines()

while True:
    print(f"\nFile has {len(lines)} lines.")
    num = int(input("Enter a line number (0 to quit): "))
    if num == 0:
        break
    elif 1 <= num <= len(lines):
        print(f"Line {num}: {lines[num - 1]}")
    else:
        print("Invalid line number.")
