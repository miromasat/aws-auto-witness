from aws_cdk import (core, aws_s3, aws_dynamodb, aws_lambda, aws_stepfunctions, aws_stepfunctions_tasks as aws_tasks)

class AmazonAutoWitnessStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)


        archive = aws_s3.Bucket(self, 
                                                    id='_archive', )
        data = aws_s3.Bucket(self, 
                                                    id='_data')
        clips = aws_s3.Bucket(self, 
                                                    id='_clips')                                
        preferences = aws_dynamodb.Table(self,      id='_preferences', 
                                                    table_name='witness_preferences', 
                                                    partition_key=aws_dynamodb.Attribute(name='preference_name', type=aws_dynamodb.AttributeType.STRING))
        
        # space for athena manifests and queries

        
        # space for feeder Lambda function
        feeder = aws_lambda.Function(self,
                                                    id='_feeder',
                                                    code=aws_lambda.Code.from_inline('pass;'),
                                                    handler='function.py',
                                                    runtime=aws_lambda.Runtime.PYTHON_3_7,
                                                    description='Feeder function for the Witness project')

        # space for saver Lambda function
        saver = aws_lambda.Function(self,
                                                    id='_saver',
                                                    code=aws_lambda.Code.from_inline('pass;'),
                                                    handler='function.py',
                                                    runtime=aws_lambda.Runtime.PYTHON_3_7,
                                                    description='Saver function for the Witness project')
        
        # space for stepfunction
        feederTask = aws_stepfunctions.Task(        self,
                                                    id='_feederTask',
                                                    task=aws_tasks.InvokeFunction(feeder))

        saverTask = aws_stepfunctions.Task(         self,
                                                    id='_saverTask',
                                                    task=aws_tasks.InvokeFunction(saver))                                            

        definition = feederTask.next(saverTask)

        orchestrator = aws_stepfunctions.StateMachine(self,
                                                    id='_orchestrator',
                                                    state_machine_name='witness_orchestrator',
                                                    definition=definition)

        # space for sagemaker notebook

        # space for iam roles
 
