# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Accesses the google.container.v1 ClusterManager API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.page_iterator
import grpc

from google.cloud.container_v1.gapic import cluster_manager_client_config
from google.cloud.container_v1.gapic import enums
from google.cloud.container_v1.gapic.transports import cluster_manager_grpc_transport
from google.cloud.container_v1.proto import cluster_service_pb2
from google.cloud.container_v1.proto import cluster_service_pb2_grpc
from google.protobuf import empty_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    "google-cloud-container"
).version


class ClusterManagerClient(object):
    """Google Kubernetes Engine Cluster Manager v1"""

    SERVICE_ADDRESS = "container.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.container.v1.ClusterManager"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ClusterManagerClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.ClusterManagerGrpcTransport,
                    Callable[[~.Credentials, type], ~.ClusterManagerGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = cluster_manager_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=cluster_manager_grpc_transport.ClusterManagerGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = cluster_manager_grpc_transport.ClusterManagerGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME]
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def list_clusters(
        self,
        project_id=None,
        zone=None,
        parent=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists all clusters owned by a project in either the specified zone or all
        zones.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> response = client.list_clusters()

        Args:
            project_id (str): This token allows you to get the next page of results for list
                requests. If the number of results is larger than ``page_size``, use the
                ``next_page_token`` as a value for the query parameter ``page_token`` in
                the next request. The value will become empty when there are no more
                pages.
            zone (str): OAuth scopes needed for the client.

                Example:

                | service Foo { option (google.api.oauth_scopes) =
                | "https://www.googleapis.com/auth/cloud-platform"; ... }

                If there is more than one scope, use a comma-separated string:

                Example:

                | service Foo { option (google.api.oauth_scopes) =
                | "https://www.googleapis.com/auth/cloud-platform,"
                  "https://www.googleapis.com/auth/monitoring"; ... }
            parent (str): [Output only] The IP address of this cluster's master endpoint. The
                endpoint can be accessed from the internet at
                ``https://username:password@endpoint/``.

                See the ``masterAuth`` property of this resource for username and
                password information.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.ListClustersResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_clusters" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_clusters"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_clusters,
                default_retry=self._method_configs["ListClusters"].retry,
                default_timeout=self._method_configs["ListClusters"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.ListClustersRequest(
            project_id=project_id, zone=zone, parent=parent
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["list_clusters"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_cluster(
        self,
        project_id=None,
        zone=None,
        cluster_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets the details of a specific cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> response = client.get_cluster()

        Args:
            project_id (str): For extensions, this is the name of the type being extended. It is
                resolved in the same manner as type_name.
            zone (str): The name (project, location, cluster id) of the cluster to set
                maintenance policy. Specified in the format
                ``projects/*/locations/*/clusters/*``.
            cluster_id (str): Deprecated. The name of the cluster to retrieve.
                This field has been deprecated and replaced by the name field.
            name (str): Deprecated. The Google Developers Console `project ID or project
                number <https://support.google.com/cloud/answer/6158840>`__. This field
                has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Cluster` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_cluster" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_cluster"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_cluster,
                default_retry=self._method_configs["GetCluster"].retry,
                default_timeout=self._method_configs["GetCluster"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.GetClusterRequest(
            project_id=project_id, zone=zone, cluster_id=cluster_id, name=name
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_cluster"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_cluster(
        self,
        cluster,
        project_id=None,
        zone=None,
        parent=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        [Output only] Base64-encoded private key used by clients to
        authenticate to the cluster endpoint.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize `cluster`:
            >>> cluster = {}
            >>>
            >>> response = client.create_cluster(cluster)

        Args:
            cluster (Union[dict, ~google.cloud.container_v1.types.Cluster]): Denotes a field as required. This indicates that the field **must**
                be provided as part of the request, and failure to do so will cause an
                error (usually ``INVALID_ARGUMENT``).

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.Cluster`
            project_id (str): The parent (project and location) where the operations will be
                listed. Specified in the format ``projects/*/locations/*``. Location "-"
                matches all zones and all regions.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__ in
                which the cluster resides. This field has been deprecated and replaced
                by the name field.
            parent (str): Minimum number of nodes in the NodePool. Must be >= 1 and <=
                max_node_count.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_cluster" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_cluster"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_cluster,
                default_retry=self._method_configs["CreateCluster"].retry,
                default_timeout=self._method_configs["CreateCluster"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.CreateClusterRequest(
            cluster=cluster, project_id=project_id, zone=zone, parent=parent
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_cluster"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_cluster(
        self,
        update,
        project_id=None,
        zone=None,
        cluster_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates the settings of a specific cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize `update`:
            >>> update = {}
            >>>
            >>> response = client.update_cluster(update)

        Args:
            update (Union[dict, ~google.cloud.container_v1.types.ClusterUpdate]): Required. A description of the update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.ClusterUpdate`
            project_id (str): Maximum number of nodes in the NodePool. Must be >= min_node_count.
                There has to enough quota to scale up the cluster.
            zone (str): The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__ in
                which the operation is taking place. This field is deprecated, use
                location instead.
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            name (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__ in
                which the operation resides. This field has been deprecated and replaced
                by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_cluster" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_cluster"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_cluster,
                default_retry=self._method_configs["UpdateCluster"].retry,
                default_timeout=self._method_configs["UpdateCluster"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.UpdateClusterRequest(
            update=update,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_cluster"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_node_pool(
        self,
        node_version,
        image_type,
        project_id=None,
        zone=None,
        cluster_id=None,
        node_pool_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates the version and/or image type for the specified node pool.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize `node_version`:
            >>> node_version = ''
            >>>
            >>> # TODO: Initialize `image_type`:
            >>> image_type = ''
            >>>
            >>> response = client.update_node_pool(node_version, image_type)

        Args:
            node_version (str): Required. The Kubernetes version to change the nodes to (typically an
                upgrade).

                Users may specify either explicit versions offered by Kubernetes Engine or
                version aliases, which have the following behavior:

                - "latest": picks the highest valid Kubernetes version
                - "1.X": picks the highest valid patch+gke.N patch in the 1.X version
                - "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
                - "1.X.Y-gke.N": picks an explicit Kubernetes version
                - "-": picks the Kubernetes master version
            image_type (str): Required. The desired image type for the node pool.
            project_id (str): Required. The monitoring service the cluster should use to write
                metrics. Currently available options:

                -  "monitoring.googleapis.com/kubernetes" - the Google Cloud Monitoring
                   service with Kubernetes-native resource model
                -  "monitoring.googleapis.com" - the Google Cloud Monitoring service
                -  "none" - no metrics will be exported from the cluster
            zone (str): A Timestamp represents a point in time independent of any time zone
                or local calendar, encoded as a count of seconds and fractions of
                seconds at nanosecond resolution. The count is relative to an epoch at
                UTC midnight on January 1, 1970, in the proleptic Gregorian calendar
                which extends the Gregorian calendar backwards to year one.

                All minutes are 60 seconds long. Leap seconds are "smeared" so that no
                leap second table is needed for interpretation, using a `24-hour linear
                smear <https://developers.google.com/time/smear>`__.

                The range is from 0001-01-01T00:00:00Z to
                9999-12-31T23:59:59.999999999Z. By restricting to that range, we ensure
                that we can convert to and from `RFC
                3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ date strings.

                # Examples

                Example 1: Compute Timestamp from POSIX ``time()``.

                ::

                    Timestamp timestamp;
                    timestamp.set_seconds(time(NULL));
                    timestamp.set_nanos(0);

                Example 2: Compute Timestamp from POSIX ``gettimeofday()``.

                ::

                    struct timeval tv;
                    gettimeofday(&tv, NULL);

                    Timestamp timestamp;
                    timestamp.set_seconds(tv.tv_sec);
                    timestamp.set_nanos(tv.tv_usec * 1000);

                Example 3: Compute Timestamp from Win32 ``GetSystemTimeAsFileTime()``.

                ::

                    FILETIME ft;
                    GetSystemTimeAsFileTime(&ft);
                    UINT64 ticks = (((UINT64)ft.dwHighDateTime) << 32) | ft.dwLowDateTime;

                    // A Windows tick is 100 nanoseconds. Windows epoch 1601-01-01T00:00:00Z
                    // is 11644473600 seconds before Unix epoch 1970-01-01T00:00:00Z.
                    Timestamp timestamp;
                    timestamp.set_seconds((INT64) ((ticks / 10000000) - 11644473600LL));
                    timestamp.set_nanos((INT32) ((ticks % 10000000) * 100));

                Example 4: Compute Timestamp from Java ``System.currentTimeMillis()``.

                ::

                    long millis = System.currentTimeMillis();

                    Timestamp timestamp = Timestamp.newBuilder().setSeconds(millis / 1000)
                        .setNanos((int) ((millis % 1000) * 1000000)).build();

                Example 5: Compute Timestamp from current time in Python.

                ::

                    timestamp = Timestamp()
                    timestamp.GetCurrentTime()

                # JSON Mapping

                In JSON format, the Timestamp type is encoded as a string in the `RFC
                3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ format. That is, the
                format is "{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z" where
                {year} is always expressed using four digits while {month}, {day},
                {hour}, {min}, and {sec} are zero-padded to two digits each. The
                fractional seconds, which can go up to 9 digits (i.e. up to 1 nanosecond
                resolution), are optional. The "Z" suffix indicates the timezone
                ("UTC"); the timezone is required. A proto3 JSON serializer should
                always use UTC (as indicated by "Z") when printing the Timestamp type
                and a proto3 JSON parser should be able to accept both UTC and other
                timezones (as indicated by an offset).

                For example, "2017-01-15T01:30:15.01Z" encodes 15.01 seconds past 01:30
                UTC on January 15, 2017.

                In JavaScript, one can convert a Date object to this format using the
                standard
                `toISOString() <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString>`__
                method. In Python, a standard ``datetime.datetime`` object can be
                converted to this format using
                ```strftime`` <https://docs.python.org/2/library/time.html#time.strftime>`__
                with the time format spec '%Y-%m-%dT%H:%M:%S.%fZ'. Likewise, in Java,
                one can use the Joda Time's
                ```ISODateTimeFormat.dateTime()`` <http://www.joda.org/joda-time/apidocs/org/joda/time/format/ISODateTimeFormat.html#dateTime%2D%2D>`__
                to obtain a formatter capable of generating timestamps in this format.
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            node_pool_id (str): Deprecated. The name of the node pool to upgrade.
                This field has been deprecated and replaced by the name field.
            name (str): If set, gives the index of a oneof in the containing type's
                oneof_decl list. This field is a member of that oneof.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_node_pool" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_node_pool"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_node_pool,
                default_retry=self._method_configs["UpdateNodePool"].retry,
                default_timeout=self._method_configs["UpdateNodePool"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.UpdateNodePoolRequest(
            node_version=node_version,
            image_type=image_type,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            node_pool_id=node_pool_id,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_node_pool"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def set_node_pool_autoscaling(
        self,
        autoscaling,
        project_id=None,
        zone=None,
        cluster_id=None,
        node_pool_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Sets the autoscaling settings for the specified node pool.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize `autoscaling`:
            >>> autoscaling = {}
            >>>
            >>> response = client.set_node_pool_autoscaling(autoscaling)

        Args:
            autoscaling (Union[dict, ~google.cloud.container_v1.types.NodePoolAutoscaling]): Required. Autoscaling configuration for the node pool.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.NodePoolAutoscaling`
            project_id (str): [Output only] The pod CIDR block size per node in this node pool.
            zone (str): Deprecated. The server-assigned ``name`` of the operation. This
                field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            node_pool_id (str): Deprecated. The name of the node pool to upgrade.
                This field has been deprecated and replaced by the name field.
            name (str): Deprecated. The Google Developers Console `project ID or project
                number <https://support.google.com/cloud/answer/6158840>`__. This field
                has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "set_node_pool_autoscaling" not in self._inner_api_calls:
            self._inner_api_calls[
                "set_node_pool_autoscaling"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.set_node_pool_autoscaling,
                default_retry=self._method_configs["SetNodePoolAutoscaling"].retry,
                default_timeout=self._method_configs["SetNodePoolAutoscaling"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.SetNodePoolAutoscalingRequest(
            autoscaling=autoscaling,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            node_pool_id=node_pool_id,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["set_node_pool_autoscaling"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def set_logging_service(
        self,
        logging_service,
        project_id=None,
        zone=None,
        cluster_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Sets the logging service for a specific cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize `logging_service`:
            >>> logging_service = ''
            >>>
            >>> response = client.set_logging_service(logging_service)

        Args:
            logging_service (str): The name of the uninterpreted option. Each string represents a
                segment in a dot-separated name. is_extension is true iff a segment
                represents an extension (denoted with parentheses in options specs in
                .proto files). E.g.,{ ["foo", false], ["bar.baz", true], ["qux", false]
                } represents "foo.(bar.baz).qux".
            project_id (str): The name (project, location, cluster) of the cluster to set
                monitoring. Specified in the format
                ``projects/*/locations/*/clusters/*``.
            zone (str): JSON name of this field. The value is set by protocol compiler. If
                the user has set a "json_name" option on this field, that option's value
                will be used. Otherwise, it's deduced from the field's name by
                converting it to camelCase.
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            name (str): The name (project, location, operation id) of the operation to
                cancel. Specified in the format ``projects/*/locations/*/operations/*``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "set_logging_service" not in self._inner_api_calls:
            self._inner_api_calls[
                "set_logging_service"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.set_logging_service,
                default_retry=self._method_configs["SetLoggingService"].retry,
                default_timeout=self._method_configs["SetLoggingService"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.SetLoggingServiceRequest(
            logging_service=logging_service,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["set_logging_service"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def set_monitoring_service(
        self,
        monitoring_service,
        project_id=None,
        zone=None,
        cluster_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Sets the monitoring service for a specific cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize `monitoring_service`:
            >>> monitoring_service = ''
            >>>
            >>> response = client.set_monitoring_service(monitoring_service)

        Args:
            monitoring_service (str): [Output only] The time the cluster was created, in
                `RFC3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ text format.
            project_id (str): The IP address range of the services IPs in this cluster. If blank,
                a range will be automatically chosen with the default size.

                This field is only applicable when ``use_ip_aliases`` is true.

                Set to blank to have a range chosen with the default size.

                Set to /netmask (e.g. ``/14``) to have a range chosen with a specific
                netmask.

                Set to a
                `CIDR <http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__
                notation (e.g. ``10.96.0.0/14``) from the RFC-1918 private networks
                (e.g. ``10.0.0.0/8``, ``172.16.0.0/12``, ``192.168.0.0/16``) to pick a
                specific range to use.
            zone (str): Deprecated. The Google Developers Console `project ID or project
                number <https://support.google.com/cloud/answer/6158840>`__. This field
                has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            name (str): Deprecated. The Google Developers Console `project ID or project
                number <https://support.google.com/cloud/answer/6158840>`__. This field
                has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "set_monitoring_service" not in self._inner_api_calls:
            self._inner_api_calls[
                "set_monitoring_service"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.set_monitoring_service,
                default_retry=self._method_configs["SetMonitoringService"].retry,
                default_timeout=self._method_configs["SetMonitoringService"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.SetMonitoringServiceRequest(
            monitoring_service=monitoring_service,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["set_monitoring_service"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def set_addons_config(
        self,
        addons_config,
        project_id=None,
        zone=None,
        cluster_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Sets the addons for a specific cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize `addons_config`:
            >>> addons_config = {}
            >>>
            >>> response = client.set_addons_config(addons_config)

        Args:
            addons_config (Union[dict, ~google.cloud.container_v1.types.AddonsConfig]): Required. The desired configurations for the various addons available to run in the
                cluster.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.AddonsConfig`
            project_id (str): The parent project where subnetworks are usable. Specified in the
                format ``projects/*``.
            zone (str): Whether a new subnetwork will be created automatically for the
                cluster.

                This field is only applicable when ``use_ip_aliases`` is true.
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            name (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__ in
                which the cluster resides. This field has been deprecated and replaced
                by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "set_addons_config" not in self._inner_api_calls:
            self._inner_api_calls[
                "set_addons_config"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.set_addons_config,
                default_retry=self._method_configs["SetAddonsConfig"].retry,
                default_timeout=self._method_configs["SetAddonsConfig"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.SetAddonsConfigRequest(
            addons_config=addons_config,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["set_addons_config"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def set_locations(
        self,
        locations,
        project_id=None,
        zone=None,
        cluster_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Sets the locations for a specific cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize `locations`:
            >>> locations = []
            >>>
            >>> response = client.set_locations(locations)

        Args:
            locations (list[str]): [Output only] This field is set when upgrades are about to commence
                with the approximate start time for the upgrades, in
                `RFC3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ text format.
            project_id (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__ in
                which the cluster resides. This field has been deprecated and replaced
                by the name field.
            zone (str): The max number of results per page that should be returned. If the
                number of available results is larger than ``page_size``, a
                ``next_page_token`` is returned which can be used to get the next page
                of results in subsequent requests. Acceptable values are 0 to 500,
                inclusive. (Default: 500)
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            name (str): [Output only] This field is set when upgrades are about to commence
                with the description of the upgrade.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "set_locations" not in self._inner_api_calls:
            self._inner_api_calls[
                "set_locations"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.set_locations,
                default_retry=self._method_configs["SetLocations"].retry,
                default_timeout=self._method_configs["SetLocations"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.SetLocationsRequest(
            locations=locations,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["set_locations"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_master(
        self,
        master_version,
        project_id=None,
        zone=None,
        cluster_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates the master for a specific cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize `master_version`:
            >>> master_version = ''
            >>>
            >>> response = client.update_master(master_version)

        Args:
            master_version (str): Required. The Kubernetes version to change the master to.

                Users may specify either explicit versions offered by Kubernetes Engine or
                version aliases, which have the following behavior:

                - "latest": picks the highest valid Kubernetes version
                - "1.X": picks the highest valid patch+gke.N patch in the 1.X version
                - "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
                - "1.X.Y-gke.N": picks an explicit Kubernetes version
                - "-": picks the default Kubernetes version
            project_id (str): [Output only] The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/regions-zones/regions-zones#available>`__
                or
                `region <https://cloud.google.com/compute/docs/regions-zones/regions-zones#available>`__
                in which the cluster resides.
            zone (str): [Output only] Server-defined URL for the resource.
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            name (str): Set true to use the old proto1 MessageSet wire format for
                extensions. This is provided for backwards-compatibility with the
                MessageSet wire format. You should not use this for any other reason:
                It's less efficient, has fewer features, and is more complicated.

                The message must be defined exactly as follows: message Foo { option
                message_set_wire_format = true; extensions 4 to max; } Note that the
                message cannot have any defined fields; MessageSets only have
                extensions.

                All extensions of your type must be singular messages; e.g. they cannot
                be int32s, enums, or repeated messages.

                Because this is an option, the above two restrictions are not enforced
                by the protocol compiler.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_master" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_master"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_master,
                default_retry=self._method_configs["UpdateMaster"].retry,
                default_timeout=self._method_configs["UpdateMaster"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.UpdateMasterRequest(
            master_version=master_version,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_master"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def set_master_auth(
        self,
        action,
        update,
        project_id=None,
        zone=None,
        cluster_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Sets master auth materials. Currently supports changing the admin password
        or a specific cluster, either via password generation or explicitly setting
        the password.

        Example:
            >>> from google.cloud import container_v1
            >>> from google.cloud.container_v1 import enums
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize `action`:
            >>> action = enums.SetMasterAuthRequest.Action.UNKNOWN
            >>>
            >>> # TODO: Initialize `update`:
            >>> update = {}
            >>>
            >>> response = client.set_master_auth(action, update)

        Args:
            action (~google.cloud.container_v1.types.Action): Required. The exact form of action to be taken on the master auth.
            update (Union[dict, ~google.cloud.container_v1.types.MasterAuth]): Required. A description of the update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.MasterAuth`
            project_id (str): display_name is an optional field for users to identify CIDR blocks.
            zone (str): [Output only] The time the operation started, in
                `RFC3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ text format.
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            name (str): [Output only] The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__ in
                which the cluster resides. This field is deprecated, use location
                instead.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "set_master_auth" not in self._inner_api_calls:
            self._inner_api_calls[
                "set_master_auth"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.set_master_auth,
                default_retry=self._method_configs["SetMasterAuth"].retry,
                default_timeout=self._method_configs["SetMasterAuth"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.SetMasterAuthRequest(
            action=action,
            update=update,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["set_master_auth"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_cluster(
        self,
        project_id=None,
        zone=None,
        cluster_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes the cluster, including the Kubernetes endpoint and all worker
        nodes.

        Firewalls and routes that were configured during cluster creation
        are also deleted.

        Other Google Compute Engine resources that might be in use by the cluster,
        such as load balancer resources, are not deleted if they weren't present
        when the cluster was initially created.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> response = client.delete_cluster()

        Args:
            project_id (str): cidr_block must be specified in CIDR notation.
            zone (str): The IP address range of the Cloud TPUs in this cluster. If
                unspecified, a range will be automatically chosen with the default size.

                This field is only applicable when ``use_ip_aliases`` is true.

                If unspecified, the range will use the default size.

                Set to /netmask (e.g. ``/14``) to have a range chosen with a specific
                netmask.

                Set to a
                `CIDR <http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__
                notation (e.g. ``10.96.0.0/14``) from the RFC-1918 private networks
                (e.g. ``10.0.0.0/8``, ``172.16.0.0/12``, ``192.168.0.0/16``) to pick a
                specific range to use.
            cluster_id (str): Deprecated. The name of the cluster to delete.
                This field has been deprecated and replaced by the name field.
            name (str): [Output only] The time the operation completed, in
                `RFC3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ text format.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_cluster" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_cluster"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_cluster,
                default_retry=self._method_configs["DeleteCluster"].retry,
                default_timeout=self._method_configs["DeleteCluster"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.DeleteClusterRequest(
            project_id=project_id, zone=zone, cluster_id=cluster_id, name=name
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["delete_cluster"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_operations(
        self,
        project_id=None,
        zone=None,
        parent=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists all operations in a project in a specific zone or all zones.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> response = client.list_operations()

        Args:
            project_id (str): [Output only] The current software version of the master endpoint.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__ in
                which the cluster resides. This field has been deprecated and replaced
                by the name field.
            parent (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__ in
                which the cluster resides. This field has been deprecated and replaced
                by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.ListOperationsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_operations" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_operations"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_operations,
                default_retry=self._method_configs["ListOperations"].retry,
                default_timeout=self._method_configs["ListOperations"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.ListOperationsRequest(
            project_id=project_id, zone=zone, parent=parent
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["list_operations"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_operation(
        self,
        project_id=None,
        zone=None,
        operation_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets the specified operation.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> response = client.get_operation()

        Args:
            project_id (str): The name (project and location) of the server config to get,
                specified in the format ``projects/*/locations/*``.
            zone (str): Deprecated. The Google Developers Console `project ID or project
                number <https://support.google.com/cloud/answer/6158840>`__. This field
                has been deprecated and replaced by the name field.
            operation_id (str): cidr_blocks define up to 50 external networks that could access
                Kubernetes master through HTTPS.
            name (str): The name (project, location, cluster id) of the cluster to start IP
                rotation. Specified in the format ``projects/*/locations/*/clusters/*``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_operation" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_operation"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_operation,
                default_retry=self._method_configs["GetOperation"].retry,
                default_timeout=self._method_configs["GetOperation"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.GetOperationRequest(
            project_id=project_id, zone=zone, operation_id=operation_id, name=name
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_operation"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def cancel_operation(
        self,
        project_id=None,
        zone=None,
        operation_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Cancels the specified operation.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> client.cancel_operation()

        Args:
            project_id (str): [Output only] Deprecated, use
                `NodePools.version <https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters.nodePools>`__
                instead. The current version of the node software components. If they
                are currently at multiple versions because they're in the process of
                being upgraded, this reflects the minimum version of all nodes.
            zone (str): Whether the message is an automatically generated map entry type for
                the maps field.

                For maps fields: map<KeyType, ValueType> map_field = 1; The parsed
                descriptor looks like: message MapFieldEntry { option map_entry = true;
                optional KeyType key = 1; optional ValueType value = 2; } repeated
                MapFieldEntry map_field = 1;

                Implementations may choose not to generate the map_entry=true message,
                but use a native map in the target language to hold the keys and values.
                The reflection APIs in such implementations still need to work as if the
                field is a repeated message field.

                NOTE: Do not set the option in .proto files. Always use the maps syntax
                instead. The option should only be implicitly set by the proto compiler
                parser.
            operation_id (str): Deprecated. The Google Developers Console `project ID or project
                number <https://support.google.com/cloud/answer/6158840>`__. This field
                has been deprecated and replaced by the parent field.
            name (str): The resource type. It must be in the format of
                {service_name}/{resource_type_kind}. The ``resource_type_kind`` must be
                singular and must not include version numbers.

                Example: ``storage.googleapis.com/Bucket``

                The value of the resource_type_kind must follow the regular expression
                /[A-Za-z][a-zA-Z0-9]+/. It should start with an upper case character and
                should use PascalCase (UpperCamelCase). The maximum number of characters
                allowed for the ``resource_type_kind`` is 100.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "cancel_operation" not in self._inner_api_calls:
            self._inner_api_calls[
                "cancel_operation"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.cancel_operation,
                default_retry=self._method_configs["CancelOperation"].retry,
                default_timeout=self._method_configs["CancelOperation"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.CancelOperationRequest(
            project_id=project_id, zone=zone, operation_id=operation_id, name=name
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["cancel_operation"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_server_config(
        self,
        project_id=None,
        zone=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Returns configuration info about the Google Kubernetes Engine service.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> response = client.get_server_config()

        Args:
            project_id (str): Deprecated. The Google Developers Console `project ID or project
                number <https://developers.google.com/console/help/new/#projectnumber>`__.
                This field has been deprecated and replaced by the name field.
            zone (str): IN_USE_SHAREABLE_POD denotes this range was created by the network
                admin and is currently claimed by a cluster for pods. It can only be
                used by other clusters as a pod range.
            name (str): A Location identifies a piece of source code in a .proto file which
                corresponds to a particular definition. This information is intended to
                be useful to IDEs, code indexers, documentation generators, and similar
                tools.

                For example, say we have a file like: message Foo { optional string foo
                = 1; } Let's look at just the field definition: optional string foo = 1;
                ^ ^^ ^^ ^ ^^^ a bc de f ghi We have the following locations: span path
                represents [a,i) [ 4, 0, 2, 0 ] The whole field definition. [a,b) [ 4,
                0, 2, 0, 4 ] The label (optional). [c,d) [ 4, 0, 2, 0, 5 ] The type
                (string). [e,f) [ 4, 0, 2, 0, 1 ] The name (foo). [g,h) [ 4, 0, 2, 0, 3
                ] The number (1).

                Notes:

                -  A location may refer to a repeated field itself (i.e. not to any
                   particular index within it). This is used whenever a set of elements
                   are logically enclosed in a single code segment. For example, an
                   entire extend block (possibly containing multiple extension
                   definitions) will have an outer location whose path refers to the
                   "extensions" repeated field without an index.
                -  Multiple locations may have the same path. This happens when a single
                   logical declaration is spread out across multiple places. The most
                   obvious example is the "extend" block again -- there may be multiple
                   extend blocks in the same scope, each of which will have the same
                   path.
                -  A location's span is not always a subset of its parent's span. For
                   example, the "extendee" of an extension declaration appears at the
                   beginning of the "extend" block and is shared by all extensions
                   within the block.
                -  Just because a location's span is a subset of some other location's
                   span does not mean that it is a descendant. For example, a "group"
                   defines both a type and a field in a single declaration. Thus, the
                   locations corresponding to the type and field and their components
                   will overlap.
                -  Code which tries to interpret locations should probably be designed
                   to ignore those that it doesn't understand, as more types of
                   locations could be recorded in the future.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.ServerConfig` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_server_config" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_server_config"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_server_config,
                default_retry=self._method_configs["GetServerConfig"].retry,
                default_timeout=self._method_configs["GetServerConfig"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.GetServerConfigRequest(
            project_id=project_id, zone=zone, name=name
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_server_config"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_node_pools(
        self,
        project_id=None,
        zone=None,
        cluster_id=None,
        parent=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists the node pools for a cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> response = client.list_node_pools()

        Args:
            project_id (str): [Output only] Additional information about the current status of
                this cluster, if available.
            zone (str): The name (project, location, cluster) of the cluster to set
                locations. Specified in the format
                ``projects/*/locations/*/clusters/*``.
            cluster_id (str): Deprecated. The name of the cluster.
                This field has been deprecated and replaced by the parent field.
            parent (str): [Output only] The size of the address space on each node for hosting
                containers. This is provisioned from within the ``container_ipv4_cidr``
                range. This field will only be set when cluster is in route-based
                network mode.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.ListNodePoolsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_node_pools" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_node_pools"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_node_pools,
                default_retry=self._method_configs["ListNodePools"].retry,
                default_timeout=self._method_configs["ListNodePools"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.ListNodePoolsRequest(
            project_id=project_id, zone=zone, cluster_id=cluster_id, parent=parent
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["list_node_pools"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_node_pool(
        self,
        project_id=None,
        zone=None,
        cluster_id=None,
        node_pool_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Retrieves the requested node pool.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> response = client.get_node_pool()

        Args:
            project_id (str): The parent (project and location) where the cluster will be created.
                Specified in the format ``projects/*/locations/*``.
            zone (str): The set of Google API scopes to be made available on all of the node
                VMs under the "default" service account.

                The following scopes are recommended, but not required, and by default
                are not included:

                -  ``https://www.googleapis.com/auth/compute`` is required for mounting
                   persistent storage on your nodes.
                -  ``https://www.googleapis.com/auth/devstorage.read_only`` is required
                   for communicating with **gcr.io** (the `Google Container
                   Registry <https://cloud.google.com/container-registry/>`__).

                If unspecified, no scopes are added, unless Cloud Logging or Cloud
                Monitoring are enabled, in which case their required scopes will be
                added.
            cluster_id (str): Deprecated. The name of the cluster.
                This field has been deprecated and replaced by the name field.
            node_pool_id (str): Deprecated. The name of the node pool.
                This field has been deprecated and replaced by the name field.
            name (str): Deprecated. The Google Developers Console `project ID or project
                number <https://developers.google.com/console/help/new/#projectnumber>`__.
                This field has been deprecated and replaced by the parent field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.NodePool` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_node_pool" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_node_pool"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_node_pool,
                default_retry=self._method_configs["GetNodePool"].retry,
                default_timeout=self._method_configs["GetNodePool"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.GetNodePoolRequest(
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            node_pool_id=node_pool_id,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_node_pool"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_node_pool(
        self,
        node_pool,
        project_id=None,
        zone=None,
        cluster_id=None,
        parent=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a node pool for a cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize `node_pool`:
            >>> node_pool = {}
            >>>
            >>> response = client.create_node_pool(node_pool)

        Args:
            node_pool (Union[dict, ~google.cloud.container_v1.types.NodePool]): Required. The node pool to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.NodePool`
            project_id (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__ in
                which the cluster resides. This field has been deprecated and replaced
                by the parent field.
            zone (str): Creates a cluster, consisting of the specified number and type of
                Google Compute Engine instances.

                By default, the cluster is created in the project's `default
                network <https://cloud.google.com/compute/docs/networks-and-firewalls#networks>`__.

                One firewall is added for the cluster. After cluster creation, the
                Kubelet creates routes for each node to allow the containers on that
                node to communicate with all other instances in the cluster.

                Finally, an entry is added to the project's global metadata indicating
                which CIDR range the cluster is using.
            cluster_id (str): Deprecated. The name of the cluster.
                This field has been deprecated and replaced by the parent field.
            parent (str): Required. The desired list of Google Compute Engine
                `zones <https://cloud.google.com/compute/docs/zones#available>`__ in
                which the cluster's nodes should be located. Changing the locations a
                cluster is in will result in nodes being either created or removed from
                the cluster, depending on whether locations are being added or removed.

                This list must always include the cluster's primary zone.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_node_pool" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_node_pool"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_node_pool,
                default_retry=self._method_configs["CreateNodePool"].retry,
                default_timeout=self._method_configs["CreateNodePool"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.CreateNodePoolRequest(
            node_pool=node_pool,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            parent=parent,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_node_pool"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_node_pool(
        self,
        project_id=None,
        zone=None,
        cluster_id=None,
        node_pool_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes a node pool from a cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> response = client.delete_node_pool()

        Args:
            project_id (str): javanano_as_lite
            zone (str): The name of a Google Compute Engine `machine
                type <https://cloud.google.com/compute/docs/machine-types>`__ (e.g.
                ``n1-standard-1``).

                If unspecified, the default machine type is ``n1-standard-1``.
            cluster_id (str): Deprecated. The name of the cluster.
                This field has been deprecated and replaced by the name field.
            node_pool_id (str): Deprecated. The name of the node pool to delete.
                This field has been deprecated and replaced by the name field.
            name (str): Required. A `cluster
                resource <https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters>`__
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_node_pool" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_node_pool"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_node_pool,
                default_retry=self._method_configs["DeleteNodePool"].retry,
                default_timeout=self._method_configs["DeleteNodePool"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.DeleteNodePoolRequest(
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            node_pool_id=node_pool_id,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["delete_node_pool"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def rollback_node_pool_upgrade(
        self,
        project_id=None,
        zone=None,
        cluster_id=None,
        node_pool_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Rolls back a previously Aborted or Failed NodePool upgrade.
        This makes no changes if the last upgrade successfully completed.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> response = client.rollback_node_pool_upgrade()

        Args:
            project_id (str): [Output only] The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/regions-zones/regions-zones#available>`__
                or
                `region <https://cloud.google.com/compute/docs/regions-zones/regions-zones#available>`__
                in which the cluster resides.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__ in
                which the cluster resides. This field has been deprecated and replaced
                by the name field.
            cluster_id (str): Deprecated. The name of the cluster to rollback.
                This field has been deprecated and replaced by the name field.
            node_pool_id (str): Deprecated. The name of the node pool to rollback.
                This field has been deprecated and replaced by the name field.
            name (str): The parent (project, location, cluster id) where the node pool will
                be created. Specified in the format
                ``projects/*/locations/*/clusters/*``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "rollback_node_pool_upgrade" not in self._inner_api_calls:
            self._inner_api_calls[
                "rollback_node_pool_upgrade"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.rollback_node_pool_upgrade,
                default_retry=self._method_configs["RollbackNodePoolUpgrade"].retry,
                default_timeout=self._method_configs["RollbackNodePoolUpgrade"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.RollbackNodePoolUpgradeRequest(
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            node_pool_id=node_pool_id,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["rollback_node_pool_upgrade"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def set_node_pool_management(
        self,
        management,
        project_id=None,
        zone=None,
        cluster_id=None,
        node_pool_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Sets the NodeManagement options for a node pool.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize `management`:
            >>> management = {}
            >>>
            >>> response = client.set_node_pool_management(management)

        Args:
            management (Union[dict, ~google.cloud.container_v1.types.NodeManagement]): Required. NodeManagement configuration for the node pool.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.NodeManagement`
            project_id (str): A custom subnetwork name to be used if ``create_subnetwork`` is
                true. If this field is empty, then an automatic name will be chosen for
                the new subnetwork.
            zone (str): Deprecated. The Google Developers Console `project ID or project
                number <https://support.google.com/cloud/answer/6158840>`__. This field
                has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to update.
                This field has been deprecated and replaced by the name field.
            node_pool_id (str): Deprecated. The name of the node pool to update.
                This field has been deprecated and replaced by the name field.
            name (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__ in
                which the cluster resides. This field has been deprecated and replaced
                by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "set_node_pool_management" not in self._inner_api_calls:
            self._inner_api_calls[
                "set_node_pool_management"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.set_node_pool_management,
                default_retry=self._method_configs["SetNodePoolManagement"].retry,
                default_timeout=self._method_configs["SetNodePoolManagement"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.SetNodePoolManagementRequest(
            management=management,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            node_pool_id=node_pool_id,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["set_node_pool_management"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def set_labels(
        self,
        resource_labels,
        label_fingerprint,
        project_id=None,
        zone=None,
        cluster_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Sets labels on a cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize `resource_labels`:
            >>> resource_labels = {}
            >>>
            >>> # TODO: Initialize `label_fingerprint`:
            >>> label_fingerprint = ''
            >>>
            >>> response = client.set_labels(resource_labels, label_fingerprint)

        Args:
            resource_labels (dict[str -> str]): Required. The labels to set for that cluster.
            label_fingerprint (str): Required. The fingerprint of the previous set of labels for this resource,
                used to detect conflicts. The fingerprint is initially generated by
                Kubernetes Engine and changes after every request to modify or update
                labels. You must always provide an up-to-date fingerprint hash when
                updating or changing labels. Make a <code>get()</code> request to the
                resource to get the latest fingerprint.
            project_id (str): Deprecated. The Google Developers Console `project ID or project
                number <https://support.google.com/cloud/answer/6158840>`__. This field
                has been deprecated and replaced by the name field.
            zone (str): [Output only] The IP address range of the Cloud TPUs in this
                cluster, in
                `CIDR <http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__
                notation (e.g. ``1.2.3.4/29``).
            cluster_id (str): Deprecated. The name of the cluster.
                This field has been deprecated and replaced by the name field.
            name (str): This field is deprecated, use services_ipv4_cidr_block.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "set_labels" not in self._inner_api_calls:
            self._inner_api_calls[
                "set_labels"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.set_labels,
                default_retry=self._method_configs["SetLabels"].retry,
                default_timeout=self._method_configs["SetLabels"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.SetLabelsRequest(
            resource_labels=resource_labels,
            label_fingerprint=label_fingerprint,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["set_labels"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def set_legacy_abac(
        self,
        enabled,
        project_id=None,
        zone=None,
        cluster_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Enables or disables the ABAC authorization mechanism on a cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize `enabled`:
            >>> enabled = False
            >>>
            >>> response = client.set_legacy_abac(enabled)

        Args:
            enabled (bool): Required. Whether ABAC authorization will be enabled in the cluster.
            project_id (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__ in
                which the cluster resides. This field has been deprecated and replaced
                by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__ in
                which the cluster resides. This field has been deprecated and replaced
                by the name field.
            cluster_id (str): Deprecated. The name of the cluster to update.
                This field has been deprecated and replaced by the name field.
            name (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__ in
                which the cluster resides. This field has been deprecated and replaced
                by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "set_legacy_abac" not in self._inner_api_calls:
            self._inner_api_calls[
                "set_legacy_abac"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.set_legacy_abac,
                default_retry=self._method_configs["SetLegacyAbac"].retry,
                default_timeout=self._method_configs["SetLegacyAbac"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.SetLegacyAbacRequest(
            enabled=enabled,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["set_legacy_abac"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def start_i_p_rotation(
        self,
        project_id=None,
        zone=None,
        cluster_id=None,
        name=None,
        rotate_credentials=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Starts master IP rotation.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> response = client.start_i_p_rotation()

        Args:
            project_id (str): Input and output type names. These are resolved in the same way as
                FieldDescriptorProto.type_name, but must refer to a message type.
            zone (str): javalite_serializable
            cluster_id (str): Deprecated. The name of the cluster.
                This field has been deprecated and replaced by the name field.
            name (str): The name of the secondary range to be used for the cluster CIDR
                block. The secondary range will be used for pod IP addresses. This must
                be an existing secondary range associated with the cluster subnetwork.

                This field is only applicable with use_ip_aliases is true and
                create_subnetwork is false.
            rotate_credentials (bool): Whether to rotate credentials during IP rotation.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "start_i_p_rotation" not in self._inner_api_calls:
            self._inner_api_calls[
                "start_i_p_rotation"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.start_i_p_rotation,
                default_retry=self._method_configs["StartIPRotation"].retry,
                default_timeout=self._method_configs["StartIPRotation"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.StartIPRotationRequest(
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            name=name,
            rotate_credentials=rotate_credentials,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["start_i_p_rotation"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def complete_i_p_rotation(
        self,
        project_id=None,
        zone=None,
        cluster_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Completes master IP rotation.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> response = client.complete_i_p_rotation()

        Args:
            project_id (str): The name of the secondary range to be used as for the services CIDR
                block. The secondary range will be used for service ClusterIPs. This
                must be an existing secondary range associated with the cluster
                subnetwork.

                This field is only applicable with use_ip_aliases is true and
                create_subnetwork is false.
            zone (str): Should this field be parsed lazily? Lazy applies only to
                message-type fields. It means that when the outer message is initially
                parsed, the inner message's contents will not be parsed but instead
                stored in encoded form. The inner message will actually be parsed when
                it is first accessed.

                This is only a hint. Implementations are free to choose whether to use
                eager or lazy parsing regardless of the value of this option. However,
                setting this option true suggests that the protocol author believes that
                using lazy parsing on this field is worth the additional bookkeeping
                overhead typically needed to implement it.

                This option does not affect the public interface of any generated code;
                all method signatures remain the same. Furthermore, thread-safety of the
                interface is not affected by this option; const methods remain safe to
                call from multiple threads concurrently, while non-const methods
                continue to require exclusive access.

                Note that implementations may choose not to check required fields within
                a lazy sub-message. That is, calling IsInitialized() on the outer
                message may return true even if the inner message has missing required
                fields. This is necessary because otherwise the inner message would have
                to be parsed in order to perform the check, defeating the purpose of
                lazy parsing. An implementation which chooses not to check required
                fields must be consistent about it. That is, for any particular
                sub-message, the implementation must either *always* check its required
                fields, or *never* check its required fields, regardless of whether or
                not the message has been parsed.
            cluster_id (str): Deprecated. The name of the cluster.
                This field has been deprecated and replaced by the name field.
            name (str): Deprecated. The Google Developers Console `project ID or project
                number <https://support.google.com/cloud/answer/6158840>`__. This field
                has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "complete_i_p_rotation" not in self._inner_api_calls:
            self._inner_api_calls[
                "complete_i_p_rotation"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.complete_i_p_rotation,
                default_retry=self._method_configs["CompleteIPRotation"].retry,
                default_timeout=self._method_configs["CompleteIPRotation"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.CompleteIPRotationRequest(
            project_id=project_id, zone=zone, cluster_id=cluster_id, name=name
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["complete_i_p_rotation"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def set_node_pool_size(
        self,
        node_count,
        project_id=None,
        zone=None,
        cluster_id=None,
        node_pool_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Sets the size for a specific node pool.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize `node_count`:
            >>> node_count = 0
            >>>
            >>> response = client.set_node_pool_size(node_count)

        Args:
            node_count (int): Required. The desired node count for the pool.
            project_id (str): [Output only] The time the cluster will be automatically deleted in
                `RFC3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ text format.
            zone (str): A human readable status message representing the reasons for cases
                where the caller cannot use the secondary ranges under the subnet. For
                example if the secondary_ip_ranges is empty due to a permission issue,
                an insufficient permission message will be given by status_message.
            cluster_id (str): Deprecated. The name of the cluster to update.
                This field has been deprecated and replaced by the name field.
            node_pool_id (str): Deprecated. The name of the node pool to update.
                This field has been deprecated and replaced by the name field.
            name (str): This field is deprecated, use cluster_ipv4_cidr_block.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "set_node_pool_size" not in self._inner_api_calls:
            self._inner_api_calls[
                "set_node_pool_size"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.set_node_pool_size,
                default_retry=self._method_configs["SetNodePoolSize"].retry,
                default_timeout=self._method_configs["SetNodePoolSize"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.SetNodePoolSizeRequest(
            node_count=node_count,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            node_pool_id=node_pool_id,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["set_node_pool_size"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def set_network_policy(
        self,
        network_policy,
        project_id=None,
        zone=None,
        cluster_id=None,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Enables or disables Network Policy for a cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize `network_policy`:
            >>> network_policy = {}
            >>>
            >>> response = client.set_network_policy(network_policy)

        Args:
            network_policy (Union[dict, ~google.cloud.container_v1.types.NetworkPolicy]): Required. Configuration options for the NetworkPolicy feature.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.NetworkPolicy`
            project_id (str): The IP address range for the cluster pod IPs. If this field is set,
                then ``cluster.cluster_ipv4_cidr`` must be left blank.

                This field is only applicable when ``use_ip_aliases`` is true.

                Set to blank to have a range chosen with the default size.

                Set to /netmask (e.g. ``/14``) to have a range chosen with a specific
                netmask.

                Set to a
                `CIDR <http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__
                notation (e.g. ``10.96.0.0/14``) from the RFC-1918 private networks
                (e.g. ``10.0.0.0/8``, ``172.16.0.0/12``, ``192.168.0.0/16``) to pick a
                specific range to use.
            zone (str): Time within the maintenance window to start the maintenance
                operations. Time format should be in
                `RFC3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ format "HH:MM", where
                HH : [00-23] and MM : [00-59] GMT.
            cluster_id (str): Deprecated. The name of the cluster.
                This field has been deprecated and replaced by the name field.
            name (str): The name (project, location, cluster, node pool id) of the node pool
                to set management properties. Specified in the format
                ``projects/*/locations/*/clusters/*/nodePools/*``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "set_network_policy" not in self._inner_api_calls:
            self._inner_api_calls[
                "set_network_policy"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.set_network_policy,
                default_retry=self._method_configs["SetNetworkPolicy"].retry,
                default_timeout=self._method_configs["SetNetworkPolicy"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.SetNetworkPolicyRequest(
            network_policy=network_policy,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["set_network_policy"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def set_maintenance_policy(
        self,
        project_id,
        zone,
        cluster_id,
        maintenance_policy,
        name=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Sets the maintenance policy for a cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize `project_id`:
            >>> project_id = ''
            >>>
            >>> # TODO: Initialize `zone`:
            >>> zone = ''
            >>>
            >>> # TODO: Initialize `cluster_id`:
            >>> cluster_id = ''
            >>>
            >>> # TODO: Initialize `maintenance_policy`:
            >>> maintenance_policy = {}
            >>>
            >>> response = client.set_maintenance_policy(project_id, zone, cluster_id, maintenance_policy)

        Args:
            project_id (str): The monitoring service the cluster should use to write metrics.
                Currently available options:

                -  ``monitoring.googleapis.com`` - the Google Cloud Monitoring service.
                -  ``none`` - no metrics will be exported from the cluster.
                -  if left as an empty string, ``monitoring.googleapis.com`` will be
                   used.
            zone (str): The IP address range of the instance IPs in this cluster.

                This is applicable only if ``create_subnetwork`` is true.

                Set to blank to have a range chosen with the default size.

                Set to /netmask (e.g. ``/14``) to have a range chosen with a specific
                netmask.

                Set to a
                `CIDR <http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__
                notation (e.g. ``10.96.0.0/14``) from the RFC-1918 private networks
                (e.g. ``10.0.0.0/8``, ``172.16.0.0/12``, ``192.168.0.0/16``) to pick a
                specific range to use.
            cluster_id (str): Required. The name of the cluster to update.
            maintenance_policy (Union[dict, ~google.cloud.container_v1.types.MaintenancePolicy]): Required. The maintenance policy to be set for the cluster. An empty field
                clears the existing maintenance policy.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.MaintenancePolicy`
            name (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`__ in
                which the cluster resides. This field has been deprecated and replaced
                by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "set_maintenance_policy" not in self._inner_api_calls:
            self._inner_api_calls[
                "set_maintenance_policy"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.set_maintenance_policy,
                default_retry=self._method_configs["SetMaintenancePolicy"].retry,
                default_timeout=self._method_configs["SetMaintenancePolicy"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.SetMaintenancePolicyRequest(
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            maintenance_policy=maintenance_policy,
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["set_maintenance_policy"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_usable_subnetworks(
        self,
        parent=None,
        filter_=None,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists subnetworks that are usable for creating clusters in a project.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_usable_subnetworks():
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_usable_subnetworks().pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): The accelerator type resource name. List of supported accelerators
                `here <https://cloud.google.com/compute/docs/gpus>`__
            filter_ (str): The desired image type for the node pool. NOTE: Set the
                "desired_node_pool" field as well.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.container_v1.types.UsableSubnetwork` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_usable_subnetworks" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_usable_subnetworks"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_usable_subnetworks,
                default_retry=self._method_configs["ListUsableSubnetworks"].retry,
                default_timeout=self._method_configs["ListUsableSubnetworks"].timeout,
                client_info=self._client_info,
            )

        request = cluster_service_pb2.ListUsableSubnetworksRequest(
            parent=parent, filter=filter_, page_size=page_size
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_usable_subnetworks"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="subnetworks",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator
