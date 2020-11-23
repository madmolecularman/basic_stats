"""
Calculating standard deviation and normality of a user defined random set of integers
"""

def summary_stats(n="Enter integer here"):
    
    """
    Calculate STD and normality of a random set of integers
    % function ex = summary_stats(n)
    %- INPUT:
    % 1) One whole integer that defines how many random numbers to generate in the data set.
    %- OUTPUT:
    % 1) How many values are within +/- 1 std.
    % 2) How many values are not within +/- 1 std.
    % 3) The percent of values that fall within +/- 1 std.
    % 4) Is the data set normally distributed?
    % 5) Graph of ther data set
    """
    
    import numpy as np
    import matplotlib.pyplot as plt
    data = np.random.randint(low=1,high=100,size=n).astype(np.float)
    summation=0.0
    counter=0
    mean=0
    sumsq=0.0
    var=0.0
    sqsum=0.0
    std_list=[]
    for i in range(len(data)):
        summation+=data[i]
        counter+=1
    mean=(summation/counter)
    for i in range(len(data)):
        sumsq=((data[i]-mean)**2)
        std_list.append(sumsq)
    for i in range(len(std_list)):
        sqsum+=std_list[i]
    var=(sqsum/counter)
    std=(var**0.5)
    print('The average(mu) of this data list is: '+ str(mean) + ' and the standard deviation (sigma) is: ' + str(std))
    lower=(mean-std)
    upper=(mean+std)
    yes=0.0
    no=0.0
    for i in data:
        if i < (upper) and i > (lower):
            yes+=1
        else:
            no+=1
    print("These are how many values are within +/- 1 std: " + str(yes))
    print("These are how many values are not within +/- 1 std: " + str(no))
    # A normal distribution will have approx. 68% of the values within this range.  
    print("The percent of values that fall within +/- 1 std are: " + str((yes/counter)*100) + "%")
    # Based on this criteria is the list normally distributed?
    if ((yes/counter)) >= .68:
        print("This is normally distributed")
    else:
        print("This is not normally distributed")
    #Make a figure object
    fig = plt.figure()
    # make histogram plot with 10 bins
    plt.hist(data, bins=10)
    #Label x-axis
    plt.xlabel("Integers in [data]")
    #Label y-axis
    plt.ylabel("Count of intergers")
    #Label title
    plt.title('Histrogram of numbers');
    #Save the figure
    fig.savefig("normality_testing.png")
    print('Image save complete')
