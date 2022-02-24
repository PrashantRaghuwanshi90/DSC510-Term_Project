# DSC 510
# Week 9
# 9.1 Programming Assignment
# Author Prashant Raghuwanshi
# Date Created: 05-16-2021
# Program Description: 9.1 ->This program will read the input text file and Calculate the total words,
# and write down the number of occurrences of each word in input file to user provided output file.
#===================================================================================================##
import re
import sys
import traceback
from pathvalidate import ValidationError, validate_filename, sanitize_filename, is_valid_filename


def add_word(splitrow, dictnm):
    for word in splitrow:
        if re.search('[a-zA-Z0-9]+', word) is None:
            continue
        else:
            if word.lower() in dictnm:
                dictnm[(word.lower()).strip()] += 1
            else:
                dictnm[(word.lower()).strip()] = 1


def process_line(line, dictnm):
    #removing numeric values and unwanted chars
    cleanrow0 = re.sub('[,.]', '', line)
    cleanrow1 = re.sub('[\n]', '', cleanrow0)
    cleanrow2 = re.sub('[^a-zA-Z- 0-9]+ ', '', cleanrow1)
    splitrow = cleanrow2.split(" ")
    add_word(splitrow, dictnm)


def process_file(dictnm, vldoutputfile):
        wrtdata = open(vldoutputfile, 'a')
        wrtdata.write(f'Words  :        Counts\n')
        wrtdata.write(f'----------------------------------------\n')
        for key, value in sorted(dictnm.items()):
            wrtrow = "{:<15} {:<4}\n".format(key, value)
            wrtdata.write(wrtrow)
        wrtdata.write('--------------END-----------------------')
        wrtdata.close()
        print(f'\nplease find the printed count file at below file path:{vldoutputfile}')


def main():

    try:
        print('Welcome File Printing system')
        # user input from terminal
        outputfile = str(input('\nPlease the file name on which you wish to print the words count information :'))
        if is_valid_filename(outputfile):
            vldoutputfile = outputfile
        else:
            print(f"Entered file name is invalid\n"
                  f"please enter 'Y' or 'y' to proceed with below suggested name\n"
                  f"or press any key to re-enter new file name:\n"
                  f"\n{sanitize_filename(outputfile)}\n")
            suggestedfilename = input("please enter your preference:").upper()
            if suggestedfilename == 'Y':
                vldoutputfile = sanitize_filename(outputfile)
            else:
                vldoutputfile = (input('\nPlease the file name for printing the words count information :'))
                validate_filename(vldoutputfile)
        # Opens input file in read mode
        filePath = 'C:/Users/dell/Desktop/MS_DataScience/sourcefile/'
        infilename = 'gettysburg.txt'
        inputfile = filePath + infilename
        outputfilename = filePath + vldoutputfile + '.txt'
        print(f"\nYou have entered below file to print the result :\n{vldoutputfile + '.txt'}")
        gbafile = open(inputfile, 'r')
        # Opens output file in write mode
        wordstore = {}
        dictnm = wordstore
        # Gets each line till end of file is reached
        for line in gbafile:
            process_line(line, dictnm)
        with open(outputfilename, 'w') as fileHandle:
            fileHandle.write('########################################\n'
                             'Total Count of Words = ')
            dictlen = str(len(dictnm))
            fileHandle.write(dictlen)
            fileHandle.write('\n########################################\n')
        process_file(dictnm, outputfilename)
        gbafile.close()

    except IOError as eio:
        print("File input output operation error")
        traceback.print_tb(eio.__traceback__)
        exit(101)
    except ValidationError as eve:
        traceback.print_tb(eve.__traceback__)
        print(f"{eve}\n", file=sys.stderr)
    except Exception as err:
        traceback.print_tb(err.__traceback__)
        exit(100)


if __name__ == '__main__':
    main()