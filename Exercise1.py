#If you put summing = 0 before, the computer keeps adding the sums to the previous ones and scaling up, but inside the loop
#it always sets it to 0 so then whenever you put a bigger number it becomes the new Max
sMax = -1000
while True:
    summing = 0
    num = input("Give me a number: ")
    try:
        num = int(num)

    except ValueError:
        print("You have not entered a proper number.")
        break

    summing = summing + num

    if summing > sMax:
        sMax = summing

    print("The Biggest Sum is: ", sMax)