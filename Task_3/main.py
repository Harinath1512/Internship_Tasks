import solutions as s

# Q1
a=s.freq_word("python is easy and python is powerful")
print("Q1:",a)

b=s.freq_word("java is also powerful but python is easier")
print("Q1:",b)

# Q2
a=s.char_freq("banana")
print("Q2:",a)

b=s.char_freq("apple")
print("Q2:",b)

# Q3

a=s.first_non_repeat_char("swiss")
print("Q3:",a)

b=s.first_non_repeat_char("aabbcc")
print("Q3:",b)

# Q4

a=s.anagram("listen", "silent")
print("Q4:",a)    

b=s.anagram("hello", "world")
print("Q4:",b)

# Q5

a=s.first_repeat_char("swiss")
print("Q5:",a)

b=s.first_repeat_char("abcdefg")
print("Q5:",b)

# Q6

a=s.move_zeroes_end([0, 1, 0, 3, 12])
print("Q6:",a)

b=s.move_zeroes_end([0, 0, 1, 0, 3, 12])
print("Q6:",b)

# Q7

a=s.second_highest_distinct([10, 20, 20, 30, 40])
print("Q7:",a)    

b=s.second_highest_distinct([10, 10, 10])
print("Q7:",b)

# Q8

a=s.remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print("Q8:",a)

b=s.remove_duplicates([1, 1, 1, 1])
print("Q8:",b)    

# Q9

a=s.missing_num([1, 2, 4, 6, 7], 7)
print("Q9:",a)

b=s.missing_num([1, 2, 3, 4, 5], 5)
print("Q9:",b)    

# Q10

a=s.two_nums_sum_target([2, 7, 11, 15], 9)
print("Q10:",a)

b=s.two_nums_sum_target([1, 2, 3, 4, 5], 10)
print("Q10:",b)

# Q11

a=s.num_close_to_zero([-4, -2, 1, 3, 5])
print("Q11:",a)    

b=s.num_close_to_zero([-5, -4, -3, -2, -1])
print("Q11:",b)

# Q12

a=s.common_ele([1, 2, 3, 4], [3, 4, 5, 6])
print("Q12:",a)    

b=s.common_ele([1, 2, 3], [4, 5, 6])
print("Q12:",b)

# Q13

a=s.rotate_k_positions([1, 2, 3, 4, 5], 2)
print("Q13:",a)

b=s.rotate_k_positions([1, 2, 3, 4, 5], 7)
print("Q13:",b)

# Q14

a=s.max_sum_consecutive([1, 2, 3, -2, 5])
print("Q14:",a)

b=s.max_sum_consecutive([-1, -2, -3, -4])
print("Q14:",b)    

# Q15

a=s.pairs_sum_target([1, 2, 3, 4, 5], 5)
print("Q15:",a)

b=s.pairs_sum_target([1, 2, 3, 4, 5], 10)
print("Q15:",b)
