# DSC 510
# Week 11
# 11.1 Programming Assignment
# Author Prashant Raghuwanshi
# Date Created: 05-29-2021
# Program Description: 11.1 ->This Programs takes input cash entries from customers
# it generate the total cash entries amount and number of entries of users.
#============================================================================================


from datetime import date
import num2words


class CashRegister:
    '''
    Cash register that records the total cost of items and adds tax.
    '''
    def __init__(self, rate):
        self.balance = 0
        self.tax_rate = rate
        self.item_count = 0
        self.cost = 0

    def add_item(self, cost):
        '''
        Adds an item with the given cost to this register's total.
        '''
        self.balance += cost


    def itemcount(self, item_no):
        '''
        Adds an item with the given cost to this register's total.
        '''
        self.item_count += item_no
        return self.item_count

    @property
    def getcount(self):

        totalcount = self.item_count
        return totalcount

    @property
    def get_total(self):
        '''
        Returns the total cost of all added items, plus 3% tax.
        '''
        totalval = self.balance
        return totalval

    def clear(self):
        '''
        Clears the register to start adding new items.
        '''
        self.balance = 0

    def process(self, item_no):
        iteration_no=self.itemcount(item_no)
        numbercount = num2words.num2words(iteration_no, to='ordinal')
        cost_input = input(f'Please Enter the cost of the {numbercount} item:')
        try:
            if (isinstance(float(cost_input), float) == True):
                cost_input = float(cost_input)
        except:
            print('input item cost is not valid , please reenter the valid cost in digit')
            cost_input = float(input())
        self.add_item(cost_input)
        print(f'Total Cash value after adding {numbercount} item ${self.get_total}')
        print(f'Total No of cash entry ={self.getcount}')


def main():
    try:
        print(f'Hello User ,Welcome to Cash Register: ')
        item_no = 1
        cashinstance = CashRegister(tax_rate)
        continueoperation = 'Y'
        while continueoperation == 'Y' or continueoperation == 'y':
            cashinstance.process(item_no)
            print('Enter Y or y if you want to enter new item cash value else press any key to exit from terminal')
            continueoperation = input()
        cashinstance.clear()

    except ValueError:
        print("error- input data is not valid")


if __name__ == '__main__':
    main()

