'''
In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

Function Description

aVeryBigSum has the following parameter(s):

int ar[n]: an array of integers .
Return

long: the sum of all array elements
Input Format

The first line of the input consists of an integer .
The next line contains  space-separated integers contained in the array.

Output Format

Return the integer sum of the elements in the array.

Constraints


Sample Input

5
1000000001 1000000002 1000000003 1000000004 1000000005
Output

5000000015
'''

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

ar = [5, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
print ('---> no. de elementos: ', ar[0])
print ('---> elementos: ', ar[1])
print (type(ar))

def aVeryBigSum(ar):
    # Write your code here
    i = 1
    resultado = 0 
    for i in range(len(ar)):
        resultado += ar[i]
    print(resultado)
    
aVeryBigSum(ar)

#  5000000015
#  5000000020

