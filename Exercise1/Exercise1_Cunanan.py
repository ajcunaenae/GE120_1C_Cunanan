"""
Hi my name is AJ Cunanan
This is GE 120
You are watching the Disney Channel
"""

dms = 118.42069

# degree part

degree = int (dms) 

print("DEGREE:", dms)

# minute part

minutes = (dms-degree) * 60

minutes_fractional = int(minutes)

print("MINUTES:", minutes)

# seconds part

seconds = (minutes - minutes_fractional) * 60

print ("SECONDS", seconds)

print("DMS: " + str(degree) + "-" + str(minutes_fractional) + "-" + str(round(seconds, 2)))


dms = "118-25-14.48"
values = dms.split ("-")

degrees = int(values[0])
minutes = int(values[1])
seconds = float(values[2])

dd = degrees + (minutes/60) + (seconds/3600)

print("VALUE OF DECIMAL DEGREES:", round(dd,6))