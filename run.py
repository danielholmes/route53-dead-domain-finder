#!/usr/bin/env python
"""Route53 Dead Domain Finder

Usage:
  run.py find --config=<config>
"""
import json

import boto3
import dns.resolver
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Route53 Dead Domain Finder')
    config_file = arguments.get('--config')
    with open(config_file) as config_content:
        for account in json.load(config_content):
            print("Checking {}".format(account.get('name')))

            client = boto3.client(
                'route53',
                aws_access_key_id=account.get('access_key_id'),
                aws_secret_access_key=account.get('secret_access_key')
            )
            for zone in client.list_hosted_zones_by_name().get('HostedZones'):
                domain = zone.get('Name').rstrip('.')
                records = client.list_resource_record_sets(
                    HostedZoneId=zone.get('Id'),
                    StartRecordType='NS',
                    StartRecordName=zone.get('Name'),
                    MaxItems='1'
                )
                ns_values = [r.get('Value') for r in records.get('ResourceRecordSets')[0].get('ResourceRecords')]
                try:
                    actual_ns_values = [
                        '.'.join([l.decode('utf8') for l in n.target.labels])
                        for n in dns.resolver.query(domain, 'NS')
                    ]
                    difference = set(ns_values) - set(actual_ns_values)

                    if len(difference) > 0:
                        print(' ' + domain)
                        print('  Route53: ' + ','.join(ns_values))
                        print('  Actual:  ' + ','.join(actual_ns_values))
                except dns.resolver.NoNameservers as e:
                    print(' ' + domain)
                    print('  Error retrieving NS: {}'.format(str(e)))
                except dns.resolver.NXDOMAIN as e:
                    print(' ' + domain)
                    print('  Error retrieving NS: {}'.format(str(e)))

            print('-' * 40)