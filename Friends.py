num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]

def mean_num_friends(x):
    count_friends = len(x)
    sum = 0
    
    for eachx in x:
        sum = sum + eachx
    
    mean = sum/count_friends
    print("mean = %.2f" %mean)

def median_num_friends(x):
    x.sort()
    count_friends = len(x)
    mod = count_friends%2
    
    if mod == 0:
        index = int(count_friends/2)
        median = (x[index-1]+x[index])/2
        print("median = %.2f" %median)
    else:
        index = int(count_friends/2)
        median = x[index]
        print("median = %d" %median)
            
mean_num_friends(num_friends)
median_num_friends(num_friends)