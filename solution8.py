days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open('input.txt', 'r', encoding='utf-8') as i:
    lines_str = i.readlines()
    lines_int = [int(line.strip()) for line in lines_str]
    if len(lines_str) == 366:
        days[1] = 29
with open('output.txt', 'w') as o:
    for item in days:
        o.write(str(sum(lines_int[:item]) / item) + '\n')
        lines_int = lines_int[item:]
        