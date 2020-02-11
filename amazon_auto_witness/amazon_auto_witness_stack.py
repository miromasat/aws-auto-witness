from aws_cdk import core, aws_dynamodb, aws_s3, aws_athena, aws_stepfunctions, aws_lambda


class AmazonAutoWitnessStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)


        archive = aws_s3.Bucket(self, 
                                                    id='_archive')
        data = aws_s3.Bucket(self, 
                                                    id='_data')
        clips = aws_s3.Bucket(self, 
                                                    id='_clips')                                
        preferences = aws_dynamodb.Table(self,      id='_preferences', 
                                                    table_name='witness_preferences', 
                                                    partition_key=aws_dynamodb.Attribute(name='preference_name', type='STRING'))
        
        # space for athena manifests and queries

        # space for stepfunction
        orchestrator = aws_stepfunctions.StateMachine(self,
                                                    id='_orchestrator',
                                                    state_machine_name='witness_orchestrator')
        # space for feeder Lambda function
        feeder = aws_lambda.Function(self,
                                                    id='_feeder',
                                                    code='return True',
                                                    handler='function.py',
                                                    runtime='python3.7',
                                                    description='Feeder function for the Witness project')

        # space for saver Lambda function
        saver = aws_lambda.Function(self,
                                                    id='saver',
                                                    code='return True',
                                                    handler='function.py',
                                                    runtime='python3.7',
                                                    description='Saver function for the Witness project')

        # space for sagemaker notebook

        # space for iam roles
 
