import boto3

cloudwatch = boto3.client("cloudwatch")

alarm_name = "my-alarm"
metric_name = "CPUUtilization"
namespace = "AWS/EC2"
statistic = "Average"
period = 60
evaluation_periods = 1
threshold = 80
comparison_operator = "GreaterThanOrEqualToThreshold"
alarm_description = "This alarm monitors EC2 CPU utilization"
alarm_actions = ["arn:aws:sns:us-east-1:123456789012:my-topic"]

cloudwatch.put_metric_alarm(
    AlarmName=alarm_name,
    ComparisonOperator=comparison_operator,
    EvaluationPeriods=evaluation_periods,
    MetricName=metric_name,
    Namespace=namespace,
    Period=period,
    Statistic=statistic,
    Threshold=threshold,
    AlarmDescription=alarm_description,
    AlarmActions=alarm_actions,
)