from math import fabs

def dist(x1, y1, x2, y2):
    
    return pow(x2 - x1, 2) + pow(y2 - y1, 2)

if __name__ == "__main__":
    
    inp = open("boomerang_constellations.txt")
    output = open("output.txt", 'w+')
    
    T = int(inp.readline())
    
    for i in range(0, T):
        N = int(inp.readline())
        coords = []
        n = 0    
        for j in range(0, N):            
            xy = inp.readline().split(" ")
            coord = [int(xy[0]), int(xy[1])]
            coords.append(coord)
                        
        for c1 in coords:
            d = dict()
            for c2 in coords:                    
                distance = dist(c1[0], c1[1], c2[0], c2[1])
                    
                if fabs(distance - 0.0) > 0.00001:                        
                    d[distance] = 1 if not distance in d else d.get(distance) + 1                      
            for num in d.values():
                if num >= 2:
                    n += num * (num - 1) / 2
        output.write("Case #{0}: {1}\n".format(i + 1, n))
