
Share your computer’s WiFi / Internet connection (See above slides)

On PocketBeagle:

    sudo /sbin/route add default gw 192.168.7.1

Password for sudo is “temppwd”

    ping 8.8.8.8

Reply: PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.64 bytes from 8.8.8.8: icmp_seq=1 ttl=117 time=10.9 ms

sudo nano /etc/resolv.conf

Add line: nameserver 8.8.8.8

Exit nano: Ctrl-x (to eXit) → “Y” (for Yes) → <Enter> (to confirm file to write)

ping www.google.com

PING www.google.com (172.217.2.228) 56(84) bytes of data.

64 bytes from dfw28s01-in-f4.1e100.net (172.217.2.228): icmp_seq=1 ttl=51 time=10.9 ms