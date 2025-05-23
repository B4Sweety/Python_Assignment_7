from functools import reduce 

Product = lambda iNo1, iNo2 : iNo1*iNo2

def main():
    Data = []
    print("Enter number of elements : ")
    iLength = int(input())

    print("Please enter numeric values : ")
    for iCnt in range(iLength):
        iValue = int(input())
        Data.append(iValue)
    print("List of interger is : ",Data)

    RData = reduce(Product,Data)
    print("Product : ",RData)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_7>python 7_4.py
Enter number of elements :
3
Please enter numeric values :
2
3
4
List of interger is :  [2, 3, 4]
Product :  24

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_7>

'''