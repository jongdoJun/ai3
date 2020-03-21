from algorythm.dtree import DTree

if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. 결정트리')
        print('2. 결정트리1')
        return input('메뉴 선택 \n')


    #app = Controller()
    while 1:
        menu = print_menu()
        if menu == '1':
            app = DTree().breast_cancer()

        if menu == '2':
            app = DTree().iris()
        if menu == '3':
            pass
        if menu == '5':
            pass

        elif menu == '0':
            break