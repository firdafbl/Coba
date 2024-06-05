#jenis-jenis operator dlm python
#operator aritmatika:
print(20/5) #bisa langsung print tanpa tmbhn variabel
print()

a = 10
b = 3
hasil = a+b
print(a,"+",b,"=",hasil) #+ dan = adalah string
print()

print(6+2)   #8(tambah)
print(6-2)   #4(kurang)
print(6*2)   #12(kali)
print(6/2)   #3.0(bagi)
print(6**2)  #36(perpangkatan)
print(6%2)   #1(sisa bagi)
print(10//3) #3

#contoh:
a = 11
b = 3

hasil = a+b
print(a,"+",b,"=",hasil)

hasil = a-b
print(a,"-",b,"=",hasil)

hasil = a*b
print(a,"*",b,"=",hasil)

hasil = a/b
print(a,"/",b,"=",hasil)

hasil = a**b
print(a,"**",b,"=",hasil)

hasil = a%b
print(a,"%",b,"=",hasil)

hasil = a//b
print(a,"//",b,"=",hasil)
print()

#prioritas operasi, operational precendence
x = 3 
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//",x, "=", hasil)
print()

hasil = x + y * z 
print(x, "+", y, "*", z, "=", hasil) #perkalian didahulukan
print()

hasil = (x + y) * z 
print("(",x, "+", y,")", "*", z, "=", hasil) #yg didlm kurung didahulukan

#(x ** y) * z + x / y - y % (z // x)
#(3**2) * 4 + 3 / 2 - 2 % (4 // 3)
#(9*4) + (3/2) - (2%1)
#36 + 1.5 - 0 = 37.5