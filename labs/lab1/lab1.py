"""
Liam Carmichael
lab1.py

Problem: A function which calculates monthly interest charge for a single billing cycle with one payment.

I certify that this assignment is entirely my own work.
"""

def monthly_interest():
    annual_interest_rate = eval(input("annual interest rate: "))
    billing_cycle = eval(input("number of days in the billing cycle: "))
    net_balance = eval(input("previous net balance: "))
    payment_amount = eval(input("payment amount: "))
    day_of_payment = eval(input("day of payment: "))

    step_one= net_balance * billing_cycle
    days_left = billing_cycle-day_of_payment
    step_two= payment_amount * days_left
    step_three=step_one-step_two
    average_daily_balance=step_three/billing_cycle
    monthly_interest_rate=(annual_interest_rate/12)/100
    monthly_interest_charge=average_daily_balance*monthly_interest_rate

    print("The monthly interest charge is $", monthly_interest_charge)