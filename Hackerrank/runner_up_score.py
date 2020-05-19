if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    scores = list(arr)
    
    scores.sort()
    
    scores_minus_duplicates = list(dict.fromkeys(scores))

    print(scores_minus_duplicates[-2])