"""ProgressiveTax"""
def main(money):
    """test"""
    if 0 <= money <= 150000:
        print(0)
    elif 150000 < money <= 300000:
        tax = (money-150000)*0.05
        print("%d"%tax)
    elif 300000 < money <= 500000:
        tax = ((money-300000)*0.1)+7500 #20000
        print("%d"%tax)
    elif 500000 < money <= 750000:
        tax = ((money-500000)*0.15)+27500 #37500
        print("%d"%tax)
    elif 750000 < money <= 1000000:
        tax = ((money-750000)*0.20)+65000 #50000
        print("%d"%tax)
    elif 1000000 < money <= 2000000:
        tax = ((money-1000000)*0.25)+115000 #250000
        print("%d"%tax)
    elif 2000000 < money <= 4000000:
        tax = ((money-2000000)*0.30)+365000 #600000
        print("%d"%tax)
    elif money > 4000000:
        tax = ((money-4000000)*0.35)+965000
        print("%d"%tax)
main(int(input()))
