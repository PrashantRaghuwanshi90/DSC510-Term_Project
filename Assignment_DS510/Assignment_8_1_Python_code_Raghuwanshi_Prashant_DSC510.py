# DSC 510
# Week 8
# 8.1 Programming Assignment
# Author Prashant Raghuwanshi
# Date Created: 05-09-2021
# Program Description: 2.1 ->This program will read the input text file and Calculate the total words,
# and output the number of occurrences of each word in the file.
#===================================================================================================##
import re
import sys
import traceback


def add_word(splitrow, dictnm):
    for word in splitrow:
        if re.search('[a-zA-Z]+', word) is None:
            continue
        else:
            if word.lower() in dictnm:
                dictnm[(word.lower()).strip()] += 1
            else:
                dictnm[(word.lower()).strip()] = 1


def process_line(line, dictnm):
    #removing numeric values and unwanted chars
    cleanrow0 = re.sub('[,.0-9]', '', line)
    cleanrow1 = re.sub('[\n]', '', cleanrow0)
    cleanrow2 = re.sub('[^a-zA-Z]+ ', '', cleanrow1)
    splitrow = cleanrow2.split(" ")
    add_word(splitrow, dictnm)


def printresult(dictnm):
    print(f'########################################')
    print(f'Total Count of Words = {len(dictnm)}')
    print(f'########################################')
    print(f'Words  :        Counts')
    print(f'----------------------------------------')
    for key, value in dictnm.items():
        print("{:<15} {:<4}".format(key, value))
    print(f'--------------END-----------------------')


def main():
    try:
        # Opens a file in read mode
        gbafile = open('C:/Users/dell/Desktop/MS_DataScience/sourcefile/gettysburg.txt', 'r')
        wordstore = {}
        dictnm = wordstore
        # Gets each line till end of file is reached
        for line in gbafile:
            process_line(line, dictnm)
        printresult(dictnm)
        gbafile.close()
    except Exception as err:
        traceback.print_tb(err.__traceback__)
        exit(100)


if __name__ == '__main__':
    main()