
nmbr_str = (input("Please enter the number "))
if nmbr_str.isdigit():
    nmbr = int(nmbr_str)
else:
    print("Please enter a number not text")
if 0 < nmbr < 100 and not 10 < nmbr < 20:
    if nmbr / 10 == 1:
        print("ten")
    elif nmbr // 10 == 2:
        print("twenty")
    elif nmbr // 10 == 3:
        print("thirty")
    elif nmbr // 10 == 4:
        print("fourty")
    elif nmbr // 10 == 5:
        print("fifty")
    elif nmbr // 10 == 6:
        print("sixty")
    elif nmbr // 10 == 7:
        print("seventy")
    elif nmbr // 10 == 8:
        print("eighty")
    elif nmbr // 10 == 9:
        print ("ninety")
    if nmbr % 10 == 1:
        print("one")
    if nmbr % 10 == 2:
        print("two")
    if nmbr % 10 == 3:
        print("three")
    if nmbr % 10 == 4:
        print("four")
    if nmbr % 10 == 5:
        print("five")
    if nmbr % 10 == 6:
        print("six")
    if nmbr % 10 == 7:
        print("seven")
    if nmbr % 10 == 8:
        print("eight")
    if nmbr % 10 == 9:
        print("nine")

if nmbr == 11:
    print("eleven")
elif nmbr == 12:
    print("twelve")
elif nmbr == 13:
    print("thirteen")
elif nmbr == 14:
    print("fourteen")
elif nmbr == 15:
    print("fifteen")
elif nmbr == 16:
    print("sixteen")
elif nmbr == 17:
    print("seventeen")
elif nmbr == 18:
    print("eighteen")
elif nmbr == 19:
    print("nineteen")