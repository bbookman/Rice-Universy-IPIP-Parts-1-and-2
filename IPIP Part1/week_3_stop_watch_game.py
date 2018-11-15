# template for "Stopwatch: The Game"

import simplegui


# define global variables
time = 0 #in miliseconds
total_stops = 0
stops_on_whole_second = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    D = t % 10
    ABC = (t - D) / 10
    A = ABC / 60
    BC = ABC % 60
    B = BC / 10
    C = BC % 10
    return str(A) + ':' + str(B) + str(C) + '.' + str(D)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer_handler()

def stop_handler():
    global total_stops, time, stops_on_whole_second
    total_stops += 1
    timer.stop()
    if time % 10 == 0:
        stops_on_whole_second += 1
        

def reset_handler():
    global time, total_stops, stops_on_whole_second
    time = 0
    total_stops = 0
    stops_on_whole_second = 0
    timer.stop()
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    timer.start()
    global time
    time += 1
    print format(time)

# define draw handler

def draw(canvas):
    global time
    canvas.draw_text(format(time), [100, 200], 70, 'White')
    canvas.draw_text(str(stops_on_whole_second)+'/'+str(total_stops), [250, 40], 30, 'Red')

# create frame
frame = simplegui.create_frame('Testing', 400, 400)
frame.set_draw_handler(draw)

# register event handlers
frame.add_button('Start', start_handler, 200)
frame.add_button('Stop', stop_handler, 200)
frame.add_button('Reset', reset_handler, 200)
timer = simplegui.create_timer(10, timer_handler)


# start frame
frame.start()

