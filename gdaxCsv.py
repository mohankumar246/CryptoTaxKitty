#!/usr/bin/env python3

#Copyright (c) 2018 Mohankumar Nekkarakalaya

# This file is part of CryptoTaxKitty.
# Licensed under the MIT license. See LICENSE.txt in the project folder.

import csv
import operator

class convertCsv:
    def __init__(self, inFileName='', outFileName=''):
        self.inFileHandle = open(inFileName, 'rb')
        self.outFileHandle = open(outFileName, 'wb')
        self.reader = csv.reader(self.inFileHandle, delimiter=' ', quotechar='|')
        self.writer = csv.reader(self.outFileHandle, delimiter=' ', quotechar='|',  quoting=csv.QUOTE_NONE)

    def processLines(self):
        for row in self.reader:
            writeParams = self.convertParams(row)
            self.writeLine(writeParams)

        self.inFileHandle.close()
        self.outFileHandle.close()

    def convertParams(self):
        writeParams = {}

        return writeParams

    def writeLine(self, writeParams):
        self.writer.writerow(writeParams)
folder="/home/mohank/Desktop/Link to projects/CryptoTaxKitty/csvs/"

filenames = ['gdaxBchAcc.csv', 'gdaxBtcAcc.csv', 'gdaxEthAcc.csv', 'gdaxLtcAcc.csv', 'gdaxUsdAcc.csv']
with open(folder+'gdax.csv', 'w') as outfile:
    print("type, time, amount, balance, amount / balance, unit, transfer, id, trade, id, order ,id", file=outfile)
    for fname in filenames:
        with open(folder+fname) as infile:
            first_line = infile.readline()
            for line in infile:
                 outfile.write(line)
        infile.close()

outfile.close()

inFileHandle = open(folder+'gdax.csv')
infields = inFileHandle.readline()

reader = csv.reader(inFileHandle, delimiter=',')
sortedlist = sorted(reader, key=operator.itemgetter(1))

inFileHandle.close()

# open the output file - it can be the same as the input file
outfile = open(folder+'gdax1.csv', 'w')
# write the header
print("type, time, amount, balance, amount / balance, unit, transfer, id, trade, id, order ,id", file=outfile)


# write the sorted list
for row in sortedlist:
    row = ','.join(map(str, row))
    row = row + "\n"
    outfile.write(row)
# processing finished, close the output file
outfile.close()

convertHandle = convertCsv('gdax1.csv', 'gdaxOut.csv')
convertHandle.processLines()

