def add(num1,num2):
    print('Addition : ',num1+num2)
    return main()
def sub(num1,num2):
    print('Subtraction : ',num1-num2)
    return main()
def mul(num1,num2):
    print('Multiplication : ',num1*num2)
    return main()
def div(num1,num2):
    print('Division : ',num1/num2)
    return main()
def main():
    print('\n')
    print('*'*60)
    while True:
        num1=float(input("Enter first number : "))
        num2=float(input("Enter second number : "))
        print('\n Basic Calculator')
        print('*'*20)
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division')
        print('5. Exit')
        select=input('Select Operations : ')
        print('\n')
        print('*'*60)
        match select:
            case'1':
                add(num1,num2)
            case'2':
                sub(num1,num2)
            case'3':
                mul(num1,num2)
            case'4':
                div(num1,num2)           
            case'5':
                break
            case'6':
                print('Invailid input')
        
if __name__==("__main__"):
    main()