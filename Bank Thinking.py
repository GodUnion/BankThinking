"""Bank Thinking"""
def main_menu():
    """First Page in Program"""
    print("ใส่เลข 1-9 เพื่อเลือกบริการ")
    print("1 การกู้เงิน")
    print("2 ลงทุนใหห้ได้กำไรมากที่สุด(TC)")
    print("3 บริหารเงินเดือน")
    print("4 คํานวณรายได้จากการทำงานล่วงเวลา")
    print("5 เปลี่ยนสกุลเงิน")
    print("6 ผ่อน")
    print("7 ภาษีบุคคล")
    print("8 ภาษีรถยนตร์")
    print("9 คิดกอกเบี้ยแบบทบต้น")
    num = input()
    if num == "1":
        borrow()
    elif num == "2":
        total_cost()
    elif num == "3":
        money_per_mount()
    elif num == "4":
        work_out()
    elif num == "5":
        currencyy()
    elif num == "6":
        installment()
    elif num == "7":
        stair_tax()
    elif num == "8":
        tax_car()
    elif num == "9":
        interest()
    else:
        print("ทำรายการไม่ถูกต้อง")

def borrow():
    """find the borrow cost function"""
    print("กรุณากรอกข้อมูลตามลำดับ") #ความสามารถในการกู้
    print("1.รายได้ หรือ เงินเดือน")
    print("2.จำนวนผ่อนชำระหนี้สูงสุดที่แบกรับได้ต่อเงินเดือน")
    print("3.อัตราส่วน ของเงินผ่อนชำระต่องวด")
    print("4.หนี้สินปัจจุบันที่ต้องชำระต่อเดือน")
    money = int(input())
    max_money = int(input())
    print("กรุณากรอกข้อมูลตามลำดับ")
    print("1.เศษ")
    print("2.ส่วน")
    func_top = int(input())
    func_low = int(input())
    dept = int(input())
    calfunc = func_top/func_low
    cal_per = max_money/money
    cal_dept = max_money-dept
    cal_bow = (money*cal_per)-dept
    total = (cal_bow*func_low)/func_top
    print("ความสามารถในการกู้สูงสุดของคุณคือ %.2f บาท"%total)

def total_cost():
    """find the total cost function"""
    print("กรุณากรอกข้อมูลตามลำดับ")
    print("1.ความต้องการสินค้าต่อปี")
    print("2.ค่าใช้จ่ายในการสั่งซื้อสินค้าต่อครั้ง")
    print("3.ค่าใช้จ่ายในการเก็บสินค้าต่อชิ้น")
    print("4.ราคาสินค้าต่อชิ้น")
    print("5.ส่วนลดต่อชิ้น(ถ้ามี == 1, ไม่มี == 0)")
    demand = int(input())
    order_cost = float(input())
    holding_cost = float(input())
    price = float(input())
    promotion = int(input())
    qual = (2*order_cost*demand/holding_cost)**0.5
    if promotion == 1:
        print("กรุณากรอกข้อมูลตามลำดับ")
        print("1.ส่วนลดราคาสินค้าต่อชิ้นเป็นร้อยละทศนิยม")
        print("2.ปริมาณสินค้า")
        pro = float(input())
        qual_new = int(input())
        cal1 = pro*price
        cal2 = price-cal1
        total_cost = (holding_cost*qual_new/2)+(order_cost*demand/qual_new)+(cal2*demand)
        print("ค่าใช้จ่ายทั้งหมด %.2f บาท"%total_cost)
    else:
        total_cost = ((holding_cost*qual)/2)+(order_cost*demand)/qual
        print("ควรสั่งสินค้า %d ชิ้น และมีค่าใช้จ่ายทั้งหมด %.2f บาท"%(qual, total_cost))

def money_per_mount():
    """this cal money per mount"""
    print("โปรดกรอกข้อมูลตามลำดับ")
    print("1.เงินเดือน")
    print("2.หนี้สิน ไม่มี ==0")
    you_money = float(input())
    dept = float(input())
    if dept == 0:
        need = you_money*0.4    #40:40:20
        eat = you_money*0.4
        cal_eat = eat//30
        keep = you_money*0.2
        print("คุณมีส่วนใช้จ่ายสิ่งที่จำเป็น %.2f บาท ส่วนใช้จ่ายอาหาร %.2f บาท/วัน ส่วนเงินเก็บ %.2f บาท"%(need, cal_eat, keep))
        print("โปรดกรอกค่าใช้จ่ายสิ่งที่จำเป็น/เดือน")
        print("1.ค่าเช่าบ้าน หรือ ค่าเช่าหอ")
        print("2.ค่าผ่อนรด")
        print("3.ค่าน้ำ-ค่าไฟ")
        print("4.ค่าโทรศัพท์")
        print("5.อื่นๆ")
        home = float(input())
        car = float(input())
        light = float(input())
        phone = float(input())
        value = float(input())
        cal = need-home-car-light-phone-value
        if cal < 0:
            print("คุณใช้จ่ายมากเกินไป %.2f บาท โปรดใช้จ่ายอย่างประหยัด"%abs(cal))
        else:
            print("คุณมีค่าใช้จ่ายสิ่งที่จำเป็นเหลืออยู่ %.2f บาท"%cal)
    elif dept != 0:
        need = you_money*0.4    #40:50:10
        eat = you_money*0.5
        cal_eat = eat//30
        keep = you_money*0.1
        print("คุณมีส่วนใช้จ่ายสิ่งที่จำเป็น %.2f บาท ส่วนใช้จ่ายอาหารรวมกับส่วนใช้หนี้ %.2f บาท/วัน ส่วนเงินเก็บ %.2f บาท"%(need, cal_eat, keep))
        print("โปรดกรอกค่าใช้จ่ายสิ่งที่จำเป็น/เดือน")
        print("1.ค่าเช่าบ้าน หรือ ค่าเช่าหอ")
        print("2.ค่าผ่อนรถ")
        print("3.ค่าน้ำ-ค่าไฟ")
        print("4.ค่าโทรศัพท์")
        print("5.อื่นๆ")
        home = float(input())
        car = float(input())
        light = float(input())
        phone = float(input())
        value = float(input())
        cal = need-home-car-light-phone-value
        if cal < 0:
            print("คุณใช้จ่ายมากเกินไป %.2f บาท โปรดใช้จ่ายอย่างประหยัด"%abs(cal))
        else:
            print("คุณมีค่าใช้จ่ายสิ่งที่จำเป็นเหลืออยู่ %.2f บาท"%cal)

def work_out():
    """find ot """
    print("โปรดเลิอกกรอกข้อมูล")
    print("1.ค่าตอบแทนกรณีทำงานล่วงเวลาปกติ/8ชม")
    print("2.ค่าตอบแทนกรณีทำงาล่วงเวลาวันหยุด/8ชม")
    print("3.ค่าตอบแทนกรณีทำงานในวันหยุดในช่วงเวลาปกติ/8ชม")
    num = int(input())
    if num == 1:
        print("โปรดกรอกข้อมูลตามลำดับ")
        print("1.ค่าจ้างต่อเดือน หรือ วัน")
        print("2.เวลาการทำโอที/ชั่วโมง")
        print("3.พนักงานรายเดือน =1, พนักงานรายวัน =0")
        money = int(input())
        time_ot = int(input())
        typ = int(input())
        if typ == 1:
            cal = (money/30/8)*1.5*time_ot
            print("คุณจะได้รับเงินโอทีรายเดือน = %.2f บาท"%cal)
        else:
            cal = (money/8)*1.5*time_ot
            print("คุณจะได้รับเงินโอทีรายวัน = %.2f บาท"%cal)
    if num == 2:
        print("โปรดกรอกข้อมูลตามลำดับ")
        print("1.ค่าจ้างต่อเดือน หรือ วัน")
        print("2.เวลาการทำโอที/ชั่วโมง")
        print("3.พนักงานรายเดือน =1, พนักงานรายวัน =0")
        money = int(input())
        time_ot = int(input())
        typ = int(input())
        if typ == 1:
            cal = (money/30/8)*3*time_ot
            print("คุณจะได้รับเงินโอทีรายเดือน = %.2f บาท"%cal)
        else:
            cal = (money/8)*3*time_ot
            print("คุณจะได้รับเงินโอทีรายวัน = %.2f บาท"%cal)
    if num == 3:
        print("โปรดกรอกข้อมูลตามลำดับ")
        print("1.ค่าจ้างต่อเดือน หรือ วัน")
        print("2.เวลาการทำโอที/ชั่วโมง")
        print("3.พนักงานรายเดือน =1, พนักงานรายวัน =0")
        money = int(input())
        time_ot = int(input())
        typ = int(input())
        if typ == 1:
            cal = (money/30/8)*1*time_ot
            print("คุณจะได้รับเงินโอทีรายเดือน = %.2f บาท"%cal)
        else:
            cal = (money/8)*2*time_ot
            print("คุณจะได้รับเงินโอทีรายวัน = %.2f บาท"%cal)

def currencyy():
    """find the currency function"""
    print("โปรกเลือกอัตราการแลกเปลี่ยน)") #***อ้างอิงวันที่22พฤศจิกายน2562***
    print("1.อัตราการซื้อ")
    print("2.อัตราการขาย")
    num = int(input())
    lis = ["USD = ดอลลาร์", "EUR = ยูโร", "GBP = ปอนด์", "JPY = เยน", "CAD = ดอลลาร์แคนาดา", "CHF = ฟรังก์สวิส", \
           "AUD = ดอลลาร์ออสเตรเลีย", "NZD = ดอลลาร์นิวซีแลนด์", "SGD = ดอลลาร์สิงคโปร์", "HKD = ดอลลาร์ฮองกง"] #total 10 member
    if num == 1:
        print("โปรดกรอกข้อมูลตามลำดับ")
        print("1.สกุลเงินที่ต้องการแลกเปลี่ยนเป็นไทย ดังนี้") #foreign land to thai
        print(*lis, sep="\n")
        print("2.จำนวนเงิน")
        currency = input()
        amount = float(input())
        if currency == "USD":
            ans = (amount*(30.15))
            print("%.2f"%ans + " บาท")
        elif currency == "EUR":
            ans = (amount*(33.25))
            print("%.2f"%ans + " บาท")
        elif currency == "GBP":
            ans = (amount*(38.75))
            print("%.2f"%ans + " บาท")
        elif currency == "JPY":
            ans = (amount*(0.278))
            print("%.2f"%ans + " บาท")
        elif currency == "CAD":
            ans = (amount*(22.65))
            print("%.2f"%ans + " บาท")
        elif currency == "CHF":
            ans = (amount*(30.25))
            print("%.2f"%ans + " บาท")
        elif currency == "AUD":
            ans = (amount*(20.40))
            print("%.2f"%ans + " บาท")
        elif currency == "NZD":
            ans = (amount*(19.25))
            print("%.2f"%ans + " บาท")
        elif currency == "SGD":
            ans = amount*22.10
            print("%.2f"%ans + " บาท")
        elif currency == "HKD":
            ans = (amount*(3.840))
            print("%.2f"%ans + " บาท")
        else:
            print("ข้อมูลไม่ตรง")

    if num == 2:
        print("โปรดกรอกข้อมูลตามลำดับ")
        print("1.สกุลเงินต่างประเทศที่ต้องการแลกเปลี่ยน ดังนี้") #thai to foreign land
        print(*lis, sep="\n")
        print("2.จำนวนเงิน")
        currency = input()
        amount = float(input())
        if currency == "USD":
            ans = (amount*(0.033))
            print("%.2f"%ans + " USD")
        elif currency == "EUR":
            ans = (amount*(0.03))
            print("%.2f"%ans + " EUR")
        elif currency == "GBP":
            ans = (amount*(0.026))
            print("%.2f"%ans + " GBP")
        elif currency == "JPY":
            ans = (amount*(3.584))
            print("%.2f"%ans + " JPY")
        elif currency == "CAD":
            ans = (amount*(0.044))
            print("%.2f"%ans + " CAD")
        elif currency == "CHF":
            ans = (amount*(0.033))
            print("%.2f"%ans + " CHF")
        elif currency == "AUD":
            ans = (amount*(0.049))
            print("%.2f"%ans + " AUD")
        elif currency == "NZD":
            ans = (amount*(0.052))
            print("%.2f"%ans + " NZD")
        elif currency == "SGD":
            ans = (amount*(0.045))
            print("%.2f"%ans + " SGD")
        elif currency == "HKD":
            ans = (amount*(0.259))
            print("%.2f"%ans + " HKD")
        else:
            print("ข้อมูลไม่ตรง")

def installment():
    """this fuction cal installment"""
    print("กรุณากรอกข้อมูลตามลำดับ")
    print("1.จำนวนเงินที่ต้องการผ่อน")
    print("2.อัตราดอกเบี้ย เป็น%")
    print("3.ระยะเวลาในการผ่อน")
    monney = float(input())
    interest = float(input())
    time = int(input())
    increase = (monney+(monney*(interest/100)))//time
    ans = round(increase, 0)
    print("ท่านจะต้องผ่อนเดือนละ %.2f บาท"%increase)

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

def tax_car():
    print("กรุณากรอกข้อมูลตามลำดับ")
    print("1.ขนาดเครื่องยนต์")
    print("2.อายุการใช้งาน")
    engine = float(input())
    year = int(input())
    tax = 0
    if engine >= 1801:
        tax += (2100 + ((engine-1800)*4))
    elif 601 <= engine <= 1800:
        tax += (300 + ((engine-600)*1.5))
    elif 1 <= engine <= 600:
        tax += (engine*0.5)
    else:
        print("กรอกข้อมูลไม่ถูกต้อง")

    if year >= 10:
        total = tax*0.5
    elif 9 <= year < 10:
        total = tax*0.6
    elif 8 <= year < 9:
        total = tax*0.7
    elif 7 <= year < 8:
        total = tax*0.8
    elif 6 <= year < 7:
        total = tax*0.9
    else:
        total = tax
    print("ต้องเสียภาษี %.2f"%total)

def interest():
    """find the interest function"""
    print("กรุณากรอกข้อมูลตามลำดับ")
    print("1.จำนวนเงินที่ฝาก หน่วยเป็นบาท")
    print("2.อัตราดอกเบี้ยต่อปี เช่น ดอกเบี้ย 2% ต่อปีให้กรอก 2 ")
    print("3.จำนวนปีที่ฝาก")
    money = float(input())
    inter = float(input())
    year = int(input())
    for _ in range(year):
        in_now = ((money*inter)/100)
        money = money+in_now
    print("%.2f บาท"%money)

main_menu()
