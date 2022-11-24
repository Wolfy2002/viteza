# Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total
# number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”


def permis(viteza):
    puncte = 0
    if viteza <= 70:
        print('Este ok!')
    elif viteza > 70:
        exces = viteza - 70
        for number in range(1, exces + 1):
            if number % 5 == 0:
                puncte += 1
        print(f'Ai {puncte} puncte!')
        if puncte > 12:
            print('Permis suspendat!')


viteza = int(input('Viteza ta: '))
permis(viteza)
