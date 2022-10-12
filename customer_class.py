import re,sys
import customer_class_ff


class Customer:
    

    def exe(self):
        choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()  

        if choice=="I":  
            self.insertData()
        elif choice=="C": 
            self.CurData()
        elif choice == 'P':
            self.preData()
        elif choice == 'N':
            self.nextData()
        elif choice=='D':
            self.DeleteData()
        elif choice=="U": 
            self.updateData()
        elif choice=="Q":
            print('프로그램 종료!!')
            sys.exit()

    def __init__(self):
        self.custlist = [{'name': 'hong1', 'gender': 'M', 'email': 'hong1@gamil.com', 'birthday': '2000'},
            {'name': 'hong2', 'gender': 'M', 'email': 'hong2@gamil.com', 'birthday': '2000'},
            {'name': 'hong3', 'gender': 'M', 'email': 'hong3@gamil.com', 'birthday': '2000'},
            {'name': 'hong4', 'gender': 'M', 'email': 'hong4@gamil.com', 'birthday': '2000'}]
        self.page=3
        while True:
            self.exe()



Customer()