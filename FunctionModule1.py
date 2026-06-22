import Marvellous

def main():
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Ret = Marvellous.Addition(Value1 , Value2)

    print("Addition is : ",Ret)
    
if __name__ == "__main__":
    main()
