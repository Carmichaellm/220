"""
Liam Carmichael
lab1.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

I certify that this assignment is entirely my own work.
"""

def monthly_interest():
    annual_interest_rate = eval(input("annual interest rate: "))
    billing_cycle = eval(input("number of days in the billing cycle: "))
    net_balance = eval(input("previous net balance: "))
    payment_amount = eval(input("payment amount: "))
    day_of_payment = eval(input("day of payment: "))

    s1= net_balance * billing_cycle
    days_left = billing_cycle-day_of_payment
    s2= payment_amount * days_left
    s3=s1-s2
    average_daily_balance=s3/billing_cycle
    monthly_interest_rate=(annual_interest_rate/12)/100
    monthly_interest_charge=average_daily_balance*monthly_interest_rate

    print("The monthly interest charge is", monthly_interest_charge)