#!/usr/bin/env python

import os
import sys
import struct
'''
struct am335x_baseboard_id {
       u8 magic[4];
       u8 name[8];
       u8 version[4];
       u8 serial[12];
       u8 config[32];
       u8 mac_addr[3][6];
};
#define as I8sI12s32s18s
'''
eeprom_path="/sys/bus/i2c/devices/2-0057/eeprom"

class eeprom:
    def __init__(self,dumpName = ''):
	self.eeprom_dump = struct.Struct("I0s16s30s6s6s6s6s15s")
    def readBoardinfo(self):
	self.fp_sys = open("eeprom.tmp",'rb')
        self.eeprom_dump = self.fp_sys.read(89)
        self.fp_sys.close()

        self.version,\
        self.length,\
        self.reserved,\
        self.productstr,\
        self.wifi_mac1,\
        self.bt_mac1,\
        self.wifi_mac2,\
        self.eth_mac,\
        self.serialNo= \
        struct.unpack("I0s16s30s6s6s6s6s15s",self.eeprom_dump)

        return self.serialNo


    def writeBoardinfo(self,new_serial):
        self.serialNo = new_serial

        self.fp_local = open('eeprom.tmp','wb+')
        self.eeprom_dump = struct.pack('I0s16s30s6s6s6s6s15s', self.version,\
                                                                self.length,\
                                                                self.reserved,\
                                                                self.productstr,\
                                                                self.wifi_mac1,\
                                                                self.bt_mac1,\
                                                                self.wifi_mac2,\
                                                                self.eth_mac,\
                                                                self.serialNo)
        self.fp_local.write(self.eeprom_dump)
        self.fp_local.close()
        os.system("sync")
        os.popen('hexdump -C ./eeprom.tmp').read()

        os.system("dd if=./eeprom.tmp of=" + eeprom_path + " > /dev/null 2>&1")
        os.system("sync")

    def restore_default(self, res = 'eeprom_data/eeprom_stand.tmp'):
        os.system("dd if=" + res + " of=" + eeprom_path + " bs=1k > /dev/null 2>&1")

#Test eeprom class
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} version serial [name]".format(sys.argv[0]))
        quit(1)

    eep_obj = eeprom()
    eep_obj.restore_default()

    # read
    serial = eep_obj.readBoardinfo()
#    print(serial)
    print("************ Data need write   ************")
    serial_w  = sys.argv[1]
#    serial_w = "120200102110289"
    print("serial  = {}".format(serial_w)) 
    eep_obj.writeBoardinfo(serial_w)

    serial_r = eep_obj.readBoardinfo()
    print("************  Data read back   ************")
    print("serial  = {}".format(serial_r))

    if serial_w in serial_r:
    	quit(0)
    else:
        quit(1)
