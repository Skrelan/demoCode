# /********************************************************************** 
#  *                                                                    *
#  *                                                                    *
#  *  Problem: Insertion Sort                                           *
#  *                                                                    *
#  *  Prompt: Given an unsorted array of numbers,                       *
#  *          return a sorted array using insertion sort.               *
#  *                                                                    *
#  *  Input:  An unsorted array                                         *
#  *  Output: A sorted array                                            *
#  *                                                                    *
#  *  Example: input = [3,9,1,4,7] , output = [1,3,4,7,9]               *
#  *                                                                    *
#  *  What are the time and auxilliary space complexity?                *
#  *  Time = O(N^2) Space= O(1)                                         *
#  **********************************************************************/

#  /**********************************************************
#   *                                                        *
#   *  Problem: Selection Sort                               *
#   *                                                        *
#   *  Prompt: Given an unsorted array of numbers,           *
#   *          return a sorted array using insertion sort.   *
#   *                                                        *
#   *  Input: An unsorted array                              *
#   *  Output: A sorted array                                *
#   *                                                        *
#   *  Example: input = [8,3,2,10] output = [2,3,8,10]       *
#   *                                                        *
#   *  What are the time and auxilliary space complexity?    *
#   *  What is the best case time complexity?                *
#   * Time = O(N^2) Space= O(1)                              *
#   **********************************************************/

#  /**********************************************************
#   *                                                        *
#   *  Problem: Bubble Sort                                  *
#   *                                                        *
#   *  Prompt: Given an unsorted array of numbers,           *
#   *          return a sorted array using bubble sort.      *
#   *                                                        *
#   *  Input: An unsorted array                              *
#   *  Output: A sorted array                                *
#   *                                                        *
#   *  Example: input = [8,3,2,10] output = [2,3,8,10]       *
#   *                                                        *
#   *  What are the time and auxilliary space complexity?    *
#   *  Time = O(N^2) Space= O(1)                             *
#   **********************************************************/

def insertionSort(input):
  # your work here
  for i in range( 1, len( input ) ):
    tmp = input[i]
    k = i
    while k > 0 and tmp < input[k - 1]:
        input[k] = input[k - 1]
        k -= 1
    input[k] = tmp

def selectionSort(input):
  # your work here
  for i in range( len( input ) ):
    least = i
    for k in range( i + 1 , len( input ) ):
      if input[k] < input[least]:
        least = k
 
    swap( input, least, i ) 

def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

def bubbleSort(input):
  # your work here
  for i in range( len( input ) ):
    for k in range( len( input ) - 1, i, -1 ):
      if ( input[k] < input[k - 1] ):
        swap( input, k, k - 1 )