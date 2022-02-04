# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for SetNetworkPolicy
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-container


# [START container_generated_container_v1beta1_ClusterManager_SetNetworkPolicy_async]
from google.cloud import container_v1beta1


async def sample_set_network_policy():
    # Create a client
    client = container_v1beta1.ClusterManagerAsyncClient()

    # Initialize request argument(s)
    request = container_v1beta1.SetNetworkPolicyRequest(
        project_id="project_id_value",
        zone="zone_value",
        cluster_id="cluster_id_value",
    )

    # Make the request
    response = await client.set_network_policy(request=request)

    # Handle response
    print(response)

# [END container_generated_container_v1beta1_ClusterManager_SetNetworkPolicy_async]
