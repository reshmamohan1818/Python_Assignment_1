future=int(input("Enter a future year="))
current=int(input("Enter the current year="))

while (current<=future):
    if current%100==0:
        if current%400==0:
            print(current)
    elif current%4==0:
        print(current)
    current+=1
