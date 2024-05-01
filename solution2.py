with open('input.txt', 'r', encoding='utf-8') as i:
    with open('output.txt', 'w') as o:
        for line in i:
            if line[0].upper() == 'A':
                o.write(line)
