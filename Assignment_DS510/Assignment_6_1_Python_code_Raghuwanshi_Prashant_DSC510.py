# DSC 510
# Week 6
# 6.1 Programming Assignment week 6
# Author Prashant Raghuwanshi
# Date Created: 04-17-2021
# Program Description: 5.1 ->This Programs will evaluate and print the largest & smallest temperature
# from multiple temperature terminal inputs  from users
# This program is using sentinel inputs to stop the terminal intake process
# also provide the no of intake temperature counts by users
#
import num2words


def greetings(greettype):  # function to print message in terminal
    if greettype == 1:
        print(f'\nWelcome to the Temperature Evaluations terminal\n',
              f'\nEnter the temperature (in Fahrenheit) of days in the digits'
              f'\n***For Terminating the Intake process, type any Alphabet to the terminal***\n')

def main():
    try:
        greetings(1)
        continueoperation = 'Y'
        loopnumber = 0
        numberlist = []
        while continueoperation == 'Y':
            loopnumber = loopnumber + 1
            numbercount = num2words.num2words(loopnumber, to='ordinal')
            inputdigit = ''
            inputdigit = input(f'Enter {numbercount} Temperature in Fahrenheit or Type any Alphabet to terminate intake:')
            if inputdigit.isupper() or inputdigit.islower():
                inputdigit = 'a'
                inputdigit = input('input temperature is not valid,please reenter the valid temperature in number \n'
                                   'or type any alphabet to terminate input process:')
                if inputdigit.isupper() or inputdigit.islower():
                    if loopnumber ==1:
                        loopnumber = 0
                    break
                else:
                    numberlist.append(float(inputdigit))
            else:
                try:
                    if isinstance(float(inputdigit), float):
                        inputdigit = float(inputdigit)
                        numberlist.append(inputdigit)
                    else:
                        inputdigit = float(
                            input('retype any Alphabet to terminate intake or '
                                  'reenter the valid temperature in number to continue:'))
                        numberlist.append(float(inputdigit))
                except ValueError:
                    print('input Number is not valid , process is terminating')
                    exit(101)
        if loopnumber > 0:
            print(f"\nMaximum temperature in the list is : {max(numberlist)} F",
                  f"\nMinimum temperature in the list is :{min(numberlist)} F",
                  f"\nNumber of Entered temperature :{num2words.num2words(len(numberlist))}",
                  f"\nPrinted all entered temperature list {numberlist}")
        else:
            print('No Input Temperature was recorded in the system')
    except ValueError:
        print("error- input data is not valid")
        exit(100)


if __name__ == '__main__':
    main()
