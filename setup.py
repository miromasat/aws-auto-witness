import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="amazon_auto_witness",
    version="0.0.2",

    description="Spatial Query Engine based on AWS Rekognition, Amazon S3, AWS Step Functions and Amazon Timestream",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Miro Masat",

    package_dir={"": "cdk"},
    packages=setuptools.find_packages(where="cdk"),

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws-stepfunctions",
        "aws-cdk.aws-stepfunctions-tasks",
        "aws_cdk.aws_s3",
        "aws_cdk.aws_s3_deployment",
        "aws_cdk.aws_s3_notifications",
        "aws_cdk.aws_dynamodb",
        "aws_cdk.aws_lambda",
        "aws_cdk.aws_apigatewayv2",
        "aws_cdk.aws_events",
        "aws_cdk.aws_events_targets",
        "aws_cdk.aws_eventschemas"

    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
