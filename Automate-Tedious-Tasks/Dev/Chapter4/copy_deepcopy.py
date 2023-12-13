import copy

print("------copy_copy----begin")
spam = ['A', 'B', 'C', 'D']
print(f"spam id = {id(spam)}")
cheese = copy.copy(spam)
print(f"cheese id = {id(cheese)}")
cheese[1] = 'H'
print(f"spam = {spam}")
print(f"cheese = {cheese}")
print("------copy_copy----end")


print("\n\n------copy_deepcopy----begin")
niutest = copy.deepcopy(spam)
print(f"spam id = {id(spam)}")
print(f"niutest id = {id(niutest)}")
niutest[1] = 'K'
print(f"spam = {spam}")
print(f"niutest = {niutest}")
print("------copy_deepcopy----end")

