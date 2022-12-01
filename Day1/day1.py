last_elf_calories = current_calories = max_calories = elf = 0
list = []
with open ('./day1input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line != '\n':
            current_calories += int(line)
        else:
            elf += 1
            list.append(current_calories)
            if current_calories > max_calories:
                max_calories = current_calories
            current_calories = 0
    print ("Top elf number", elf, " with ", max_calories, " calories!")
    print("Top 3 elves total calories: ", sum((sorted(list))[-3:]))

