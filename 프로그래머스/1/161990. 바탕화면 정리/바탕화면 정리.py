def solution(wallpaper):
    # '#'이 wallpaper 중 처음 등장할 때의 인덱스 lux에 저장
    # '#'이 등장하는 행 중 가장 작은 인덱스 luy에 저장
    # '#'이 wallpaper 중 마지막 등장할 때의 인덱스 + 1 rdx에 저장
    # '#'이 등장하는 행 중 가장 큰 인덱스 + 1 rdy에 저장
    
    lux, luy, rdx, rdy = len(wallpaper), len(wallpaper[0]), 0, 0

    for i, f in enumerate(wallpaper):
        if "#" in f:
            lux = min(lux, i)
            luy = min(luy, f.index("#"))
            rdx = max(rdx, i)
            rdy = max(rdy, f.rindex("#"))
    
    return [lux, luy, rdx + 1, rdy + 1]