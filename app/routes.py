from flask import request, render_template
from flask import current_app as app
from .models import db, Clients, Routers, Interfaces, Maps
from .executer import Executer
import ipaddress
from mac_vendor_lookup import MacLookup


@app.route('/', methods=['GET'])
def index():
    clients = Clients.query.order_by(Clients.name).all()
    return render_template('index.html', clients=clients)


@app.route('/about', methods=['POST', 'GET'])
def about():
    client_id = request.form.get("client")
    client = Clients.query.filter_by(id=client_id).first()
    client_map = Maps.query.filter_by(client_id=client_id).first()
    interface = Interfaces.query.filter_by(id=client_map.if_id).first()
    router = Routers.query.filter_by(id=client_map.router_id).first()
#    router_ip = str(ipaddress.IPv4Address(router.ip))
    ip_map = Maps.query.filter_by(client_id=client_id).all()
    ip_addresses = []
    for ip in ip_map:
        ip_addresses.append(str(ipaddress.IPv4Address(ip.client_ip)))

    con = Executer(str(ipaddress.IPv4Address(router.ip)))
    status = con.status(interface.name)
    arps = con.arp(interface.name)
    for arp in arps:
        if arp['mac'] != 'Incomplete':
            arp['vendor'] = MacLookup().lookup(arp['mac'])
        else:
            arp['vendor'] = "Incomplete"
    ip_addresses_for_ping = []
    for arp in arps:
        if arp['mac'] != 'Incomplete':
            ip_addresses_for_ping.append(arp['address'])

    pings = []
    for ip in ip_addresses_for_ping:
        pings.append(con.ping(ip))

    con.disconnect()

    return render_template('about.html', client=client, router=router, interface=interface,
                           ip_addresses=ip_addresses, status=status, arps=arps, pings=pings)