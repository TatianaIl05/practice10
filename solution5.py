with open('input.txt', 'r', encoding='utf-8') as i:
    with open('output.txt', 'w') as o:
        try:
            number1 = int(i.readline())
            number2 = int(i.readline())
            number3 = int(i.readline())
            o.write(str(number1 / number2 + number3))
        except ValueError:
            o.write('data error')
        except ZeroDivisionError:
            o.write('division by 0')
