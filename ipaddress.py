import nmap

class network(object):
    def __init__(self):
        ip = input("Enter the ip, default is 192.168.1.1/192.168.0.1:")
        self.ip=ip

    def networkScanner(self):
        if len(self.ip) == 0:
            network = '192.168.1.1'

        else:
            network = self.ip + '/24'
        
        print("Scanning please wait......")
        nm=nmap.PortScanner()
        nm.scan(hosts=network, arguments='-sn')
        host_list=[(x,nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in host_list:
            print("host\t{}".format(host))

if __name__=="__main__":
    d=network()
    d.networkScanner()
