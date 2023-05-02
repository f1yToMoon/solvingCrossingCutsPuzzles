import PySimpleGUI as psg
import noNoiseSolution


psg.theme('SandyBeach')
layout = [[psg.Text('Введите количество разрезов', font='Default 12'), psg.InputText(key='num_cuts', justification='r')]] + \
         [[psg.Text('Введите размер головоломки x*y', font='Default 12'), psg.InputText(key='a', justification='r'), psg.InputText(key='b', justification='r')]] + \
         [[psg.Button('Собрать')]] + \
         [[psg.Image('pictures/initial.png', key='init_img', visible=False, size=(10, 10))]] + \
         [[psg.Image('pictures/0.png', key='i_img', visible=False, size=(10, 10))]] + \
         [[psg.Button('Назад', visible=False, key='back_but'), psg.Button('Далее', visible=False, key='next_but')]]

n = 0
max_n = 0
data = []

num_cuts = 0
a = 0
b = 0

window = psg.Window('crossingCutsPuzzles', layout, size=(900, 750), default_element_size=(8, 1), element_padding=(1, 1), return_keyboard_events=True)
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break

    if event == 'Собрать':
        # считываем данные с GUI
        num_cuts = int(values['num_cuts'])
        a = float(values['a'])
        b = float(values['b'])

        # запускаем алгоритм
        data = noNoiseSolution.noNoiseAlgorithm(num_cuts, a, b)

        #max_n = len(data) - 1
        max_n = data - 1

        # отображаем результаты
        window['init_img'].update('pictures/initial.png', visible=True)
        window['i_img'].update('pictures/0.png', visible=True)
        if max_n > 0:
            window['back_but'].update(visible=True, disabled=True)
            window['next_but'].update(visible=True, disabled=False)

    # логика кнопки "Назад"
    if event == 'back_but':
        n -= 1
        window['i_img'].update(f'pictures/{n}.png')
        window['next_but'].update(disabled=False)
        if n == 0:
            window['back_but'].update(disabled=True)

    # логика кнопки "Далее"
    if event == 'next_but':
        n += 1
        window['i_img'].update(f'pictures/{n}.png')
        window['back_but'].update(disabled=False)
        if n == max_n:
            window['next_but'].update(disabled=True)

window.close()