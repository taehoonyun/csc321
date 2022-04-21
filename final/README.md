to merge all of packet capture in to a single file.

I use this code
mergecap -w full-task.pcap tasksink.pcap taskvent.pcap taskwork.pcap weaserver.pcap wuclient.pcap

And to split weather and task.pcap I use this code
tcpdump -r full-task.pcap -A -s0 port 5556 -w weather.pcap
tcpdump -r full-task.pcap -A -s0 port 5557 or port 5558 -w task.pcap

-r is reading and port 5556 is for weather, port 5557 or 5558 is for task
I could not use other source or ip, because it is same..
But these codes worked!
