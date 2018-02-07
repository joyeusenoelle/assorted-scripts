__author__ = "Noëlle Anthony"
__version__ = "1.0.0"

import datetime

class DebugLogger():
	""" A quick and dirty debug logger.

	Use this instead of print() statements for debugging. This way instead of
	ferreting out all the print() statements you can just toggle the logger
	off when you don't need them anymore, and searching for the name of the
	DebugLogger object to remove lines is easier than deciding whether each
	print() statement can stay.

	You don't have to pass your package's name but you really should if you 
	want a logfile; it's cleaner than just logging everything to debug.log,
	which is the default behavior.

	The default state of the logger is on! You can turn it off with 
	    <your_object>.debug_on = False
	and on again, of course, with
	    <your_object>.debug_on = True
	"""
	def __init__(self, package=None, debug_on=None):
		self.logfile = "debug.log" if package == None else "{}.log".format(str(package))
		self.__debug_on = True if debug_on == None else bool(debug_on)

	@property
	def debug_on(self):
		return self.__debug_on

	def debug_on(self, val):
		self.__debug_on = bool(val)

	def debug_log(self, msg):
		if self.__debug_on:
			with open(self.logfile, "a+") as logfile:
				timestamp = datetime.datetime.now().strftime("[%Y/%m/%d %H:%M:%S]")
				logfile.write("{} {}\n".format(timestamp, msg))

	def debug_print(self, msg):
		if self.__debug_on:
			timestamp = datetime.datetime.now().strftime("[%Y/%m/%d %H:%M:%S]")
			print("[DEBUG] {} {}".format(timestamp, msg))
