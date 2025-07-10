# update_doh_doq_list.py
import socket

providers = {
    "dns0.eu": "zero.dns0.eu",
    "Google": "dns.google",
    "AdGuard Default": "dns.adguard-dns.com",
    "AdGuard Family": "family.adguard-dns.com",
    "AdGuard Unfiltered": "unfiltered.adguard-dns.com",
    "Cloudflare": "dns.cloudflare.com",
    "Cloudflare Security": "security.cloudflare-dns.com",
    "Cloudflare Family": "family.cloudflare-dns.com",
    "Quad9": "dns.quad9.net",
    "CleanBrowsing Family": "doh.cleanbrowsing.org",
    "OpenDNS": "doh.opendns.com",
    "Dandelion Sprout": "dandelionsprout.asuscomm.com",
    "DNSForge": "dnsforge.de",
    "dnswarden": "dns.dnswarden.com",
    "FFMUC": "doh.ffmuc.net",
    "stevenz.net": "dns.stevenz.net",
}

def resolve_ips(hostname):
    ipv4 = []
    ipv6 = []
    try:
        infos = socket.getaddrinfo(hostname, None)
        for info in infos:
            ip = info[4][0]
            if ':' in ip:
                ipv6.append(ip)
            else:
                ipv4.append(ip)
    except Exception as e:
        print(f"Failed to resolve {hostname}: {e}")
    return list(set(ipv4)), list(set(ipv6))

with open("doh_doq_list.txt", "w") as f:
    for name, host in providers.items():
        ipv4, ipv6 = resolve_ips(host)
        f.write(f"# {name}\n")
        f.write(f"DoH: https://{host}/dns-query\n")
        f.write(f"DoQ: quic://{host}\n")
        f.write(f"IPv4: {', '.join(ipv4) or 'N/A'}\n")
        f.write(f"IPv6: {', '.join
