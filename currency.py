"""chang money"""
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
currencyy()
