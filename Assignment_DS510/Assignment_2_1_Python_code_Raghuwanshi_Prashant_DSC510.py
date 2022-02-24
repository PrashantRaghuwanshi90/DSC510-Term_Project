# DSC 510
# Week 2
# 2.1 Programming Assignment
# Author Prashant Raghuwanshi
# Date Created: 03-27-2021
# Program Description: 2.1 ->This Programs pickup order details from customers and generate the sales receipt for them
#============================================================================================#

from datetime import date
from random import seed, randrange

if __name__ == '__main__':
    try:
        print("\nWelcome to the Optical fiber installation order terminal")
        # user input from terminal
        customername = str(input('\nPlease enter customer Full Name :'))
        opticalfibercompanyname = str(input('\nPlease enter the required Optical Fiber Company Name :'))
        lengthoffiber = input('\nPlease enter the required length of optical cable in feats :')
        # verifying input datatype
        try:
            if isinstance(float(lengthoffiber), float):
                lengthoffiber = float(lengthoffiber)
            else:
                print('input length is not valid , please reenter the valid length in digit')
                lengthoffiber = float(input())
        except ValueError:
            print('input length is not valid , please reenter the valid length in digit')
            lengthoffiber = float(input())
        # computing cost
        actualcostperunit = 0.87
        actualcost = round(lengthoffiber * actualcostperunit, 2)
        print('\nPlease Verify below order details before generating the sales receipt')
        print(f'\nOrdered Company name of optical fiber = {opticalfibercompanyname}',
              f'\nOrdered length of optical fiber = {lengthoffiber} ft',
              f'\nActual cost per feet = ${actualcostperunit}',
              f'\nActual Order Cost = ${actualcost}')
        # Printing Receipt
        orderconfirm = str(input('\nType y to proceed with the order other wise type any key to exit :'))
        if orderconfirm == 'y' or orderconfirm == 'Y':
            print("Thank you Very Much for the order and please find below printed order receipt")
            seed(1)
            print('\n========================================================')
            print(f'*XYZ Optical Fiber Installation Company Sales Receipt  *')
            print('========================================================')
            print(f'*Order No: {randrange(1, 10)} || order date: {date.today()}\n*Customer Name: {customername} ')
            print('========================================================')
            print(f'Optical fiber company name: {opticalfibercompanyname}'  # 3.1 Programming Assignment start
                  f'\nlength of cable = {lengthoffiber} ft'
                  f'\nActual cost per feet =${actualcostperunit}/ft'
                  f'\nTotal  cost = ${actualcost}')
            print(f'*******************Total cost =${actualcost}**')
        else:
            print("Thank you for visiting to order terminal")
            exit(101)

    except ValueError:
        print("error- input data is not valid")
