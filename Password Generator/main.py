import random

def main():
    while True:
        lowercase_letters="abcdefghijklmnopqrstuvwxyz"
        uppercase_letters=lowercase_letters.upper()
        nums="0123456789"
        symbol="!@#$%^&*()_+<>?/"
        print("-------PASSWORD GENERATOR-------\n")
        user=int(input('Enter length of the password: '))
        generator=[]
        generator.extend(lowercase_letters)
        generator.extend(uppercase_letters)
        generator.extend(nums)
        generator.extend(symbol)

        password="".join(random.sample(generator,user))
        print(f"\nYour Password: {password}")
        print('-'*32,'\n')


if __name__=="__main__":
    main()