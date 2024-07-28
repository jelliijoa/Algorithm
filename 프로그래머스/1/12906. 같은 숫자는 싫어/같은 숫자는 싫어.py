def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for n in range(1, len(arr)):
        if arr[n-1] != arr[n]:
            answer.append(arr[n])
            
        elif (n == len(arr)-1) and (arr[n-1] != arr[n]):
            answer.append(arr[n-1])
            
    return answer
        