with open('input.txt', 'r', encoding='utf-8') as i:
    with open('output.txt', 'w') as o:
        for x in i:
            o.write(x.upper())
