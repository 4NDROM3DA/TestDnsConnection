#####################################################################
#Python script to determine the fastest DNS server at your location
#DNS servers can be added freely under "dnsserver = "
#Domains can be added freely under "domains = "
#####################################################################
#DNS Server:
#Cloudflare - 1.1.1.1
#Google - 8.8.8.8
#OpenDNS - 208.67.222.222
#Quad9 - 9.9.9.9
#Comodo Secure DNS - 8.26.56.10
#Verisign Public DNS - 64.6.64.6
#Alternate DNS - 23.253.163.53
#Domains:
#DuckDuckGo
#####################################################################
import dns.resolver
import time
#DNS servers to be tested
dnsserver = ['1.1.1.1','8.8.8.8','208.67.222.222','9.9.9.9','8.26.56.10','64.6.64.6','23.253.163.53']
#Domains to be resolved for testing
domains = ['duckduckgo.com']

toplist = []

for i in dnsserver:
	avg = 0
	for j in domains:
		try:
			resolv = dns.resolver.Resolver()
			resolv.nameservers = [i]
			resolv.timeout = 1
			start = time.time()
			result = resolv.query(j)
			end = time.time()
			avg = avg + (end-start)
		except Exception as e:
			avg = avg + 100000
	avg = avg / len(domains)
	toplist.append([i, avg])

toplist = sorted(toplist, key=lambda x: x[1])

for elem in toplist:
	print("{0:>17} :: {1}".format(elem[0], elem[1]))
