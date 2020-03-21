from textmining.controller import Controller

if __name__ == '__main__':
    def print_menu():
        print('0,Exit')
        print('1, 사전 다운로드')
        print('2, 삼성 전략보고서 분석')
        return input('Select Menu\n')
    app = Controller()
    while 1:
        menu = print_menu()
        if menu =='1':
            app.download_dictionary()
        if menu =='2':
            app.data_analysis()
        elif menu == '0':
            break