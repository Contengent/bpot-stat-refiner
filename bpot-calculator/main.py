potential_lines = [
    ["+1 for every 10 levels", 3.74], # 0
    ["4% all stat", 4.02],            # 1
    ["5% stat", 5.00],                # 2
    ["5% all stat", 5.02],            # 3
    ["+12 att", 5.82],                # 4
    ["+13 att", 6.34],                # 5
    ["+14 att", 6.83],                # 6
    ["7% stat", 7.00],                # 7
    ["+2 for every 10 levels", 7.48]  # 8
]

with open("output.txt", "w") as file:
    file.write("")

for x in potential_lines:
    for y in potential_lines:
        for z in potential_lines:
            if(x[1]+y[1]+z[1] >= 17):
                with open("output.txt", "a+") as file:
                    file.write("found: {}, {}, {}\n".format(x[0],y[0],z[0]))
            else:
                pass

print("Finished.")