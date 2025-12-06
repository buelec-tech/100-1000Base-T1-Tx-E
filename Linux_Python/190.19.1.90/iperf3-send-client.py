import os


# As Server
os.system('sudo iperf3 -s')  # As Server


# As client
# TCP Test 
# os.system('sudo iperf3 -c 190.19.1.9 -n 1020M -i 30') 

# UDP Test
# os.system('sudo iperf3 -c 190.19.1.9 -u -b 1024M -l 8k -n 1024M')
# os.system('sudo iperf3 -c 190.19.1.9 -u -b 1024M -l 8k -n 1024000000M')
# iperf3 -c 190.19.1.9 -u
# iperf3 -c 190.19.1.9 -u -b 1000M
# iperf3 -c 190.19.1.9 -u -b 1000000M
# iperf3 -c 190.19.1.9 -u -b 1024M
# iperf3 -c 190.19.1.9 -u -b 1000M -l 2k
# iperf3 -c 190.19.1.9 -u -b 1000M -l 8k
# iperf3 -c 190.19.1.9 -u -b 1000M -l 8k  -n 
# iperf3 -c 190.19.1.9 -u -b 1000M -l 8k  -n 1000M  -i 30
# iperf3 -c 195.20.1.31 -u -b 1000M -l 8k  -n 1000M 


