firstValue = int(input('Frist value: '))
secondValue = int(input('Second Value: '))
while True:
    while True:
        print('''
        [1] Add Up
        [2] Multiply
        [3] Bigger
        [4] New values
        [5] Exit
            ''')
        option = int(input('Select option: '))
        if option == 1:
            addup = firstValue + secondValue
            print(f'Add Up: {firstValue} + {secondValue} = {addup}')
        if option == 2:
            multiply = firstValue * secondValue
            print(f'Multiply: {firstValue} x {secondValue} = {multiply}')
        if option == 3:
            if firstValue > secondValue:
                print(f'The biggest number is: {firstValue}')
            else:
                print(f'The biggest number is: {secondValue} ')
        if option == 4:
            firstValue = int(input('First value: '))
            secondValue = int(input('Second value: '))
        if option == 5:
            break
    break
print('Program closed!!!')
