#! /usr/bin/env python3

import argparse
import socket

authorSignature = 'Knocker.py - Published by Moritz Nentwig\n'
authorSignature += '----------------------------------------'


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
