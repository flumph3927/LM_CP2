#LM 1st Word Counter
import datetime

#create function get time
def get_time():
    #get timestamp
    stamp=datetime.datetime.now()
    #reformat time
    out=stamp.strftime('%Y-%m-%d %H:%M:%S')
    #return time
    return out