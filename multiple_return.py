import statistics
def mean_median_mode(list1):
    return statistics.mean(list1),statistics.median(list1),statistics.mode(list1)
    print("wohhhoooo")
    
#if we want the output in list form then
    # return [statistics.mean(list1),statistics.median(list1),statistics.mode(list1)]

a,b,c=mean_median_mode([3,5,7,9,1,25,98])
print([a,b,c])
print(f"Mean is {a}\nMedian is {b}\nMode is {c}")