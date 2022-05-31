from datetime import datetime


# FAAAAB    ABBBBC
# F    B    D    E
# F    B    D    E
# FGGGGB    FGGGGH
# E    C    I    J
# E    C    I    J
# EDDDDC    KLLLLM

# L[0] = 
#   '▐████▌' = 0,2,3,5,6,7,8,9  = 1005
#   '     ▌' = 1                = 2
#   '▐    ▌' = 4                = 16
# L[1] = 
#   '█    █' = 0,4,8,9          = 785
#   '     █' = 1,2,3,7          = 142
#   '█     ' = 5,6              = 96
# L[2] = 
#   '█    █' = 0,4,8,9          = 785
#   '     █' = 1,2,3,7          = 142
#   '█     ' = 5,6              = 96
# L[3] = 
#   '▐    ▌' = 0                = 1
#   '     ▌' = 1,7              = 130
#   '▐████▌' = 2,3,4,5,6,8,9    = 892
# L[4] = 
#   '█    █' = 0,4,8,9          = 785
#   '     █' = 1,2,3,7          = 142
#   '█     ' = 5,6              = 96
# L[5] = 
#   '█    █' = 0,4,8,9          = 785
#   '     █' = 1,2,3,7          = 142
#   '█     ' = 5,6              = 96
# L[6] = 
#   '▐████▌' = 0,2,3,5,6,8,9    = 877
#   '     ▌' = 2,4,7            = 148

# A[0] = 0,2,3,5,6,7,8,9   = 1005
# B[1] = 0,1,2,3,4,7,8,9   = 927
# C[2] = 0,1,3,4,5,6,7,8,9 = 1019
# D[3] = 0,2,3,5,6,8,9     = 877
# E[4] = 0,2,6,8           = 325
# F[5] = 0,4,5,6,8,9       = 881
# G[6] = 2,3,4,5,6,8,9     = 892
# 0 1 2 3 4 5 6 7 8 9

# ▐████▌   ░░░░▌   ████▌   ████▌  ▐░░░░▌  ▐████   ▐████    ████   ▐████▌  ▐████▌
# █    █  ░    █  ░    █  ░    █  █    █  █    ░  █    ░  ░    █  █    █  █    █
# █    █  ░    █  ░    █  ░    █  █    █  █    ░  █    ░  ░    █  █    █  █    █
# ▐░░░░▌   ░░░░▌  ▐████▌   ████▌  ▐████▌  ▐████   ▐████    ░░░░▌  ▐████▌  ▐████▌
# █    █  ░    █  █    ░  ░    █  ░    █  ░    █  █    █  ░    █  █    █  ░    █
# █    █  ░    █  █    ░  ░    █  ░    █  ░    █  █    █  ░    █  █    █  ░    █
# ▐████▌   ░░░░▌  ▐████▌   ████▌   ░░░░▌   ████▌   ████▌   ░░░░▌  ▐████▌   ████▌

#  ████        █   ████    ████   █    █   ████    ████    ████    ████    ████ 
# █    █       █       █       █  █    █  █       █            █  █    █  █    █
# █    █       █       █       █  █    █  █       █            █  █    █  █    █
# █    █       █   ████    ████    ████    ████    ████        █   ████    ████
# █    █       █  █            █       █       █  █    █       █  █    █       █
# █    █       █  █            █       █       █  █    █       █  █    █       █
#  ████        █   ████    ████        █   ████    ████        █   ████    ████ 

# [0:' ████ ',1:'█    █',2:'     █',3:'█     ']
#        0 1 2 3 4 5 6 7 8 9
# L[0] = 0,2,0,0,1,0,0,0,0,0 = 
#   ' ████ '[0] = 0,2,3,5,6,7,8,9  = 1005
#   '     █'[2] = 1                = 2
#   '█    █'[1] = 4                = 16
# L[1] = 1,2,2,2,1,3,3,2,1,1 = 
#   '█    █'[1] = 0,4,8,9          = 785
#   '     █'[2] = 1,2,3,7          = 142
#   '█     '[3] = 5,6              = 96
# L[2] = ^
# L[3] = 1,2,0,0,0,0,0,2,0,0 = 
#   '█    █'[1] = 0                = 1
#   '     █'[2] = 1,7              = 130
#   ' ████ '[0] = 2,3,4,5,6,8,9    = 892
# L[4] = 1,2,3,2,2,2,1,2,1,1 = 
#   '█    █'[1] = 0,6,8,9          = 833
#   '     █'[2] = 1,3,4,5,7        = 186
#   '█     '[3] = 2                = 4
# L[5] ^
# L[6] = 0,2,0,0,2,0,0,2,0,0 = 
#   ' ████ '[0] = 0,2,3,5,6,8,9    = 877
#   '     █'[2] = 1,4,7            = 146


def calc(l):
    out = 0
    for i in range(len(l)):
        out += l[i] << (i<<1)
    
    return out


def glyph(num):
    print([' ████ ','█    █','     █','█     '])



# def glyph(num):
#     p = lambda n : n >> num & 1
#     b = ' █▐▌'
#     s = [p(1005),p(927),p(1019),p(877),p(325),p(881),p(892)]

#     return [
#         f' {b[s[0]]*4} ',
#         f'{b[s[5]]}    {b[s[1]]}',
#         f'{b[s[5]]}    {b[s[1]]}',
#         f' {b[s[6]]*4} ',
#         f'{b[s[4]]}    {b[s[2]]}',
#         f'{b[s[4]]}    {b[s[2]]}',
#         f' {b[s[3]]*4} ',
#     ]

    # return [
    #     f'{b[s[5]+(1&s[5])]}{b[s[0]]*4}{b[s[1]+(2&(s[1]<<1))]}',
    #     f'{b[s[5]]}{(b[0]*4)}{b[s[1]]}',f'{b[s[5]]}{(b[0]*4)}{b[s[1]]}',
    #     f'{b[s[5]+(1&s[5])]}{b[s[6]]*4}{b[s[1]+(2&(s[1]<<1))]}',
    #     f'{b[s[4]]}{(b[0]*4)}{b[s[2]]}',f'{b[s[4]]}{(b[0]*4)}{b[s[2]]}',
    #     f'{b[s[4]+(1&s[4])]}{b[s[3]]*4}{b[s[2]+(2&(s[2]<<1))]}',
    # ]


    # return [
    #     ' ' + (s[0]*4) + ' ',
    #     s[5] + (' '*4) + s[1],
    #     s[5] + (' '*4) + s[1],
    #     ' ' + (s[6]*4) + ' ',
    #     s[4] + (' '*4) + s[2],
    #     s[4] + (' '*4) + s[2],
    #     ' ' + (s[3]*4) + ' ',
    # ]

now = datetime.now()

time = now.strftime('%H:%M:%S')

# for i in range(10):
#     print('\n'.join(glyph(i)),'\n')


glyph(4)