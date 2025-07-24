import calendar

# Iterate from 1 to 12 to get month abbreviations
for i in range(1, 13):
    print(f"{i}: {calendar.month_abbr[i]}")