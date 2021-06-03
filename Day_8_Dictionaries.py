n = int(input())

phoneBook = {}
for i in range(n):
    values = input().split()
    phoneBook[values[0]] = values[1]
answers = []
while True:
    try:
        values = input()
        if values in phoneBook:
            answers.append(f"{values}={phoneBook[values]}")
        else:
            answers.append("Not found")
    except EOFError:
        break

for i in answers:
    print(i)
