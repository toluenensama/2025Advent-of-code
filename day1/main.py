

example = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
init_val = 50

def parse(text: str):
    action = text[0]
    steps = int(text[1:])
    return (action,steps)

def l_movement(init_val: int,steps: int):
    current_val = (init_val - steps) % 100
    return current_val

def r_movement(init_val: int,steps: int):
    current_val = (init_val + steps) % 100
    return current_val


a = 0
dails :list = []
for i in example:
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
    
print(dails)
print(dails.count(0))

# i = 0
# while i < len(example):    
#     action = parse(example[i])
#     if action[0] == "L":
#         fin_val = normalizer(l_movement(action[1]))
#         print(fin_val)
#     else:
#         fin_val = normalizer(r_movement(action[1]))
#         print(fin_val)

#     i += 1

#     if i > len(example):
#         print(fin_val)
#     else:
#         init_val = fin_val
