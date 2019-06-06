altura = float(input('Sua altura: '))
peso = float(input('Seu peso: '))
imc = peso / (altura * altura)

if imc <= 18.4:
    print(f'Seu IMC é {imc:.2f} e você está abaixo do peso.')
elif 18.5 <= imc <= 25:
    print(f'Seu IMC é {imc:.2f} e você está no peso ideal.')
elif 25.1 <= imc <= 30:
    print(f'Seu IMC é {imc:.2f} e você está com sobrepeso.')
elif 30.1 <= imc <= 40:
    print(f'Seu IMC é {imc:.2f} e você está com obesidade.')
else:
    print(f'Seu IMC é {imc:.2f} e você está com obesidade mórbida.')
