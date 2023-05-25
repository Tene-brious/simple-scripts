import os

# Line to populate the host value
host = input("Specify the ip address: ")
def check_host_alive(host):
# Line to activate ping
	response = os.system("ping -c 1 " + host)
	if response == 0:
 		status = "Host is alive!"
	else:
 		status = "Host is down!"
	return status

# Let's test this task
print("\n""Let's check what is going on:", check_host_alive(host))
