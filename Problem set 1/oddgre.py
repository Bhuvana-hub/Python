"""'""
Write a program that examines three variables—x, y, and z— and
prints the largest odd number among them. If none of them are odd,
it should print a message to that effect"""
import math

def oddfind(x,y,z):
    s1=x%2
    s2=y%2
    s3=z%2
    if(s1!=0) and (s2!=0) and (s3!=0) :
        a=max(x,y,z)
        return a
    elif(s1!=0) and (s2!=0) and(s3==0):
        a=max(x,y)
        return a
    elif(s1!=0) and (s2==0) and(s3!=0):
        a = max(x, z)
        return a
    elif(s1==0) and (s2!=0) and(s3!=0):
        a = max(y, z)
        return a
    else:
        return  0

def main():
    print("To get Three Largest Odd Number")
    x = int(input("Enter the number1 \n"))
    y = int(input("Enter the number2 \n"))
    z = int(input("Enter the number3 \n"))
    m=oddfind(x,y,z)
    if m==0:
        print("All 3 Numbers are not odd number")
    else:
        print("The Largest Number", m)

if __name__ == '__main__':
    main()