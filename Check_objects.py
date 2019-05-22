#!/usr/bin/env python
import ipaddress
import sys
with open('DC_ASA.txt',encoding = 'utf-8') as f:
    for line in f:
        lines_c = f.read().splitlines()
        length = len(lines_c)
        for i in range(-1,int(length)):
            #print (lines_c[i])
            try:
               network = ipaddress.IPv4Network(str(lines_c[i]))
            except ValueError:
               print('address/netmask is invalid for IPv4:', str(lines_c[i]))
               sys.exit()
for i in range(-1,int(length-1)):
    try:
        if ipaddress.ip_address(str(lines_c[i])):
            #print("IPaddresss")
            lines_c[i] = "network-object host"+" " + lines_c[i].rstrip()
    except ValueError:
        if ipaddress.ip_network(str(lines_c[i])):
            abc = lines_c[i].replace('/',' ')
            lines_c[i] = "network-object"+" "+str(abc).rstrip()
            #print(abc)
#with open('Commands', "w") as f:
with open('Commands', "w", encoding = 'utf-8') as f:
    #f.write("terminal width 511")
    f.write("object-group network SOC_BLOCK_LIST")
    f.write("\n")
    for item in lines_c:
        f.write("%s\n" % item)
