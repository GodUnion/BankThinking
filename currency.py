"""ggg"""
def currencyy():
    """find the currency function"""
    print("โปรกเลือกอัตราการแลกเปลี่ยน)") #อ้างอิงวันที่22พฤศจิกายน2562
    print("1.อัตราการซื้อ")
    print("2.อัตราการขาย")
    num = int(input())
    if num == 1:
        print("โปรดกรอกข้อมูลตามลำดับ")
        print("1.สกุลเงินที่ต้องการแลกเปลี่ยนเป็นไทย")
        print("2.จำนวนเงิน")
        currency = input()
        amount = float(input())
        if currency == "USD":
            ans = (amount*(30.15))
            print("%.2f"%ans + " บาท")
        if currency == "EUR":
            ans = (amount*(33.25))
            print("%.2f"%ans + " บาท")
        if currency == "GBP":
            ans = (amount*(38.75))
            print("%.2f"%ans + " บาท")
        if currency == "JPY":
            ans = (amount*(0.278))
            print("%.2f"%ans + " บาท")
        if currency == "CHD":
            ans = (amount*(22.65))
            print("%.2f"%ans + " บาท")
        if currency == "CHF":
            ans = (amount*(30.25))
            print("%.2f"%ans + " บาท")
        if currency == "AUD":
            ans = (amount*(20.40))
            print("%.2f"%ans + " บาท")
        if currency == "NZD":
            ans = (amount*(19.25))
            print("%.2f"%ans + " บาท")
        if currency == "SGD":
            ans = amount*22.10
            print("%.2f"%ans + " บาท")
        if currency == "HKD":
            ans = (amount*(3.840))
            print("%.2f"%ans + " บาท")

    if num == 2:
        print("โปรดกรอกข้อมูลตามลำดับ")
        print("1.สกุลเงินต่างประเทศที่ต้องการแลกเปลี่ยน")
        print("2.จำนวนเงิน")
        currency = input()
        amount = float(input())
        if currency == "USD":
            ans = (amount*(0.33))
            print("%.2f"%ans + " USD")
        if currency == "EUR":
            ans = (amount*(0.03))
            print("%.2f"%ans + " EUR")
        if currency == "GBP":
            ans = (amount*(0.026))
            print("%.2f"%ans + " GBP")
        if currency == "JPY":
            ans = (amount*(3.584))
            print("%.2f"%ans + " JPY")
        if currency == "CHD":
            ans = (amount*(0.44))
            print("%.2f"%ans + " CHD")
        if currency == "CHF":
            ans = (amount*(0.033))
            print("%.2f"%ans + " CHF")
        if currency == "AUD":
            ans = (amount*(0.049))
            print("%.2f"%ans + " AUD")
        if currency == "NZD":
            ans = (amount*(0.052))
            print("%.2f"%ans + " NZD")
        if currency == "SGD":
            ans = (amount*(0.045))
            print("%.2f"%ans + " SGD")
        if currency == "HKD":
            ans = (amount*(0.259))
            print("%.2f"%ans + " HKD")

currencyy()
