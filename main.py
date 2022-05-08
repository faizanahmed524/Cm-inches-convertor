print("Inches/Cm converter")


def intocm(n):
    convert = n * 2.54
    print(n, "inches = ", convert, "cm")
    return


def cmtoin(n):
    convert = n * 0.393700787
    print(n, "cm = ", convert, "inches")
    return


num = int(input("Enter the number you want to convert: "))
unit = int(input("Chose an option:\n1=Inches to Centimetres\n2=Centimetre to Inches\n"))
if unit==1:
    intocm(num)
elif unit==2:
    cmtoin(num)