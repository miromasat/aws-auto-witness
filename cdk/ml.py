from aws_cdk import (core, aws_s3, aws_dynamodb, aws_lambda, aws_stepfunctions, aws_stepfunctions_tasks as aws_tasks, aws_s3_notifications as s3n)

class Ml(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        