from aws_cdk import core, aws_dynamodb, aws_s3, aws_athena


class AmazonAutoWitnessStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)


        archive = aws_s3.Bucket(self, 
                                        id='_archive')
        datastore = aws_s3.Bucket(self, 
                                        id='_datastore')

        configuration = aws_dynamodb.Table(self,    id='_configuration', 
                                                    table_name='witness_configuration', 
                                                    partition_key=aws_dynamodb.Attribute(name='parameter', type='STRING'))
        
