import os

def recon(ip):
    os.system(f"nmap -A -p- -Pn {ip} -v -sV -oN '{ip} nmap.txt'")
    os.system(f"dirb {ip} -o '{ip} dirb.txt'")

recon(input("What ip address would you like to scan?"))
