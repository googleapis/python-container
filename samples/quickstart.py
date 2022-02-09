# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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

# [START gke_list_cluster]
import argparse
from google.cloud import container_v1


def list_clusters(client: container_v1.ClusterManagerClient, project_id: str, location: str) -> None:
    """List all the GKE clusters in the given GCP Project and Zone"""

    # Create a fully qualified location identifier of form `projects/{project_id}/location/{zone}'.
    clusterLocation = client.common_location_path(project_id, location)
    # Create the request object with the location identifier.
    request = { 'parent': clusterLocation }
    listResponse = client.list_clusters(request)

    print(f"There were {len(listResponse.clusters)} clusters in {location} for project {project_id}.")
    for cluster in listResponse.clusters:
        print(f"- {cluster.name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("project_id", help="Google Cloud project ID")
    parser.add_argument("zone", help="GKE Cluster zone")
    args = parser.parse_args()

    # Initialize the Cluster management client.
    gcp_client = container_v1.ClusterManagerClient()
    list_clusters(gcp_client, args.project_id, args.zone)
# [END gke_list_cluster]