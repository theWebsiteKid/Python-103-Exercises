day = int(raw_input("Day (0-6)? "))
weekdays = [
    "Sunday", 
    "Monday", 
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

if 0 < day < 6:
    print "Go to work" 
else:
    print "Sleep in"