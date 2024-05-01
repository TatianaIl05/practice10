with open('input.txt', 'r', encoding='utf-8') as i:
    with open('output.txt', 'w') as o:
        n = i.readline().strip()
        if n.isdigit():
            count = 0
            for line in i:
                count += 1
            if count == int(n):
                o.write('YES')
            else:
                o.write('NO')
        else:
            o.write('ERROR')
