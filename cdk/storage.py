from aws_cdk import (core, aws_s3, aws_dynamodb, aws_lambda, aws_stepfunctions, aws_stepfunctions_tasks as aws_tasks, aws_s3_notifications as s3n)

class Storage(core.Stack):

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

        # space for feeder lambda permissions
        preferences.grant_read_data(feeder)
        
        # space for saver lambda permissions
        data.grant_put(saver)
        clips.grant_put(saver)

        # space for sagemaker notebook

        # space for iam roles
 
