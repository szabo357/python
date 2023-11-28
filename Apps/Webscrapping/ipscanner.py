# This works but is too slow......
# Has some bugs to fix

import ipaddress
import os

net = ipaddress.ip_network('192.168.1.0/24')

# list all hosts in network.
with open("ip_list.txt","a") as file:
    for ip in net.hosts():
       file.write(f"{ip}\n")


with open("ip_list.txt") as file:
    park = file.read()
    park = park.splitlines()
    print(" {park}  \n")
    # ping for each ip in the file
for ip in park:
    response = os.popen(f"ping -n 4 {ip} ").read()
    # Pinging each IP address 4 times
    
    #saving some ping output details to output file
    if("Tiempo de espera agotado para esta solicitud."
       or "Host de destino inaccesible." 
       or "Request timed out." or "unreachable") in response:
       
        print(response)
        f = open("ip_output.txt","a")
        f.write(str(ip) + ' link is down'+'\n')
        f.close() 
    else:
        print(response)
        f = open("ip_output.txt","a")  
        f.write(str(ip) + ' is up '+'\n')
        f.close() 
    # print output file to screen
with open("ip_output.txt") as file:
    output = file.read()
    print(output)
