from calcaulator.controller import Controller
if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. Calculator')
        print('2. TensorCalculate')
        return input('메뉴선택 \n')
    while 1:
        menu = print_menu()
        if menu == '0':
            break
        if menu == '1':
            app = Controller()
            print('계산기 작동')
            num1 = int(input('첫번째 수\n'))
            opcode = input('연산자\n')
            num2 = int(input('두번째 수\n'))
            result = app.exec(num1, num2, opcode)
            print('결과: %d' % result)
        if menu == '2':
            app = Controller()
            print('계산기 작동')
            num1 = int(input('첫번째 수\n'))
            opcode = input('연산자\n')
            num2 = int(input('두번째 수\n'))
            result = app.tensorExec(num1, num2, opcode)
            print('결과: %d' % result)