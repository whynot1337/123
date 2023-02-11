count = 0;
s = 551;
while count < 200:
    n = 3;
    k = 6;
    print("sss =",s+6,";")
    s+=6;
    count+=1;
    while n < 760:
        print("window->DrawList->AddRectFilled(window->Pos + ImVec2(sss,",n+6,"), window->Pos + ImVec2(sss + 3,",n+7,"), setochka);")
        n+=6
    while k < 760:
        print("window->DrawList->AddRectFilled(window->Pos + ImVec2(sss + 3,",k+6,"), window->Pos + ImVec2(sss + 6,",k+7,"), setochka);")
        k+=6
