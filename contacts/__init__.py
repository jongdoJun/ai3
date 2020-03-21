from contacts.controller import Controller
if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. 연락처 추가')
        print('2. 연락처 목록')
        print('3. 연락처 삭제')
        return input('메뉴 선택 \n')


    app = Controller()
    while 1:
        menu = print_menu()
        if menu == '1':
            app.register(input('이름\n'),
                         input('전화번호\n'),
                         input('이메일\n'),
                         input('주소\n'))
        if menu == '2':
            print(app.list())
        if menu == '3':
            app.remove(input('삭제할 이름\n'))
        elif menu == '0':
            break