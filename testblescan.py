import blescan
import sys
import MySQLdb

import bluetooth._bluetooth as bluez

conn = MySQLdb.connect(host = "localhost", user="root", passwd="hanium", db="rpidb")
cursor = conn.cursor()

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
	returnedList = blescan.parse_events(sock, 10)
	print "----------"
	for beacon in returnedList:
		print beacon
		sql = """insert into users(id)
                         values {0}"""
		cursor.execute(sql.format(beacon))
		conn.commit()
	db.close()
