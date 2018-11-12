#!/usr/bin/python

import spidev
import ws2812
spi = spidev.SpiDev()
spi.open(1,0)

#write 4 WS2812's, with the following colors: red, green, blue, yellow


#def qwe(i):
#	ws2812.write2812(spi, [[1,1,1]])
#	print i


#i = 10

#while True:
#    i += 1
#    qwe(i)

ws2812.write2812(spi, [[0,0,0], [0,0,0], [0,0,0], [1,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0]])
 

#for i in range(10):
#    qwe()


