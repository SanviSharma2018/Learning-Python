days_in_month = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}
sum = 0
for key, val in days_in_month.items():
    if val == 31:
        sum += 31
        print(key, "has 31 days")
    if val == 30:
        sum += 30
        print(key, "has 30 days")

print(sum)
