##print("Enter 'c' to convert from Celsius to Farenheit")
##print("Enter 'f' to convert from Fahrenheit to Celsius")
##choice=input("Enter your choice:")
##if choice=='c':
##    celsius=float(input("Enter temperature in celsius: "))
##    fahrenheit=(celsius*9/5)+32
##    print('%.2f Celsius is:%0.2f Fahrenheit'%(celsius,fahrenheit))
##elif choice=='f':
##    fahrenheit=float(input("Enter temperature in Fahrenheit:"))
##    celsius=(fahrenheit+32)*5/9
##    print('%.2f Fahrenheit is:%0.2f Celsius'%(fahrenheit,celsius))
##else:
##    print("Invalid imput")
##
##
##
##a=int(input("Enter marks obtained in subject 1:"))
##b=int(input("Enter marks obtained in subject 2:"))
##c=int(input("Enter marks obtained in subject 3:"))
##d=int(input("Enter marks obtained in subject 4:"))
##e=int(input("Enter marks obtained in subject 5:"))
##tot=a+b+c+d+e
##per=(tot/500)*100
##if per>=80:
##    print('Grade A')
##elif per>=70:
##    print('Grade B')
##elif per>=60:
##    print('Grade C')
##elif per>=40:
##    print('Grade D')
##else:
##    print("Grade E")


###area of rectangle
##l=int(input('enter length'))
##b=int(input('enter breadth'))
##a=l*b
##print('Area of rectangle is',a)
##
###area of square
##a=int(input('enter length of square'))
##print('Area of Square is',a*a)
##
###area of circle
##r=int(input('enter radius'))
##a=3.14*r*r
##print('Area of circle',a)
##
###area of triangle
##base=int(input('enter base'))
##height=int(input('enter height'))
##a=1/2*base*height
##print("Area of Triangle",a)

n=int(input('enter no.of terms'))
f1=0
f2=1
count=0
while count<n:
    f1,f2=f2,f1+f2
    count+=1
    print(f1,end=" ")










