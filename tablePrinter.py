#! /usr/bin/python3

def printTable(tableData):
    colWidth = [0] * len(tableData)
    for i in range(len(tableData)):
        colWidth[i] = max(len(s) for s in tableData[i])
    
    for v in range(len(tableData[0])):
        print(tableData[0][v].rjust(max(colWidth)) + 
              tableData[1][v].rjust(max(colWidth)) + 
              tableData[2][v].rjust(max(colWidth)))



tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
