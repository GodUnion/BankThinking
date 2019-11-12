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
total_cost()
