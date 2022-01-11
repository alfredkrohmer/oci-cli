# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.operator_access_control.src.oci_cli_operator_access_control.generated import opctl_service_cli


@click.command(cli_util.override('access_requests.access_requests_root_group.command_name', 'access-requests'), cls=CommandGroupWithAlias, help=cli_util.override('access_requests.access_requests_root_group.help', """Operator Access Control enables you to control the time duration and the actions an Oracle operator can perform on your Exadata Cloud@Customer infrastructure.
Using logging service, you can view a near real-time audit report of all actions performed by an Oracle operator.

Use the table of contents and search tool to explore the OperatorAccessControl API."""), short_help=cli_util.override('access_requests.access_requests_root_group.short_help', """OperatorAccessControl API"""))
@cli_util.help_option_group
def access_requests_root_group():
    pass


@click.command(cli_util.override('access_requests.access_request_group.command_name', 'access-request'), cls=CommandGroupWithAlias, help="""An Oracle operator raises access request when they need access to any infrastructure resource governed by Operator Access Control. The access request identifies the target resource and the set of operator actions. Access request handling depends upon the Operator Control that governs the target resource, and the set of operator actions listed for approval in the access request. If all of the operator actions listed in the access request are in the pre-approved list in the Operator Control that governs the target resource, then the access request is automatically approved. If not, then the access request requires explicit approval from the approver group specified by the Operator Control governing the target resource.

You can approve or reject an access request. You can also revoke the approval of an already approved access request. While creating an access request, the operator specifies the duration of access. You have the option to approve the entire duration or reduce or even increase the time duration. An operator can also request for an extension. The approval for such an extension is processed the same way the original access request was processed.""")
@cli_util.help_option_group
def access_request_group():
    pass


opctl_service_cli.opctl_service_group.add_command(access_requests_root_group)
access_requests_root_group.add_command(access_request_group)


@access_request_group.command(name=cli_util.override('access_requests.approve_access_request.command_name', 'approve'), help=u"""Approves an access request. \n[Command Reference](approveAccessRequest)""")
@cli_util.option('--access-request-id', required=True, help=u"""unique AccessRequest identifier""")
@cli_util.option('--approver-comment', help=u"""Comment by the approver during approval.""")
@cli_util.option('--audit-type', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Specifies the type of auditing to be enabled. There are two levels of auditing: command-level and keystroke-level. By default, auditing is enabled at the command level i.e., each command issued by the operator is audited. When keystroke-level is chosen, in addition to command level logging, key strokes are also logged.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--additional-message', help=u"""Message that needs to be displayed to the Ops User.""")
@cli_util.option('--time-of-user-creation', type=custom_types.CLI_DATETIME, help=u"""The time when access request is scheduled to be approved in [RFC 3339] timestamp format.Example: '2020-05-22T21:10:29.600Z'""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'audit-type': {'module': 'operator_access_control', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'audit-type': {'module': 'operator_access_control', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def approve_access_request(ctx, from_json, access_request_id, approver_comment, audit_type, additional_message, time_of_user_creation, if_match):

    if isinstance(access_request_id, six.string_types) and len(access_request_id.strip()) == 0:
        raise click.UsageError('Parameter --access-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if approver_comment is not None:
        _details['approverComment'] = approver_comment

    if audit_type is not None:
        _details['auditType'] = cli_util.parse_json_parameter("audit_type", audit_type)

    if additional_message is not None:
        _details['additionalMessage'] = additional_message

    if time_of_user_creation is not None:
        _details['timeOfUserCreation'] = time_of_user_creation

    client = cli_util.build_client('operator_access_control', 'access_requests', ctx)
    result = client.approve_access_request(
        access_request_id=access_request_id,
        approve_access_request_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@access_request_group.command(name=cli_util.override('access_requests.get_access_request.command_name', 'get'), help=u"""Gets details of an access request. \n[Command Reference](getAccessRequest)""")
@cli_util.option('--access-request-id', required=True, help=u"""unique AccessRequest identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'operator_access_control', 'class': 'AccessRequest'})
@cli_util.wrap_exceptions
def get_access_request(ctx, from_json, access_request_id):

    if isinstance(access_request_id, six.string_types) and len(access_request_id.strip()) == 0:
        raise click.UsageError('Parameter --access-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('operator_access_control', 'access_requests', ctx)
    result = client.get_access_request(
        access_request_id=access_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@access_request_group.command(name=cli_util.override('access_requests.list_access_request_histories.command_name', 'list-access-request-histories'), help=u"""Returns a history of all status associated with the accessRequestId. \n[Command Reference](listAccessRequestHistories)""")
@cli_util.option('--access-request-id', required=True, help=u"""unique AccessRequest identifier""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'operator_access_control', 'class': 'AccessRequestHistoryCollection'})
@cli_util.wrap_exceptions
def list_access_request_histories(ctx, from_json, all_pages, page_size, access_request_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(access_request_id, six.string_types) and len(access_request_id.strip()) == 0:
        raise click.UsageError('Parameter --access-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('operator_access_control', 'access_requests', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_access_request_histories,
            access_request_id=access_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_access_request_histories,
            limit,
            page_size,
            access_request_id=access_request_id,
            **kwargs
        )
    else:
        result = client.list_access_request_histories(
            access_request_id=access_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@access_request_group.command(name=cli_util.override('access_requests.list_access_requests.command_name', 'list'), help=u"""Lists all access requests in the compartment. \n[Command Reference](listAccessRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--resource-name', help=u"""A filter to return only resources that match the given ResourceName.""")
@cli_util.option('--resource-type', help=u"""A filter to return only lists of resources that match the entire given service type.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATED", "APPROVALWAITING", "PREAPPROVED", "APPROVED", "REJECTED", "DEPLOYED", "DEPLOYFAILED", "UNDEPLOYED", "UNDEPLOYFAILED", "CLOSEFAILED", "REVOKEFAILED", "EXPIRYFAILED", "REVOKING", "REVOKED", "EXTENDING", "EXTENDED", "EXTENSIONREJECTED", "COMPLETING", "COMPLETED", "EXPIRED", "APPROVEDFORFUTURE", "INREVIEW"]), help=u"""A filter to return only resources whose lifecycleState matches the given AccessRequest lifecycleState.""")
@cli_util.option('--time-start', type=custom_types.CLI_DATETIME, help=u"""Query start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd parameters are used together.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-end', type=custom_types.CLI_DATETIME, help=u"""Query start time in UTC in ISO 8601 format(inclusive). Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ). timeIntervalStart and timeIntervalEnd parameters are used together.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'operator_access_control', 'class': 'AccessRequestCollection'})
@cli_util.wrap_exceptions
def list_access_requests(ctx, from_json, all_pages, page_size, compartment_id, resource_name, resource_type, lifecycle_state, time_start, time_end, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if resource_name is not None:
        kwargs['resource_name'] = resource_name
    if resource_type is not None:
        kwargs['resource_type'] = resource_type
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if time_start is not None:
        kwargs['time_start'] = time_start
    if time_end is not None:
        kwargs['time_end'] = time_end
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('operator_access_control', 'access_requests', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_access_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_access_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_access_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@access_request_group.command(name=cli_util.override('access_requests.reject_access_request.command_name', 'reject'), help=u"""Rejects an access request. \n[Command Reference](rejectAccessRequest)""")
@cli_util.option('--access-request-id', required=True, help=u"""unique AccessRequest identifier""")
@cli_util.option('--approver-comment', help=u"""Comment by the approver explaining why the request is rejected.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def reject_access_request(ctx, from_json, access_request_id, approver_comment, if_match):

    if isinstance(access_request_id, six.string_types) and len(access_request_id.strip()) == 0:
        raise click.UsageError('Parameter --access-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if approver_comment is not None:
        _details['approverComment'] = approver_comment

    client = cli_util.build_client('operator_access_control', 'access_requests', ctx)
    result = client.reject_access_request(
        access_request_id=access_request_id,
        reject_access_request_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@access_request_group.command(name=cli_util.override('access_requests.review_access_request.command_name', 'review'), help=u"""Reviews the access request. \n[Command Reference](reviewAccessRequest)""")
@cli_util.option('--access-request-id', required=True, help=u"""unique AccessRequest identifier""")
@cli_util.option('--approver-comment', help=u"""Comment by the approver explaining that the access request is in review.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATED", "APPROVALWAITING", "PREAPPROVED", "APPROVED", "REJECTED", "DEPLOYED", "DEPLOYFAILED", "UNDEPLOYED", "UNDEPLOYFAILED", "CLOSEFAILED", "REVOKEFAILED", "EXPIRYFAILED", "REVOKING", "REVOKED", "EXTENDING", "EXTENDED", "EXTENSIONREJECTED", "COMPLETING", "COMPLETED", "EXPIRED", "APPROVEDFORFUTURE", "INREVIEW"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'operator_access_control', 'class': 'AccessRequest'})
@cli_util.wrap_exceptions
def review_access_request(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, access_request_id, approver_comment, if_match):

    if isinstance(access_request_id, six.string_types) and len(access_request_id.strip()) == 0:
        raise click.UsageError('Parameter --access-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if approver_comment is not None:
        _details['approverComment'] = approver_comment

    client = cli_util.build_client('operator_access_control', 'access_requests', ctx)
    result = client.review_access_request(
        access_request_id=access_request_id,
        review_access_request_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_access_request') and callable(getattr(client, 'get_access_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_access_request(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@access_request_group.command(name=cli_util.override('access_requests.revoke_access_request.command_name', 'revoke'), help=u"""Revokes an already approved access request. \n[Command Reference](revokeAccessRequest)""")
@cli_util.option('--access-request-id', required=True, help=u"""unique AccessRequest identifier""")
@cli_util.option('--approver-comment', help=u"""Comment specified by the approver explaining why the approval is revoked.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def revoke_access_request(ctx, from_json, access_request_id, approver_comment, if_match):

    if isinstance(access_request_id, six.string_types) and len(access_request_id.strip()) == 0:
        raise click.UsageError('Parameter --access-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if approver_comment is not None:
        _details['approverComment'] = approver_comment

    client = cli_util.build_client('operator_access_control', 'access_requests', ctx)
    result = client.revoke_access_request(
        access_request_id=access_request_id,
        revoke_access_request_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
