def solution(wallpaper):
    lux, luy, rdx, rdy = len(wallpaper), len(wallpaper[0]), 0, 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                if i < lux:
                    lux = i
                if j < luy:
                    luy = j
                if i + 1 > rdx:
                    rdx = i + 1
                if j + 1 > rdy:
                    rdy = j + 1
    return lux, luy, rdx, rdy