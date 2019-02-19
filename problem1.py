sayi = int(input("reqemi daxil edin: "))
a  = sayi //1000
b = (sayi - a*1000)//100
c = (sayi - a*1000 - b*100)//10
d = sayi - a*1000 - b*100 - c*10
print("Reqemlerin toplami: ", a+b+c+d)
