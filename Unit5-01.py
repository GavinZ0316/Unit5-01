import ui
from numpy import random

my_number = []

def create_array_touch_up_inside(sender):

    global my_number
    view['textview'].text = ''
    for index in range(0,10):
        my_number.append(random.randint(0,100))
        view['textview'].text = view['textview'].text + str(my_number[index]) + '\n'
 
def get_average_touch_up_inside(sender):
    total = my_number[0] + my_number[1] + my_number[2] + my_number[3] + my_number[4] + my_number[5] + my_number[6] + my_number[7] + my_number[8] + my_number[9]
    total = total/10
    view['average_label'].text = str(total)
    

view = ui.load_view()
view.present('full_screen')
