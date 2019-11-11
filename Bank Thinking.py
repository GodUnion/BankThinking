"""Bank Thinking"""
def main():
    """First Page in Program"""
    print("ใส่เลข 1-5 เพื่อเลือกบริการ")
    print("1 คำนวณหาดอกเบี้ยแบบทบต้น")
    print("2")
    print("3")
    print("4")
    num = input()
    if num == "1":
        interest()
    elif num == "2":
        print("no")
    elif num == "3":
        print("no")
    elif num == "4":
        print("no")
    elif num == "5":
        print("no")
    else:
        print("ทำรายการไม่ถูกต้องกรุณาใส่เลขใหม่")
        num = input()

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

main()
