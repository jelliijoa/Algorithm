def solution(sizes):
    # 각 리스트 max의 최댓값과 각 리스트 min의 최댓값을 곱해서 리턴
    return max(max(w, h) for w, h in sizes) * max(min(w, h) for w, h in sizes)