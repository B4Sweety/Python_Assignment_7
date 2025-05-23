Double = lambda iNo : 2*iNo

def main():
    Data = []
    print("Enter number of elements : ")
    iLength = int(input())

    print("Please enter numeric values : ")
    for iCnt in range(iLength):
        iValue = int(input())
        Data.append(iValue)
    print("List of interger is : ",Data)

    MData = list(map(Double,Data))
    print("Doubled List : ",MData)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_7>python 7_2.py
Enter number of elements :
5
Please enter numeric values :
1
2
3
4
5
List of interger is :  [1, 2, 3, 4, 5]
Doubled List :  [2, 4, 6, 8, 10]

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_7>

'''