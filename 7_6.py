PrimeNumbers = lambda iNo: iNo > 1 and all(iNo % iCnt != 0 for iCnt in range(2, iNo))

def main():
    Data = []
    print("Enter number of elements : ")
    iLength = int(input())

    print("Please enter numeric values : ")
    for iCnt in range(iLength):
        iValue = int(input())
        Data.append(iValue)
    print("List of interger is : ",Data)

    FData = list(filter(PrimeNumbers,Data))
    print("Prime Numbers : ",FData)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_7>python 7_6.py
Enter number of elements :
8
Please enter numeric values :
10
11
12
13
14
15
16
17
List of interger is :  [10, 11, 12, 13, 14, 15, 16, 17]
Prime Numbers :  [11, 13, 17]

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_7>

'''