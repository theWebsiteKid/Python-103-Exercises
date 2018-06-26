complete = False

while complete == False:
    bill_input = raw_input("Total bill amount? $")

    try:
        bill = float(bill_input)
        service_input = raw_input("Level of service (good, fair, or bad)? \n")

        if service_input == "good":
            service = 0.20
            complete = True
        elif service_input == "fair":
            service = 0.15
            complete = True
        elif service_input == "bad":
            service = 0.10
            complete = True
        else:
            print "* Please rate your service as 'good', 'fair', or 'bad'! *"

    except:
        print "* Please use numeric values for bill amount! *"
        pass

tip_amount = bill * service
print "Tip amount: $%.2f" % tip_amount

total_amount = bill + tip_amount
print "Total: $%.2f" % total_amount