import customer_func1 as cf

custlist = [{'name': 'hong1', 'gender': 'M', 'email':'hong1@gmail.com', 'birthday': '2000'},
            {'name': 'hong2', 'gender': 'M', 'email':'hong2@gmail.com', 'birthday': '2000'},
            {'name': 'hong3', 'gender': 'M', 'email':'hong3@gmail.com', 'birthday': '2000'},
            {'name': 'hong4', 'gender': 'M', 'email':'hong4@gmail.com', 'birthday': '2000'}]

page=3
 
while True:
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
        page = cf.insertData(custlist) #선언한 list. #페이지에 리턴값을 넣어줌.
    elif choice=="C": #주소값이 넘어오면 리턴, 주소가 넘어오면 리턴안해두됨
        cf.curData(custlist,page) #여기는 page 안해두댐 ㅇㅇ
    elif choice == 'P':
        page = cf.preData(custlist,page)
    elif choice == 'N':
        page = cf.nextData(custlist,page)
    elif choice=='D':
        page = cf.deleteData(custlist)
    elif choice=="U": 
        cf.updateData(custlist)
    elif choice=="Q":
        break
    else:
        print('메뉴 입력이 잘못되었습니다. 다시 입력해 주세요.')