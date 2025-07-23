import time
Q = ["1) Capital of India. \n A.Mumbai \n B.Gujrat \n C.Delhi \n D.Madhyapradesh", "\n2) First Prim minister of India. \n A.Pandit Jawaharlal Nehru \n B.Valhabbhai Patel \n C.Indira Gandhi \n D.Narendra Modi", "\n3) Who is the first Chief minister of Maharashtra? \n A.Devendra Fadanvis \n B.Vilasrao Deshmukh \n C.Vasantrao Naik \n D.Yashwantrao Chavan"]
Ans = ["C.Delhi","A.Pandit Jawaharlal Nehru","D.Yashwantrao Chavan"]
ans = ["c","a","d"]
P = 0
for i in range(len(Q)):
    print(Q[i])
    # print(i)
    UA = input("Enter the correct option: ")
    CA = Ans[i]
    ca = ans[i]
    print("\nUser ans: ", UA.upper())
    # print("Correct ans: ",CA)
    if UA == ca:
        print("Correct ans:",CA , "\nSahi jawab!!")
        P=P+100000
        print("Your points are:",P)
    else :
        print("Galat jawab...\nYou are Out..")
        break
time.sleep(30) 
print("Your wining price is: ",P)
print("You complete the game with 3 rounds...")
time.sleep(60) 