today_seats = [
    "Xavier",
    "Clinton",
    "Andrew",
    "Jimmy"
]

yesterday_seats = [
    "Xavier",
    "Andrew",
    "Clinton",
    "Jimmy"
]

current_row = 0

# [4, 5, 6, 7, 8]
# range (1, 100)

while current_row < 4:
    if today_seats[current_row] == yesterday_seats[current_row]:
        print "Move to another seat, %s" % today_seats[current_row]
    current_row += 1

print "Thanks!"