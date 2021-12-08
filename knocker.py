#! /usr/bin/env python3

import argparse
import socket
import time

authorSignature = 'Knocker.py - Published by Moritz Nentwig\n'
authorSignature += '----------------------------------------'

## knock the ports
def func(args):

    for port in args.targetPorts:
        
        # create an INET, STREAMing socket (TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.setblocking(False)

        try:

            print("[+] Knocking at port: " + str(port))

            # now connect to the server on port xxx 
            s.connect((args.targetHost, port))

        except socket.error:

            pass
        
        # sleep between each knock
        time.sleep(args.delay/1000)
    
    print("[+] Done")

## print header first 
print("")
print(authorSignature)

## parse arguments 
parser = argparse.ArgumentParser(description='Knocker.py is an easy port knocking service', 
                                 epilog='--- Knocker.py - Moritz Nentwig --------', add_help=True)
parser.add_argument('targetHost', help='target IP address')
parser.add_argument('targetPorts', type=int, nargs='+', help='target ports to knock')
parser.add_argument('-d', '--delay', type=int, default=500, help='delay between each port knock in milliseconds')
args = parser.parse_args()

# print entered arguments
print("[+] Targethost: " + args.targetHost)
print("[+] TargetPorts: " + ' '.join(map(str, args.targetPorts)))
print("[+] Delay: " + str(args.delay) + " milliseconds")

func(args)