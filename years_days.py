# # very basic and time consuming

# year=int(input("enter the selecte year: "))
# month=int(input("enter month number in integer:"))

# leap_year=False

# def year_check(year):
#     if year %4 ==0 and (year %100 !=0 or year %400 ==0):
#         leap_year = True

# while not leap_year:
#     if month == 2:
#         print(f"your selcted month is february and it has 28 days in {year}")
#         break
#     elif month in [1,3,5,7,8,10,12]:
#         print(f"your selcted month has 31 days in {year}")
#         break
#     elif month in [4,6,9,11]:
#         print(f"your selcted month has 30 days in {year}")
#         break
#     else:
#         print("invalid input")
#         break

# while leap_year:
#     if month == 2:
#         print(f"your selcted month is february and it has 29 days in {year}")
#         break
#     elif month in [1,3,5,7,8,10,12]:
#         print(f"your selcted month has 31 days in {year}")
#         break
#     elif month in [4,6,9,11]:
#         print(f"your selcted month has 30 days in {year}")
#         break
#     else:
#         print("invalid input")
#         break   
# year_check(year)

#tad bit better code

year=int(input("enter the selecte year: "))
month=int(input("enter month number in integer:"))

month_name=["0","january","february","march","april","may","june","july","august","september","october","november","december"]
def days_in_month(month,year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        if year %4 ==0 and (year %100 !=0 or year %400 ==0):
            return 29
        else:
            return 28
    else:
        return "invalid input"
print(f"days in the month {month_name[month]} is {days_in_month(month,year)} for the year {year}")