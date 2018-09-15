def triangularNumbers(m, n):
    triangulars = []
    t = 1
    while(True):
        i = int((t * (t+1)) / 2)
        if i > n:
            print(triangulars)
            return triangulars
                
        if i >= m:
            triangulars.append(i)
            t = t + 1
            print(triangulars)
