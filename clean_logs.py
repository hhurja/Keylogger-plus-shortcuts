#!/usr/bin/env python

log = open('log.txt', 'r')
clean_log = open('log_final.txt', 'a')

for line in log:
	print >> clean_log, line.rstrip()[45:]

log.close()
clean_log.close()