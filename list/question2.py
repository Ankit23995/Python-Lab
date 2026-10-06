subject_list=["math","science","english","computer","nepali"]
mark_list=[80,75,89,95,80]

total_marks=sum(mark_list)
print(total_marks)

average_marks =total_marks / len(mark_list)
print(average_marks)

highest=max(mark_list)
print(highest)

lowest=min(mark_list)
print(lowest)

print("Mark obtained in english is", mark_list[2])

print("Marks in second last subject:", mark_list[-2])

print("Marks in last two subjects:", mark_list[-2:])

print("Marks in first three subjects:", mark_list[:3])


highest_index = mark_list.index(max(mark_list))
print("Subject with highest marks:", subject_list[highest_index])


lowest_index = mark_list.index(min(mark_list))
print("Subject with lowest marks:", subject_list[lowest_index])


print("Number of subjects with 80 marks:", mark_list.count(80))