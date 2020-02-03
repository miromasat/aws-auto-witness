"""
## AWS::APIGatewayv2 Construct Library

<!--BEGIN STABILITY BANNER-->---


![Stability: Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

> **This is a *developer preview* (public beta) module. Releases might lack important features and might have
> future breaking changes.**
>
> This API is still under active development and subject to non-backward
> compatible changes or removal in any future version. Use of the API is not recommended in production
> environments. Experimental APIs are not subject to the Semantic Versioning model.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_apigatewayv2 as apigatewayv2
```
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

import aws_cdk.core

__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-apigatewayv2", "1.22.0", __name__, "aws-apigatewayv2@1.22.0.jsii.tgz")


@jsii.implements(aws_cdk.core.IInspectable)
class CfnApi(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-apigatewayv2.CfnApi"):
    """A CloudFormation ``AWS::ApiGatewayV2::Api``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html
    cloudformationResource:
    :cloudformationResource:: AWS::ApiGatewayV2::Api
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, api_key_selection_expression: typing.Optional[str]=None, base_path: typing.Optional[str]=None, body: typing.Any=None, body_s3_location: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["BodyS3LocationProperty"]]]=None, cors_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CorsProperty"]]]=None, credentials_arn: typing.Optional[str]=None, description: typing.Optional[str]=None, disable_schema_validation: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, fail_on_warnings: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, name: typing.Optional[str]=None, protocol_type: typing.Optional[str]=None, route_key: typing.Optional[str]=None, route_selection_expression: typing.Optional[str]=None, tags: typing.Any=None, target: typing.Optional[str]=None, version: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::ApiGatewayV2::Api``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_key_selection_expression: ``AWS::ApiGatewayV2::Api.ApiKeySelectionExpression``.
        :param base_path: ``AWS::ApiGatewayV2::Api.BasePath``.
        :param body: ``AWS::ApiGatewayV2::Api.Body``.
        :param body_s3_location: ``AWS::ApiGatewayV2::Api.BodyS3Location``.
        :param cors_configuration: ``AWS::ApiGatewayV2::Api.CorsConfiguration``.
        :param credentials_arn: ``AWS::ApiGatewayV2::Api.CredentialsArn``.
        :param description: ``AWS::ApiGatewayV2::Api.Description``.
        :param disable_schema_validation: ``AWS::ApiGatewayV2::Api.DisableSchemaValidation``.
        :param fail_on_warnings: ``AWS::ApiGatewayV2::Api.FailOnWarnings``.
        :param name: ``AWS::ApiGatewayV2::Api.Name``.
        :param protocol_type: ``AWS::ApiGatewayV2::Api.ProtocolType``.
        :param route_key: ``AWS::ApiGatewayV2::Api.RouteKey``.
        :param route_selection_expression: ``AWS::ApiGatewayV2::Api.RouteSelectionExpression``.
        :param tags: ``AWS::ApiGatewayV2::Api.Tags``.
        :param target: ``AWS::ApiGatewayV2::Api.Target``.
        :param version: ``AWS::ApiGatewayV2::Api.Version``.
        """
        props = CfnApiProps(api_key_selection_expression=api_key_selection_expression, base_path=base_path, body=body, body_s3_location=body_s3_location, cors_configuration=cors_configuration, credentials_arn=credentials_arn, description=description, disable_schema_validation=disable_schema_validation, fail_on_warnings=fail_on_warnings, name=name, protocol_type=protocol_type, route_key=route_key, route_selection_expression=route_selection_expression, tags=tags, target=target, version=version)

        jsii.create(CfnApi, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::ApiGatewayV2::Api.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Api.Body``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-body
        """
        return jsii.get(self, "body")

    @body.setter
    def body(self, value: typing.Any):
        jsii.set(self, "body", value)

    @builtins.property
    @jsii.member(jsii_name="apiKeySelectionExpression")
    def api_key_selection_expression(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.ApiKeySelectionExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-apikeyselectionexpression
        """
        return jsii.get(self, "apiKeySelectionExpression")

    @api_key_selection_expression.setter
    def api_key_selection_expression(self, value: typing.Optional[str]):
        jsii.set(self, "apiKeySelectionExpression", value)

    @builtins.property
    @jsii.member(jsii_name="basePath")
    def base_path(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.BasePath``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-basepath
        """
        return jsii.get(self, "basePath")

    @base_path.setter
    def base_path(self, value: typing.Optional[str]):
        jsii.set(self, "basePath", value)

    @builtins.property
    @jsii.member(jsii_name="bodyS3Location")
    def body_s3_location(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["BodyS3LocationProperty"]]]:
        """``AWS::ApiGatewayV2::Api.BodyS3Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-bodys3location
        """
        return jsii.get(self, "bodyS3Location")

    @body_s3_location.setter
    def body_s3_location(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["BodyS3LocationProperty"]]]):
        jsii.set(self, "bodyS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="corsConfiguration")
    def cors_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CorsProperty"]]]:
        """``AWS::ApiGatewayV2::Api.CorsConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-corsconfiguration
        """
        return jsii.get(self, "corsConfiguration")

    @cors_configuration.setter
    def cors_configuration(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CorsProperty"]]]):
        jsii.set(self, "corsConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="credentialsArn")
    def credentials_arn(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.CredentialsArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-credentialsarn
        """
        return jsii.get(self, "credentialsArn")

    @credentials_arn.setter
    def credentials_arn(self, value: typing.Optional[str]):
        jsii.set(self, "credentialsArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disableSchemaValidation")
    def disable_schema_validation(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::ApiGatewayV2::Api.DisableSchemaValidation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-disableschemavalidation
        """
        return jsii.get(self, "disableSchemaValidation")

    @disable_schema_validation.setter
    def disable_schema_validation(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        jsii.set(self, "disableSchemaValidation", value)

    @builtins.property
    @jsii.member(jsii_name="failOnWarnings")
    def fail_on_warnings(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::ApiGatewayV2::Api.FailOnWarnings``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-failonwarnings
        """
        return jsii.get(self, "failOnWarnings")

    @fail_on_warnings.setter
    def fail_on_warnings(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        jsii.set(self, "failOnWarnings", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="protocolType")
    def protocol_type(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.ProtocolType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-protocoltype
        """
        return jsii.get(self, "protocolType")

    @protocol_type.setter
    def protocol_type(self, value: typing.Optional[str]):
        jsii.set(self, "protocolType", value)

    @builtins.property
    @jsii.member(jsii_name="routeKey")
    def route_key(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.RouteKey``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-routekey
        """
        return jsii.get(self, "routeKey")

    @route_key.setter
    def route_key(self, value: typing.Optional[str]):
        jsii.set(self, "routeKey", value)

    @builtins.property
    @jsii.member(jsii_name="routeSelectionExpression")
    def route_selection_expression(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.RouteSelectionExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-routeselectionexpression
        """
        return jsii.get(self, "routeSelectionExpression")

    @route_selection_expression.setter
    def route_selection_expression(self, value: typing.Optional[str]):
        jsii.set(self, "routeSelectionExpression", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.Target``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-target
        """
        return jsii.get(self, "target")

    @target.setter
    def target(self, value: typing.Optional[str]):
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.Version``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-version
        """
        return jsii.get(self, "version")

    @version.setter
    def version(self, value: typing.Optional[str]):
        jsii.set(self, "version", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnApi.BodyS3LocationProperty", jsii_struct_bases=[], name_mapping={'bucket': 'bucket', 'etag': 'etag', 'key': 'key', 'version': 'version'})
    class BodyS3LocationProperty():
        def __init__(self, *, bucket: typing.Optional[str]=None, etag: typing.Optional[str]=None, key: typing.Optional[str]=None, version: typing.Optional[str]=None):
            """
            :param bucket: ``CfnApi.BodyS3LocationProperty.Bucket``.
            :param etag: ``CfnApi.BodyS3LocationProperty.Etag``.
            :param key: ``CfnApi.BodyS3LocationProperty.Key``.
            :param version: ``CfnApi.BodyS3LocationProperty.Version``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html
            """
            self._values = {
            }
            if bucket is not None: self._values["bucket"] = bucket
            if etag is not None: self._values["etag"] = etag
            if key is not None: self._values["key"] = key
            if version is not None: self._values["version"] = version

        @builtins.property
        def bucket(self) -> typing.Optional[str]:
            """``CfnApi.BodyS3LocationProperty.Bucket``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-bucket
            """
            return self._values.get('bucket')

        @builtins.property
        def etag(self) -> typing.Optional[str]:
            """``CfnApi.BodyS3LocationProperty.Etag``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-etag
            """
            return self._values.get('etag')

        @builtins.property
        def key(self) -> typing.Optional[str]:
            """``CfnApi.BodyS3LocationProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-key
            """
            return self._values.get('key')

        @builtins.property
        def version(self) -> typing.Optional[str]:
            """``CfnApi.BodyS3LocationProperty.Version``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-version
            """
            return self._values.get('version')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'BodyS3LocationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnApi.CorsProperty", jsii_struct_bases=[], name_mapping={'allow_credentials': 'allowCredentials', 'allow_headers': 'allowHeaders', 'allow_methods': 'allowMethods', 'allow_origins': 'allowOrigins', 'expose_headers': 'exposeHeaders', 'max_age': 'maxAge'})
    class CorsProperty():
        def __init__(self, *, allow_credentials: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, allow_headers: typing.Optional[typing.List[str]]=None, allow_methods: typing.Optional[typing.List[str]]=None, allow_origins: typing.Optional[typing.List[str]]=None, expose_headers: typing.Optional[typing.List[str]]=None, max_age: typing.Optional[jsii.Number]=None):
            """
            :param allow_credentials: ``CfnApi.CorsProperty.AllowCredentials``.
            :param allow_headers: ``CfnApi.CorsProperty.AllowHeaders``.
            :param allow_methods: ``CfnApi.CorsProperty.AllowMethods``.
            :param allow_origins: ``CfnApi.CorsProperty.AllowOrigins``.
            :param expose_headers: ``CfnApi.CorsProperty.ExposeHeaders``.
            :param max_age: ``CfnApi.CorsProperty.MaxAge``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html
            """
            self._values = {
            }
            if allow_credentials is not None: self._values["allow_credentials"] = allow_credentials
            if allow_headers is not None: self._values["allow_headers"] = allow_headers
            if allow_methods is not None: self._values["allow_methods"] = allow_methods
            if allow_origins is not None: self._values["allow_origins"] = allow_origins
            if expose_headers is not None: self._values["expose_headers"] = expose_headers
            if max_age is not None: self._values["max_age"] = max_age

        @builtins.property
        def allow_credentials(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnApi.CorsProperty.AllowCredentials``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-allowcredentials
            """
            return self._values.get('allow_credentials')

        @builtins.property
        def allow_headers(self) -> typing.Optional[typing.List[str]]:
            """``CfnApi.CorsProperty.AllowHeaders``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-allowheaders
            """
            return self._values.get('allow_headers')

        @builtins.property
        def allow_methods(self) -> typing.Optional[typing.List[str]]:
            """``CfnApi.CorsProperty.AllowMethods``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-allowmethods
            """
            return self._values.get('allow_methods')

        @builtins.property
        def allow_origins(self) -> typing.Optional[typing.List[str]]:
            """``CfnApi.CorsProperty.AllowOrigins``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-alloworigins
            """
            return self._values.get('allow_origins')

        @builtins.property
        def expose_headers(self) -> typing.Optional[typing.List[str]]:
            """``CfnApi.CorsProperty.ExposeHeaders``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-exposeheaders
            """
            return self._values.get('expose_headers')

        @builtins.property
        def max_age(self) -> typing.Optional[jsii.Number]:
            """``CfnApi.CorsProperty.MaxAge``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-maxage
            """
            return self._values.get('max_age')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'CorsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.implements(aws_cdk.core.IInspectable)
class CfnApiMapping(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-apigatewayv2.CfnApiMapping"):
    """A CloudFormation ``AWS::ApiGatewayV2::ApiMapping``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html
    cloudformationResource:
    :cloudformationResource:: AWS::ApiGatewayV2::ApiMapping
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, api_id: str, domain_name: str, stage: str, api_mapping_key: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::ApiGatewayV2::ApiMapping``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::ApiGatewayV2::ApiMapping.ApiId``.
        :param domain_name: ``AWS::ApiGatewayV2::ApiMapping.DomainName``.
        :param stage: ``AWS::ApiGatewayV2::ApiMapping.Stage``.
        :param api_mapping_key: ``AWS::ApiGatewayV2::ApiMapping.ApiMappingKey``.
        """
        props = CfnApiMappingProps(api_id=api_id, domain_name=domain_name, stage=stage, api_mapping_key=api_mapping_key)

        jsii.create(CfnApiMapping, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::ApiMapping.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter
    def api_id(self, value: str):
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> str:
        """``AWS::ApiGatewayV2::ApiMapping.DomainName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-domainname
        """
        return jsii.get(self, "domainName")

    @domain_name.setter
    def domain_name(self, value: str):
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="stage")
    def stage(self) -> str:
        """``AWS::ApiGatewayV2::ApiMapping.Stage``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-stage
        """
        return jsii.get(self, "stage")

    @stage.setter
    def stage(self, value: str):
        jsii.set(self, "stage", value)

    @builtins.property
    @jsii.member(jsii_name="apiMappingKey")
    def api_mapping_key(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::ApiMapping.ApiMappingKey``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-apimappingkey
        """
        return jsii.get(self, "apiMappingKey")

    @api_mapping_key.setter
    def api_mapping_key(self, value: typing.Optional[str]):
        jsii.set(self, "apiMappingKey", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnApiMappingProps", jsii_struct_bases=[], name_mapping={'api_id': 'apiId', 'domain_name': 'domainName', 'stage': 'stage', 'api_mapping_key': 'apiMappingKey'})
class CfnApiMappingProps():
    def __init__(self, *, api_id: str, domain_name: str, stage: str, api_mapping_key: typing.Optional[str]=None):
        """Properties for defining a ``AWS::ApiGatewayV2::ApiMapping``.

        :param api_id: ``AWS::ApiGatewayV2::ApiMapping.ApiId``.
        :param domain_name: ``AWS::ApiGatewayV2::ApiMapping.DomainName``.
        :param stage: ``AWS::ApiGatewayV2::ApiMapping.Stage``.
        :param api_mapping_key: ``AWS::ApiGatewayV2::ApiMapping.ApiMappingKey``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html
        """
        self._values = {
            'api_id': api_id,
            'domain_name': domain_name,
            'stage': stage,
        }
        if api_mapping_key is not None: self._values["api_mapping_key"] = api_mapping_key

    @builtins.property
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::ApiMapping.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-apiid
        """
        return self._values.get('api_id')

    @builtins.property
    def domain_name(self) -> str:
        """``AWS::ApiGatewayV2::ApiMapping.DomainName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-domainname
        """
        return self._values.get('domain_name')

    @builtins.property
    def stage(self) -> str:
        """``AWS::ApiGatewayV2::ApiMapping.Stage``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-stage
        """
        return self._values.get('stage')

    @builtins.property
    def api_mapping_key(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::ApiMapping.ApiMappingKey``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-apimappingkey
        """
        return self._values.get('api_mapping_key')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnApiMappingProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnApiProps", jsii_struct_bases=[], name_mapping={'api_key_selection_expression': 'apiKeySelectionExpression', 'base_path': 'basePath', 'body': 'body', 'body_s3_location': 'bodyS3Location', 'cors_configuration': 'corsConfiguration', 'credentials_arn': 'credentialsArn', 'description': 'description', 'disable_schema_validation': 'disableSchemaValidation', 'fail_on_warnings': 'failOnWarnings', 'name': 'name', 'protocol_type': 'protocolType', 'route_key': 'routeKey', 'route_selection_expression': 'routeSelectionExpression', 'tags': 'tags', 'target': 'target', 'version': 'version'})
class CfnApiProps():
    def __init__(self, *, api_key_selection_expression: typing.Optional[str]=None, base_path: typing.Optional[str]=None, body: typing.Any=None, body_s3_location: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnApi.BodyS3LocationProperty"]]]=None, cors_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnApi.CorsProperty"]]]=None, credentials_arn: typing.Optional[str]=None, description: typing.Optional[str]=None, disable_schema_validation: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, fail_on_warnings: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, name: typing.Optional[str]=None, protocol_type: typing.Optional[str]=None, route_key: typing.Optional[str]=None, route_selection_expression: typing.Optional[str]=None, tags: typing.Any=None, target: typing.Optional[str]=None, version: typing.Optional[str]=None):
        """Properties for defining a ``AWS::ApiGatewayV2::Api``.

        :param api_key_selection_expression: ``AWS::ApiGatewayV2::Api.ApiKeySelectionExpression``.
        :param base_path: ``AWS::ApiGatewayV2::Api.BasePath``.
        :param body: ``AWS::ApiGatewayV2::Api.Body``.
        :param body_s3_location: ``AWS::ApiGatewayV2::Api.BodyS3Location``.
        :param cors_configuration: ``AWS::ApiGatewayV2::Api.CorsConfiguration``.
        :param credentials_arn: ``AWS::ApiGatewayV2::Api.CredentialsArn``.
        :param description: ``AWS::ApiGatewayV2::Api.Description``.
        :param disable_schema_validation: ``AWS::ApiGatewayV2::Api.DisableSchemaValidation``.
        :param fail_on_warnings: ``AWS::ApiGatewayV2::Api.FailOnWarnings``.
        :param name: ``AWS::ApiGatewayV2::Api.Name``.
        :param protocol_type: ``AWS::ApiGatewayV2::Api.ProtocolType``.
        :param route_key: ``AWS::ApiGatewayV2::Api.RouteKey``.
        :param route_selection_expression: ``AWS::ApiGatewayV2::Api.RouteSelectionExpression``.
        :param tags: ``AWS::ApiGatewayV2::Api.Tags``.
        :param target: ``AWS::ApiGatewayV2::Api.Target``.
        :param version: ``AWS::ApiGatewayV2::Api.Version``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html
        """
        self._values = {
        }
        if api_key_selection_expression is not None: self._values["api_key_selection_expression"] = api_key_selection_expression
        if base_path is not None: self._values["base_path"] = base_path
        if body is not None: self._values["body"] = body
        if body_s3_location is not None: self._values["body_s3_location"] = body_s3_location
        if cors_configuration is not None: self._values["cors_configuration"] = cors_configuration
        if credentials_arn is not None: self._values["credentials_arn"] = credentials_arn
        if description is not None: self._values["description"] = description
        if disable_schema_validation is not None: self._values["disable_schema_validation"] = disable_schema_validation
        if fail_on_warnings is not None: self._values["fail_on_warnings"] = fail_on_warnings
        if name is not None: self._values["name"] = name
        if protocol_type is not None: self._values["protocol_type"] = protocol_type
        if route_key is not None: self._values["route_key"] = route_key
        if route_selection_expression is not None: self._values["route_selection_expression"] = route_selection_expression
        if tags is not None: self._values["tags"] = tags
        if target is not None: self._values["target"] = target
        if version is not None: self._values["version"] = version

    @builtins.property
    def api_key_selection_expression(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.ApiKeySelectionExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-apikeyselectionexpression
        """
        return self._values.get('api_key_selection_expression')

    @builtins.property
    def base_path(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.BasePath``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-basepath
        """
        return self._values.get('base_path')

    @builtins.property
    def body(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Api.Body``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-body
        """
        return self._values.get('body')

    @builtins.property
    def body_s3_location(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnApi.BodyS3LocationProperty"]]]:
        """``AWS::ApiGatewayV2::Api.BodyS3Location``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-bodys3location
        """
        return self._values.get('body_s3_location')

    @builtins.property
    def cors_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnApi.CorsProperty"]]]:
        """``AWS::ApiGatewayV2::Api.CorsConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-corsconfiguration
        """
        return self._values.get('cors_configuration')

    @builtins.property
    def credentials_arn(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.CredentialsArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-credentialsarn
        """
        return self._values.get('credentials_arn')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-description
        """
        return self._values.get('description')

    @builtins.property
    def disable_schema_validation(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::ApiGatewayV2::Api.DisableSchemaValidation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-disableschemavalidation
        """
        return self._values.get('disable_schema_validation')

    @builtins.property
    def fail_on_warnings(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::ApiGatewayV2::Api.FailOnWarnings``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-failonwarnings
        """
        return self._values.get('fail_on_warnings')

    @builtins.property
    def name(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-name
        """
        return self._values.get('name')

    @builtins.property
    def protocol_type(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.ProtocolType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-protocoltype
        """
        return self._values.get('protocol_type')

    @builtins.property
    def route_key(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.RouteKey``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-routekey
        """
        return self._values.get('route_key')

    @builtins.property
    def route_selection_expression(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.RouteSelectionExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-routeselectionexpression
        """
        return self._values.get('route_selection_expression')

    @builtins.property
    def tags(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Api.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-tags
        """
        return self._values.get('tags')

    @builtins.property
    def target(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.Target``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-target
        """
        return self._values.get('target')

    @builtins.property
    def version(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Api.Version``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-version
        """
        return self._values.get('version')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnApiProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnAuthorizer(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-apigatewayv2.CfnAuthorizer"):
    """A CloudFormation ``AWS::ApiGatewayV2::Authorizer``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html
    cloudformationResource:
    :cloudformationResource:: AWS::ApiGatewayV2::Authorizer
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, api_id: str, authorizer_type: str, identity_source: typing.List[str], name: str, authorizer_credentials_arn: typing.Optional[str]=None, authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number]=None, authorizer_uri: typing.Optional[str]=None, identity_validation_expression: typing.Optional[str]=None, jwt_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["JWTConfigurationProperty"]]]=None) -> None:
        """Create a new ``AWS::ApiGatewayV2::Authorizer``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::ApiGatewayV2::Authorizer.ApiId``.
        :param authorizer_type: ``AWS::ApiGatewayV2::Authorizer.AuthorizerType``.
        :param identity_source: ``AWS::ApiGatewayV2::Authorizer.IdentitySource``.
        :param name: ``AWS::ApiGatewayV2::Authorizer.Name``.
        :param authorizer_credentials_arn: ``AWS::ApiGatewayV2::Authorizer.AuthorizerCredentialsArn``.
        :param authorizer_result_ttl_in_seconds: ``AWS::ApiGatewayV2::Authorizer.AuthorizerResultTtlInSeconds``.
        :param authorizer_uri: ``AWS::ApiGatewayV2::Authorizer.AuthorizerUri``.
        :param identity_validation_expression: ``AWS::ApiGatewayV2::Authorizer.IdentityValidationExpression``.
        :param jwt_configuration: ``AWS::ApiGatewayV2::Authorizer.JwtConfiguration``.
        """
        props = CfnAuthorizerProps(api_id=api_id, authorizer_type=authorizer_type, identity_source=identity_source, name=name, authorizer_credentials_arn=authorizer_credentials_arn, authorizer_result_ttl_in_seconds=authorizer_result_ttl_in_seconds, authorizer_uri=authorizer_uri, identity_validation_expression=identity_validation_expression, jwt_configuration=jwt_configuration)

        jsii.create(CfnAuthorizer, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::Authorizer.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter
    def api_id(self, value: str):
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerType")
    def authorizer_type(self) -> str:
        """``AWS::ApiGatewayV2::Authorizer.AuthorizerType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizertype
        """
        return jsii.get(self, "authorizerType")

    @authorizer_type.setter
    def authorizer_type(self, value: str):
        jsii.set(self, "authorizerType", value)

    @builtins.property
    @jsii.member(jsii_name="identitySource")
    def identity_source(self) -> typing.List[str]:
        """``AWS::ApiGatewayV2::Authorizer.IdentitySource``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-identitysource
        """
        return jsii.get(self, "identitySource")

    @identity_source.setter
    def identity_source(self, value: typing.List[str]):
        jsii.set(self, "identitySource", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::ApiGatewayV2::Authorizer.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerCredentialsArn")
    def authorizer_credentials_arn(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Authorizer.AuthorizerCredentialsArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizercredentialsarn
        """
        return jsii.get(self, "authorizerCredentialsArn")

    @authorizer_credentials_arn.setter
    def authorizer_credentials_arn(self, value: typing.Optional[str]):
        jsii.set(self, "authorizerCredentialsArn", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(self) -> typing.Optional[jsii.Number]:
        """``AWS::ApiGatewayV2::Authorizer.AuthorizerResultTtlInSeconds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizerresultttlinseconds
        """
        return jsii.get(self, "authorizerResultTtlInSeconds")

    @authorizer_result_ttl_in_seconds.setter
    def authorizer_result_ttl_in_seconds(self, value: typing.Optional[jsii.Number]):
        jsii.set(self, "authorizerResultTtlInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerUri")
    def authorizer_uri(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Authorizer.AuthorizerUri``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizeruri
        """
        return jsii.get(self, "authorizerUri")

    @authorizer_uri.setter
    def authorizer_uri(self, value: typing.Optional[str]):
        jsii.set(self, "authorizerUri", value)

    @builtins.property
    @jsii.member(jsii_name="identityValidationExpression")
    def identity_validation_expression(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Authorizer.IdentityValidationExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-identityvalidationexpression
        """
        return jsii.get(self, "identityValidationExpression")

    @identity_validation_expression.setter
    def identity_validation_expression(self, value: typing.Optional[str]):
        jsii.set(self, "identityValidationExpression", value)

    @builtins.property
    @jsii.member(jsii_name="jwtConfiguration")
    def jwt_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["JWTConfigurationProperty"]]]:
        """``AWS::ApiGatewayV2::Authorizer.JwtConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-jwtconfiguration
        """
        return jsii.get(self, "jwtConfiguration")

    @jwt_configuration.setter
    def jwt_configuration(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["JWTConfigurationProperty"]]]):
        jsii.set(self, "jwtConfiguration", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnAuthorizer.JWTConfigurationProperty", jsii_struct_bases=[], name_mapping={'audience': 'audience', 'issuer': 'issuer'})
    class JWTConfigurationProperty():
        def __init__(self, *, audience: typing.Optional[typing.List[str]]=None, issuer: typing.Optional[str]=None):
            """
            :param audience: ``CfnAuthorizer.JWTConfigurationProperty.Audience``.
            :param issuer: ``CfnAuthorizer.JWTConfigurationProperty.Issuer``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html
            """
            self._values = {
            }
            if audience is not None: self._values["audience"] = audience
            if issuer is not None: self._values["issuer"] = issuer

        @builtins.property
        def audience(self) -> typing.Optional[typing.List[str]]:
            """``CfnAuthorizer.JWTConfigurationProperty.Audience``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html#cfn-apigatewayv2-authorizer-jwtconfiguration-audience
            """
            return self._values.get('audience')

        @builtins.property
        def issuer(self) -> typing.Optional[str]:
            """``CfnAuthorizer.JWTConfigurationProperty.Issuer``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html#cfn-apigatewayv2-authorizer-jwtconfiguration-issuer
            """
            return self._values.get('issuer')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'JWTConfigurationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnAuthorizerProps", jsii_struct_bases=[], name_mapping={'api_id': 'apiId', 'authorizer_type': 'authorizerType', 'identity_source': 'identitySource', 'name': 'name', 'authorizer_credentials_arn': 'authorizerCredentialsArn', 'authorizer_result_ttl_in_seconds': 'authorizerResultTtlInSeconds', 'authorizer_uri': 'authorizerUri', 'identity_validation_expression': 'identityValidationExpression', 'jwt_configuration': 'jwtConfiguration'})
class CfnAuthorizerProps():
    def __init__(self, *, api_id: str, authorizer_type: str, identity_source: typing.List[str], name: str, authorizer_credentials_arn: typing.Optional[str]=None, authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number]=None, authorizer_uri: typing.Optional[str]=None, identity_validation_expression: typing.Optional[str]=None, jwt_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnAuthorizer.JWTConfigurationProperty"]]]=None):
        """Properties for defining a ``AWS::ApiGatewayV2::Authorizer``.

        :param api_id: ``AWS::ApiGatewayV2::Authorizer.ApiId``.
        :param authorizer_type: ``AWS::ApiGatewayV2::Authorizer.AuthorizerType``.
        :param identity_source: ``AWS::ApiGatewayV2::Authorizer.IdentitySource``.
        :param name: ``AWS::ApiGatewayV2::Authorizer.Name``.
        :param authorizer_credentials_arn: ``AWS::ApiGatewayV2::Authorizer.AuthorizerCredentialsArn``.
        :param authorizer_result_ttl_in_seconds: ``AWS::ApiGatewayV2::Authorizer.AuthorizerResultTtlInSeconds``.
        :param authorizer_uri: ``AWS::ApiGatewayV2::Authorizer.AuthorizerUri``.
        :param identity_validation_expression: ``AWS::ApiGatewayV2::Authorizer.IdentityValidationExpression``.
        :param jwt_configuration: ``AWS::ApiGatewayV2::Authorizer.JwtConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html
        """
        self._values = {
            'api_id': api_id,
            'authorizer_type': authorizer_type,
            'identity_source': identity_source,
            'name': name,
        }
        if authorizer_credentials_arn is not None: self._values["authorizer_credentials_arn"] = authorizer_credentials_arn
        if authorizer_result_ttl_in_seconds is not None: self._values["authorizer_result_ttl_in_seconds"] = authorizer_result_ttl_in_seconds
        if authorizer_uri is not None: self._values["authorizer_uri"] = authorizer_uri
        if identity_validation_expression is not None: self._values["identity_validation_expression"] = identity_validation_expression
        if jwt_configuration is not None: self._values["jwt_configuration"] = jwt_configuration

    @builtins.property
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::Authorizer.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-apiid
        """
        return self._values.get('api_id')

    @builtins.property
    def authorizer_type(self) -> str:
        """``AWS::ApiGatewayV2::Authorizer.AuthorizerType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizertype
        """
        return self._values.get('authorizer_type')

    @builtins.property
    def identity_source(self) -> typing.List[str]:
        """``AWS::ApiGatewayV2::Authorizer.IdentitySource``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-identitysource
        """
        return self._values.get('identity_source')

    @builtins.property
    def name(self) -> str:
        """``AWS::ApiGatewayV2::Authorizer.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-name
        """
        return self._values.get('name')

    @builtins.property
    def authorizer_credentials_arn(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Authorizer.AuthorizerCredentialsArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizercredentialsarn
        """
        return self._values.get('authorizer_credentials_arn')

    @builtins.property
    def authorizer_result_ttl_in_seconds(self) -> typing.Optional[jsii.Number]:
        """``AWS::ApiGatewayV2::Authorizer.AuthorizerResultTtlInSeconds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizerresultttlinseconds
        """
        return self._values.get('authorizer_result_ttl_in_seconds')

    @builtins.property
    def authorizer_uri(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Authorizer.AuthorizerUri``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizeruri
        """
        return self._values.get('authorizer_uri')

    @builtins.property
    def identity_validation_expression(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Authorizer.IdentityValidationExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-identityvalidationexpression
        """
        return self._values.get('identity_validation_expression')

    @builtins.property
    def jwt_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnAuthorizer.JWTConfigurationProperty"]]]:
        """``AWS::ApiGatewayV2::Authorizer.JwtConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-jwtconfiguration
        """
        return self._values.get('jwt_configuration')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnAuthorizerProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDeployment(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-apigatewayv2.CfnDeployment"):
    """A CloudFormation ``AWS::ApiGatewayV2::Deployment``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html
    cloudformationResource:
    :cloudformationResource:: AWS::ApiGatewayV2::Deployment
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, api_id: str, description: typing.Optional[str]=None, stage_name: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::ApiGatewayV2::Deployment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::ApiGatewayV2::Deployment.ApiId``.
        :param description: ``AWS::ApiGatewayV2::Deployment.Description``.
        :param stage_name: ``AWS::ApiGatewayV2::Deployment.StageName``.
        """
        props = CfnDeploymentProps(api_id=api_id, description=description, stage_name=stage_name)

        jsii.create(CfnDeployment, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::Deployment.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter
    def api_id(self, value: str):
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Deployment.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="stageName")
    def stage_name(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Deployment.StageName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-stagename
        """
        return jsii.get(self, "stageName")

    @stage_name.setter
    def stage_name(self, value: typing.Optional[str]):
        jsii.set(self, "stageName", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnDeploymentProps", jsii_struct_bases=[], name_mapping={'api_id': 'apiId', 'description': 'description', 'stage_name': 'stageName'})
class CfnDeploymentProps():
    def __init__(self, *, api_id: str, description: typing.Optional[str]=None, stage_name: typing.Optional[str]=None):
        """Properties for defining a ``AWS::ApiGatewayV2::Deployment``.

        :param api_id: ``AWS::ApiGatewayV2::Deployment.ApiId``.
        :param description: ``AWS::ApiGatewayV2::Deployment.Description``.
        :param stage_name: ``AWS::ApiGatewayV2::Deployment.StageName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html
        """
        self._values = {
            'api_id': api_id,
        }
        if description is not None: self._values["description"] = description
        if stage_name is not None: self._values["stage_name"] = stage_name

    @builtins.property
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::Deployment.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-apiid
        """
        return self._values.get('api_id')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Deployment.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-description
        """
        return self._values.get('description')

    @builtins.property
    def stage_name(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Deployment.StageName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-stagename
        """
        return self._values.get('stage_name')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnDeploymentProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDomainName(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-apigatewayv2.CfnDomainName"):
    """A CloudFormation ``AWS::ApiGatewayV2::DomainName``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html
    cloudformationResource:
    :cloudformationResource:: AWS::ApiGatewayV2::DomainName
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, domain_name: str, domain_name_configurations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union["DomainNameConfigurationProperty", aws_cdk.core.IResolvable]]]]]=None, tags: typing.Any=None) -> None:
        """Create a new ``AWS::ApiGatewayV2::DomainName``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param domain_name: ``AWS::ApiGatewayV2::DomainName.DomainName``.
        :param domain_name_configurations: ``AWS::ApiGatewayV2::DomainName.DomainNameConfigurations``.
        :param tags: ``AWS::ApiGatewayV2::DomainName.Tags``.
        """
        props = CfnDomainNameProps(domain_name=domain_name, domain_name_configurations=domain_name_configurations, tags=tags)

        jsii.create(CfnDomainName, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="attrRegionalDomainName")
    def attr_regional_domain_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: RegionalDomainName
        """
        return jsii.get(self, "attrRegionalDomainName")

    @builtins.property
    @jsii.member(jsii_name="attrRegionalHostedZoneId")
    def attr_regional_hosted_zone_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: RegionalHostedZoneId
        """
        return jsii.get(self, "attrRegionalHostedZoneId")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::ApiGatewayV2::DomainName.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> str:
        """``AWS::ApiGatewayV2::DomainName.DomainName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-domainname
        """
        return jsii.get(self, "domainName")

    @domain_name.setter
    def domain_name(self, value: str):
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="domainNameConfigurations")
    def domain_name_configurations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union["DomainNameConfigurationProperty", aws_cdk.core.IResolvable]]]]]:
        """``AWS::ApiGatewayV2::DomainName.DomainNameConfigurations``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-domainnameconfigurations
        """
        return jsii.get(self, "domainNameConfigurations")

    @domain_name_configurations.setter
    def domain_name_configurations(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union["DomainNameConfigurationProperty", aws_cdk.core.IResolvable]]]]]):
        jsii.set(self, "domainNameConfigurations", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnDomainName.DomainNameConfigurationProperty", jsii_struct_bases=[], name_mapping={'certificate_arn': 'certificateArn', 'certificate_name': 'certificateName', 'endpoint_type': 'endpointType'})
    class DomainNameConfigurationProperty():
        def __init__(self, *, certificate_arn: typing.Optional[str]=None, certificate_name: typing.Optional[str]=None, endpoint_type: typing.Optional[str]=None):
            """
            :param certificate_arn: ``CfnDomainName.DomainNameConfigurationProperty.CertificateArn``.
            :param certificate_name: ``CfnDomainName.DomainNameConfigurationProperty.CertificateName``.
            :param endpoint_type: ``CfnDomainName.DomainNameConfigurationProperty.EndpointType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html
            """
            self._values = {
            }
            if certificate_arn is not None: self._values["certificate_arn"] = certificate_arn
            if certificate_name is not None: self._values["certificate_name"] = certificate_name
            if endpoint_type is not None: self._values["endpoint_type"] = endpoint_type

        @builtins.property
        def certificate_arn(self) -> typing.Optional[str]:
            """``CfnDomainName.DomainNameConfigurationProperty.CertificateArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-certificatearn
            """
            return self._values.get('certificate_arn')

        @builtins.property
        def certificate_name(self) -> typing.Optional[str]:
            """``CfnDomainName.DomainNameConfigurationProperty.CertificateName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-certificatename
            """
            return self._values.get('certificate_name')

        @builtins.property
        def endpoint_type(self) -> typing.Optional[str]:
            """``CfnDomainName.DomainNameConfigurationProperty.EndpointType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-endpointtype
            """
            return self._values.get('endpoint_type')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'DomainNameConfigurationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnDomainNameProps", jsii_struct_bases=[], name_mapping={'domain_name': 'domainName', 'domain_name_configurations': 'domainNameConfigurations', 'tags': 'tags'})
class CfnDomainNameProps():
    def __init__(self, *, domain_name: str, domain_name_configurations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union["CfnDomainName.DomainNameConfigurationProperty", aws_cdk.core.IResolvable]]]]]=None, tags: typing.Any=None):
        """Properties for defining a ``AWS::ApiGatewayV2::DomainName``.

        :param domain_name: ``AWS::ApiGatewayV2::DomainName.DomainName``.
        :param domain_name_configurations: ``AWS::ApiGatewayV2::DomainName.DomainNameConfigurations``.
        :param tags: ``AWS::ApiGatewayV2::DomainName.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html
        """
        self._values = {
            'domain_name': domain_name,
        }
        if domain_name_configurations is not None: self._values["domain_name_configurations"] = domain_name_configurations
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def domain_name(self) -> str:
        """``AWS::ApiGatewayV2::DomainName.DomainName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-domainname
        """
        return self._values.get('domain_name')

    @builtins.property
    def domain_name_configurations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union["CfnDomainName.DomainNameConfigurationProperty", aws_cdk.core.IResolvable]]]]]:
        """``AWS::ApiGatewayV2::DomainName.DomainNameConfigurations``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-domainnameconfigurations
        """
        return self._values.get('domain_name_configurations')

    @builtins.property
    def tags(self) -> typing.Any:
        """``AWS::ApiGatewayV2::DomainName.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnDomainNameProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnIntegration(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-apigatewayv2.CfnIntegration"):
    """A CloudFormation ``AWS::ApiGatewayV2::Integration``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html
    cloudformationResource:
    :cloudformationResource:: AWS::ApiGatewayV2::Integration
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, api_id: str, integration_type: str, connection_type: typing.Optional[str]=None, content_handling_strategy: typing.Optional[str]=None, credentials_arn: typing.Optional[str]=None, description: typing.Optional[str]=None, integration_method: typing.Optional[str]=None, integration_uri: typing.Optional[str]=None, passthrough_behavior: typing.Optional[str]=None, payload_format_version: typing.Optional[str]=None, request_parameters: typing.Any=None, request_templates: typing.Any=None, template_selection_expression: typing.Optional[str]=None, timeout_in_millis: typing.Optional[jsii.Number]=None) -> None:
        """Create a new ``AWS::ApiGatewayV2::Integration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::ApiGatewayV2::Integration.ApiId``.
        :param integration_type: ``AWS::ApiGatewayV2::Integration.IntegrationType``.
        :param connection_type: ``AWS::ApiGatewayV2::Integration.ConnectionType``.
        :param content_handling_strategy: ``AWS::ApiGatewayV2::Integration.ContentHandlingStrategy``.
        :param credentials_arn: ``AWS::ApiGatewayV2::Integration.CredentialsArn``.
        :param description: ``AWS::ApiGatewayV2::Integration.Description``.
        :param integration_method: ``AWS::ApiGatewayV2::Integration.IntegrationMethod``.
        :param integration_uri: ``AWS::ApiGatewayV2::Integration.IntegrationUri``.
        :param passthrough_behavior: ``AWS::ApiGatewayV2::Integration.PassthroughBehavior``.
        :param payload_format_version: ``AWS::ApiGatewayV2::Integration.PayloadFormatVersion``.
        :param request_parameters: ``AWS::ApiGatewayV2::Integration.RequestParameters``.
        :param request_templates: ``AWS::ApiGatewayV2::Integration.RequestTemplates``.
        :param template_selection_expression: ``AWS::ApiGatewayV2::Integration.TemplateSelectionExpression``.
        :param timeout_in_millis: ``AWS::ApiGatewayV2::Integration.TimeoutInMillis``.
        """
        props = CfnIntegrationProps(api_id=api_id, integration_type=integration_type, connection_type=connection_type, content_handling_strategy=content_handling_strategy, credentials_arn=credentials_arn, description=description, integration_method=integration_method, integration_uri=integration_uri, passthrough_behavior=passthrough_behavior, payload_format_version=payload_format_version, request_parameters=request_parameters, request_templates=request_templates, template_selection_expression=template_selection_expression, timeout_in_millis=timeout_in_millis)

        jsii.create(CfnIntegration, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::Integration.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter
    def api_id(self, value: str):
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="integrationType")
    def integration_type(self) -> str:
        """``AWS::ApiGatewayV2::Integration.IntegrationType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationtype
        """
        return jsii.get(self, "integrationType")

    @integration_type.setter
    def integration_type(self, value: str):
        jsii.set(self, "integrationType", value)

    @builtins.property
    @jsii.member(jsii_name="requestParameters")
    def request_parameters(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Integration.RequestParameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-requestparameters
        """
        return jsii.get(self, "requestParameters")

    @request_parameters.setter
    def request_parameters(self, value: typing.Any):
        jsii.set(self, "requestParameters", value)

    @builtins.property
    @jsii.member(jsii_name="requestTemplates")
    def request_templates(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Integration.RequestTemplates``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-requesttemplates
        """
        return jsii.get(self, "requestTemplates")

    @request_templates.setter
    def request_templates(self, value: typing.Any):
        jsii.set(self, "requestTemplates", value)

    @builtins.property
    @jsii.member(jsii_name="connectionType")
    def connection_type(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.ConnectionType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-connectiontype
        """
        return jsii.get(self, "connectionType")

    @connection_type.setter
    def connection_type(self, value: typing.Optional[str]):
        jsii.set(self, "connectionType", value)

    @builtins.property
    @jsii.member(jsii_name="contentHandlingStrategy")
    def content_handling_strategy(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.ContentHandlingStrategy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-contenthandlingstrategy
        """
        return jsii.get(self, "contentHandlingStrategy")

    @content_handling_strategy.setter
    def content_handling_strategy(self, value: typing.Optional[str]):
        jsii.set(self, "contentHandlingStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="credentialsArn")
    def credentials_arn(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.CredentialsArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-credentialsarn
        """
        return jsii.get(self, "credentialsArn")

    @credentials_arn.setter
    def credentials_arn(self, value: typing.Optional[str]):
        jsii.set(self, "credentialsArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="integrationMethod")
    def integration_method(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.IntegrationMethod``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationmethod
        """
        return jsii.get(self, "integrationMethod")

    @integration_method.setter
    def integration_method(self, value: typing.Optional[str]):
        jsii.set(self, "integrationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="integrationUri")
    def integration_uri(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.IntegrationUri``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationuri
        """
        return jsii.get(self, "integrationUri")

    @integration_uri.setter
    def integration_uri(self, value: typing.Optional[str]):
        jsii.set(self, "integrationUri", value)

    @builtins.property
    @jsii.member(jsii_name="passthroughBehavior")
    def passthrough_behavior(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.PassthroughBehavior``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-passthroughbehavior
        """
        return jsii.get(self, "passthroughBehavior")

    @passthrough_behavior.setter
    def passthrough_behavior(self, value: typing.Optional[str]):
        jsii.set(self, "passthroughBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="payloadFormatVersion")
    def payload_format_version(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.PayloadFormatVersion``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-payloadformatversion
        """
        return jsii.get(self, "payloadFormatVersion")

    @payload_format_version.setter
    def payload_format_version(self, value: typing.Optional[str]):
        jsii.set(self, "payloadFormatVersion", value)

    @builtins.property
    @jsii.member(jsii_name="templateSelectionExpression")
    def template_selection_expression(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.TemplateSelectionExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-templateselectionexpression
        """
        return jsii.get(self, "templateSelectionExpression")

    @template_selection_expression.setter
    def template_selection_expression(self, value: typing.Optional[str]):
        jsii.set(self, "templateSelectionExpression", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutInMillis")
    def timeout_in_millis(self) -> typing.Optional[jsii.Number]:
        """``AWS::ApiGatewayV2::Integration.TimeoutInMillis``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-timeoutinmillis
        """
        return jsii.get(self, "timeoutInMillis")

    @timeout_in_millis.setter
    def timeout_in_millis(self, value: typing.Optional[jsii.Number]):
        jsii.set(self, "timeoutInMillis", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnIntegrationProps", jsii_struct_bases=[], name_mapping={'api_id': 'apiId', 'integration_type': 'integrationType', 'connection_type': 'connectionType', 'content_handling_strategy': 'contentHandlingStrategy', 'credentials_arn': 'credentialsArn', 'description': 'description', 'integration_method': 'integrationMethod', 'integration_uri': 'integrationUri', 'passthrough_behavior': 'passthroughBehavior', 'payload_format_version': 'payloadFormatVersion', 'request_parameters': 'requestParameters', 'request_templates': 'requestTemplates', 'template_selection_expression': 'templateSelectionExpression', 'timeout_in_millis': 'timeoutInMillis'})
class CfnIntegrationProps():
    def __init__(self, *, api_id: str, integration_type: str, connection_type: typing.Optional[str]=None, content_handling_strategy: typing.Optional[str]=None, credentials_arn: typing.Optional[str]=None, description: typing.Optional[str]=None, integration_method: typing.Optional[str]=None, integration_uri: typing.Optional[str]=None, passthrough_behavior: typing.Optional[str]=None, payload_format_version: typing.Optional[str]=None, request_parameters: typing.Any=None, request_templates: typing.Any=None, template_selection_expression: typing.Optional[str]=None, timeout_in_millis: typing.Optional[jsii.Number]=None):
        """Properties for defining a ``AWS::ApiGatewayV2::Integration``.

        :param api_id: ``AWS::ApiGatewayV2::Integration.ApiId``.
        :param integration_type: ``AWS::ApiGatewayV2::Integration.IntegrationType``.
        :param connection_type: ``AWS::ApiGatewayV2::Integration.ConnectionType``.
        :param content_handling_strategy: ``AWS::ApiGatewayV2::Integration.ContentHandlingStrategy``.
        :param credentials_arn: ``AWS::ApiGatewayV2::Integration.CredentialsArn``.
        :param description: ``AWS::ApiGatewayV2::Integration.Description``.
        :param integration_method: ``AWS::ApiGatewayV2::Integration.IntegrationMethod``.
        :param integration_uri: ``AWS::ApiGatewayV2::Integration.IntegrationUri``.
        :param passthrough_behavior: ``AWS::ApiGatewayV2::Integration.PassthroughBehavior``.
        :param payload_format_version: ``AWS::ApiGatewayV2::Integration.PayloadFormatVersion``.
        :param request_parameters: ``AWS::ApiGatewayV2::Integration.RequestParameters``.
        :param request_templates: ``AWS::ApiGatewayV2::Integration.RequestTemplates``.
        :param template_selection_expression: ``AWS::ApiGatewayV2::Integration.TemplateSelectionExpression``.
        :param timeout_in_millis: ``AWS::ApiGatewayV2::Integration.TimeoutInMillis``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html
        """
        self._values = {
            'api_id': api_id,
            'integration_type': integration_type,
        }
        if connection_type is not None: self._values["connection_type"] = connection_type
        if content_handling_strategy is not None: self._values["content_handling_strategy"] = content_handling_strategy
        if credentials_arn is not None: self._values["credentials_arn"] = credentials_arn
        if description is not None: self._values["description"] = description
        if integration_method is not None: self._values["integration_method"] = integration_method
        if integration_uri is not None: self._values["integration_uri"] = integration_uri
        if passthrough_behavior is not None: self._values["passthrough_behavior"] = passthrough_behavior
        if payload_format_version is not None: self._values["payload_format_version"] = payload_format_version
        if request_parameters is not None: self._values["request_parameters"] = request_parameters
        if request_templates is not None: self._values["request_templates"] = request_templates
        if template_selection_expression is not None: self._values["template_selection_expression"] = template_selection_expression
        if timeout_in_millis is not None: self._values["timeout_in_millis"] = timeout_in_millis

    @builtins.property
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::Integration.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-apiid
        """
        return self._values.get('api_id')

    @builtins.property
    def integration_type(self) -> str:
        """``AWS::ApiGatewayV2::Integration.IntegrationType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationtype
        """
        return self._values.get('integration_type')

    @builtins.property
    def connection_type(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.ConnectionType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-connectiontype
        """
        return self._values.get('connection_type')

    @builtins.property
    def content_handling_strategy(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.ContentHandlingStrategy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-contenthandlingstrategy
        """
        return self._values.get('content_handling_strategy')

    @builtins.property
    def credentials_arn(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.CredentialsArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-credentialsarn
        """
        return self._values.get('credentials_arn')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-description
        """
        return self._values.get('description')

    @builtins.property
    def integration_method(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.IntegrationMethod``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationmethod
        """
        return self._values.get('integration_method')

    @builtins.property
    def integration_uri(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.IntegrationUri``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationuri
        """
        return self._values.get('integration_uri')

    @builtins.property
    def passthrough_behavior(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.PassthroughBehavior``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-passthroughbehavior
        """
        return self._values.get('passthrough_behavior')

    @builtins.property
    def payload_format_version(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.PayloadFormatVersion``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-payloadformatversion
        """
        return self._values.get('payload_format_version')

    @builtins.property
    def request_parameters(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Integration.RequestParameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-requestparameters
        """
        return self._values.get('request_parameters')

    @builtins.property
    def request_templates(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Integration.RequestTemplates``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-requesttemplates
        """
        return self._values.get('request_templates')

    @builtins.property
    def template_selection_expression(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Integration.TemplateSelectionExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-templateselectionexpression
        """
        return self._values.get('template_selection_expression')

    @builtins.property
    def timeout_in_millis(self) -> typing.Optional[jsii.Number]:
        """``AWS::ApiGatewayV2::Integration.TimeoutInMillis``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-timeoutinmillis
        """
        return self._values.get('timeout_in_millis')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnIntegrationProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnIntegrationResponse(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-apigatewayv2.CfnIntegrationResponse"):
    """A CloudFormation ``AWS::ApiGatewayV2::IntegrationResponse``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html
    cloudformationResource:
    :cloudformationResource:: AWS::ApiGatewayV2::IntegrationResponse
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, api_id: str, integration_id: str, integration_response_key: str, content_handling_strategy: typing.Optional[str]=None, response_parameters: typing.Any=None, response_templates: typing.Any=None, template_selection_expression: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::ApiGatewayV2::IntegrationResponse``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::ApiGatewayV2::IntegrationResponse.ApiId``.
        :param integration_id: ``AWS::ApiGatewayV2::IntegrationResponse.IntegrationId``.
        :param integration_response_key: ``AWS::ApiGatewayV2::IntegrationResponse.IntegrationResponseKey``.
        :param content_handling_strategy: ``AWS::ApiGatewayV2::IntegrationResponse.ContentHandlingStrategy``.
        :param response_parameters: ``AWS::ApiGatewayV2::IntegrationResponse.ResponseParameters``.
        :param response_templates: ``AWS::ApiGatewayV2::IntegrationResponse.ResponseTemplates``.
        :param template_selection_expression: ``AWS::ApiGatewayV2::IntegrationResponse.TemplateSelectionExpression``.
        """
        props = CfnIntegrationResponseProps(api_id=api_id, integration_id=integration_id, integration_response_key=integration_response_key, content_handling_strategy=content_handling_strategy, response_parameters=response_parameters, response_templates=response_templates, template_selection_expression=template_selection_expression)

        jsii.create(CfnIntegrationResponse, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::IntegrationResponse.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter
    def api_id(self, value: str):
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="integrationId")
    def integration_id(self) -> str:
        """``AWS::ApiGatewayV2::IntegrationResponse.IntegrationId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-integrationid
        """
        return jsii.get(self, "integrationId")

    @integration_id.setter
    def integration_id(self, value: str):
        jsii.set(self, "integrationId", value)

    @builtins.property
    @jsii.member(jsii_name="integrationResponseKey")
    def integration_response_key(self) -> str:
        """``AWS::ApiGatewayV2::IntegrationResponse.IntegrationResponseKey``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-integrationresponsekey
        """
        return jsii.get(self, "integrationResponseKey")

    @integration_response_key.setter
    def integration_response_key(self, value: str):
        jsii.set(self, "integrationResponseKey", value)

    @builtins.property
    @jsii.member(jsii_name="responseParameters")
    def response_parameters(self) -> typing.Any:
        """``AWS::ApiGatewayV2::IntegrationResponse.ResponseParameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-responseparameters
        """
        return jsii.get(self, "responseParameters")

    @response_parameters.setter
    def response_parameters(self, value: typing.Any):
        jsii.set(self, "responseParameters", value)

    @builtins.property
    @jsii.member(jsii_name="responseTemplates")
    def response_templates(self) -> typing.Any:
        """``AWS::ApiGatewayV2::IntegrationResponse.ResponseTemplates``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-responsetemplates
        """
        return jsii.get(self, "responseTemplates")

    @response_templates.setter
    def response_templates(self, value: typing.Any):
        jsii.set(self, "responseTemplates", value)

    @builtins.property
    @jsii.member(jsii_name="contentHandlingStrategy")
    def content_handling_strategy(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::IntegrationResponse.ContentHandlingStrategy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-contenthandlingstrategy
        """
        return jsii.get(self, "contentHandlingStrategy")

    @content_handling_strategy.setter
    def content_handling_strategy(self, value: typing.Optional[str]):
        jsii.set(self, "contentHandlingStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="templateSelectionExpression")
    def template_selection_expression(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::IntegrationResponse.TemplateSelectionExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-templateselectionexpression
        """
        return jsii.get(self, "templateSelectionExpression")

    @template_selection_expression.setter
    def template_selection_expression(self, value: typing.Optional[str]):
        jsii.set(self, "templateSelectionExpression", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnIntegrationResponseProps", jsii_struct_bases=[], name_mapping={'api_id': 'apiId', 'integration_id': 'integrationId', 'integration_response_key': 'integrationResponseKey', 'content_handling_strategy': 'contentHandlingStrategy', 'response_parameters': 'responseParameters', 'response_templates': 'responseTemplates', 'template_selection_expression': 'templateSelectionExpression'})
class CfnIntegrationResponseProps():
    def __init__(self, *, api_id: str, integration_id: str, integration_response_key: str, content_handling_strategy: typing.Optional[str]=None, response_parameters: typing.Any=None, response_templates: typing.Any=None, template_selection_expression: typing.Optional[str]=None):
        """Properties for defining a ``AWS::ApiGatewayV2::IntegrationResponse``.

        :param api_id: ``AWS::ApiGatewayV2::IntegrationResponse.ApiId``.
        :param integration_id: ``AWS::ApiGatewayV2::IntegrationResponse.IntegrationId``.
        :param integration_response_key: ``AWS::ApiGatewayV2::IntegrationResponse.IntegrationResponseKey``.
        :param content_handling_strategy: ``AWS::ApiGatewayV2::IntegrationResponse.ContentHandlingStrategy``.
        :param response_parameters: ``AWS::ApiGatewayV2::IntegrationResponse.ResponseParameters``.
        :param response_templates: ``AWS::ApiGatewayV2::IntegrationResponse.ResponseTemplates``.
        :param template_selection_expression: ``AWS::ApiGatewayV2::IntegrationResponse.TemplateSelectionExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html
        """
        self._values = {
            'api_id': api_id,
            'integration_id': integration_id,
            'integration_response_key': integration_response_key,
        }
        if content_handling_strategy is not None: self._values["content_handling_strategy"] = content_handling_strategy
        if response_parameters is not None: self._values["response_parameters"] = response_parameters
        if response_templates is not None: self._values["response_templates"] = response_templates
        if template_selection_expression is not None: self._values["template_selection_expression"] = template_selection_expression

    @builtins.property
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::IntegrationResponse.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-apiid
        """
        return self._values.get('api_id')

    @builtins.property
    def integration_id(self) -> str:
        """``AWS::ApiGatewayV2::IntegrationResponse.IntegrationId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-integrationid
        """
        return self._values.get('integration_id')

    @builtins.property
    def integration_response_key(self) -> str:
        """``AWS::ApiGatewayV2::IntegrationResponse.IntegrationResponseKey``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-integrationresponsekey
        """
        return self._values.get('integration_response_key')

    @builtins.property
    def content_handling_strategy(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::IntegrationResponse.ContentHandlingStrategy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-contenthandlingstrategy
        """
        return self._values.get('content_handling_strategy')

    @builtins.property
    def response_parameters(self) -> typing.Any:
        """``AWS::ApiGatewayV2::IntegrationResponse.ResponseParameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-responseparameters
        """
        return self._values.get('response_parameters')

    @builtins.property
    def response_templates(self) -> typing.Any:
        """``AWS::ApiGatewayV2::IntegrationResponse.ResponseTemplates``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-responsetemplates
        """
        return self._values.get('response_templates')

    @builtins.property
    def template_selection_expression(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::IntegrationResponse.TemplateSelectionExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-templateselectionexpression
        """
        return self._values.get('template_selection_expression')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnIntegrationResponseProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnModel(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-apigatewayv2.CfnModel"):
    """A CloudFormation ``AWS::ApiGatewayV2::Model``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html
    cloudformationResource:
    :cloudformationResource:: AWS::ApiGatewayV2::Model
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, api_id: str, name: str, schema: typing.Any, content_type: typing.Optional[str]=None, description: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::ApiGatewayV2::Model``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::ApiGatewayV2::Model.ApiId``.
        :param name: ``AWS::ApiGatewayV2::Model.Name``.
        :param schema: ``AWS::ApiGatewayV2::Model.Schema``.
        :param content_type: ``AWS::ApiGatewayV2::Model.ContentType``.
        :param description: ``AWS::ApiGatewayV2::Model.Description``.
        """
        props = CfnModelProps(api_id=api_id, name=name, schema=schema, content_type=content_type, description=description)

        jsii.create(CfnModel, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::Model.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter
    def api_id(self, value: str):
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::ApiGatewayV2::Model.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Model.Schema``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-schema
        """
        return jsii.get(self, "schema")

    @schema.setter
    def schema(self, value: typing.Any):
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Model.ContentType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-contenttype
        """
        return jsii.get(self, "contentType")

    @content_type.setter
    def content_type(self, value: typing.Optional[str]):
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Model.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        jsii.set(self, "description", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnModelProps", jsii_struct_bases=[], name_mapping={'api_id': 'apiId', 'name': 'name', 'schema': 'schema', 'content_type': 'contentType', 'description': 'description'})
class CfnModelProps():
    def __init__(self, *, api_id: str, name: str, schema: typing.Any, content_type: typing.Optional[str]=None, description: typing.Optional[str]=None):
        """Properties for defining a ``AWS::ApiGatewayV2::Model``.

        :param api_id: ``AWS::ApiGatewayV2::Model.ApiId``.
        :param name: ``AWS::ApiGatewayV2::Model.Name``.
        :param schema: ``AWS::ApiGatewayV2::Model.Schema``.
        :param content_type: ``AWS::ApiGatewayV2::Model.ContentType``.
        :param description: ``AWS::ApiGatewayV2::Model.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html
        """
        self._values = {
            'api_id': api_id,
            'name': name,
            'schema': schema,
        }
        if content_type is not None: self._values["content_type"] = content_type
        if description is not None: self._values["description"] = description

    @builtins.property
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::Model.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-apiid
        """
        return self._values.get('api_id')

    @builtins.property
    def name(self) -> str:
        """``AWS::ApiGatewayV2::Model.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-name
        """
        return self._values.get('name')

    @builtins.property
    def schema(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Model.Schema``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-schema
        """
        return self._values.get('schema')

    @builtins.property
    def content_type(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Model.ContentType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-contenttype
        """
        return self._values.get('content_type')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Model.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-description
        """
        return self._values.get('description')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnModelProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnRoute(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-apigatewayv2.CfnRoute"):
    """A CloudFormation ``AWS::ApiGatewayV2::Route``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html
    cloudformationResource:
    :cloudformationResource:: AWS::ApiGatewayV2::Route
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, api_id: str, route_key: str, api_key_required: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, authorization_scopes: typing.Optional[typing.List[str]]=None, authorization_type: typing.Optional[str]=None, authorizer_id: typing.Optional[str]=None, model_selection_expression: typing.Optional[str]=None, operation_name: typing.Optional[str]=None, request_models: typing.Any=None, request_parameters: typing.Any=None, route_response_selection_expression: typing.Optional[str]=None, target: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::ApiGatewayV2::Route``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::ApiGatewayV2::Route.ApiId``.
        :param route_key: ``AWS::ApiGatewayV2::Route.RouteKey``.
        :param api_key_required: ``AWS::ApiGatewayV2::Route.ApiKeyRequired``.
        :param authorization_scopes: ``AWS::ApiGatewayV2::Route.AuthorizationScopes``.
        :param authorization_type: ``AWS::ApiGatewayV2::Route.AuthorizationType``.
        :param authorizer_id: ``AWS::ApiGatewayV2::Route.AuthorizerId``.
        :param model_selection_expression: ``AWS::ApiGatewayV2::Route.ModelSelectionExpression``.
        :param operation_name: ``AWS::ApiGatewayV2::Route.OperationName``.
        :param request_models: ``AWS::ApiGatewayV2::Route.RequestModels``.
        :param request_parameters: ``AWS::ApiGatewayV2::Route.RequestParameters``.
        :param route_response_selection_expression: ``AWS::ApiGatewayV2::Route.RouteResponseSelectionExpression``.
        :param target: ``AWS::ApiGatewayV2::Route.Target``.
        """
        props = CfnRouteProps(api_id=api_id, route_key=route_key, api_key_required=api_key_required, authorization_scopes=authorization_scopes, authorization_type=authorization_type, authorizer_id=authorizer_id, model_selection_expression=model_selection_expression, operation_name=operation_name, request_models=request_models, request_parameters=request_parameters, route_response_selection_expression=route_response_selection_expression, target=target)

        jsii.create(CfnRoute, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::Route.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter
    def api_id(self, value: str):
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="requestModels")
    def request_models(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Route.RequestModels``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-requestmodels
        """
        return jsii.get(self, "requestModels")

    @request_models.setter
    def request_models(self, value: typing.Any):
        jsii.set(self, "requestModels", value)

    @builtins.property
    @jsii.member(jsii_name="requestParameters")
    def request_parameters(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Route.RequestParameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-requestparameters
        """
        return jsii.get(self, "requestParameters")

    @request_parameters.setter
    def request_parameters(self, value: typing.Any):
        jsii.set(self, "requestParameters", value)

    @builtins.property
    @jsii.member(jsii_name="routeKey")
    def route_key(self) -> str:
        """``AWS::ApiGatewayV2::Route.RouteKey``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-routekey
        """
        return jsii.get(self, "routeKey")

    @route_key.setter
    def route_key(self, value: str):
        jsii.set(self, "routeKey", value)

    @builtins.property
    @jsii.member(jsii_name="apiKeyRequired")
    def api_key_required(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::ApiGatewayV2::Route.ApiKeyRequired``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-apikeyrequired
        """
        return jsii.get(self, "apiKeyRequired")

    @api_key_required.setter
    def api_key_required(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        jsii.set(self, "apiKeyRequired", value)

    @builtins.property
    @jsii.member(jsii_name="authorizationScopes")
    def authorization_scopes(self) -> typing.Optional[typing.List[str]]:
        """``AWS::ApiGatewayV2::Route.AuthorizationScopes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizationscopes
        """
        return jsii.get(self, "authorizationScopes")

    @authorization_scopes.setter
    def authorization_scopes(self, value: typing.Optional[typing.List[str]]):
        jsii.set(self, "authorizationScopes", value)

    @builtins.property
    @jsii.member(jsii_name="authorizationType")
    def authorization_type(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Route.AuthorizationType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizationtype
        """
        return jsii.get(self, "authorizationType")

    @authorization_type.setter
    def authorization_type(self, value: typing.Optional[str]):
        jsii.set(self, "authorizationType", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerId")
    def authorizer_id(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Route.AuthorizerId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizerid
        """
        return jsii.get(self, "authorizerId")

    @authorizer_id.setter
    def authorizer_id(self, value: typing.Optional[str]):
        jsii.set(self, "authorizerId", value)

    @builtins.property
    @jsii.member(jsii_name="modelSelectionExpression")
    def model_selection_expression(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Route.ModelSelectionExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-modelselectionexpression
        """
        return jsii.get(self, "modelSelectionExpression")

    @model_selection_expression.setter
    def model_selection_expression(self, value: typing.Optional[str]):
        jsii.set(self, "modelSelectionExpression", value)

    @builtins.property
    @jsii.member(jsii_name="operationName")
    def operation_name(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Route.OperationName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-operationname
        """
        return jsii.get(self, "operationName")

    @operation_name.setter
    def operation_name(self, value: typing.Optional[str]):
        jsii.set(self, "operationName", value)

    @builtins.property
    @jsii.member(jsii_name="routeResponseSelectionExpression")
    def route_response_selection_expression(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Route.RouteResponseSelectionExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-routeresponseselectionexpression
        """
        return jsii.get(self, "routeResponseSelectionExpression")

    @route_response_selection_expression.setter
    def route_response_selection_expression(self, value: typing.Optional[str]):
        jsii.set(self, "routeResponseSelectionExpression", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Route.Target``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-target
        """
        return jsii.get(self, "target")

    @target.setter
    def target(self, value: typing.Optional[str]):
        jsii.set(self, "target", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnRoute.ParameterConstraintsProperty", jsii_struct_bases=[], name_mapping={'required': 'required'})
    class ParameterConstraintsProperty():
        def __init__(self, *, required: typing.Union[bool, aws_cdk.core.IResolvable]):
            """
            :param required: ``CfnRoute.ParameterConstraintsProperty.Required``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-route-parameterconstraints.html
            """
            self._values = {
                'required': required,
            }

        @builtins.property
        def required(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
            """``CfnRoute.ParameterConstraintsProperty.Required``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-route-parameterconstraints.html#cfn-apigatewayv2-route-parameterconstraints-required
            """
            return self._values.get('required')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ParameterConstraintsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnRouteProps", jsii_struct_bases=[], name_mapping={'api_id': 'apiId', 'route_key': 'routeKey', 'api_key_required': 'apiKeyRequired', 'authorization_scopes': 'authorizationScopes', 'authorization_type': 'authorizationType', 'authorizer_id': 'authorizerId', 'model_selection_expression': 'modelSelectionExpression', 'operation_name': 'operationName', 'request_models': 'requestModels', 'request_parameters': 'requestParameters', 'route_response_selection_expression': 'routeResponseSelectionExpression', 'target': 'target'})
class CfnRouteProps():
    def __init__(self, *, api_id: str, route_key: str, api_key_required: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, authorization_scopes: typing.Optional[typing.List[str]]=None, authorization_type: typing.Optional[str]=None, authorizer_id: typing.Optional[str]=None, model_selection_expression: typing.Optional[str]=None, operation_name: typing.Optional[str]=None, request_models: typing.Any=None, request_parameters: typing.Any=None, route_response_selection_expression: typing.Optional[str]=None, target: typing.Optional[str]=None):
        """Properties for defining a ``AWS::ApiGatewayV2::Route``.

        :param api_id: ``AWS::ApiGatewayV2::Route.ApiId``.
        :param route_key: ``AWS::ApiGatewayV2::Route.RouteKey``.
        :param api_key_required: ``AWS::ApiGatewayV2::Route.ApiKeyRequired``.
        :param authorization_scopes: ``AWS::ApiGatewayV2::Route.AuthorizationScopes``.
        :param authorization_type: ``AWS::ApiGatewayV2::Route.AuthorizationType``.
        :param authorizer_id: ``AWS::ApiGatewayV2::Route.AuthorizerId``.
        :param model_selection_expression: ``AWS::ApiGatewayV2::Route.ModelSelectionExpression``.
        :param operation_name: ``AWS::ApiGatewayV2::Route.OperationName``.
        :param request_models: ``AWS::ApiGatewayV2::Route.RequestModels``.
        :param request_parameters: ``AWS::ApiGatewayV2::Route.RequestParameters``.
        :param route_response_selection_expression: ``AWS::ApiGatewayV2::Route.RouteResponseSelectionExpression``.
        :param target: ``AWS::ApiGatewayV2::Route.Target``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html
        """
        self._values = {
            'api_id': api_id,
            'route_key': route_key,
        }
        if api_key_required is not None: self._values["api_key_required"] = api_key_required
        if authorization_scopes is not None: self._values["authorization_scopes"] = authorization_scopes
        if authorization_type is not None: self._values["authorization_type"] = authorization_type
        if authorizer_id is not None: self._values["authorizer_id"] = authorizer_id
        if model_selection_expression is not None: self._values["model_selection_expression"] = model_selection_expression
        if operation_name is not None: self._values["operation_name"] = operation_name
        if request_models is not None: self._values["request_models"] = request_models
        if request_parameters is not None: self._values["request_parameters"] = request_parameters
        if route_response_selection_expression is not None: self._values["route_response_selection_expression"] = route_response_selection_expression
        if target is not None: self._values["target"] = target

    @builtins.property
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::Route.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-apiid
        """
        return self._values.get('api_id')

    @builtins.property
    def route_key(self) -> str:
        """``AWS::ApiGatewayV2::Route.RouteKey``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-routekey
        """
        return self._values.get('route_key')

    @builtins.property
    def api_key_required(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::ApiGatewayV2::Route.ApiKeyRequired``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-apikeyrequired
        """
        return self._values.get('api_key_required')

    @builtins.property
    def authorization_scopes(self) -> typing.Optional[typing.List[str]]:
        """``AWS::ApiGatewayV2::Route.AuthorizationScopes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizationscopes
        """
        return self._values.get('authorization_scopes')

    @builtins.property
    def authorization_type(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Route.AuthorizationType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizationtype
        """
        return self._values.get('authorization_type')

    @builtins.property
    def authorizer_id(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Route.AuthorizerId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizerid
        """
        return self._values.get('authorizer_id')

    @builtins.property
    def model_selection_expression(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Route.ModelSelectionExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-modelselectionexpression
        """
        return self._values.get('model_selection_expression')

    @builtins.property
    def operation_name(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Route.OperationName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-operationname
        """
        return self._values.get('operation_name')

    @builtins.property
    def request_models(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Route.RequestModels``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-requestmodels
        """
        return self._values.get('request_models')

    @builtins.property
    def request_parameters(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Route.RequestParameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-requestparameters
        """
        return self._values.get('request_parameters')

    @builtins.property
    def route_response_selection_expression(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Route.RouteResponseSelectionExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-routeresponseselectionexpression
        """
        return self._values.get('route_response_selection_expression')

    @builtins.property
    def target(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Route.Target``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-target
        """
        return self._values.get('target')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnRouteProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnRouteResponse(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-apigatewayv2.CfnRouteResponse"):
    """A CloudFormation ``AWS::ApiGatewayV2::RouteResponse``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html
    cloudformationResource:
    :cloudformationResource:: AWS::ApiGatewayV2::RouteResponse
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, api_id: str, route_id: str, route_response_key: str, model_selection_expression: typing.Optional[str]=None, response_models: typing.Any=None, response_parameters: typing.Any=None) -> None:
        """Create a new ``AWS::ApiGatewayV2::RouteResponse``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::ApiGatewayV2::RouteResponse.ApiId``.
        :param route_id: ``AWS::ApiGatewayV2::RouteResponse.RouteId``.
        :param route_response_key: ``AWS::ApiGatewayV2::RouteResponse.RouteResponseKey``.
        :param model_selection_expression: ``AWS::ApiGatewayV2::RouteResponse.ModelSelectionExpression``.
        :param response_models: ``AWS::ApiGatewayV2::RouteResponse.ResponseModels``.
        :param response_parameters: ``AWS::ApiGatewayV2::RouteResponse.ResponseParameters``.
        """
        props = CfnRouteResponseProps(api_id=api_id, route_id=route_id, route_response_key=route_response_key, model_selection_expression=model_selection_expression, response_models=response_models, response_parameters=response_parameters)

        jsii.create(CfnRouteResponse, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::RouteResponse.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter
    def api_id(self, value: str):
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="responseModels")
    def response_models(self) -> typing.Any:
        """``AWS::ApiGatewayV2::RouteResponse.ResponseModels``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-responsemodels
        """
        return jsii.get(self, "responseModels")

    @response_models.setter
    def response_models(self, value: typing.Any):
        jsii.set(self, "responseModels", value)

    @builtins.property
    @jsii.member(jsii_name="responseParameters")
    def response_parameters(self) -> typing.Any:
        """``AWS::ApiGatewayV2::RouteResponse.ResponseParameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-responseparameters
        """
        return jsii.get(self, "responseParameters")

    @response_parameters.setter
    def response_parameters(self, value: typing.Any):
        jsii.set(self, "responseParameters", value)

    @builtins.property
    @jsii.member(jsii_name="routeId")
    def route_id(self) -> str:
        """``AWS::ApiGatewayV2::RouteResponse.RouteId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-routeid
        """
        return jsii.get(self, "routeId")

    @route_id.setter
    def route_id(self, value: str):
        jsii.set(self, "routeId", value)

    @builtins.property
    @jsii.member(jsii_name="routeResponseKey")
    def route_response_key(self) -> str:
        """``AWS::ApiGatewayV2::RouteResponse.RouteResponseKey``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-routeresponsekey
        """
        return jsii.get(self, "routeResponseKey")

    @route_response_key.setter
    def route_response_key(self, value: str):
        jsii.set(self, "routeResponseKey", value)

    @builtins.property
    @jsii.member(jsii_name="modelSelectionExpression")
    def model_selection_expression(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::RouteResponse.ModelSelectionExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-modelselectionexpression
        """
        return jsii.get(self, "modelSelectionExpression")

    @model_selection_expression.setter
    def model_selection_expression(self, value: typing.Optional[str]):
        jsii.set(self, "modelSelectionExpression", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnRouteResponse.ParameterConstraintsProperty", jsii_struct_bases=[], name_mapping={'required': 'required'})
    class ParameterConstraintsProperty():
        def __init__(self, *, required: typing.Union[bool, aws_cdk.core.IResolvable]):
            """
            :param required: ``CfnRouteResponse.ParameterConstraintsProperty.Required``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-routeresponse-parameterconstraints.html
            """
            self._values = {
                'required': required,
            }

        @builtins.property
        def required(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
            """``CfnRouteResponse.ParameterConstraintsProperty.Required``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-routeresponse-parameterconstraints.html#cfn-apigatewayv2-routeresponse-parameterconstraints-required
            """
            return self._values.get('required')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ParameterConstraintsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnRouteResponseProps", jsii_struct_bases=[], name_mapping={'api_id': 'apiId', 'route_id': 'routeId', 'route_response_key': 'routeResponseKey', 'model_selection_expression': 'modelSelectionExpression', 'response_models': 'responseModels', 'response_parameters': 'responseParameters'})
class CfnRouteResponseProps():
    def __init__(self, *, api_id: str, route_id: str, route_response_key: str, model_selection_expression: typing.Optional[str]=None, response_models: typing.Any=None, response_parameters: typing.Any=None):
        """Properties for defining a ``AWS::ApiGatewayV2::RouteResponse``.

        :param api_id: ``AWS::ApiGatewayV2::RouteResponse.ApiId``.
        :param route_id: ``AWS::ApiGatewayV2::RouteResponse.RouteId``.
        :param route_response_key: ``AWS::ApiGatewayV2::RouteResponse.RouteResponseKey``.
        :param model_selection_expression: ``AWS::ApiGatewayV2::RouteResponse.ModelSelectionExpression``.
        :param response_models: ``AWS::ApiGatewayV2::RouteResponse.ResponseModels``.
        :param response_parameters: ``AWS::ApiGatewayV2::RouteResponse.ResponseParameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html
        """
        self._values = {
            'api_id': api_id,
            'route_id': route_id,
            'route_response_key': route_response_key,
        }
        if model_selection_expression is not None: self._values["model_selection_expression"] = model_selection_expression
        if response_models is not None: self._values["response_models"] = response_models
        if response_parameters is not None: self._values["response_parameters"] = response_parameters

    @builtins.property
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::RouteResponse.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-apiid
        """
        return self._values.get('api_id')

    @builtins.property
    def route_id(self) -> str:
        """``AWS::ApiGatewayV2::RouteResponse.RouteId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-routeid
        """
        return self._values.get('route_id')

    @builtins.property
    def route_response_key(self) -> str:
        """``AWS::ApiGatewayV2::RouteResponse.RouteResponseKey``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-routeresponsekey
        """
        return self._values.get('route_response_key')

    @builtins.property
    def model_selection_expression(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::RouteResponse.ModelSelectionExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-modelselectionexpression
        """
        return self._values.get('model_selection_expression')

    @builtins.property
    def response_models(self) -> typing.Any:
        """``AWS::ApiGatewayV2::RouteResponse.ResponseModels``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-responsemodels
        """
        return self._values.get('response_models')

    @builtins.property
    def response_parameters(self) -> typing.Any:
        """``AWS::ApiGatewayV2::RouteResponse.ResponseParameters``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-responseparameters
        """
        return self._values.get('response_parameters')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnRouteResponseProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnStage(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-apigatewayv2.CfnStage"):
    """A CloudFormation ``AWS::ApiGatewayV2::Stage``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html
    cloudformationResource:
    :cloudformationResource:: AWS::ApiGatewayV2::Stage
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, api_id: str, stage_name: str, access_log_settings: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AccessLogSettingsProperty"]]]=None, auto_deploy: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, client_certificate_id: typing.Optional[str]=None, default_route_settings: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RouteSettingsProperty"]]]=None, deployment_id: typing.Optional[str]=None, description: typing.Optional[str]=None, route_settings: typing.Any=None, stage_variables: typing.Any=None, tags: typing.Any=None) -> None:
        """Create a new ``AWS::ApiGatewayV2::Stage``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_id: ``AWS::ApiGatewayV2::Stage.ApiId``.
        :param stage_name: ``AWS::ApiGatewayV2::Stage.StageName``.
        :param access_log_settings: ``AWS::ApiGatewayV2::Stage.AccessLogSettings``.
        :param auto_deploy: ``AWS::ApiGatewayV2::Stage.AutoDeploy``.
        :param client_certificate_id: ``AWS::ApiGatewayV2::Stage.ClientCertificateId``.
        :param default_route_settings: ``AWS::ApiGatewayV2::Stage.DefaultRouteSettings``.
        :param deployment_id: ``AWS::ApiGatewayV2::Stage.DeploymentId``.
        :param description: ``AWS::ApiGatewayV2::Stage.Description``.
        :param route_settings: ``AWS::ApiGatewayV2::Stage.RouteSettings``.
        :param stage_variables: ``AWS::ApiGatewayV2::Stage.StageVariables``.
        :param tags: ``AWS::ApiGatewayV2::Stage.Tags``.
        """
        props = CfnStageProps(api_id=api_id, stage_name=stage_name, access_log_settings=access_log_settings, auto_deploy=auto_deploy, client_certificate_id=client_certificate_id, default_route_settings=default_route_settings, deployment_id=deployment_id, description=description, route_settings=route_settings, stage_variables=stage_variables, tags=tags)

        jsii.create(CfnStage, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        """Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.

        stability
        :stability: experimental
        """
        return jsii.invoke(self, "inspect", [inspector])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::ApiGatewayV2::Stage.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::Stage.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-apiid
        """
        return jsii.get(self, "apiId")

    @api_id.setter
    def api_id(self, value: str):
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="routeSettings")
    def route_settings(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Stage.RouteSettings``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-routesettings
        """
        return jsii.get(self, "routeSettings")

    @route_settings.setter
    def route_settings(self, value: typing.Any):
        jsii.set(self, "routeSettings", value)

    @builtins.property
    @jsii.member(jsii_name="stageName")
    def stage_name(self) -> str:
        """``AWS::ApiGatewayV2::Stage.StageName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-stagename
        """
        return jsii.get(self, "stageName")

    @stage_name.setter
    def stage_name(self, value: str):
        jsii.set(self, "stageName", value)

    @builtins.property
    @jsii.member(jsii_name="stageVariables")
    def stage_variables(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Stage.StageVariables``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-stagevariables
        """
        return jsii.get(self, "stageVariables")

    @stage_variables.setter
    def stage_variables(self, value: typing.Any):
        jsii.set(self, "stageVariables", value)

    @builtins.property
    @jsii.member(jsii_name="accessLogSettings")
    def access_log_settings(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AccessLogSettingsProperty"]]]:
        """``AWS::ApiGatewayV2::Stage.AccessLogSettings``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-accesslogsettings
        """
        return jsii.get(self, "accessLogSettings")

    @access_log_settings.setter
    def access_log_settings(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AccessLogSettingsProperty"]]]):
        jsii.set(self, "accessLogSettings", value)

    @builtins.property
    @jsii.member(jsii_name="autoDeploy")
    def auto_deploy(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::ApiGatewayV2::Stage.AutoDeploy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-autodeploy
        """
        return jsii.get(self, "autoDeploy")

    @auto_deploy.setter
    def auto_deploy(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        jsii.set(self, "autoDeploy", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificateId")
    def client_certificate_id(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Stage.ClientCertificateId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-clientcertificateid
        """
        return jsii.get(self, "clientCertificateId")

    @client_certificate_id.setter
    def client_certificate_id(self, value: typing.Optional[str]):
        jsii.set(self, "clientCertificateId", value)

    @builtins.property
    @jsii.member(jsii_name="defaultRouteSettings")
    def default_route_settings(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RouteSettingsProperty"]]]:
        """``AWS::ApiGatewayV2::Stage.DefaultRouteSettings``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-defaultroutesettings
        """
        return jsii.get(self, "defaultRouteSettings")

    @default_route_settings.setter
    def default_route_settings(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RouteSettingsProperty"]]]):
        jsii.set(self, "defaultRouteSettings", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentId")
    def deployment_id(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Stage.DeploymentId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-deploymentid
        """
        return jsii.get(self, "deploymentId")

    @deployment_id.setter
    def deployment_id(self, value: typing.Optional[str]):
        jsii.set(self, "deploymentId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Stage.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        jsii.set(self, "description", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnStage.AccessLogSettingsProperty", jsii_struct_bases=[], name_mapping={'destination_arn': 'destinationArn', 'format': 'format'})
    class AccessLogSettingsProperty():
        def __init__(self, *, destination_arn: typing.Optional[str]=None, format: typing.Optional[str]=None):
            """
            :param destination_arn: ``CfnStage.AccessLogSettingsProperty.DestinationArn``.
            :param format: ``CfnStage.AccessLogSettingsProperty.Format``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-accesslogsettings.html
            """
            self._values = {
            }
            if destination_arn is not None: self._values["destination_arn"] = destination_arn
            if format is not None: self._values["format"] = format

        @builtins.property
        def destination_arn(self) -> typing.Optional[str]:
            """``CfnStage.AccessLogSettingsProperty.DestinationArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-accesslogsettings.html#cfn-apigatewayv2-stage-accesslogsettings-destinationarn
            """
            return self._values.get('destination_arn')

        @builtins.property
        def format(self) -> typing.Optional[str]:
            """``CfnStage.AccessLogSettingsProperty.Format``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-accesslogsettings.html#cfn-apigatewayv2-stage-accesslogsettings-format
            """
            return self._values.get('format')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'AccessLogSettingsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnStage.RouteSettingsProperty", jsii_struct_bases=[], name_mapping={'data_trace_enabled': 'dataTraceEnabled', 'detailed_metrics_enabled': 'detailedMetricsEnabled', 'logging_level': 'loggingLevel', 'throttling_burst_limit': 'throttlingBurstLimit', 'throttling_rate_limit': 'throttlingRateLimit'})
    class RouteSettingsProperty():
        def __init__(self, *, data_trace_enabled: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, detailed_metrics_enabled: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, logging_level: typing.Optional[str]=None, throttling_burst_limit: typing.Optional[jsii.Number]=None, throttling_rate_limit: typing.Optional[jsii.Number]=None):
            """
            :param data_trace_enabled: ``CfnStage.RouteSettingsProperty.DataTraceEnabled``.
            :param detailed_metrics_enabled: ``CfnStage.RouteSettingsProperty.DetailedMetricsEnabled``.
            :param logging_level: ``CfnStage.RouteSettingsProperty.LoggingLevel``.
            :param throttling_burst_limit: ``CfnStage.RouteSettingsProperty.ThrottlingBurstLimit``.
            :param throttling_rate_limit: ``CfnStage.RouteSettingsProperty.ThrottlingRateLimit``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html
            """
            self._values = {
            }
            if data_trace_enabled is not None: self._values["data_trace_enabled"] = data_trace_enabled
            if detailed_metrics_enabled is not None: self._values["detailed_metrics_enabled"] = detailed_metrics_enabled
            if logging_level is not None: self._values["logging_level"] = logging_level
            if throttling_burst_limit is not None: self._values["throttling_burst_limit"] = throttling_burst_limit
            if throttling_rate_limit is not None: self._values["throttling_rate_limit"] = throttling_rate_limit

        @builtins.property
        def data_trace_enabled(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnStage.RouteSettingsProperty.DataTraceEnabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-datatraceenabled
            """
            return self._values.get('data_trace_enabled')

        @builtins.property
        def detailed_metrics_enabled(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnStage.RouteSettingsProperty.DetailedMetricsEnabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-detailedmetricsenabled
            """
            return self._values.get('detailed_metrics_enabled')

        @builtins.property
        def logging_level(self) -> typing.Optional[str]:
            """``CfnStage.RouteSettingsProperty.LoggingLevel``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-logginglevel
            """
            return self._values.get('logging_level')

        @builtins.property
        def throttling_burst_limit(self) -> typing.Optional[jsii.Number]:
            """``CfnStage.RouteSettingsProperty.ThrottlingBurstLimit``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-throttlingburstlimit
            """
            return self._values.get('throttling_burst_limit')

        @builtins.property
        def throttling_rate_limit(self) -> typing.Optional[jsii.Number]:
            """``CfnStage.RouteSettingsProperty.ThrottlingRateLimit``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-throttlingratelimit
            """
            return self._values.get('throttling_rate_limit')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RouteSettingsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-apigatewayv2.CfnStageProps", jsii_struct_bases=[], name_mapping={'api_id': 'apiId', 'stage_name': 'stageName', 'access_log_settings': 'accessLogSettings', 'auto_deploy': 'autoDeploy', 'client_certificate_id': 'clientCertificateId', 'default_route_settings': 'defaultRouteSettings', 'deployment_id': 'deploymentId', 'description': 'description', 'route_settings': 'routeSettings', 'stage_variables': 'stageVariables', 'tags': 'tags'})
class CfnStageProps():
    def __init__(self, *, api_id: str, stage_name: str, access_log_settings: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnStage.AccessLogSettingsProperty"]]]=None, auto_deploy: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, client_certificate_id: typing.Optional[str]=None, default_route_settings: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnStage.RouteSettingsProperty"]]]=None, deployment_id: typing.Optional[str]=None, description: typing.Optional[str]=None, route_settings: typing.Any=None, stage_variables: typing.Any=None, tags: typing.Any=None):
        """Properties for defining a ``AWS::ApiGatewayV2::Stage``.

        :param api_id: ``AWS::ApiGatewayV2::Stage.ApiId``.
        :param stage_name: ``AWS::ApiGatewayV2::Stage.StageName``.
        :param access_log_settings: ``AWS::ApiGatewayV2::Stage.AccessLogSettings``.
        :param auto_deploy: ``AWS::ApiGatewayV2::Stage.AutoDeploy``.
        :param client_certificate_id: ``AWS::ApiGatewayV2::Stage.ClientCertificateId``.
        :param default_route_settings: ``AWS::ApiGatewayV2::Stage.DefaultRouteSettings``.
        :param deployment_id: ``AWS::ApiGatewayV2::Stage.DeploymentId``.
        :param description: ``AWS::ApiGatewayV2::Stage.Description``.
        :param route_settings: ``AWS::ApiGatewayV2::Stage.RouteSettings``.
        :param stage_variables: ``AWS::ApiGatewayV2::Stage.StageVariables``.
        :param tags: ``AWS::ApiGatewayV2::Stage.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html
        """
        self._values = {
            'api_id': api_id,
            'stage_name': stage_name,
        }
        if access_log_settings is not None: self._values["access_log_settings"] = access_log_settings
        if auto_deploy is not None: self._values["auto_deploy"] = auto_deploy
        if client_certificate_id is not None: self._values["client_certificate_id"] = client_certificate_id
        if default_route_settings is not None: self._values["default_route_settings"] = default_route_settings
        if deployment_id is not None: self._values["deployment_id"] = deployment_id
        if description is not None: self._values["description"] = description
        if route_settings is not None: self._values["route_settings"] = route_settings
        if stage_variables is not None: self._values["stage_variables"] = stage_variables
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def api_id(self) -> str:
        """``AWS::ApiGatewayV2::Stage.ApiId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-apiid
        """
        return self._values.get('api_id')

    @builtins.property
    def stage_name(self) -> str:
        """``AWS::ApiGatewayV2::Stage.StageName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-stagename
        """
        return self._values.get('stage_name')

    @builtins.property
    def access_log_settings(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnStage.AccessLogSettingsProperty"]]]:
        """``AWS::ApiGatewayV2::Stage.AccessLogSettings``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-accesslogsettings
        """
        return self._values.get('access_log_settings')

    @builtins.property
    def auto_deploy(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::ApiGatewayV2::Stage.AutoDeploy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-autodeploy
        """
        return self._values.get('auto_deploy')

    @builtins.property
    def client_certificate_id(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Stage.ClientCertificateId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-clientcertificateid
        """
        return self._values.get('client_certificate_id')

    @builtins.property
    def default_route_settings(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnStage.RouteSettingsProperty"]]]:
        """``AWS::ApiGatewayV2::Stage.DefaultRouteSettings``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-defaultroutesettings
        """
        return self._values.get('default_route_settings')

    @builtins.property
    def deployment_id(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Stage.DeploymentId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-deploymentid
        """
        return self._values.get('deployment_id')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::ApiGatewayV2::Stage.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-description
        """
        return self._values.get('description')

    @builtins.property
    def route_settings(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Stage.RouteSettings``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-routesettings
        """
        return self._values.get('route_settings')

    @builtins.property
    def stage_variables(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Stage.StageVariables``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-stagevariables
        """
        return self._values.get('stage_variables')

    @builtins.property
    def tags(self) -> typing.Any:
        """``AWS::ApiGatewayV2::Stage.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnStageProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["CfnApi", "CfnApiMapping", "CfnApiMappingProps", "CfnApiProps", "CfnAuthorizer", "CfnAuthorizerProps", "CfnDeployment", "CfnDeploymentProps", "CfnDomainName", "CfnDomainNameProps", "CfnIntegration", "CfnIntegrationProps", "CfnIntegrationResponse", "CfnIntegrationResponseProps", "CfnModel", "CfnModelProps", "CfnRoute", "CfnRouteProps", "CfnRouteResponse", "CfnRouteResponseProps", "CfnStage", "CfnStageProps", "__jsii_assembly__"]

publication.publish()
