from traceback import print_tb


class Calculator:
    sum = 100
    def __init__(self): #self > 객체별로 따로따로 저장(객체 생성할때마다), 인스턴스변수 
        self.result = 0
        
    def add(self, num): # num : 지역변수
        self.result += num
        return self.result


cal1 = Calculator() # > 이런식으로 호출해서 사용하고, 주소가 call에 들어감
cal2 = Calculator()
#cal1.result=2
#cal2.result=9

#print(call.result)
#print(cal2.result)
#print(Calculator.sum)
#Calculator.sum = 200  
# self안붙은 변수 = 클래스당 하나 > 클래스에 어떤 값을 하나만 정해놓고 써야할 때 사용
#print(call.sum)
#print(cal2.sum)

cal1.add(3)
cal1.add(4)
print(cal1.result)
print(cal2.result)

class FourCal(Calculator):
    def sub(self,num):
        self.result -= num
        return self.result

cal3 = FourCal()
cal4 = FourCal()

cal3.add(5)
cal3.sub(3)
print(cal3.result)