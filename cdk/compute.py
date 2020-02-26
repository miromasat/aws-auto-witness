from aws_cdk import (core, aws_s3, aws_dynamodb, aws_lambda, aws_stepfunctions, aws_stepfunctions_tasks as aws_tasks, aws_s3_notifications as s3n)

class Computes(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # space for feeder Lambda function
        feeder = aws_lambda.Function(self,
                                                    id='_feeder',
                                                    code=aws_lambda.Code.asset('./code'),
                                                    handler='feeder.handler',
                                                    runtime=aws_lambda.Runtime.PYTHON_3_7,
                                                    description='Feeder function for the Witness project')

        # space for saver Lambda function
        saver = aws_lambda.Function(self,
                                                    id='_saver',
                                                    code=aws_lambda.Code.asset('./code'),
                                                    handler='saver.handler',
                                                    runtime=aws_lambda.Runtime.PYTHON_3_7,
                                                    description='Saver function for the Witness project')
        # space for feeder lambda trigger
        archive.add_event_notification(aws_s3.EventType.OBJECT_CREATED_PUT, s3n.LambdaDestination(feeder))


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