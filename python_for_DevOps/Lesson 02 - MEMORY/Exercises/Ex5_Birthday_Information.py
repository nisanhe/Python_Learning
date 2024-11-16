import calendar

birthday = input("Enter your birthday (DD-MM-YYYY): ")
month_number = int(birthday.split('-')[1])
month_name = calendar.month_name[month_number]
print(f"You were born in {month_name}.")
