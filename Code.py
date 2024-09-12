import random
x=input("do you want create your own food list press 1\ndo you want to go with computers food list press 2\nif you want to go with both food press 3:\n")
if x=="1":
    s="yes"
    b_f=[]
    l=[]
    d=[]
    while s.lower()=='yes':
        k=input("which time food do you want to enter\nfor breakfast(b)\nfor lunch (l)\nfor dinner(d):\n")
        f=input("enter your food list seperated by comma:").split(",")
        for m in f:
            if k.lower()=='b':
                b_f.append(m)
            elif k.lower()=='l':
                l.append(m)
            elif k.lower()=='d':
                d.append(m)
            else:
                print("you does not entered any list")
        if len(b_f)==0:
            print("You have to enter the list of food for breakfast because breakfast list is Empty.")
            s="YES"
        elif len(l)==0:
            print("You have to enter the list of food for lunch because lunch list is Empty")
            s="YES"
        elif len(d)==0:
            print("You have to enter the list of food for dinner because dinner list is Empty")
            s="YES"
        elif len(d)>0 and len(l)>0 and len(b_f) >0:
            s=input("do you want to enter more foods yes/no:")
elif x=="2":
    b_f = [["Gobhi/Mooli Paratha","pickle","Milk"],["sandwich","banana","tea"],["aloo sabzi","plane paratha","tea"],["poori","sabzi","tea"],["aloo paratha/pyaaz paratha","tea & milk"],["methi paratha ","tea","fruit"],["chhola","bhatura","tea"]]
    l= [["rajma","aloo gajar","roti","rice","salad","raita"],["chhole","kaddu veg","puri","rice","salad","raita"],["mix dal","aloo bandgobbhi","rice","roti","salad"],["kadhi pakoda","aloo","jeera rice","roti","salad"],["dal makhni","mix veg","rice","roti","salad","raita"],["aloo channa","dal mix","rice","roti","salad"],["fried rice/veg biryani","raita","roti","salad"]]
    d=[["dal arahar", "palak aloo veg","rice","roti","salad"],["chhana dal","soyabean aloo","rice","roti","salad"],["masoor dal","aloo gobhi","kheer","rice","roti","salad"],["dal arhar","lauki kofta","rice","roti","salad","gulab jamun"],["aloo methi/saag","urad dal","rice","roti","salad"],["daal moong","mix vef/spring onion(green onion)","rice","roti","salad"],["palak paneer/matar paneer/soya chaap", "pulao","rice","roti","salad" "halwa"]]
elif x=="3":
    b_f = [["Gobhi/Mooli Paratha","pickle","Milk"],["sandwich","banana","tea"],["aloo sabzi","plane paratha","tea"],["poori","sabzi","tea"],["aloo paratha/pyaaz paratha","tea & milk"],["methi paratha ","tea","fruit"],["chhola","bhatura","tea"]]
    l= [["rajma","aloo gajar","roti","rice","salad","raita"],["chhole","kaddu veg","puri","rice","salad","raita"],["mix dal","aloo bandgobbhi","rice","roti","salad"],["kadhi pakoda","aloo","jeera rice","roti","salad"],["dal makhni","mix veg","rice","roti","salad","raita"],["aloo channa","dal mix","rice","roti","salad"],["fried rice/veg biryani","raita","roti","salad"]]
    d=[["dal arahar", "palak aloo veg","rice","roti","salad"],["chhana dal","soyabean aloo","rice","roti","salad"],["masoor dal","aloo gobhi","kheer","rice","roti","salad"],["dal arhar","lauki kofta","rice","roti","salad","gulab jamun"],["aloo methi/saag","urad dal","rice","roti","salad"],["daal moong","mix vef/spring onion(green onion)","rice","roti","salad"],["palak paneer/matar paneer/soya chaap", "pulao","rice","roti","salad" "halwa"]]
    a="yes"
    while a=="yes":
        k=input("which time food do you want to enter\nfor breakfast(b)\nfor lunch (l)\nfor dinner(d):\n")
        f=input("enter your food list seperated by comma:").split(",")
        for m in f:
            if k.lower()=='b':
                b_f.append(m)
            elif k.lower()=='l':
                l.append(m)
            elif k.lower()=='d':
                d.append(m)
            else:
                print("you does not selected any list")
        a=input("do you want to enter more food? yes/no:")
b_f1 = random.choice(b_f)
l1 = random.choice(l)
d1 = random.choice(d)
day=input("enter today's day:")
listw=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
j=0
for i in range (7):
    if listw[i]==day.lower():
        print("\nToday is",day,"I suggest you:\nIn breakfast:",b_f1,"\nIn lunch:",l1,"\nIn dinner",d1)
        j=0
        break
        fg=1
    else:
        j=j+1
if j>0:
    print("you entered wrong day")
