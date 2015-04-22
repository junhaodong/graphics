import math


xres = 512
yres = 512
maxval = 255

header = "P3 {0} {1} {2}\n".format(xres, yres, maxval)

pic = open("pic.ppm", 'w+')
pic.write(header)

for i in range(xres):
    for j in range(yres):
        #r = math.log(xres, yres)
        r = math.cos(i)
        g = (i+j) % maxval
        b = math.sin(j)
        line = "{0} {1} {2} ".format(r, g, b)
        pic.write(line)

pic.close()
