#!/usr/bin/env python3

from aws_cdk import core

from amazon_auto_witness.amazon_auto_witness_stack import AmazonAutoWitnessStack

#app > stack(s) > constructs

app = core.App()
AmazonAutoWitnessStack(app, "amazon-auto-witness")

app.synth()
