"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride.
Each person wears a sticker indicating their initial position in the queue.
Initial positions increment by  from  at the front of the line to  at the back.

Any person in the queue can bribe the person directly in front of them to swap positions.
If two people swap positions, they still wear the same sticker denoting their original places in line.
One person can bribe at most two others. For example, if  and  bribes , the queue will look like this: .

Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get
the queue into its current state. If anyone has bribed more than two people, the line is too chaotic to compute the answer.

Function Description

Complete the function minimumBribes in the editor below.

minimumBribes has the following parameter(s):

int q[n]: the positions of the people after all bribes
Returns

No value is returned. Print the minimum number of bribes necessary or Too chaotic if someone has bribed more than  people.
Input Format

The first line contains an integer , the number of test cases.

Each of the next  pairs of lines are as follows:
- The first line contains an integer , the number of people in the queue
- The second line has  space-separated integers describing the final state of the queue.

"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.


def minimum_bribes(q):
    total_bribes = 0
    for i, j in enumerate(q):
        if j - i > 3:
            return print('Too chaotic')
        for k in range(max(j - 2, 0), i):
            if j < q[k]:
                total_bribes += 1
    print(total_bribes)


def minimum_bribes2(l):
    for i in range(len(l)):
        if l[i] - i > 3:
            print('Too chaotic')
            return

    def msort(low, high):
        def merge(low, mid, high):
            nonlocal inversions
            temp = list()
            i = low
            j = mid + 1
            while i <= mid and j <= high:
                if l[i] <= l[j]:
                    temp.append(l[i])
                    i += 1
                else:
                    temp.append(l[j])
                    j += 1
                    inversions += (mid+1) - i
            while i <= mid:
                temp.append(l[i])
                i += 1
            while j <= high:
                temp.append(l[j])
                j += 1
            for e in temp:
                l[low] = e
                low += 1

        if low < high:
            mid = (low + high) // 2
            msort(low, mid)
            msort(mid + 1, high)
            merge(low, mid, high)

    print(inversions)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimum_bribes(q)
