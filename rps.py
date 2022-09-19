import random
a = ["가위", "바위", "보"]
b = False
while b == False:
    cp = random.choice(a)
    c = input()
    win = f"컴퓨터 : {cp}\n인간 : {c}\n결과 : 이김"
    lose = f"컴퓨터 : {cp}\n인간 : {c}\n결과 : 짐"
    if cp == c:
        print(f"컴퓨터 : {cp}\n인간 : {c}\n결과 : 비김")
    elif c == "가위":
        if cp == "보":
            print(win)
        else:
            print(lose)

    elif c == "바위":
        if cp == "가위":
            print(win)
        else:
            print(lose)

    elif c == "보":
        if cp == "바위":
            print(win)
        else:
            print(lose)
        
    elif c == "종료":
        break
    else:
        print("지정된 단어가 아니에요")