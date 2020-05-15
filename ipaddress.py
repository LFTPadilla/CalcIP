import pip._vendor.ipaddress as ipaddress

"""
metodo que permite a partir de un direccion de un host en formto simplificado /x calcular:
direccion de red
Numero de hosts de la red
rango de direcciones hosts asignables
"""


def dirHost(ipHost):
    ipNetwork = ipaddress.ip_network(ipHost, strict=False)  # Direccion de red
    hosts = list(ipNetwork.hosts())  # Lista de host de la red
    hostNumber = len(hosts)+2  # numero de host de la red
    # rango de direcciones
    minDir = hosts[0]  # direccion de primer host asignable
    maxDir = hosts[-1]  # direccion del ultimo host asignable

    return ipNetwork.compressed, hostNumber, minDir.compressed, maxDir.compressed


"""
metodo que permite a partir de una direccion de una red en formato simplificado /x calcular:
Máscara de subred en formato decimal.
Dirección de broadcast en esa red.
# de bits de la red.
# de bits de los hosts.
# de direcciones que se pueden asignar a los hosts en la red.
Rango completo de direcciones indicando la dirección de la red, las direcciones que se
pueden asignar a los hosts y la dirección de broadcast.
"""


def dirNetwork(networkDir):
    ipNetwork = ipaddress.ip_network(
        networkDir, strict=False)  # Direccion de red
    subNetMask = ipNetwork.netmask  # mascara de sub red en formato decimal
    dirBroadcast = ipNetwork.broadcast_address  # direccion de broadcast
    prefixLen = ipNetwork._prefixlen  # numero de bits de la red
    suffixLen = 32-prefixLen  # numero de bist de los hosts
    hostsAux = list(ipNetwork.hosts())  # Lista de host de la red
    hostNumber = len(hostsAux)  # numero de host asignables de la red
    # se agrega la direccion de red y de broadcast
    hostsAux.insert(0, ipNetwork)
    hostsAux.append(dirBroadcast)
    hosts = list()  # lista de host en str
    for host in hostsAux:
        hosts.append(host.compressed)
    return subNetMask.compressed, dirBroadcast.compressed, prefixLen, suffixLen, hostNumber, hosts


print(dirHost("192.168.1.5/24"))
