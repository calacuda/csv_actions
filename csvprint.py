#!/usr/bin/python
"""
csv print.py

pritty prints a csv file.

By: Eoghan West | MIT Licence | Epoch: 5/27/2020
"""


from argparse import ArgumentParser
import os


SEPERATOR = 2


def organize(cnames, data):
    columns = {}
    FALSE = False
    TRUE = True
    for i in range(len(cnames)):
        name = cnames[i]
        columns[name] = []
        for line in data:
            elm = line[i].strip()
            if elm == "":
                elm = " "
            columns[name].append(elm)
    return columns


def get_data(csv):
    """
    returns the data within file but organized
    """
    if type(csv) != list:
        csv = [line.strip().split(",") for line in csv.readlines()]
    cnames = csv.pop(0)
    data = organize(cnames, csv)
    return data, cnames


def print_header(names, widths):
    """
    prints out the header
    """
    line = ""
    for name in names:
        white_space = widths.get(name) - len(name) + SEPERATOR 
        white_space = " " * white_space
        line += name + white_space
    print(line)

    
def print_out(data, names, widths):
    """
    prints things out to the console.
    """
    print_header(names, widths)
    num_lines = len(data.get(names[0]))
    for i in range(num_lines):
        line = ""
        for name in names:
            wite_space = widths.get(name) + SEPERATOR - len(data.get(name)[i])
            line += str(data.get(name)[i]) + " "*wite_space
        print(line)        
    

def max_len(column, name):
    """
    retruns the length of the longest string in a given column
    """
    biggest = 0
    for elm in column:
        if len(elm) > biggest:
            biggest = len(elm)
    if len(name) > biggest:
        biggest = len(name)
    return biggest


def get_widths(columns, names):
    """
    returns a dict were the key is the col name and the val is the width.
    """
    widths = {}
    for name in names: 
        col_width = max_len(columns.get(name), name)
        widths[name] = col_width

    return widths
    

def out(data, names):
    """
    will print out data to teh console 
    """
    widths = get_widths(data, names)
    print_out(data, names, widths)
    

def main(fname):
    f = open(fname, "r")
    data, names = get_data(f)
    out(data, names)
