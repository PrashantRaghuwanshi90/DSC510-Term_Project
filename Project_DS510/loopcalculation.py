# DSC 510
# Week 5
# 5.1 Programming Assignment week 5
# Author Prashant Raghuwanshi
# Date Created: 04-17-2021
# Program Description: 5.1 ->This Programs will pickup the user selected calculation operations and accept the required
#                            data input from user and print the requested calculation operation result
#                             Additional Notes:
#                            This program will perform below mentioned calculations
#                            (addition, subtraction, multiplication, division, and average calculation)
#                            This program will contain a variety of loops and functions.
#                            The program will add, subtract, multiply, divide two numbers
#                            and provide the average of multiple numbers input by the user.
#
import num2words


def greetings(greettype):  # function to print message in terminal
    if greettype == 1:
        print('\nWelcome to the Mathematical calculation terminal\n',
              '\nPlease select the required Mathematical Operation Number from below listed',
              '\nCalculations\n',
              '1  Addition\n',
              '2  Substraction\n',
              '3  Multiplication\n',
              '4  Divison\n',
              '5  Average\n',
              'Enter the required Operation Number:'
              )


def calculationengin(operatordescription):
    inputnumber = []
    for i in range(2):
        if i == 0:
            numbercount = 'First'
            print(f"You have Selected {operatordescription} Operation\n\nPlease enter two input numbers")
        else:
            numbercount = 'Second'
        print(f'\nenter {numbercount} Number:')
        inputdigit = float(input())
        try:
            if isinstance(float(inputdigit), float):
                inputnumber.append(float(inputdigit))
            else:
                print('input Number is not valid , please reenter the valid number in digit')
                inputdigit = float(input())
                inputnumber.append(float(inputdigit))
        except ValueError:
            print('input Number is not valid , process is terminating')
            exit(101)

        if i == 0:
            print(f'We have accepted {numbercount} Input Number = {inputnumber[i]}')

        else:
            if operatordescription == 'Addition':
                calculationresult = inputnumber[i] + inputnumber[0]
                print(f'accepted {numbercount} Input Number = {inputnumber[i]}\n',
                      f'\nTotal {operatordescription} result = {calculationresult}\n')
            elif operatordescription == 'Subtraction':
                calculationresult = inputnumber[i] - inputnumber[0]
                print(f'accepted {numbercount} Input Number = {inputnumber[i]}\n',
                      f'\n{operatordescription} result = {calculationresult}\n')
            elif operatordescription == 'Multiplication':
                calculationresult = inputnumber[i] * inputnumber[0]
                print(f'accepted {numbercount} Input Number = {inputnumber[i]}\n',
                      f'\n{operatordescription} result = {calculationresult}\n')
            elif operatordescription == 'Division':
                calculationresult = inputnumber[i] / inputnumber[0]
                print(f'accepted {numbercount} Input Number = {inputnumber[i]}\n',
                      f'\n{operatordescription} result = {calculationresult}\n')


def performcalculation(selectedoperation):
    if selectedoperation == 1:
        operatordescription = 'Addition'
        calculationengin(operatordescription)
    elif selectedoperation == 2:
        print("You have Selected Subtraction Operation , Please enter the count of numbers")
        operatordescription = 'Subtraction'
        calculationengin(operatordescription)
    if selectedoperation == 3:
        print("You have Selected Multiplication Operation , Please enter the count of numbers")
        operatordescription = 'Multiplication'
        calculationengin(operatordescription)
    if selectedoperation == 4:
        print("You have Selected Division Operation , Please enter the count of numbers")
        operatordescription = 'Division'
        calculationengin(operatordescription)
    if selectedoperation == 5:
        print(f"You have Selected Average Operation, Please enter count of numbers you wish to enter")
        operatordescription = 'Average'
        calculateaverage(operatordescription)


def calculateaverage(operatordescription):
    i = 1
    calculationresult = 0
    numberlist = []
    n = input('Enter number counts: ')
    print(f'\nNow enter {num2words.num2words(n)} numbers to calculate Total Average\n')
    while i <= int(n):
        numbercount = num2words.num2words(i, to='ordinal')
        inputdigit = input(f'enter {numbercount} Number:')
        try:
            if isinstance(float(inputdigit), float):
                inputdigit = float(inputdigit)
                numberlist.append(inputdigit)
            else:
                print('input Number is not valid , please reenter the valid number in digit')
                inputdigit = float(input())
                numberlist.append(float(inputdigit))
        except ValueError:
            print('input Number is not valid , process is terminating')
            exit(102)
        j = 0
        calculationresult = 0
        for j in range(0, len(numberlist)):
            calculationresult = calculationresult + numberlist[j]

        runningaverage = calculationresult / i
        print(f'Entered {numbercount} Input Number = {numberlist[i - 1]}',
              f"\nComputed Running Sum for {num2words.num2words(i, to='ordinal')} input = {calculationresult}",
              f"\nComputed Running {operatordescription} for {num2words.num2words(i, to='ordinal')} input = {runningaverage}")
        if int(i) == int(n):
            print('\n=======================================')
            print(f'Input Number list {numberlist}')
            print('=======================================')
            print(f'Computed final {operatordescription} of input number list = {runningaverage}')
            print('=======================================')
        i = i + 1


def selectoperation():
    greetings(1)
    requestedoperation = input()
    selectedoperation = 0
    if isinstance(int(requestedoperation), int):
        selectedoperation = int(requestedoperation)
        if selectedoperation < 1 and selectedoperation < 5:
            print('Enter Valid requested operation Number (in-between 1 to 5)')
            try:
                if isinstance(int(requestedoperation), int):
                    selectedoperation = int(requestedoperation)
                    performcalculation(selectedoperation)
            except ValueError:
                print("Invalid Operation selection Error")
        else:
            performcalculation(selectedoperation)
    else:
        print('Enter Valid requested operation Number (in-between 1 to 5)')
        selectedoperation = int(input())
        if selectedoperation < 1 and selectedoperation < 5:
            raise ValueError
        else:
            if isinstance(int(requestedoperation), int):
                selectedoperation = int(requestedoperation)
                performcalculation(selectedoperation)
            else:
                raise ValueError


def main():
    try:
        selectoperation()
        print('Enter Y if you want to request next Mathematical Operation else press any key exit')
        continueoperation = input()
        while continueoperation == 'Y' or continueoperation == 'y':
            selectoperation()
            print('Enter Y if you want to request next Mathematical Operation else press any key exit')
            continueoperation = input()

    except ValueError:
        print("error- input data is not valid")


if __name__ == '__main__':
    main()
