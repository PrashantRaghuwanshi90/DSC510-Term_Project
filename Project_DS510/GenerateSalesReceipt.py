# DSC 510
# Week 2
# 2.1 Programming Assignment
# Author Prashant Raghuwanshi
# Date Created: 03-27-2021
# Program Description: 2.1 ->This Programs pickup order details from customers and generate the sales receipt for them
#============================================================================================
# Change Log :3.1 Programming Assignment
# Change(s) Made: Added logic to evaluate bulk discount
# Date of Change: 04/01/2021
# Author: Prashant Raghuwanshi
# Change Approved by: Catie Williams
# Date Moved to Production: 04/01/2021
#=============================================================================================


from datetime import date
from random import seed, randrange
import strip as strip


class GenerateSalesReceipt:

    def __init__(self, opticalfibercompanyname=False, lengthoffiber=False, customername=False):
        self.opticalfibercompanyname = opticalfibercompanyname
        self.lengthoffiber = float(lengthoffiber)
        self.customername = customername

    def greetings(self, greettype):  # method to print message in terminal
        if greettype == 1:
            print("\nWelcome to the Optical fiber installation order terminal")
        if greettype == 2:
            print("Please enter your Full Name")
        if greettype == 3:
            print("Please enter the required Optical fiber company name")
        if greettype == 4:
            print("Please enter the required length of optical cable in feets")
        if greettype == 5:
            print(f'Ordered Company name of optical fiber = {self.opticalfibercompanyname}',
                  f'\nOrdered length of optical fiber = {self.lengthoffiber}', # 3.1 Programming Assignment start
                  f'\nActual cost per feet ={self.calculatecost()[3]}',
                  f'\nActual Order Cost = {self.calculatecost()[1]}',
                  f'\nDiscounted cost per feet ={self.calculatecost()[2]}'
                  f'\nDiscounted Order Cost = {self.calculatecost()[0]}')   # 3.1 Programming Assignment end
        if greettype == 6:
            print("Type y to proceed with the order other wise type any key to exit")
        if greettype == 7:
            print("Thank you Very Much for the order and please find below printed order receipt")
        if greettype == 8:
            print("Thank you for visiting to order terminal")
            exit()
        if greettype == 9:
            seed(1)
            print('\n========================================================')
            print(f'*XYZ Optical Fiber Installation Company Sales Receipt  *')
            print('========================================================')
            print(f'*Order No: {randrange(1, 10)} || order date: {date.today()}\n*Customer Name: {self.customername} ')
            print('========================================================')
            print(f'Optical fiber company name: {opticalfibercompanyname}' # 3.1 Programming Assignment start
                  f'\nlength of cable = {self.lengthoffiber}'
                  f'\nActual cost per feet ={self.calculatecost()[3]}'
                  f'\nBefore Discount cost = {self.calculatecost()[1]}'
                  f'\nDiscounted cost per feet ={self.calculatecost()[2]}'
                  f'\nafter Discount cost = {self.calculatecost()[0]}')   # 3.1 Programming Assignment end
            print(f'*******************Total cost ={self.calculatecost()[0]}**')
        if greettype == 10:
            print("Please reenter the length of fiber in digits")

    def calculatecost(self):  # method to calculate cost
    # 3.1 Programming Assignment start
        actualcost = round(self.lengthoffiber * 0.87, 2)
        actualcostperunit = 0.87
        if self.lengthoffiber <= 100:
           calccost = round(self.lengthoffiber * 0.87, 2)
           costperunit = 'N.A'
        elif self.lengthoffiber > 500:
           calccost = round(self.lengthoffiber * 0.50, 2)
           costperunit = 0.50
        elif (self.lengthoffiber <= 500) and (self.lengthoffiber > 250):
           calccost = round(self.lengthoffiber * 0.70, 2)
           costperunit = 0.70
        elif (self.lengthoffiber <= 250) and (self.lengthoffiber > 100):
           calccost = round(self.lengthoffiber * 0.80, 2)
           costperunit = 0.80
        return calccost, actualcost, costperunit, actualcostperunit
    # 3.1 Programming Assignment end


if __name__ == '__main__':
    try:
        gsr = GenerateSalesReceipt()  # calling method to print terminal message
        gsr.greetings(1)
        gsr.greetings(2)
        customername = str(input())
        gsr.greetings(3)
        opticalfibercompanyname = str(input())
        gsr.greetings(4)
        lengthoffiber = input()
        try:
            if (isinstance(float(lengthoffiber), float) == True):
                lengthoffiber = float(lengthoffiber)
        except:
            print('input length is not valid , please reenter the valid length in digit')
            lengthoffiber = float(input())
        gsr1 = GenerateSalesReceipt(opticalfibercompanyname, lengthoffiber, customername,)
        gsr1.greetings(5)
        gsr1.greetings(6)
        orderconfirm = str(input())
        if orderconfirm == 'y' or orderconfirm == 'Y':
            gsr1.greetings(7)   # calling method to print receipt message
            gsr1.greetings(9)
        else:
            gsr1.greetings(8)

    except:
        print("error- input data is not valid")
