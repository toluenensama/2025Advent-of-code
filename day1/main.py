
with open("day1.txt","r") as file:
    figures = [line.rstrip('\n') for line in file.readlines()]

example = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
init_val = 50

def parse(text: str):
    action = text[0]
    steps = int(text[1:])
    return (action,steps)

def l_movement(init_val: int,steps: int):
    current_val = (init_val - steps) 
    # current_val = (init_val - steps) % 100 
    for i in range(init_val,current_val + 1):
        if i == 0 or i % 100 == 0:
            aux_dail.append(i)
            

    return current_val

def r_movement(init_val: int,steps: int):
    current_val = (init_val + steps)
    # current_val = (init_val + steps) % 100
    for i in range(init_val,current_val + 1):
        if i == 0 or i % 100 == 0:
            aux_dail.append(i)
    return current_val

aux_dail = []
a = 0
dails :list = []
for i in figures:
    action = parse(i)
    direction = action[0]
    steps = action[1]
    if direction == "L":
        current = l_movement(init_val,steps=steps) 
        dails.append(current)
        init_val = current
    if direction == "R":
        current = r_movement(init_val,steps=steps) 
        dails.append(current)
        init_val = current
    

print(dails.count(0))
passed_zero = [i for i in dails if i > 99 or i <= 0]

print(len(passed_zero))

# more_passed = [i == 1 for i in passed_zero if i >= 99 or i <= -99 else i = abs(i//99)]
more_passed = [abs(i // 100) if (i > 99 or i < -99) else 1 for i in passed_zero]

print(sum(more_passed))
print(len(aux_dail))
print(aux_dail)

