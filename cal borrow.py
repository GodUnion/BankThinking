"""borrow"""
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
borrow()
