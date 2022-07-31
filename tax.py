amt=0
amt=int(input("Enter the price of Bike "))
if amt >100000:
    tax=15/100*amt
    print("Tax for 15%" ,tax)
if amt>50000 and amt<=100000:
    tax=10/100*amt
    print("Tax for 10%" ,tax)
if amt<=50000:
    tax=5/100*amt
    print("Tax for 5%" ,tax)
(#(use elif need to value error else updating)
