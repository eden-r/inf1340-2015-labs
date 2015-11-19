#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it

# global constants
PROVINCIAL_TAX = .05
FEDERAL_TAX = .025

# print your bill
def print_your_bill(purchase, prov_tax, fed_tax, all_tax, sale_price):
    print "Amout of purchase: {0:2f}".format(purchase)
    print "Provincial tax: {0:.2f}".format(prov_tax)
    print "Federal tax: {0:.2f}".format(fed_tax)
    print "Total tax: {0:.2f}".format(all_tax)
    print "Total sale: {0:.2f}".format(sale_price)

# calculate taxes
def calculate_your_bill(purchase):
    prov_tax = purchase * PROVINCIAL_TAX
    fed_tax = purchase * FEDERAL_TAX
    all_tax = fed_tax + prov_tax
    sale_price = purchase + (purchase * all_tax)
    print_your_bill(purchase, prov_tax, fed_tax, all_tax, sale_price)

print calculate_your_bill(100.35)

# write to file
file_name = "receipt.txt"

with open(file_name, "w") as output_file:
    output_file.write(str(calculate_your_bill(100.35)))

with open(file_name, "r") as file_reader:
    for line in file_reader:
        print line,

def bill_of_sale(purchase):
    print ("Amount of purchase: {0:.2f}".format(purchase))
    print ("Provincial tax: {0:.2f}".format(purchase * .05))
    print ("Federal tax: {0:.2f}".format(purchase * .025))
    print ("Total tax: {0:.2f}".format(purchase * .075))
    print ("Total sale: {0:.2f}".format(purchase * 1.075))

