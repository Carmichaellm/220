"""
Name: Liam Carmichael
lab3.py

Problem:
write a program that will help analyze traffic patterns

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def traffic():
    total_roads_surveyed = eval(input("How many roads were surveyed? "))
    total_vehicles_all = 0
    for i in range(1,total_roads_surveyed + 1):
        print("How many days was road", i,end=" ")
        days_surveyed = eval(input("surveyed?"))
        total_vehicles_road = 0
        for j in range(1,days_surveyed+1):
            print("\t","How many cars traveled on day", j, end="")
            total_vehicles_day = eval(input("?"))
            total_vehicles_road = total_vehicles_road + total_vehicles_day
        avg_vehicles_day = total_vehicles_road / days_surveyed
        avg_vehicles_day = round(avg_vehicles_day,1)
        total_vehicles_all = total_vehicles_all + total_vehicles_road
        print("Road", i, "average vehicles per day:", avg_vehicles_day)
    avg_vehicles_road = total_vehicles_all / total_roads_surveyed
    avg_vehicles_road = round(avg_vehicles_road,2)
    print("Total number of vehicles traveled on all roads:", total_vehicles_all)
    print("Average number of vehicles per road:",avg_vehicles_road)