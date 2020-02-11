
# Welcome to AutoWitness
### Spatial Query Engine based on AWS Rekognition, Amazon S3, AWS Step Functions and Amazon Timestream

- to set up an infrsatructure, follow [https://github.com/aws-samples/aws-cdk-examples#Python]

## Architecture Diagram can be found below:
![AutoWitness Architecture](AutoWitnessArchitectureEXPORT.png?raw=true "AutoWitness Architecture")
### The mechanics of the architecture are described below:
1. Architecture awaits ingestion into `Archive` S3 bucket either from the video archive or from live cameras. Videos need to land in `Archive` S3 bucket in one of supported formats.
2. `Archive` S3 bucket upon the object landing triggers a notification to `Feeder` Lambda function that lies within `Orchestrator` Step Function Workflow that kicks in and manages the rest of the labelling and storing the result.
3. `Feeder` Lambda function reads and loads `Preferences` DynamoDB table, that describes, what is required of the `Label` Rekognition task and what metadata should be tracked and recorded.
4. `Label` Rekognition task runs and returns the finished metadata and spatial representation of the scene to the `Saver` Lambda function.
5. `Saver` Lambda function populates `Data` S3 bucket with searchable metadata and `Clip` S3 bucket with processed video clips that contain features only.
6. `Witness` SageMaker Notebook is set up and equipped with all libraries that allow to consume and query both `Data` S3 bucket and `Clips` S3 bucket.
7. Customer can access this on-demand `Witness` SageMaker Notebook to query, preview, manipulate or channel both processed video clips and metadata into further ML pipelines and/or simulations. 