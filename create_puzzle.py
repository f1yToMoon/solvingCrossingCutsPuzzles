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
        cut.append([x, y])
        
        # точка на оси y
        ch = random.randint(0, 1)
        x = choise_x[ch]
        y = round(random.uniform(0.001, b-0.001), 3)
        cut.append([x, y])
        cuts.append(cut)
    return cuts
 
cuts = generate_cuts(n, a, b)

def line_intersection(line1, line2, a, b):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
    
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return False
    else: 
        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
    if x < 0 or y < 0 or x > a or y > b:
        return False
    return [x, y]
 
points = [[0, 0],
         [0, b],
         [a, 0],
         [a, b]]

lines = [[] for _ in range(len(cuts) + 2)] 

m = [[], []]
intersect = []

for i in range(len(cuts)):
    points.append(cuts[i][0])
    points.append(cuts[i][1])
    
k = 0    
for i in range(len(cuts)):
    for j in range(i+1, len(cuts)):
        p = line_intersection(cuts[i], cuts[j], a, b)
        if p != False:
            points.append(p)
            intersect.append(p)
            k = k + 1
            lines[i].append(p)
            lines[j].append(p)
    lines[i].append(cuts[i][0])
    lines[i].append(cuts[i][1])        

graph_size = 4 + k + len(cuts)*2
graph = [[0 for _ in range(graph_size)] for arr in range(graph_size)]

for i in range(len(points)):
    if points[i][1] == b:
        m[0].append([points[i][0], points[i][1]])
    if points[i][1] == 0:
        m[1].append([points[i][0], points[i][1]])
    if points[i][0] == a:
        lines[len(cuts)].append([points[i][0], points[i][1]])
    if points[i][0] == 0:
        lines[len(cuts) + 1].append([points[i][0], points[i][1]])
    
for i in range(len(m)):   
    sorted(m[i], key=lambda x: x[0])

for i in range(len(lines)):
    sorted(lines[i], key=lambda x: x[1])
    
for i in range(len(m)):
    for j in range(1, len(m[i])):
        graph[points.index(m[i][j - 1])][points.index(m[i][j])] = 1
        graph[points.index(m[i][j])][points.index(m[i][j - 1])] = 1  
    
for i in range(len(lines)):
    for j in range(1, len(lines[i])):
        graph[points.index(lines[i][j - 1])][points.index(lines[i][j])] = 1
        graph[points.index(lines[i][j])][points.index(lines[i][j - 1])] = 1
