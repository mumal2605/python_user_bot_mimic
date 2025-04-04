import re
def positions(x,y,M,N):
    x=x%M
    y=y%N
    return x,y

def movement(inp_st,x,y):
    '''st=[int(item) for item in inp_st if item.isdigit()]
    al=[int(item) for item in inp_st if item.ischar()]
    dict01 = dict(zip(al, st))
    x=x+dict01['R']-dict01['L']
    y=y+dict01['T']-dict01['B']'''

    matches = re.findall(r'(\d+)([A-Z])', inp_st)
    dict01={'R': 0, 'L': 0, 'T': 0, 'B': 0}
    for num, dir in matches:
        dict01[dir] += int(num)

    x=x+dict01['R']-dict01['L']
    y=y-dict01['T']+dict01['B']

    return positions(x, y,8,8)

def main():
    M,N=8,8
    x,y=0,0
    xb,yb=1,4
    x,y=positions(x,y,M,N)
    xb,yb=positions(xb,yb,M,N)
    inp_st="4R3T5B21L2B"

    user_pos = movement(inp_st,x,y)
    bot_pos = movement(inp_st,xb,yb)

    if(user_pos==bot_pos):
        xb, yb = movement("1R1T", xb, yb)
        bot_pos = (xb, yb)

    x,y=positions(x,y,M,N)
    xb,yb=positions(xb,yb,M,N)

    print("Final User Position:", user_pos)
    print("Final Bot Position:", bot_pos)

if __name__ == "__main__":
    main()

    


