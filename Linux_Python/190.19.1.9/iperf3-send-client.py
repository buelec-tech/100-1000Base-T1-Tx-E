import os

# As client
# TCP Test 
# os.system('sudo iperf3 -c 190.19.1.90 -n 800000M -i 30')
os.system('sudo iperf3 -c 190.19.1.90 -n 8000M -i 30') 



# UDP Test
# os.system('sudo iperf3 -c 190.19.1.90 -u -b 8000M -l 8k -n 1000M')
# os.system('sudo iperf3 -c 190.19.1.90 -u -b 8000000M')
# iperf3 -c 190.19.1.90 -u
# iperf3 -c 190.19.1.90 -u -b 1000M
# iperf3 -c 190.19.1.90 -u -b 1000M
# iperf3 -c 190.19.1.90 -u -b 1024M
# iperf3 -c 190.19.1.90 -u -b 1000M -l 2k
# iperf3 -c 190.19.1.90 -u -b 1000M -l 8k
# iperf3 -c 190.19.1.90 -u -b 1000M -l 8k  -n 8000000M
# iperf3 -c 190.19.1.90 -u -b 1000M -l 8k  -n 8000000M  -i 30
# iperf3 -c 190.19.1.90 -u -b 1000M -l 8k  -n 1000M 


# As Server
# os.system('sudo iperf3 -s') # As Server