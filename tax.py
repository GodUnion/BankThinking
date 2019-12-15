"""stairs tax for common person"""
def stair_tax():
    """this function find stairs tax"""
    print("1.โปรดกรอกจำนวนเงินเดือนของท่าน")
    money = int(input()) #take money in to if/elif for cal tax
    tax = 0
    if 0 <= money <= 150000:
        print(0)
    elif 150000 < money <= 300000:
        tax += (money-150000)*0.05
        print("ท่านต้องเสียภาษีเป็นเงินจำนวน %d บาท"%tax)
    elif 300000 < money <= 500000:
        tax += ((money-300000)*0.1)+7500 #20000
        print("ท่านต้องเสียภาษีเป็นเงินจำนวน %d บาท"%tax)
    elif 500000 < money <= 750000:
        tax += ((money-500000)*0.15)+27500 #37500
        print("ท่านต้องเสียภาษีเป็นเงินจำนวน %d บาท"%tax)
    elif 750000 < money <= 1000000:
        tax += ((money-750000)*0.20)+65000 #50000
        print("ท่านต้องเสียภาษีเป็นเงินจำนวน %d บาท"%tax)
    elif 1000000 < money <= 2000000:
        tax += ((money-1000000)*0.25)+115000 #250000
        print("ท่านต้องเสียภาษีเป็นเงินจำนวน %d บาท"%tax)
    elif 2000000 < money <= 5000000:
        tax += ((money-2000000)*0.30)+365000 #900000
        print("ท่านต้องเสียภาษีเป็นเงินจำนวน %d บาท"%tax)
    elif money > 5000000:
        tax += ((money-5000000)*0.35)+1265000
        print("ท่านต้องเสียภาษีเป็นเงินจำนวน %d บาท"%tax)
stair_tax()
