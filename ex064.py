count = 0
addup = 0
while True:
    number = int(input('Insert a number [999 Stop]: '))
    if number <= 998:
        addup += number
        count += 1
    elif number == 999:
        break
    else:
        print('Invalid value')
print(f'Inserted {count} numbes and addup is {addup}')
