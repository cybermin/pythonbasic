while True:    
    #입력
    dan = input('단 입력(종료:q) : ')

    #종료조건 확인
    if dan.lower() == 'q' : break
    
    if dan in ['2','3','4','5','6','7','8','9'] : dan = int(dan)
    else : continue

    #1~9 출력
    for i in range(1, 10) :
        print(f'{dan} x {i} = {dan * i}' )