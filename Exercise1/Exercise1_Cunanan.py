"""
Hi my name is AJ Cunanan
This is GE 120-1C
Machine Exercise 1
You are watching the Disney Channel
"""

dms = 118.42069

# how to get degree part

degree = int (dms) 

# print("DEGREE:", dms)

# how to get minute part

minutes = (dms-degree) * 60

minutes_fractional = int(minutes)

# print("MINUTES:", minutes)

# how to get seconds part

seconds = (minutes - minutes_fractional) * 60

# print ("SECONDS", seconds)

print("DMS: " + str(degree) + "-" + str(minutes_fractional) + "-" + str(round(seconds, 2)))

# how to convert DMS to Decimal Degree

dms = "118-25-14.48"
values = dms.split ("-")

degrees = int(values[0])
minutes = int(values[1])
seconds = float(values[2])

dd = degrees + (minutes/60) + (seconds/3600)

print("VALUE OF DMS TO DECIMAL DEGREES:", round(dd,6))
