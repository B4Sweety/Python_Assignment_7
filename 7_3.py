EvenNumbers = lambda iNo : iNo % 2 == 0

def main():
    Data = []
    print("Enter number of elements : ")
    iLength = int(input())

    print("Please enter numeric values : ")
    for iCnt in range(iLength):
        iValue = int(input())
        Data.append(iValue)
    print("List of interger is : ",Data)

    FData = list(filter(EvenNumbers,Data))
    print("Even numbers : ",FData)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_7>python 7_3.py
Enter number of elements :
6
Please enter numeric values :
1
2
3
4
5
6
List of interger is :  [1, 2, 3, 4, 5, 6]
Even numbers :  [2, 4, 6]

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_7>

'''