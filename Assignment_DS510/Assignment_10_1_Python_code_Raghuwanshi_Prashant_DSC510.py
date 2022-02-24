# DSC 510
# Week 10
# 10.1 Programming Assignment
# Author Prashant Raghuwanshi
# Date Created: 05-23-2021
# Program Description: 10.1 ->  This program is to access Chuck Norris jokes from the web and
# display them for the user of the program.
#===================================================================================================##
import re
import sys
import traceback
import requests
from urllib3.exceptions import HTTPError as BaseHTTPError


def loadcategories(url, dictnm):
    getcategories = makecall(url, 'categories')
    catergoriesrawlist = getcategories.json()
    count = 1
    for cattype in catergoriesrawlist:
        if cattype.lower() in dictnm:
            continue
        else:
            dictnm[(cattype.lower()).strip()] = count
            count = count + 1
    return dictnm


def printwelcomemessage(categorydict):
    print("Welcome to the hub of Chuck Norris jokes!\n")
    print("Choose random jokes from below listed category:\n")
    print(f'----------------------------------------')
    print(f'Category  :  Select Value')
    print(f'----------------------------------------')
    for key, value in categorydict.items():
        print("{:<15} {:<4}".format(key, value))
    print(f'----------------------------------------')
    print(" ***Type 99 if you want to print random jokes from any category")
    print(" ***Type X or x if you want to exit")


# function to return key for any value
def get_key(val, categorydict):
    for key, value in categorydict.items():
        if int(val) == value:
            return key
    if int(val) != 99:
       return print("Invalid entered category no "+str(val))


def performfetch(selectcategory, chucknorrisurl, categorydict):

    try:
        selectcategoryno = 0
        if isinstance(int(selectcategory), int):
            selectcategoryno = int(selectcategory)
            selectcategory = ''
            categorykey = get_key(selectcategoryno, categorydict)
    except ValueError:
        pass
    try:
          if selectcategoryno in range(1, 16):
             req_joke = makecall(chucknorrisurl, 'random?'+'category='+categorykey)
             data = req_joke.json()
             print(f'Enjoy below printed joke from {categorykey} category:')
             print(data["value"]+"\n")
          elif selectcategoryno == 99:
             req_joke = makecall(chucknorrisurl, 'random?')
             data = req_joke.json()
             print("\n" + data["value"]+"\n")
          else:
             if selectcategory.lower() == 'x':
                print("Exiting from Chuck Norris jokes Terminal")
                exit(101)
             elif selectcategory != '':
                  print(f'Invalid selected category no: {selectcategory}')
    except ValueError:
        print(f'Invalid selected category no: {selectcategory}')


def startprocess(chucknorrisurl, categorydict):
    selectcategory = input('Enter Category No or Type X or x to exit :\n')
    performfetch(selectcategory, chucknorrisurl, categorydict)


def makecall(url, mpath):
    try:
      getdata = ''
      getdata = requests.get(url+mpath)
      getdata.raise_for_status()
      return getdata
    except requests.exceptions.IOError as ioerr:
        print("IOError", ioerr.response.text)
        exit(102)
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh.response.text)
        exit(103)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc.response.text)
        exit(104)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt.response.text)
        exit(105)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err.response.text)
        exit(106)


def main():
    try:
        chucknorrisurl = 'https://api.chucknorris.io/jokes/'
        categorydict = {}
        loadcategories(chucknorrisurl, categorydict)
        printwelcomemessage(categorydict)
        startprocess(chucknorrisurl, categorydict)
        print('Enter Y (in uppercase) if you want to request next joke else press any key to exit from terminal')
        continueoperation = input()
        while continueoperation == 'Y' or continueoperation == 'y':
            if continueoperation == 'y':
               print('You have Entered y (in lowercase), to continue please reenter Y /or/ enter any other key to exit:')
               continueoperation = input()
            if continueoperation == 'Y':
               printwelcomemessage(categorydict)
               startprocess(chucknorrisurl, categorydict)
               print('Enter Y (in uppercase) if you want to request next joke else press any key to exit from terminal')
               continueoperation = input()

    except ValueError as err:
        print("Error", err.response.text)
        exit(101)
    exit(100)

if __name__ == '__main__':
    main()