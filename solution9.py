from os import mkdir
mkdir('simple')
with open('input.txt', 'r', encoding='utf-8') as i:
    with open(r'simple\output.txt', 'w') as o:
        count = 1
        for line in i:
            if count % 2 == 0:
                o.write(line)
                print(line)
            count += 1
