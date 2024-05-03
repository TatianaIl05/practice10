with open('input.txt', 'r', encoding='utf-8') as i:
    lines = i.readlines()

with open('input.txt', 'w', encoding='utf-8') as i:
    for line in lines:
        if int(line) != 100:
            i.write(line)
