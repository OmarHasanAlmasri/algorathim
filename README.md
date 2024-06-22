Hotel Finder :A Hotel Sorting and Search Engine

1. Introduction: 
HotalFinder is a comprehensive hotel search and sorting system designed to help users efficiently find and rank hotels based on various criteria.
 By leveraging sorting algorithms and search techniques, Hotel finder  1)ensures quick and  2)accurate retrieval of hotel information, thereby enhancing the user experience.
Informally, an algorithm is any well-defined computational procedure that takes some value, or set of values, as input and produces some value,
or set of values, as output. An algorithm is thus a sequence of computational steps that transform the input into the output.

Input: A sequence of n numbers(h1, h2,….,hn)
Output: A permutation (reordering) (h`1, h`2,….,h`n) of the input sequence such that h`1<= h`2<= h`n.[1]

2.Binary Search:
Binary search has the advantage that it takes only O(logn) time to search an n-element array.[2]
BINARY-SEARCH(A,n,x)
Inputs and Output : Same as Linear-Search.
1.	Set p to 1, and set r to n .
2.	While p <=r ,do the following : 
    A.Set q to [(p+r)/2].
    B. Otherwise (A[q] != x), if  A[q] >x , then set r to q-1.
    D. Otherwise (A[q] < x),set p to q + 1.
3.	Return Not -Found. [3]

3.Bubble sort :
Another brute-force application to the sorting problem is to compare adjacent elements of the list and exchange them if they are out of order.
By doing it repeatedly, we end up “bubbling up” the largest element to the last position on the list. The next pass bubbles up the second largest element, 
and so on, until after n − 1 passes the list is sorted.[4]

ALGORITHM Bubble Sort(A[0..n − 1])
 #Sorts a given array by bubble sort 
#Input: An array A[0..n − 1] of orderable elements 
#Output: Array A[0..n − 1] sorted in nondecreasing order
 for i ← 0 to n − 2 do
       for j ← 0 to n − 2 − i do 
              if A[j + 1] < A[j ] swap A[j ] and A[j + 1] . [4]


              modified from omar hasan
