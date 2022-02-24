# DSC 510
# Week 4
# 4.1 Programming Assignment
# Author Prashant Raghuwanshi
# Date Created: 04-10-2021
# Program Description: 4.1 ->This Programs pickup order details from customers
#                            and generate the sales receipt for them (use of functions)
#


from datetime import date
from random import seed, randrange


def greetings(greettype):  # function to print message in terminal
    if greettype == 1:
        print("\nWelcome to the Optical fiber installation order terminal")
    if greettype == 2:
        print("Please enter your Full Name")
    if greettype == 3:
        print("Please enter the required Optical fiber company name")
    if greettype == 4:
        print("Please enter the required length of optical cable in feets")
    if greettype == 6:
        print("\nType y to proceed with the order other wise type any key to exit")
    if greettype == 7:
        print("\nThank you Very Much for the order and please find below printed order receipt")
    if greettype == 8:
        print("Thank you for visiting to order terminal")
        exit()
    if greettype == 10:
        print("Please reenter the length of fiber in digits")


def receipt(greettype, customername, opticalfibercompanyname, lengthoffiber, perunitcost):
    if greettype == 5:
        print(f'Optical fiber company name = {opticalfibercompanyname}',
              f'\nOrdered length of optical fiber = {lengthoffiber} ft',
              f'\nActual cost per feet = ${0.87}',
              f'\nActual Order Cost = ${calculatecost(lengthoffiber, 0.87)}',
              f'\nSpecial Discount only apply if ordered fiber length is equal or greater than 100 ft'
              f'\nDiscounted cost per feet = ${perunitcost}'
              f'\nDiscounted Order Cost = ${calculatecost(lengthoffiber, perunitcost)}')
    if greettype == 9:
        seed(1)
        print('========================================================')
        print(f'*XYZ Optical Fiber Installation Company Sales Receipt  *')
        print('========================================================')
        print(f'*Order No: {randrange(1, 10)} || order date: {date.today()}\n*Customer Name: {customername} ')
        print('========================================================')
        print(f'Optical fiber company name: {opticalfibercompanyname}'
              f'\nlength of cable = {lengthoffiber} ft'
              f'\ncost per feet = ${0.87}'
              f'\nActual pOrder Cost = ${calculatecost(lengthoffiber, 0.87)}'
              f'\nDiscounted cost per feet = ${perunitcost}'
              f'\nafter Discount cost = ${calculatecost(lengthoffiber, perunitcost)}')
        print(f'*******************Total Paid Amount = ${calculatecost(lengthoffiber, perunitcost)}**')


def calculatecost(lengthoffiber, perunitcost):
    actualcost = round(lengthoffiber * perunitcost, 2)
    return actualcost


def main():
    try:
        greetings(1)
        greetings(2)
        customername = str(input())
        greetings(3)
        opticalfibercompanyname = str(input())
        greetings(4)
        lengthoffiber = input()
        try:
            if isinstance(float(lengthoffiber), float):
                lengthoffiber = float(lengthoffiber)
        except ValueError:
            print('input length is not valid , please reenter the valid length in digit')
            lengthoffiber = float(input())
        if lengthoffiber < 100:
            perunitcost = 0.87
        elif lengthoffiber >= 500:
            perunitcost = 0.50
        elif (lengthoffiber < 500) and (lengthoffiber >= 250):
            perunitcost = 0.70
        elif (lengthoffiber < 250) and (lengthoffiber >= 100):
            perunitcost = 0.80

        receipt(5, customername, opticalfibercompanyname, lengthoffiber, perunitcost)
        greetings(6)
        orderconfirm = str(input())
        if orderconfirm == 'y' or orderconfirm == 'Y':
            greetings(7)
            receipt(9, customername, opticalfibercompanyname, lengthoffiber, perunitcost)
        else:
            greetings(8)
    except ValueError:
        print("error- input data is not valid")


if __name__ == '__main__':
    main()
