"""Manage money value"""
def main():
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
main()
