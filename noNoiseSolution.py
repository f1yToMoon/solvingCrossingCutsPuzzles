import cv2
import random


def get_matrix(n, p):
    # функция считывает изображение и возвращает матрицу полутонов каждого пикселя
    adress = 'C:/Users/magla/Downloads/database/s' + str(n) + '/' + str(p) + '.pgm'
    img = cv2.imread(adress)
    #matrix = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


print(get_matrix(1, 1))


class Side:
    def __init__(self, colors_amount, colors, len, angles):
        self.colors_amount = colors_amount
        self.colors = colors # цвета слева на право [color, pix start]
        self.len = len
        self.angles = angles # (l_ang, r_ang) смотрим на сторону со внешней стороны куска


class Piece:
    def __init__(self, sides):
        self.sides = sides
        self.sides_amount = len(sides)


p1_sides = [Side(0, [], 2, [90, 90]),
            Side(0, [], 1, [90, 127]),
            Side(0, [], 2.5, [127, 53]),
            Side(0, [], 2.5, [53, 90])]

p2_sides = [Side(0, [], 4, [90, 90]),
            Side(0, [], 2.5, [90, 127]),
            Side(0, [], 2.5, [127, 143]),
            Side(0, [], 2, [143, 90]),
            Side(0, [], 4, [90, 90])]

p3_sides = [Side(0, [], 2.5, (127, 53)),
            Side(0, [], 3, (53, 90)),
            Side(0, [], 2, (90, 90)),
            Side(0, [], 1.5, (90, 127))]

p4_sides = [Side(0, [], 2.5, (37, 53)),
            Side(0, [], 1.5, (53, 90)),
            Side(0, [], 2, (90, 37))]

p1 = Piece(p1_sides)
p2 = Piece(p2_sides)
p3 = Piece(p3_sides)
p4 = Piece(p4_sides)

pieces = [p1, p2, p3, p4]
pairs = {}
tru_pairs = []
fours = []
sol = []


def compare(piece1, np1, piece2, np2):
    """записывает пары сторон в массивы"""
    n = 0
    for s1 in range(len(piece1.sides)):
        for s2 in range(len(piece2.sides)):
            if piece1.sides[s1].len == piece2.sides[s2].len and \
               piece1.sides[s1].angles[0]+piece2.sides[s2].angles[1] == 180 and \
               piece1.sides[s1].angles[1]+piece2.sides[s2].angles[0] == 180 and \
               [[piece1, s1], [piece2, s2]] not in pairs:
                    pairs.append([[np1, s1], [np2, s2]])#, piece1.sides[s1].len])
                    n += 1
    if n == 1:
        p = pairs[len(pairs)-1]
        pairs.remove(p)
        if p not in tru_pairs:
            tru_pairs.append(p)


def line_x(y, x1, y1, x2, y2):
    return (y-y1)*(x2-x1)/(y2-y1) + x1


def line_y(x, x1, y1, x2, y2):
    return (x-x1)*(y2-y1)/(x2-x1) + y2


def generate_cuts(num_cuts, a, b):
    cuts = []
    choise_x = [a, 0]
    choise_y = [b, 0]
    for i in range(num_cuts):
        cut = []
        # точка на оси х
        ch = random.randint(0, 1)
        x = round(random.uniform(0.001, a - 0.001), 3)
        y = choise_y[ch]
        cut.append((x, y))
        # точка на оси y
        ch = random.randint(0, 1)
        x = choise_x[ch]
        y = round(random.uniform(0.001, b-0.001), 3)
        cut.append((x, y))
        cuts.append(cut)
    return cuts


def main():
    # генерируем
    cuts = generate_cuts(3, 10, 5)
    print(cuts)

    cross_points = []
    #for i in range(len(cuts)):
        #for j in range(i+1, len(cuts)):






    for i in range(len(pieces)):
        for j in range(i+1, len(pieces)):
            if i != j:
                compare(pieces[i], i, pieces[j], j)
    '''
    for i in range(len(tru_pairs)):
        for j in range(i+1, len(tru_pairs)):
            four = [tru_pairs[i], 0, 0]
            four[2] = tru_pairs[j]
            if tru_pairs[i][0][0] != tru_pairs[j][0][0] and \
               tru_pairs[i][0][0] != tru_pairs[j][1][0] and \
               tru_pairs[i][1][0] != tru_pairs[j][0][0] and \
               tru_pairs[i][1][0] != tru_pairs[j][1][0]:

                
                for el in pairs:
                    if (tru_pairs[i][0][0] == el[0][0] and (el[1][0] == tru_pairs[j][0][0] or el[1][0] == tru_pairs[j][1][0]) and el[0][1] == )  or \
                       (tru_pairs[i][0][0] == el[1][0] and (el[0][0] == tru_pairs[j][0][0] or el[0][0] == tru_pairs[j][1][0])): # ищу с кем смержить кусочки из противоположного мержа
                        lenp_i = pieces[tru_pairs[i][0][0]].sides_amount
                        lenp_j = pieces[tru_pairs[j][0][0]].sides_amount
                        if 

                    if (tru_pairs[i][1][0] == el[0][0] and (el[1][0] == tru_pairs[j][0][0] or el[1][0] == tru_pairs[j][1][0])) or \
                       (tru_pairs[i][1][0] == el[1][0] and (el[0][0] == tru_pairs[j][0][0] or el[0][0] == tru_pairs[j][1][0])):
            
            if len(four) == 4 and four[1] != 0:
                pairs.remove(four[1])
                pairs.remove(four[3])
                for elem in four:
                    if elem not in sol:
                        sol.append(elem)
                        '''


    compare(p1, 0, p2, 1)
    print(pairs)
    print('=====')
    print(tru_pairs)


if __name__ == '__main__':
    main()


