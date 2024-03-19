print ("Vertical Control Survey & Accuracy")
print ("by Al-Amin Jamil A. Cunanan")
print ("A program designed to perform direct vertical levelling survey computations and vertical accuracy")

# Create floatInput as a function
def floatInput (prompt):
    '''
    The function floatInput
    Input:
    prompt - float
    Output:
    input - float
    '''
    return floatInput

floatInput = input ("Input initial elevation of BM0: ")

# Create the following variables
levelling_table = []
#  list of tuples of all measurements and derived values

total_distance = 0
# sum of all distances between turning points

tp_counter = 1
# number of turning points between benchmarks

running_elev = float
backsight = float
instrument_height = float
new_elev = float
# Values of running elevation, backsight, height of instrument, and new elevation

while True:

    print()
    print("Turning Point: ", tp_counter)

    input_error = False
    while not(input_error):
        backsight = input   ("Backsight Distance (meters): ")
        foresight = input ("Foresight Distance (meters): ")
        tpdistance = input ("Turning point distance (meters): ")
        floatInput
        if input_error :
            print ("INPUT ERROR")
            continue
        if not (input_error):
            break
# Input all needed values for the turning points: (backsight, foresight, turning point distance)
        
    ih = floatInput(running_elev = float(running_elev), backsight = float(backsight))
    ne = floatInput(ih = float(ih), foresight = float(foresight)) 
    instrument_height += ih
    new_elev += ne

# equations for the height of instrument and the new running elevation for each input
    total_distance += tpdistance

    level = (backsight, instrument_height, foresight, new_elev)
    levelling_table.append (level)
# appending the list with tuple
    yn = input("Add new measurement? ")
    if yn.lower() == "yes" or yn.lower() == "y" or yn.upper() == "YES" or yn.upper*() == "Y":
        tp_counter = tp_counter + 1
        continue
    else:
        break
# incrementing the tp_counter

print(level)
print ("\n\n")
print ("____________________________________________________________________________________________")
print ('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}' .format ("Sta.", "B.S", "H.I", "F.S", "Elev."))
for line in lines:
    print ('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}' .format (line [0], line [1], line [2], line[3], line [4] ))
print ("____________________________________________________________________________________________")
# table format for final values

bm_error = new_elev - running_elev

from math import sqrt


        
        
        

