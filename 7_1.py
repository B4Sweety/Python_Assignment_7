Square = lambda iNo : iNo*iNo

Cube = lambda iNo : iNo**3

def main():
    print("Enter number : ")
    iValue = int(input())

    iRet = Square(iValue)
    print("Square : ",iRet)

    iRet = Cube(iValue)
    print("Cube : ",iRet)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_7>python 7_1.py
Enter number :
3
Square :  9
Cube :  27

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_7>python 7_1.py
Enter number :
4
Square :  16
Cube :  64

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_7>

'''