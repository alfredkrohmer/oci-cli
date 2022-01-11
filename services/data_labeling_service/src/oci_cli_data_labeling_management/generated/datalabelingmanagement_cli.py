# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('data_labeling_service.data_labeling_service_root_group.command_name', 'data-labeling-service'), cls=CommandGroupWithAlias, help=cli_util.override('data_labeling_service.data_labeling_service_root_group.help', """A description of the DataLabelingService API"""), short_help=cli_util.override('data_labeling_service.data_labeling_service_root_group.short_help', """DataLabelingService API"""))
@cli_util.help_option_group
def data_labeling_service_root_group():
    pass


@click.command(cli_util.override('data_labeling_service.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workrequest status""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('data_labeling_service.dataset_group.command_name', 'dataset'), cls=CommandGroupWithAlias, help="""A dataset is a logical collection of records. The dataset contains all the information necessary to describe a record's source, format, type of annotations allowed on these records, and labels allowed on annotations.""")
@cli_util.help_option_group
def dataset_group():
    pass


@click.command(cli_util.override('data_labeling_service.dataset_collection_group.command_name', 'dataset-collection'), cls=CommandGroupWithAlias, help="""Results of a dataset list operation. Contains DatasetSummary items.""")
@cli_util.help_option_group
def dataset_collection_group():
    pass


@click.command(cli_util.override('data_labeling_service.annotation_format_group.command_name', 'annotation-format'), cls=CommandGroupWithAlias, help="""annotation format""")
@cli_util.help_option_group
def annotation_format_group():
    pass


data_labeling_service_root_group.add_command(work_request_group)
data_labeling_service_root_group.add_command(dataset_group)
data_labeling_service_root_group.add_command(dataset_collection_group)
data_labeling_service_root_group.add_command(annotation_format_group)


@dataset_group.command(name=cli_util.override('data_labeling_service.add_dataset_labels.command_name', 'add'), help=u"""Add Labels to the Dataset LabelSet until the maximum number of Labels has been reached. \n[Command Reference](addDatasetLabels)""")
@cli_util.option('--dataset-id', required=True, help=u"""Unique Dataset OCID""")
@cli_util.option('--label-set', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "FAILED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}})
@cli_util.wrap_exceptions
def add_dataset_labels(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dataset_id, label_set, if_match):

    if isinstance(dataset_id, six.string_types) and len(dataset_id.strip()) == 0:
        raise click.UsageError('Parameter --dataset-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if label_set is not None:
        _details['labelSet'] = cli_util.parse_json_parameter("label_set", label_set)

    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    result = client.add_dataset_labels(
        dataset_id=dataset_id,
        add_dataset_labels_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@dataset_group.command(name=cli_util.override('data_labeling_service.change_dataset_compartment.command_name', 'change-compartment'), help=u"""Moves a Dataset resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeDatasetCompartment)""")
@cli_util.option('--dataset-id', required=True, help=u"""Unique Dataset OCID""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "FAILED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_dataset_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dataset_id, compartment_id, if_match):

    if isinstance(dataset_id, six.string_types) and len(dataset_id.strip()) == 0:
        raise click.UsageError('Parameter --dataset-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    result = client.change_dataset_compartment(
        dataset_id=dataset_id,
        change_dataset_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@dataset_group.command(name=cli_util.override('data_labeling_service.create_dataset.command_name', 'create'), help=u"""Creates a new Dataset. \n[Command Reference](createDataset)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment of the resource.""")
@cli_util.option('--annotation-format', required=True, help=u"""The annotation format name required for labeling records.""")
@cli_util.option('--dataset-source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dataset-format-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--label-set', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource.""")
@cli_util.option('--description', help=u"""A user provided description of the dataset""")
@cli_util.option('--initial-record-generation-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "FAILED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'dataset-source-details': {'module': 'data_labeling_service', 'class': 'DatasetSourceDetails'}, 'dataset-format-details': {'module': 'data_labeling_service', 'class': 'DatasetFormatDetails'}, 'initial-record-generation-configuration': {'module': 'data_labeling_service', 'class': 'InitialRecordGenerationConfiguration'}, 'label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}, 'freeform-tags': {'module': 'data_labeling_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dataset-source-details': {'module': 'data_labeling_service', 'class': 'DatasetSourceDetails'}, 'dataset-format-details': {'module': 'data_labeling_service', 'class': 'DatasetFormatDetails'}, 'initial-record-generation-configuration': {'module': 'data_labeling_service', 'class': 'InitialRecordGenerationConfiguration'}, 'label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}, 'freeform-tags': {'module': 'data_labeling_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_labeling_service', 'class': 'Dataset'})
@cli_util.wrap_exceptions
def create_dataset(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, annotation_format, dataset_source_details, dataset_format_details, label_set, display_name, description, initial_record_generation_configuration, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['annotationFormat'] = annotation_format
    _details['datasetSourceDetails'] = cli_util.parse_json_parameter("dataset_source_details", dataset_source_details)
    _details['datasetFormatDetails'] = cli_util.parse_json_parameter("dataset_format_details", dataset_format_details)
    _details['labelSet'] = cli_util.parse_json_parameter("label_set", label_set)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if initial_record_generation_configuration is not None:
        _details['initialRecordGenerationConfiguration'] = cli_util.parse_json_parameter("initial_record_generation_configuration", initial_record_generation_configuration)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    result = client.create_dataset(
        create_dataset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@dataset_group.command(name=cli_util.override('data_labeling_service.create_dataset_object_storage_source_details.command_name', 'create-dataset-object-storage-source-details'), help=u"""Creates a new Dataset. \n[Command Reference](createDataset)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment of the resource.""")
@cli_util.option('--annotation-format', required=True, help=u"""The annotation format name required for labeling records.""")
@cli_util.option('--dataset-format-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--label-set', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dataset-source-details-namespace', required=True, help=u"""Namespace of the bucket that contains the dataset data source""")
@cli_util.option('--dataset-source-details-bucket', required=True, help=u"""The object storage bucket that contains the dataset data source""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource.""")
@cli_util.option('--description', help=u"""A user provided description of the dataset""")
@cli_util.option('--initial-record-generation-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dataset-source-details-prefix', help=u"""A common path prefix shared by the objects that make up the dataset.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "FAILED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'dataset-format-details': {'module': 'data_labeling_service', 'class': 'DatasetFormatDetails'}, 'initial-record-generation-configuration': {'module': 'data_labeling_service', 'class': 'InitialRecordGenerationConfiguration'}, 'label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}, 'freeform-tags': {'module': 'data_labeling_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dataset-format-details': {'module': 'data_labeling_service', 'class': 'DatasetFormatDetails'}, 'initial-record-generation-configuration': {'module': 'data_labeling_service', 'class': 'InitialRecordGenerationConfiguration'}, 'label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}, 'freeform-tags': {'module': 'data_labeling_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_labeling_service', 'class': 'Dataset'})
@cli_util.wrap_exceptions
def create_dataset_object_storage_source_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, annotation_format, dataset_format_details, label_set, dataset_source_details_namespace, dataset_source_details_bucket, display_name, description, initial_record_generation_configuration, freeform_tags, defined_tags, dataset_source_details_prefix):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['datasetSourceDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['annotationFormat'] = annotation_format
    _details['datasetFormatDetails'] = cli_util.parse_json_parameter("dataset_format_details", dataset_format_details)
    _details['labelSet'] = cli_util.parse_json_parameter("label_set", label_set)
    _details['datasetSourceDetails']['namespace'] = dataset_source_details_namespace
    _details['datasetSourceDetails']['bucket'] = dataset_source_details_bucket

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if initial_record_generation_configuration is not None:
        _details['initialRecordGenerationConfiguration'] = cli_util.parse_json_parameter("initial_record_generation_configuration", initial_record_generation_configuration)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if dataset_source_details_prefix is not None:
        _details['datasetSourceDetails']['prefix'] = dataset_source_details_prefix

    _details['datasetSourceDetails']['sourceType'] = 'OBJECT_STORAGE'

    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    result = client.create_dataset(
        create_dataset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@dataset_group.command(name=cli_util.override('data_labeling_service.create_dataset_image_dataset_format_details.command_name', 'create-dataset-image-dataset-format-details'), help=u"""Creates a new Dataset. \n[Command Reference](createDataset)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment of the resource.""")
@cli_util.option('--annotation-format', required=True, help=u"""The annotation format name required for labeling records.""")
@cli_util.option('--dataset-source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--label-set', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource.""")
@cli_util.option('--description', help=u"""A user provided description of the dataset""")
@cli_util.option('--initial-record-generation-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "FAILED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'dataset-source-details': {'module': 'data_labeling_service', 'class': 'DatasetSourceDetails'}, 'initial-record-generation-configuration': {'module': 'data_labeling_service', 'class': 'InitialRecordGenerationConfiguration'}, 'label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}, 'freeform-tags': {'module': 'data_labeling_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dataset-source-details': {'module': 'data_labeling_service', 'class': 'DatasetSourceDetails'}, 'initial-record-generation-configuration': {'module': 'data_labeling_service', 'class': 'InitialRecordGenerationConfiguration'}, 'label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}, 'freeform-tags': {'module': 'data_labeling_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_labeling_service', 'class': 'Dataset'})
@cli_util.wrap_exceptions
def create_dataset_image_dataset_format_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, annotation_format, dataset_source_details, label_set, display_name, description, initial_record_generation_configuration, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['datasetFormatDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['annotationFormat'] = annotation_format
    _details['datasetSourceDetails'] = cli_util.parse_json_parameter("dataset_source_details", dataset_source_details)
    _details['labelSet'] = cli_util.parse_json_parameter("label_set", label_set)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if initial_record_generation_configuration is not None:
        _details['initialRecordGenerationConfiguration'] = cli_util.parse_json_parameter("initial_record_generation_configuration", initial_record_generation_configuration)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['datasetFormatDetails']['formatType'] = 'IMAGE'

    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    result = client.create_dataset(
        create_dataset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@dataset_group.command(name=cli_util.override('data_labeling_service.create_dataset_document_dataset_format_details.command_name', 'create-dataset-document-dataset-format-details'), help=u"""Creates a new Dataset. \n[Command Reference](createDataset)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment of the resource.""")
@cli_util.option('--annotation-format', required=True, help=u"""The annotation format name required for labeling records.""")
@cli_util.option('--dataset-source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--label-set', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource.""")
@cli_util.option('--description', help=u"""A user provided description of the dataset""")
@cli_util.option('--initial-record-generation-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "FAILED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'dataset-source-details': {'module': 'data_labeling_service', 'class': 'DatasetSourceDetails'}, 'initial-record-generation-configuration': {'module': 'data_labeling_service', 'class': 'InitialRecordGenerationConfiguration'}, 'label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}, 'freeform-tags': {'module': 'data_labeling_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dataset-source-details': {'module': 'data_labeling_service', 'class': 'DatasetSourceDetails'}, 'initial-record-generation-configuration': {'module': 'data_labeling_service', 'class': 'InitialRecordGenerationConfiguration'}, 'label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}, 'freeform-tags': {'module': 'data_labeling_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_labeling_service', 'class': 'Dataset'})
@cli_util.wrap_exceptions
def create_dataset_document_dataset_format_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, annotation_format, dataset_source_details, label_set, display_name, description, initial_record_generation_configuration, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['datasetFormatDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['annotationFormat'] = annotation_format
    _details['datasetSourceDetails'] = cli_util.parse_json_parameter("dataset_source_details", dataset_source_details)
    _details['labelSet'] = cli_util.parse_json_parameter("label_set", label_set)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if initial_record_generation_configuration is not None:
        _details['initialRecordGenerationConfiguration'] = cli_util.parse_json_parameter("initial_record_generation_configuration", initial_record_generation_configuration)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['datasetFormatDetails']['formatType'] = 'DOCUMENT'

    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    result = client.create_dataset(
        create_dataset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@dataset_group.command(name=cli_util.override('data_labeling_service.create_dataset_text_dataset_format_details.command_name', 'create-dataset-text-dataset-format-details'), help=u"""Creates a new Dataset. \n[Command Reference](createDataset)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment of the resource.""")
@cli_util.option('--annotation-format', required=True, help=u"""The annotation format name required for labeling records.""")
@cli_util.option('--dataset-source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--label-set', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource.""")
@cli_util.option('--description', help=u"""A user provided description of the dataset""")
@cli_util.option('--initial-record-generation-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "FAILED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'dataset-source-details': {'module': 'data_labeling_service', 'class': 'DatasetSourceDetails'}, 'initial-record-generation-configuration': {'module': 'data_labeling_service', 'class': 'InitialRecordGenerationConfiguration'}, 'label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}, 'freeform-tags': {'module': 'data_labeling_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dataset-source-details': {'module': 'data_labeling_service', 'class': 'DatasetSourceDetails'}, 'initial-record-generation-configuration': {'module': 'data_labeling_service', 'class': 'InitialRecordGenerationConfiguration'}, 'label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}, 'freeform-tags': {'module': 'data_labeling_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_labeling_service', 'class': 'Dataset'})
@cli_util.wrap_exceptions
def create_dataset_text_dataset_format_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, annotation_format, dataset_source_details, label_set, display_name, description, initial_record_generation_configuration, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['datasetFormatDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['annotationFormat'] = annotation_format
    _details['datasetSourceDetails'] = cli_util.parse_json_parameter("dataset_source_details", dataset_source_details)
    _details['labelSet'] = cli_util.parse_json_parameter("label_set", label_set)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if initial_record_generation_configuration is not None:
        _details['initialRecordGenerationConfiguration'] = cli_util.parse_json_parameter("initial_record_generation_configuration", initial_record_generation_configuration)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['datasetFormatDetails']['formatType'] = 'TEXT'

    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    result = client.create_dataset(
        create_dataset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@dataset_group.command(name=cli_util.override('data_labeling_service.delete_dataset.command_name', 'delete'), help=u"""Deletes a Dataset resource by identifier \n[Command Reference](deleteDataset)""")
@cli_util.option('--dataset-id', required=True, help=u"""Unique Dataset OCID""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "FAILED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_dataset(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dataset_id, if_match):

    if isinstance(dataset_id, six.string_types) and len(dataset_id.strip()) == 0:
        raise click.UsageError('Parameter --dataset-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    result = client.delete_dataset(
        dataset_id=dataset_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@dataset_group.command(name=cli_util.override('data_labeling_service.generate_dataset_records.command_name', 'generate-dataset-records'), help=u"""Generates Record resources from the Dataset's data source \n[Command Reference](generateDatasetRecords)""")
@cli_util.option('--dataset-id', required=True, help=u"""Unique Dataset OCID""")
@cli_util.option('--limit', type=click.FLOAT, help=u"""the maximum number of records to generate.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "FAILED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def generate_dataset_records(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dataset_id, limit, if_match):

    if isinstance(dataset_id, six.string_types) and len(dataset_id.strip()) == 0:
        raise click.UsageError('Parameter --dataset-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if limit is not None:
        _details['limit'] = limit

    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    result = client.generate_dataset_records(
        dataset_id=dataset_id,
        generate_dataset_records_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@dataset_group.command(name=cli_util.override('data_labeling_service.get_dataset.command_name', 'get'), help=u"""Gets a Dataset by identifier \n[Command Reference](getDataset)""")
@cli_util.option('--dataset-id', required=True, help=u"""Unique Dataset OCID""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_labeling_service', 'class': 'Dataset'})
@cli_util.wrap_exceptions
def get_dataset(ctx, from_json, dataset_id):

    if isinstance(dataset_id, six.string_types) and len(dataset_id.strip()) == 0:
        raise click.UsageError('Parameter --dataset-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    result = client.get_dataset(
        dataset_id=dataset_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('data_labeling_service.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_labeling_service', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@annotation_format_group.command(name=cli_util.override('data_labeling_service.list_annotation_formats.command_name', 'list'), help=u"""These are a static list in a given region. \n[Command Reference](listAnnotationFormats)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_labeling_service', 'class': 'AnnotationFormatCollection'})
@cli_util.wrap_exceptions
def list_annotation_formats(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_annotation_formats,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_annotation_formats,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_annotation_formats(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@dataset_collection_group.command(name=cli_util.override('data_labeling_service.list_datasets.command_name', 'list-datasets'), help=u"""Returns a list of Datasets. \n[Command Reference](listDatasets)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--id', help=u"""Unique Dataset OCID""")
@cli_util.option('--annotation-format', help=u"""A filter to return only resources that match the entire annotation format given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "NEEDS_ATTENTION", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources whose lifecycleState matches this query param.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_labeling_service', 'class': 'DatasetCollection'})
@cli_util.wrap_exceptions
def list_datasets(ctx, from_json, all_pages, page_size, compartment_id, id, annotation_format, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if annotation_format is not None:
        kwargs['annotation_format'] = annotation_format
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_datasets,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_datasets,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_datasets(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('data_labeling_service.list_work_request_errors.command_name', 'list-work-request-errors'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_labeling_service', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('data_labeling_service.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_labeling_service', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('data_labeling_service.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--work-request-id', help=u"""The ID of the asynchronous work request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_labeling_service', 'class': 'WorkRequestSummaryCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if work_request_id is not None:
        kwargs['work_request_id'] = work_request_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@dataset_group.command(name=cli_util.override('data_labeling_service.remove_dataset_labels.command_name', 'remove'), help=u"""Removes the labels from the Dataset Labelset.  Labels can only be removed if there are no Annotations associated with the Dataset that reference the Label names. \n[Command Reference](removeDatasetLabels)""")
@cli_util.option('--dataset-id', required=True, help=u"""Unique Dataset OCID""")
@cli_util.option('--label-set', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "FAILED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}})
@cli_util.wrap_exceptions
def remove_dataset_labels(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dataset_id, label_set, if_match):

    if isinstance(dataset_id, six.string_types) and len(dataset_id.strip()) == 0:
        raise click.UsageError('Parameter --dataset-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if label_set is not None:
        _details['labelSet'] = cli_util.parse_json_parameter("label_set", label_set)

    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    result = client.remove_dataset_labels(
        dataset_id=dataset_id,
        remove_dataset_labels_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@dataset_group.command(name=cli_util.override('data_labeling_service.rename_dataset_labels.command_name', 'rename-dataset-labels'), help=u"""Renames the labels from the Dataset Labelset.  Labels that are renamed will be reflected in Annotations associated with the Dataset that reference the Label names. \n[Command Reference](renameDatasetLabels)""")
@cli_util.option('--dataset-id', required=True, help=u"""Unique Dataset OCID""")
@cli_util.option('--source-label-set', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target-label-set', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "FAILED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'source-label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}, 'target-label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}, 'target-label-set': {'module': 'data_labeling_service', 'class': 'LabelSet'}})
@cli_util.wrap_exceptions
def rename_dataset_labels(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dataset_id, source_label_set, target_label_set, if_match):

    if isinstance(dataset_id, six.string_types) and len(dataset_id.strip()) == 0:
        raise click.UsageError('Parameter --dataset-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if source_label_set is not None:
        _details['sourceLabelSet'] = cli_util.parse_json_parameter("source_label_set", source_label_set)

    if target_label_set is not None:
        _details['targetLabelSet'] = cli_util.parse_json_parameter("target_label_set", target_label_set)

    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    result = client.rename_dataset_labels(
        dataset_id=dataset_id,
        rename_dataset_labels_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@dataset_group.command(name=cli_util.override('data_labeling_service.snapshot_dataset.command_name', 'snapshot'), help=u"""Writes the dataset records and annotations in a consolidated format out to an object storage reference for consumption. While the snapshot takes place, there may be a time while records and annotations cannot be created to ensure the snapshot is a point in time. \n[Command Reference](snapshotDataset)""")
@cli_util.option('--dataset-id', required=True, help=u"""Unique Dataset OCID""")
@cli_util.option('--are-annotations-included', required=True, type=click.BOOL, help=u"""Whether annotations are to be included in the export dataset digest.""")
@cli_util.option('--are-unannotated-records-included', required=True, type=click.BOOL, help=u"""Whether to include records that have yet to be annotated in the export dataset digest.""")
@cli_util.option('--export-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "SUCCEEDED", "CANCELING", "CANCELED", "FAILED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'export-details': {'module': 'data_labeling_service', 'class': 'ObjectStorageSnapshotExportDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'export-details': {'module': 'data_labeling_service', 'class': 'ObjectStorageSnapshotExportDetails'}})
@cli_util.wrap_exceptions
def snapshot_dataset(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dataset_id, are_annotations_included, are_unannotated_records_included, export_details, if_match):

    if isinstance(dataset_id, six.string_types) and len(dataset_id.strip()) == 0:
        raise click.UsageError('Parameter --dataset-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['areAnnotationsIncluded'] = are_annotations_included
    _details['areUnannotatedRecordsIncluded'] = are_unannotated_records_included
    _details['exportDetails'] = cli_util.parse_json_parameter("export_details", export_details)

    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    result = client.snapshot_dataset(
        dataset_id=dataset_id,
        snapshot_dataset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@dataset_group.command(name=cli_util.override('data_labeling_service.update_dataset.command_name', 'update'), help=u"""Updates the Dataset \n[Command Reference](updateDataset)""")
@cli_util.option('--dataset-id', required=True, help=u"""Unique Dataset OCID""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the resource.""")
@cli_util.option('--description', help=u"""A user provided description of the dataset""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "NEEDS_ATTENTION", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_labeling_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_labeling_service', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_labeling_service', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_labeling_service', 'class': 'Dataset'})
@cli_util.wrap_exceptions
def update_dataset(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, dataset_id, display_name, description, freeform_tags, defined_tags, if_match):

    if isinstance(dataset_id, six.string_types) and len(dataset_id.strip()) == 0:
        raise click.UsageError('Parameter --dataset-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_labeling_service', 'data_labeling_management', ctx)
    result = client.update_dataset(
        dataset_id=dataset_id,
        update_dataset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_dataset') and callable(getattr(client, 'get_dataset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_dataset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
