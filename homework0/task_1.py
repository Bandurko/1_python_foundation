# color = input('Твой любимый цвет: ')
# if color == 'красный':
#     print('Любитель яркого')
# elif color == 'зеленый':
#     print('Ты охотник?')
# elif color == 'синий':
#     print('Ха! Классика!')
# else:
#     print('Тебя не понять')


color = input('Твой любимый цвет: ')
match color:
    case 'красный':
        print('Любитель яркого')
    case 'зеленый':
        print('Ты охотник?')
    case 'синий':
        print('Ха! Классика!')
    case _:              # _ - означает любое другое значение
        print('Тебя не понять')