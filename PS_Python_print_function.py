# The included code stub will read an integer, n, from STDIN.
#
# Without using any string methods, try to print the following:
#123....n
#
# Note that "..." represents the consecutive values in between.
#
# Example
#n=5
# Print the string .
#12345
# Input Format
#
# The first line contains an integer "n" .
#
# Constraints
#1<=n<=150
#
# Output Format
#
# Print the list of integers from 1 through "n" as a string, without spaces.

if __name__ == '__main__':
    n = int(input())
    result = 0
    for i in range(1,n+1):
        if i <=9:
            result = result*10+i
        elif i <=99:
            result = result*100+i
        else:
            result = result*1000+i
    print(result)
