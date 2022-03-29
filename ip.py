import socket
import pandas as pd
import graphviz


arrIp = []
originDom = 1
grapNode = 300
domainsSource = pd.read_csv('domains.tsv', sep='\t')
domains = domainsSource['domain']
removeRep = ""

dot = graphviz.Digraph(
    engine='fdp', comment='The Round Table')


for domainNames in domains:

    try:
        addrInfo = socket.getaddrinfo(
            domainNames, 443, type=socket.SOCK_STREAM)
    except Exception:
        pass
    originDom = originDom + 1
    domainsIpNum = len(addrInfo) - 1
    with dot.subgraph() as s:
        s.node(str(originDom), domainNames)
    for num in range(domainsIpNum):
        try:
            ipNport = addrInfo[num][4]
            removeRep = socket.gethostbyaddr(ipNport[0])[0]
        except Exception:
            pass
        grapNode = grapNode+1

        dot.node(str(grapNode), removeRep)
        dot.edge(str(grapNode), str(originDom))
# dot.view()

dot.render(directory='doctest-output', view=True)
