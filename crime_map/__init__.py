from crime_map.controller import Controller
from crime_map.folium_test import Folium_test

if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. DF 전환')
        print('2. 모델링')
        print('3. 정규분포')
        print('4. 범죄지도')
        print('5. 미국 실업률 지도')
        return input('메뉴 선택 \n')


    app = Controller()
    while 1:
        menu = print_menu()
        if menu == '1':
            app.convert_df()
        if menu == '2':
            app.modeling()
        if menu == '3':
            pass
        if menu == '5':
            t= Folium_test()
            t.show_map()

        elif menu == '0':
            break