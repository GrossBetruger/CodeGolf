from time import time , sleep

SEC = 1000
MINUTE = 60 * SEC 
HOUR = 60 * MINUTE 

HOUR_30_MIN_10_SEC = HOUR + 30*MINUTE + 10*SEC
TWO_HOURS_15_MIN_59_SEC = HOUR*2 + 15*MINUTE +59*SEC

def milis_to_time_str(milis):
	hours = milis / HOUR
	milis -= HOUR * hours
	minutes = milis / MINUTE 
	milis -= MINUTE * minutes
	seconds = milis / SEC 
	print "{}:{}:{}".format(hours, minutes, seconds)

milis_to_time_str(HOUR_30_MIN_10_SEC)
milis_to_time_str(TWO_HOURS_15_MIN_59_SEC)