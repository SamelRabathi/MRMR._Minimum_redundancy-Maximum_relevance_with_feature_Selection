#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:52:40 2020

@author: samelrabathi
"""
class own_timsort():
    # based off of this code 
    #  https://gist.github.com/nandajavarma/a3a6b62f34e74ec4c31674934327bbd3
    # Brandon Skerritt
    # https://skerritt.tech
    
    def __init__(self, array):
        self.the_array = array
        
    
    def binary_search(the_array, item, start, end):
        if start == end:
            if the_array[start] > item:
                return start
            else:
                return start + 1
        if start > end:
            return start
    
        mid = round((start + end)/ 2)
    
        if the_array[mid] < item:
            return own_timsort.binary_search(the_array, item, mid + 1, end)
    
        elif the_array[mid] > item:
            return own_timsort.binary_search(the_array, item, start, mid - 1)
    
        else:
            return mid
    
    """
    Insertion sort that timsort uses if the array size is small or if
    the size of the "run" is small
    """
    def insertion_sort(the_array):
        l = len(the_array)
        for index in range(1, l):
            value = the_array[index]
            pos = own_timsort.binary_search(the_array, value, 0, index - 1)
            the_array = (the_array[:pos] + [value] + the_array[pos:index] +
                         the_array[index+1:])
        return the_array
    
    def merge(left, right):
        """Takes two sorted lists and returns a single sorted list by
        comparing the elements one at a time.
        """
        if not left:
            return right
        if not right:
            return left
        if left[0] < right[0]:
            return [left[0]] + own_timsort.merge(left[1:], right)
        return [right[0]] + own_timsort.merge(left, right[1:])
    
    def timsort(self):
        runs, sorted_runs = [], []
        length = len(self.the_array)
        new_run = [self.the_array[0]]
    
        # for every i in the range of 1 to length of array
        for i in range(1, length):
            # if i is at the end of the list
            if i == length - 1:
                new_run.append(self.the_array[i])
                runs.append(new_run)
                break
            # if the i'th element of the array is less than the one before it
            if self.the_array[i] < self.the_array[i-1]:
                # if new_run is set to None (NULL)
                if not new_run:
                    runs.append([self.the_array[i]])
                    new_run.append(self.the_array[i])
                else:
                    runs.append(new_run)
                    new_run = [self.the_array[i]]
            # else if its equal to or more than
            else:
                new_run.append(self.the_array[i])
    
        # for every item in runs, append it using insertion sort
        for item in runs:
            sorted_runs.append(own_timsort.insertion_sort(item))
        
        # for every run in sorted_runs, merge them
        sorted_array = []
        for run in sorted_runs:
            sorted_array = own_timsort.merge(sorted_array, run)
    
        print(sorted_array)
        
# =============================================================================
# https://gist.github.com/brandonskerritt/f6ccc000ab6527769999fd0a9ebf59de#file-timsort-py
# =============================================================================