from ipaddress import IPv4Address, IPv4Network
from typing import Optional, Sequence, Set, Union

DEFAULT_QIWI_NETWORKS = [
    IPv4Network("79.142.16.0/20"),
    IPv4Network("195.189.100.0/22"),
    IPv4Network("91.232.230.0/23"),
    IPv4Network("91.213.51.0/24"),
]


class IPFilter:
    def __init__(self, ips: Optional[Sequence[Union[str, IPv4Network, IPv4Address]]] = None):
        self._allowed_ips: Set[IPv4Address] = set()

        if ips:
            self.allow(*ips)

    def allow(self, *ips: Union[str, IPv4Network, IPv4Address]) -> None:
        for ip in ips:
            self.allow_ip(ip)

    def allow_ip(self, ip: Union[str, IPv4Network, IPv4Address]) -> None:
        if isinstance(ip, str):
            ip = IPv4Network(ip) if "/" in ip else IPv4Address(ip)
        if isinstance(ip, IPv4Address):
            self._allowed_ips.add(ip)
        elif isinstance(ip, IPv4Network):
            self._allowed_ips.update(ip.hosts())
        else:
            raise ValueError(f"Invalid type of ipaddress: {type(ip)} ('{ip}')")

    @classmethod
    def default(cls) -> "IPFilter":
        return cls(DEFAULT_QIWI_NETWORKS)

    def __contains__(self, item: Union[str, IPv4Address]) -> bool:
        return self.check(item)

    def check(self, ip: Union[str, IPv4Address]) -> bool:
        if not isinstance(ip, IPv4Address):
            ip = IPv4Address(ip)
        return ip in self._allowed_ips
