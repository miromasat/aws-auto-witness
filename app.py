#!/usr/bin/env python3

from aws_cdk import core

from cdk.storage import Storage
from cdk.compute import Computes
from cdk.ml import Ml

#app > stack(s) > constructs

app = core.App()
Storage(app, "witness-storage")
Compute(app, "witness-compute")
Ml(app, "witness-ml")


app.synth()
