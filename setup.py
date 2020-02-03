import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="amazon_auto_witness",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "amazon_auto_witness"},
    packages=setuptools.find_packages(where="amazon_auto_witness"),

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws-stepfunctions",
        "aws-cdk.aws-stepfunctions-tasks",
        "aws_cdk.aws_s3",
        "aws_cdk.aws_s3_deployment",
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
