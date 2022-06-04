from datetime import datetime


def get_character(num, line_map=0x208204cd5c899ab901001216f6a42ded4800108, lines=['▐████▌','█    █','     █','█     ']):
    return [lines[(line_map >> ((line * 23) + (num * 2))) & 3] for line in range(7)]


now = datetime.now()

time = now.strftime('%H:%M:%S')

for i in range(10):
    print('\n'.join(get_character(i)),'\n')
