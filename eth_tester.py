# LAN8720 MODULE

#GPIO00 - EMAC_TX_CLK : nINT/REFCLK (50MHz)
#GPIO16 - SMI_MDC     : MDC (relocateable)
#GPIO17 - SMI_MDIO    : MDIO (relocateable)
#GPIO19 - EMAC_TXD0   : TX0
#GPIO21 - EMAC_TX_EN  : TX_EN
#GPIO22 - EMAC_TXD1   : TX1
#GPIO25 - EMAC_RXD0   : RX0
#GPIO26 - EMAC_RXD1   : RX1
#GPIO27 - EMAC_RX_DV  : CRS
#GND                  : GND
#3V3                  : VCC

# press RESET or power ON/OFF ESP32 several times until it boots
# speed: ftp get from ESP32 flash is 300KB/s (3Mbps)

# some free pins recommended for ESP32 to be used as JTAG programmer

#GPIO23 JTAG_TDI
#GPIO34 JTAG_TDO (was 19)
#GPIO18 JTAG_TCK
#GPIO5  JTAG_TMS (was 21)

import network
from machine import Pin
lan = network.LAN(mdc=Pin(16), mdio=Pin(17), power=None, id=None, phy_addr=1, phy_type=network.PHY_LAN8720)
lan.active(True)
# by default (no parameters), ifconfig() will request DHCP
lan.ifconfig()
# set fixed IP (address, netmask, gateway, dns)
lan.ifconfig(('192.168.0.2', '255.255.255.0', '192.168.0.1', '192.168.0.1'))


# # first ping the address
# # then arp -a to get the mac address.
# import socket
# port = 10086  #typical port for UDP protocol
# s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 
# s.bind( ('192.168.0.2', port) )
# 
# while True:
#     data,addr=s.recvfrom(1024)
#     if(len(data) != 0):
#         print('received:',data,'from: ', addr)
#         #runs in loop until something is received
# 
# #when writing, always convert string to byteArray
# s.sendto(bytearray("hello worldW")  , ('192.168.0.1', port) )
# 