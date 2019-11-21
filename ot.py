"""OT"""
def work():
    """find ot """
    print("โปรดเลิอกกรอกข้อมูล")
    print("1.ค่าตอบแทนกรณีทำงานล่วงเวลาปกติ/8ชม")
    print("2.ค่าตอบแทนกรณีทำงานล่วงเวลาวันหยุด/8ชม")
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
work()
