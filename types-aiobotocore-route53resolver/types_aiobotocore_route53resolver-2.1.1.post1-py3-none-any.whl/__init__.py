"""
Main interface for route53resolver service.

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_route53resolver import (
        Client,
        ListFirewallConfigsPaginator,
        ListFirewallDomainListsPaginator,
        ListFirewallDomainsPaginator,
        ListFirewallRuleGroupAssociationsPaginator,
        ListFirewallRuleGroupsPaginator,
        ListFirewallRulesPaginator,
        ListResolverConfigsPaginator,
        ListResolverDnssecConfigsPaginator,
        ListResolverEndpointIpAddressesPaginator,
        ListResolverEndpointsPaginator,
        ListResolverQueryLogConfigAssociationsPaginator,
        ListResolverQueryLogConfigsPaginator,
        ListResolverRuleAssociationsPaginator,
        ListResolverRulesPaginator,
        ListTagsForResourcePaginator,
        Route53ResolverClient,
    )

    session = get_session()
    async with session.create_client("route53resolver") as client:
        client: Route53ResolverClient
        ...


    list_firewall_configs_paginator: ListFirewallConfigsPaginator = client.get_paginator("list_firewall_configs")
    list_firewall_domain_lists_paginator: ListFirewallDomainListsPaginator = client.get_paginator("list_firewall_domain_lists")
    list_firewall_domains_paginator: ListFirewallDomainsPaginator = client.get_paginator("list_firewall_domains")
    list_firewall_rule_group_associations_paginator: ListFirewallRuleGroupAssociationsPaginator = client.get_paginator("list_firewall_rule_group_associations")
    list_firewall_rule_groups_paginator: ListFirewallRuleGroupsPaginator = client.get_paginator("list_firewall_rule_groups")
    list_firewall_rules_paginator: ListFirewallRulesPaginator = client.get_paginator("list_firewall_rules")
    list_resolver_configs_paginator: ListResolverConfigsPaginator = client.get_paginator("list_resolver_configs")
    list_resolver_dnssec_configs_paginator: ListResolverDnssecConfigsPaginator = client.get_paginator("list_resolver_dnssec_configs")
    list_resolver_endpoint_ip_addresses_paginator: ListResolverEndpointIpAddressesPaginator = client.get_paginator("list_resolver_endpoint_ip_addresses")
    list_resolver_endpoints_paginator: ListResolverEndpointsPaginator = client.get_paginator("list_resolver_endpoints")
    list_resolver_query_log_config_associations_paginator: ListResolverQueryLogConfigAssociationsPaginator = client.get_paginator("list_resolver_query_log_config_associations")
    list_resolver_query_log_configs_paginator: ListResolverQueryLogConfigsPaginator = client.get_paginator("list_resolver_query_log_configs")
    list_resolver_rule_associations_paginator: ListResolverRuleAssociationsPaginator = client.get_paginator("list_resolver_rule_associations")
    list_resolver_rules_paginator: ListResolverRulesPaginator = client.get_paginator("list_resolver_rules")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
from .client import Route53ResolverClient
from .paginator import (
    ListFirewallConfigsPaginator,
    ListFirewallDomainListsPaginator,
    ListFirewallDomainsPaginator,
    ListFirewallRuleGroupAssociationsPaginator,
    ListFirewallRuleGroupsPaginator,
    ListFirewallRulesPaginator,
    ListResolverConfigsPaginator,
    ListResolverDnssecConfigsPaginator,
    ListResolverEndpointIpAddressesPaginator,
    ListResolverEndpointsPaginator,
    ListResolverQueryLogConfigAssociationsPaginator,
    ListResolverQueryLogConfigsPaginator,
    ListResolverRuleAssociationsPaginator,
    ListResolverRulesPaginator,
    ListTagsForResourcePaginator,
)

Client = Route53ResolverClient


__all__ = (
    "Client",
    "ListFirewallConfigsPaginator",
    "ListFirewallDomainListsPaginator",
    "ListFirewallDomainsPaginator",
    "ListFirewallRuleGroupAssociationsPaginator",
    "ListFirewallRuleGroupsPaginator",
    "ListFirewallRulesPaginator",
    "ListResolverConfigsPaginator",
    "ListResolverDnssecConfigsPaginator",
    "ListResolverEndpointIpAddressesPaginator",
    "ListResolverEndpointsPaginator",
    "ListResolverQueryLogConfigAssociationsPaginator",
    "ListResolverQueryLogConfigsPaginator",
    "ListResolverRuleAssociationsPaginator",
    "ListResolverRulesPaginator",
    "ListTagsForResourcePaginator",
    "Route53ResolverClient",
)
