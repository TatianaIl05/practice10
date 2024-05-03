days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open('input.txt', 'r', encoding='utf-8') as i:
    current_date = i.readline()
    current_day, current_month = int(current_date[:2]), int(current_date[3:])
    n = i.readline()
    lines = i.readlines()
    for line in lines:
        line = line[:-1]
        cell_day = int(line[len(line) - 5:len(line) - 3])
        cell_month = int(line[len(line) - 2:])

        with open('output.txt', 'a') as o:
            match cell_month - current_month:
                case 0:
                    if abs(current_day - cell_day) > 3:
                        o.write(line[:len(line) - 6] + '\n')
                case 1:
                    if cell_day + days[current_month - 1] - current_day > 3:
                        o.write(line[:len(line) - 6] + '\n')
                case -1:
                    if current_day + days[cell_month - 1] - cell_day > 3:
                        o.write(line[:len(line) - 6] + '\n')

'''
                case 11:
                    if current_day + days[cell_month - 1] - cell_day > 3:
                        o.write(line[:len(line) - 6] + '\n')
                case -11:
                    if cell_day + days[current_month - 1] - current_day > 3:
                        o.write(line[:len(line) - 6] + '\n')
                    
'''
