import numpy

num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]

def mean_num_friends(x):
    count_friends = len(x)
    sum = 0
    
    for each_x in x:
        sum = sum + each_x
    
    mean = sum/count_friends
    print("mean = %f" %mean)
    
    mean_numpy = numpy.mean(x)
    print("mean using python's numpy lib= %f" %mean_numpy)

def median_num_friends(x):
    x.sort()
    count_friends = len(x)
    mod = count_friends%2
    
    if mod == 0:
        index = int(count_friends/2)
        median = (x[index-1]+x[index])/2
    else:
        index = int(count_friends/2)
        median = x[index]
    
    print("median = %f" %median)
    
    median_numpy = numpy.median(x)
    print("median using python's numpy lib = %f" %median_numpy)
            
mean_num_friends(num_friends)
print("\n")
median_num_friends(num_friends)