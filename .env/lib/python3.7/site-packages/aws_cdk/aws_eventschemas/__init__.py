"""
## AWS::EventSchemas Construct Library

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
import aws_cdk.aws_eventschemas as eventschemas
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

__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-eventschemas", "1.22.0", __name__, "aws-eventschemas@1.22.0.jsii.tgz")


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDiscoverer(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-eventschemas.CfnDiscoverer"):
    """A CloudFormation ``AWS::EventSchemas::Discoverer``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html
    cloudformationResource:
    :cloudformationResource:: AWS::EventSchemas::Discoverer
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, source_arn: str, description: typing.Optional[str]=None, tags: typing.Optional[typing.List["TagsEntryProperty"]]=None) -> None:
        """Create a new ``AWS::EventSchemas::Discoverer``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param source_arn: ``AWS::EventSchemas::Discoverer.SourceArn``.
        :param description: ``AWS::EventSchemas::Discoverer.Description``.
        :param tags: ``AWS::EventSchemas::Discoverer.Tags``.
        """
        props = CfnDiscovererProps(source_arn=source_arn, description=description, tags=tags)

        jsii.create(CfnDiscoverer, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrDiscovererArn")
    def attr_discoverer_arn(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: DiscovererArn
        """
        return jsii.get(self, "attrDiscovererArn")

    @builtins.property
    @jsii.member(jsii_name="attrDiscovererId")
    def attr_discoverer_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: DiscovererId
        """
        return jsii.get(self, "attrDiscovererId")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EventSchemas::Discoverer.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="sourceArn")
    def source_arn(self) -> str:
        """``AWS::EventSchemas::Discoverer.SourceArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-sourcearn
        """
        return jsii.get(self, "sourceArn")

    @source_arn.setter
    def source_arn(self, value: str):
        jsii.set(self, "sourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::EventSchemas::Discoverer.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        jsii.set(self, "description", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-eventschemas.CfnDiscoverer.TagsEntryProperty", jsii_struct_bases=[], name_mapping={'key': 'key', 'value': 'value'})
    class TagsEntryProperty():
        def __init__(self, *, key: str, value: str):
            """
            :param key: ``CfnDiscoverer.TagsEntryProperty.Key``.
            :param value: ``CfnDiscoverer.TagsEntryProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html
            """
            self._values = {
                'key': key,
                'value': value,
            }

        @builtins.property
        def key(self) -> str:
            """``CfnDiscoverer.TagsEntryProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html#cfn-eventschemas-discoverer-tagsentry-key
            """
            return self._values.get('key')

        @builtins.property
        def value(self) -> str:
            """``CfnDiscoverer.TagsEntryProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html#cfn-eventschemas-discoverer-tagsentry-value
            """
            return self._values.get('value')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TagsEntryProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-eventschemas.CfnDiscovererProps", jsii_struct_bases=[], name_mapping={'source_arn': 'sourceArn', 'description': 'description', 'tags': 'tags'})
class CfnDiscovererProps():
    def __init__(self, *, source_arn: str, description: typing.Optional[str]=None, tags: typing.Optional[typing.List["CfnDiscoverer.TagsEntryProperty"]]=None):
        """Properties for defining a ``AWS::EventSchemas::Discoverer``.

        :param source_arn: ``AWS::EventSchemas::Discoverer.SourceArn``.
        :param description: ``AWS::EventSchemas::Discoverer.Description``.
        :param tags: ``AWS::EventSchemas::Discoverer.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html
        """
        self._values = {
            'source_arn': source_arn,
        }
        if description is not None: self._values["description"] = description
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def source_arn(self) -> str:
        """``AWS::EventSchemas::Discoverer.SourceArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-sourcearn
        """
        return self._values.get('source_arn')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::EventSchemas::Discoverer.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-description
        """
        return self._values.get('description')

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["CfnDiscoverer.TagsEntryProperty"]]:
        """``AWS::EventSchemas::Discoverer.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnDiscovererProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnRegistry(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-eventschemas.CfnRegistry"):
    """A CloudFormation ``AWS::EventSchemas::Registry``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html
    cloudformationResource:
    :cloudformationResource:: AWS::EventSchemas::Registry
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, description: typing.Optional[str]=None, registry_name: typing.Optional[str]=None, tags: typing.Optional[typing.List["TagsEntryProperty"]]=None) -> None:
        """Create a new ``AWS::EventSchemas::Registry``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::EventSchemas::Registry.Description``.
        :param registry_name: ``AWS::EventSchemas::Registry.RegistryName``.
        :param tags: ``AWS::EventSchemas::Registry.Tags``.
        """
        props = CfnRegistryProps(description=description, registry_name=registry_name, tags=tags)

        jsii.create(CfnRegistry, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrRegistryArn")
    def attr_registry_arn(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: RegistryArn
        """
        return jsii.get(self, "attrRegistryArn")

    @builtins.property
    @jsii.member(jsii_name="attrRegistryName")
    def attr_registry_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: RegistryName
        """
        return jsii.get(self, "attrRegistryName")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EventSchemas::Registry.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::EventSchemas::Registry.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="registryName")
    def registry_name(self) -> typing.Optional[str]:
        """``AWS::EventSchemas::Registry.RegistryName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-registryname
        """
        return jsii.get(self, "registryName")

    @registry_name.setter
    def registry_name(self, value: typing.Optional[str]):
        jsii.set(self, "registryName", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-eventschemas.CfnRegistry.TagsEntryProperty", jsii_struct_bases=[], name_mapping={'key': 'key', 'value': 'value'})
    class TagsEntryProperty():
        def __init__(self, *, key: str, value: str):
            """
            :param key: ``CfnRegistry.TagsEntryProperty.Key``.
            :param value: ``CfnRegistry.TagsEntryProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html
            """
            self._values = {
                'key': key,
                'value': value,
            }

        @builtins.property
        def key(self) -> str:
            """``CfnRegistry.TagsEntryProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html#cfn-eventschemas-registry-tagsentry-key
            """
            return self._values.get('key')

        @builtins.property
        def value(self) -> str:
            """``CfnRegistry.TagsEntryProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html#cfn-eventschemas-registry-tagsentry-value
            """
            return self._values.get('value')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TagsEntryProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-eventschemas.CfnRegistryProps", jsii_struct_bases=[], name_mapping={'description': 'description', 'registry_name': 'registryName', 'tags': 'tags'})
class CfnRegistryProps():
    def __init__(self, *, description: typing.Optional[str]=None, registry_name: typing.Optional[str]=None, tags: typing.Optional[typing.List["CfnRegistry.TagsEntryProperty"]]=None):
        """Properties for defining a ``AWS::EventSchemas::Registry``.

        :param description: ``AWS::EventSchemas::Registry.Description``.
        :param registry_name: ``AWS::EventSchemas::Registry.RegistryName``.
        :param tags: ``AWS::EventSchemas::Registry.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html
        """
        self._values = {
        }
        if description is not None: self._values["description"] = description
        if registry_name is not None: self._values["registry_name"] = registry_name
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::EventSchemas::Registry.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-description
        """
        return self._values.get('description')

    @builtins.property
    def registry_name(self) -> typing.Optional[str]:
        """``AWS::EventSchemas::Registry.RegistryName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-registryname
        """
        return self._values.get('registry_name')

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["CfnRegistry.TagsEntryProperty"]]:
        """``AWS::EventSchemas::Registry.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnRegistryProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSchema(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-eventschemas.CfnSchema"):
    """A CloudFormation ``AWS::EventSchemas::Schema``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html
    cloudformationResource:
    :cloudformationResource:: AWS::EventSchemas::Schema
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, content: str, registry_name: str, type: str, description: typing.Optional[str]=None, schema_name: typing.Optional[str]=None, tags: typing.Optional[typing.List["TagsEntryProperty"]]=None) -> None:
        """Create a new ``AWS::EventSchemas::Schema``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param content: ``AWS::EventSchemas::Schema.Content``.
        :param registry_name: ``AWS::EventSchemas::Schema.RegistryName``.
        :param type: ``AWS::EventSchemas::Schema.Type``.
        :param description: ``AWS::EventSchemas::Schema.Description``.
        :param schema_name: ``AWS::EventSchemas::Schema.SchemaName``.
        :param tags: ``AWS::EventSchemas::Schema.Tags``.
        """
        props = CfnSchemaProps(content=content, registry_name=registry_name, type=type, description=description, schema_name=schema_name, tags=tags)

        jsii.create(CfnSchema, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrSchemaArn")
    def attr_schema_arn(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: SchemaArn
        """
        return jsii.get(self, "attrSchemaArn")

    @builtins.property
    @jsii.member(jsii_name="attrSchemaName")
    def attr_schema_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: SchemaName
        """
        return jsii.get(self, "attrSchemaName")

    @builtins.property
    @jsii.member(jsii_name="attrSchemaVersion")
    def attr_schema_version(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: SchemaVersion
        """
        return jsii.get(self, "attrSchemaVersion")

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EventSchemas::Schema.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-tags
        """
        return jsii.get(self, "tags")

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> str:
        """``AWS::EventSchemas::Schema.Content``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-content
        """
        return jsii.get(self, "content")

    @content.setter
    def content(self, value: str):
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="registryName")
    def registry_name(self) -> str:
        """``AWS::EventSchemas::Schema.RegistryName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-registryname
        """
        return jsii.get(self, "registryName")

    @registry_name.setter
    def registry_name(self, value: str):
        jsii.set(self, "registryName", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> str:
        """``AWS::EventSchemas::Schema.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-type
        """
        return jsii.get(self, "type")

    @type.setter
    def type(self, value: str):
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::EventSchemas::Schema.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="schemaName")
    def schema_name(self) -> typing.Optional[str]:
        """``AWS::EventSchemas::Schema.SchemaName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-schemaname
        """
        return jsii.get(self, "schemaName")

    @schema_name.setter
    def schema_name(self, value: typing.Optional[str]):
        jsii.set(self, "schemaName", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-eventschemas.CfnSchema.TagsEntryProperty", jsii_struct_bases=[], name_mapping={'key': 'key', 'value': 'value'})
    class TagsEntryProperty():
        def __init__(self, *, key: str, value: str):
            """
            :param key: ``CfnSchema.TagsEntryProperty.Key``.
            :param value: ``CfnSchema.TagsEntryProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html
            """
            self._values = {
                'key': key,
                'value': value,
            }

        @builtins.property
        def key(self) -> str:
            """``CfnSchema.TagsEntryProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html#cfn-eventschemas-schema-tagsentry-key
            """
            return self._values.get('key')

        @builtins.property
        def value(self) -> str:
            """``CfnSchema.TagsEntryProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html#cfn-eventschemas-schema-tagsentry-value
            """
            return self._values.get('value')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TagsEntryProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-eventschemas.CfnSchemaProps", jsii_struct_bases=[], name_mapping={'content': 'content', 'registry_name': 'registryName', 'type': 'type', 'description': 'description', 'schema_name': 'schemaName', 'tags': 'tags'})
class CfnSchemaProps():
    def __init__(self, *, content: str, registry_name: str, type: str, description: typing.Optional[str]=None, schema_name: typing.Optional[str]=None, tags: typing.Optional[typing.List["CfnSchema.TagsEntryProperty"]]=None):
        """Properties for defining a ``AWS::EventSchemas::Schema``.

        :param content: ``AWS::EventSchemas::Schema.Content``.
        :param registry_name: ``AWS::EventSchemas::Schema.RegistryName``.
        :param type: ``AWS::EventSchemas::Schema.Type``.
        :param description: ``AWS::EventSchemas::Schema.Description``.
        :param schema_name: ``AWS::EventSchemas::Schema.SchemaName``.
        :param tags: ``AWS::EventSchemas::Schema.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html
        """
        self._values = {
            'content': content,
            'registry_name': registry_name,
            'type': type,
        }
        if description is not None: self._values["description"] = description
        if schema_name is not None: self._values["schema_name"] = schema_name
        if tags is not None: self._values["tags"] = tags

    @builtins.property
    def content(self) -> str:
        """``AWS::EventSchemas::Schema.Content``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-content
        """
        return self._values.get('content')

    @builtins.property
    def registry_name(self) -> str:
        """``AWS::EventSchemas::Schema.RegistryName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-registryname
        """
        return self._values.get('registry_name')

    @builtins.property
    def type(self) -> str:
        """``AWS::EventSchemas::Schema.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-type
        """
        return self._values.get('type')

    @builtins.property
    def description(self) -> typing.Optional[str]:
        """``AWS::EventSchemas::Schema.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-description
        """
        return self._values.get('description')

    @builtins.property
    def schema_name(self) -> typing.Optional[str]:
        """``AWS::EventSchemas::Schema.SchemaName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-schemaname
        """
        return self._values.get('schema_name')

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["CfnSchema.TagsEntryProperty"]]:
        """``AWS::EventSchemas::Schema.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnSchemaProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["CfnDiscoverer", "CfnDiscovererProps", "CfnRegistry", "CfnRegistryProps", "CfnSchema", "CfnSchemaProps", "__jsii_assembly__"]

publication.publish()
