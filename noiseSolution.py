def calculate_color_dissimilarity(side1, side2):
    it1, it2 = 0, 0
    dis_counter = 0
    col1 = side1.colors[0][0]
    col2 = side2.colors[0][0]
    for i in range(side1.len):
        if side1.colors[it1][1] == i:
            it1 += 1
            col1 = side1.colors[it1][0]
        if side2.colors[it2][1] == i:
            it2 += 2
            col2 = side2.colors[it2][0]
        if col1 != col2:
            dis_counter += 1
    return dis_counter


def calculate_len_dissimilarity(side1, side2):
    return abs(side1.len - side2.len)


def compare(piece1, piece2):
    for s1 in piece1.sides:
        for s2 in piece2.sides:
            if piece1.sides[s1].len == piece2.sides[s2].len:
                color_dis = calculate_color_dissimilarity(piece1.sides[s1], piece2.sides[s2])
            else:
                len_dis = abs(piece1.sides[s1].len - piece2.sides[s2].len)