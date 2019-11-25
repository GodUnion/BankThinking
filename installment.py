"""installment"""
def installment():
	"""installment"""
	print("กรุณากรอกข้อมูลตามลำดับ")
	print("1.จำนวนเงินที่ต้องการผ่อน")
	print("2.อัตราดอกเบี้ย")
	print("3.ระยะเวลาในการผ่อน")
	monney = float(input())
	interest = float(input())
	time = int(input())
	increase = (monney+(monney*(interest/100)))//time
	ans = round(increase, 0)
	
	print(increase)
installment()
