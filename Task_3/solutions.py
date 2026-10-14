#!/usr/bin/env python
# coding: utf-8

# ## Q1. Find the Frequency of Each Word in a Sentence
# 
# - Write a Python program to count how many times each word appears in a given sentence and store the result in a dictionary.
# - Example Input:
# - python is easy and python is powerful
# - Expected Output:
# - {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}
# 

# In[29]:


def freq_word(sentence):
    splitted=sentence.split(" ")
    d={}
    for i in splitted:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d


# ## Q2. Find the Frequency of Each Character in a Word
# - Write a Python program to count how many times each character appears in a given word and store the result in a dictionary.
# - Example Input:
# - banana
# - Expected Output:
# - {'b': 1, 'a': 3, 'n': 2}

# In[30]:


def char_freq(word):
    d={}
    for i in word:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d


# ## Q3. Find the First Non-Repeating Character in a Word
# - Write a Python program to find the first character that appears only once in a given word. If no such character exists, return None.
# - Example Input:
# - swiss
# - Expected Output:
# - w
# 

# In[31]:


def first_non_repeat_char(word):
    d=char_freq(word)
    for i,j in d.items():
        if j==1:
            return i


# ## Q4. Check Whether Two Strings Are Anagrams
# - Write a Python program to check whether two strings are anagrams.
# - Two strings are anagrams if they contain the same characters with the same frequencies, regardless of their order.
# - Example Input:
# - s1 = "listen"
# - s2 = "silent"
# - Expected Output:
# - True

# In[32]:


def anagram(word1,word2):
    word1=sorted(word1)
    word2=sorted(word2)
    if word1==word2:
        return True
    else:
        return False


# ## Q5. Find the First Repeating Character in a String
# - Write a Python program to find the first character whose second occurrence is encountered while reading the string from left to right.
# - If no character repeats, return None.
# - Example Input:
# - programming
# - Expected Output:
# - r
# 

# In[33]:


def first_repeat_char(word):
    d=char_freq(word)
    for i,j in d.items():
        if j>1:
            return i


# ## Q6. Move All Zeros to the End of a List
# - Write a Python program to move all zeros to the end of a list while maintaining the original order of non-zero elements.
# - Example Input:
# - [0, 3, 0, 1, 2, 0, 4]
# - Expected Output:
# - [3, 1, 2, 4, 0, 0, 0]
# 

# In[34]:


def move_zeroes_end(nums):
    i=0
    while i<len(nums)-1:
        if nums[i]==0 and nums[i+1]>=1:
            nums[i],nums[i+1]=nums[i+1],nums[i]
            i=0
        else:
            i+=1
    return nums


# ## Q7. Find the Second Highest Distinct Number in a List
# - Write a Python program to find the second-largest distinct number in a given list.
# - Duplicate values should not be considered separate ranks.
# - If a second distinct number does not exist, return None.
# - Example Input:
# - [10, 20, 40, 30, 40, 20]
# - Expected Output:
# - 30
# 

# In[35]:


def second_highest_distinct(nums):
    nums=set(nums)
    large=-1
    second=-1
    for i in nums:
        if i>large:
            second=large
            large=i
        elif large > i > second:
            second=i
    return second


# In[36]:


second_highest_distinct([10,20,40,30,40,20])


# ## Q8. Remove Duplicates Without Changing the Original Order
# - Write a Python program to remove duplicate elements from a list while preserving the order of their first occurrence.
# - Example Input:
# - [4, 2, 4, 5, 2, 7, 5]
# - Expected Output:
# - [4, 2, 5, 7]
# 

# In[37]:


def remove_duplicates(nums):
    d=char_freq(nums)
    a=[]
    for i,j in d.items():
        a.append(i)
    return a


# ## Q9. Find the Missing Number from 1 to N
# - Write a Python program to find the missing number in a list containing numbers from 1 to N.
# - The list contains exactly one missing number, and all remaining numbers appear only once.
# - Example Input:
# - nums = [1, 2, 4, 5, 6]
# - N = 6
# - Expected Output:
# - 3
# 

# In[38]:


def missing_num(nums,N):
    for i in range(1,N+1):
        if i not in nums:
            return i



# ## Q10. Find Two Numbers Whose Sum Equals a Target
# - Write a Python program to find the first pair of numbers whose sum equals a given target.
# - Return the pair as a list. If no valid pair exists, return an empty list.
# - Return the pair whose second element is encountered earliest when scanning the input from left to right. If multiple earlier elements qualify, - - --- choose the earliest one.
# - Example Input:
# - nums = [2, 7, 11, 15]
# - target = 9
# - Expected Output:
# - [2, 7]
# 

# In[39]:


def two_nums_sum_target(nums,target):
    seen={}
    d=char_freq(nums)
    for i in nums:
        c=target-i
        if c in d.keys() and i<c:
            return [i,c]


# ## Q11. Find the Number Closest to Zero
# - Write a Python program to find the number closest to zero in a given list.
# - If two numbers are equally close to zero, return the positive number.
# - Example Input:
# - [-8, -3, 2, 5, -2]
# - Expected Output:
# - 2
# 

# In[40]:


def num_close_to_zero(nums):
    closest=min(nums,key=lambda x:(abs(x),x))
    return closest


# ## Q12. Find Common Elements Between Two Lists
# - Write a Python program to find the common elements between two lists.
# - Each common element should appear only once in the result, maintaining the order of its first occurrence in the first list.
# - Example Input:
# - list1 = [1, 2, 3, 4, 5]
# - list2 = [3, 4, 5, 6, 7]
# - Expected Output:
# - [3, 4, 5]
# 

# In[41]:


def common_ele(list1,list2):
    set1=set(list1)
    set2=set(list2)
    return list(set1.intersection(set2))


# ## Q13. Rotate a List to the Right by K Positions
# - Write a Python program to rotate the elements of a list to the right by K positions.
# - Elements shifted beyond the last position should move to the beginning of the list.
# - Example Input:
# - nums = [1, 2, 3, 4, 5]
# - K = 2
# - Expected Output:
# - [4, 5, 1, 2, 3]
# 

# In[42]:


def rotate_k_positions(nums,k):
    return nums[-k:]+nums[:-k]


# ## Q14. Find the Maximum Sum of Two Consecutive Elements
# - Write a Python program to find the maximum sum of any two consecutive elements in a list.
# - Assume the list contains at least two elements.
# - Example Input:
# - [4, 7, 2, 9, 5]
# - Expected Output:
# - 14
# 

# In[43]:


def max_sum_consecutive(nums):
    a=[]
    maxi=nums[0] + nums[1]
    for i in range(len(nums)-1):
        sum1=nums[i]+nums[i+1]
        maxi=max(maxi,sum1)
    return maxi
max_sum_consecutive([4, 7, 2, 9, 5])


# ## Q15. Find All Pairs of Numbers Whose Sum Equals a Target
# - Write a Python program to find all unique pairs of numbers whose sum equals a given target.
# - Each pair should contain two distinct list positions, and duplicate pairs should not be included.
# - Return each pair in ascending numerical order. Return the list of pairs sorted by their first element. If no valid pairs - exist, return an empty list.
# - Example Input:
# - nums = [2, 4, 3, 5, 7, 8, 1]
# - target = 9
# - Expected Output:
# - [[1, 8], [2, 7], [4, 5]]
# 

# In[63]:


def pairs_sum_target(nums,k):
    a=[]
    for i in nums:
        c=k-i
        if c in nums and i<c:
            a.append([i,c])
    return a
pairs_sum_target([2, 4, 3, 5, 7, 8, 1],9)


# In[ ]:





# In[ ]:




