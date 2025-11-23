- list = [1, 2, 3, 4, 5]

- print(list[0]) --- returns 1, counts from 0

- print(list[-1]) --- returns the last value of the list, 5. -2 and -3 does what expected

- list[0] = 17 --- the value 1 is now 17, used to replace things in a list

- list.append(6) --- adds an item to the end of a list without effecting the list

- list.insert(0, 12) --- inserts a value into a list but does not replace, list[0] now returns 12 instead of 1, and list[1] returns 1

- del list[2] --- completely removes the value at 2 so 3 from the list, remember: completely removes

- popped_list = list.pop() --- popped_list is now a variable for 5, by default pop() pops the last value in a list. Although methods such as pop(0) are completely valid. Finally, pop is used instead of del when you want to use the value instead of losing it

- 1 = number_first and list.remove(number_first) --- python removes 1 from the list, bear in mind that 1 could be in the list more than once- python will stop after finding the first 1

- list.sort(reverse=True) --- if the list was lowercase letters, this would return the list in the opposite of alaphebetical order (and permenently change it)

- print(sorted(list)) --- this would print the list in alphabetical order but not store the list as this new order

- list.reverse() --- reverses the order of a list

- len(list) --- finds the length of a list (starting from 1)

- min(),max() and sum() do what is obvious to a list of numbers, use min(list)

- print(list[0:3]) --- slices the list and returns values 1, 2, 3 corresponding to 0, 1 and 2, missing out the first or second nymber tells python either do it from start or to end of list, negative values can be used. A third value can be added telling how many items python should skip through.


