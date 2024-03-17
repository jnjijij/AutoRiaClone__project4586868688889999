import boto3

route53 = boto3.client('route53')

response = route53.change_resource_record_sets(
    HostedZoneId='your-hosted-zone-id',
    ChangeBatch={
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': 'your-domain-name',
                    'Type': 'A',
                    'AliasTarget': {
                        'HostedZoneId': 'your-alias-hosted-zone-id',
                        'DNSName': 'your-alias-dns-name',
                        'EvaluateTargetHealth': False
                    }
                }
            }
        ]
    }
)