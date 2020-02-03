from aws_cdk import core, aws_dynamodb


class AmazonAutoWitnessStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)



        # The code that defines your stack goes here
