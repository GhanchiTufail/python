def main(num):

    def f(num):

        if num == 0:
            return 0
        else:
            return f(num - 1) + 100
    print(f(num))

if __name__ == '__main__':
    try:
        num = int(input('Enter any number: '))
        main(num)
    except ValueError:  
        print('Check Value')