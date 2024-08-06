def solution(sizes):
    # 각 리스트 max의 최댓값과 각 리스트 min의 최댓값을 곱해서 리턴
    return max(max(s) for s in sizes) * max(min(s) for s in sizes)