"""
Sap
===
This combiner combines the result of
insights.parsers.saphostctrl.SAPHostCtrlInstances` and
`:class:`insights.parsers.lssap.Lssap` to get the available SAP instances.
Prefer the ``SAPHostCtrlInstances`` to ``Lssap``.

"""

from collections import namedtuple
from insights import SkipComponent
from insights.core.plugins import combiner
from insights.combiners.hostname import Hostname
from insights.parsers.lssap import Lssap
from insights.parsers.saphostctrl import SAPHostCtrlInstances


SAPInstances = namedtuple("SAPInstances",
        field_names=["name", "hostname", "sid", "type", "number", "fqdn", "version"])
"""namedtuple: Type for storing the SAP instance."""

FUNC_TYPES = ('SMDA',)
"""
SMDA   :    Solution Manager Diagnostics Agents
"""
NETW_TYPES = ('D', 'ASCS', 'DVEBMGS', 'J', 'SCS', 'ERS', 'W', 'G', 'JC')
"""
D      :    NetWeaver (ABAP Dialog Instance)
ASCS   :    NetWeaver (ABAP Central Services)
DVEBMGS:    NetWeaver (Primary Application server
J      :    NetWeaver (Java App Server Instance)
SCS    :    NetWeaver (Java Central Services)
ERS    :    NetWeaver (Enqueue Replication Server)
W      :    NetWeaver (WebDispatcher)
G      :    NetWeaver (Gateway)
JC     :    NetWeaver (Java App Server Instance)
"""


@combiner(Hostname, [SAPHostCtrlInstances, Lssap])
class Sap(dict):
    """
    Combiner for combining the result of :class:`insights.parsers.lssap.Lssap`
    generated by command ``lssap`` and
    `insights.parsers.saphostctrl.SAPHostCtrlInstances` generated by command
    ``saphostctrl``.

    Prefer ``SAPHostCtrlInstances`` to ``Lssap``.

    Examples:
        >>> type(saps)
        <class 'insights.combiners.sap.Sap'>
        >>> 'D16' in saps
        True
        >>> saps['D16'].number
        '16'
        >>> saps.sid('HDB16')
        'HA2'
        >>> saps.hostname('HDB16')
        'lu0417'
        >>> len(saps.business_instances)
        3
        >>> saps.is_hana
        True
        >>> saps.is_netweaver
        True
        >>> saps.is_ascs
        False

    Attributes:
        all_instances (list): List of all the SAP instances listed by the command.
        function_instances (list): List of functional SAP instances
                                   E.g. Diagnostics Agents SMDA97/SMDA98
        business_instances (list): List of business SAP instances
                                   E.g. HANA, NetWeaver, ASCS, or others
        local_instances (list): List of all SAP instances running on this host
    """
    """ tuple: Tuple of the prefix string of the functional SAP instances"""

    def __init__(self, hostname, insts, lssap):
        hn = hostname.hostname
        fqdn = hostname.fqdn
        data = {}
        self.local_instances = []
        self.business_instances = []
        self.function_instances = []
        self.all_instances = []
        self._types = set()
        if insts:
            self._types = insts.types
            self.all_instances = insts.instances
            for inst in insts.data:
                k = inst['InstanceName']
                if (hn == inst['Hostname'].split('.')[0] or
                        fqdn == inst['FullQualifiedHostname'] or
                        fqdn == inst['Hostname']):
                    self.local_instances.append(k)
                data[k] = SAPInstances(k,
                                       inst['Hostname'],
                                       inst['SID'],
                                       inst['InstanceType'],
                                       inst['SystemNumber'],
                                       inst['FullQualifiedHostname'],
                                       inst['SapVersionInfo'])
        elif lssap:
            for inst in lssap.data:
                k = inst['Instance']
                t = k.rstrip('1234567890')
                self.all_instances.append(k)
                self._types.add(t)
                self.local_instances.append(k) if hn == inst['SAPLOCALHOST'].split('.')[0] else None
                data[k] = SAPInstances(k,
                                       inst['SAPLOCALHOST'],
                                       inst['SID'],
                                       t,
                                       inst['Nr'],
                                       None,
                                       inst['Version'])
        if not data:
            raise SkipComponent('No SAP instance.')

        self.update(data)

        for i in self.all_instances:
            (self.function_instances if i.startswith(FUNC_TYPES) else self.business_instances).append(i)

    def version(self, instance):
        """str: Returns the version of the ``instance``."""
        return self[instance].version if instance in self else None

    def sid(self, instance):
        """str: Returns the sid of the ``instance``."""
        return self[instance].sid if instance in self else None

    def type(self, instance):
        """str: Returns the type code of the ``instance``."""
        return self[instance].type if instance in self else None

    def hostname(self, instance):
        """str: Returns the hostname of the ``instance``."""
        return self[instance].hostname if instance in self else None

    def number(self, instance):
        """str: Returns the systeme number of the ``instance``."""
        return self[instance].number if instance in self else None

    @property
    def is_netweaver(self):
        """bool: Is any SAP NetWeaver instance detected?"""
        return any(_t in self._types for _t in NETW_TYPES)

    @property
    def is_hana(self):
        """bool: Is any SAP HANA instance detected?"""
        return 'HDB' in self._types

    @property
    def is_ascs(self):
        """bool: Is any ABAP Central Services instance detected?"""
        return 'ASCS' in self._types

    @property
    def data(self):
        """dict: Dict with the instance name as the key and instance details as the value."""
        return self
