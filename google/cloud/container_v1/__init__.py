# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
from google.cloud.container_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.cluster_manager import ClusterManagerAsyncClient, ClusterManagerClient
from .types.cluster_service import (
    AcceleratorConfig,
    AdditionalPodRangesConfig,
    AddonsConfig,
    AdvancedMachineFeatures,
    AuthenticatorGroupsConfig,
    Autopilot,
    AutopilotCompatibilityIssue,
    AutoprovisioningNodePoolDefaults,
    AutoUpgradeOptions,
    BestEffortProvisioning,
    BinaryAuthorization,
    BlueGreenSettings,
    CancelOperationRequest,
    CheckAutopilotCompatibilityRequest,
    CheckAutopilotCompatibilityResponse,
    ClientCertificateConfig,
    CloudRunConfig,
    Cluster,
    ClusterAutoscaling,
    ClusterUpdate,
    CompleteIPRotationRequest,
    CompleteNodePoolUpgradeRequest,
    ConfidentialNodes,
    ConfigConnectorConfig,
    CostManagementConfig,
    CreateClusterRequest,
    CreateNodePoolRequest,
    DailyMaintenanceWindow,
    DatabaseEncryption,
    DatapathProvider,
    DefaultSnatStatus,
    DeleteClusterRequest,
    DeleteNodePoolRequest,
    DnsCacheConfig,
    DNSConfig,
    EphemeralStorageLocalSsdConfig,
    FastSocket,
    Fleet,
    GatewayAPIConfig,
    GcePersistentDiskCsiDriverConfig,
    GcfsConfig,
    GcpFilestoreCsiDriverConfig,
    GetClusterRequest,
    GetJSONWebKeysRequest,
    GetJSONWebKeysResponse,
    GetNodePoolRequest,
    GetOpenIDConfigRequest,
    GetOpenIDConfigResponse,
    GetOperationRequest,
    GetServerConfigRequest,
    GkeBackupAgentConfig,
    GPUDriverInstallationConfig,
    GPUSharingConfig,
    HorizontalPodAutoscaling,
    HttpLoadBalancing,
    IdentityServiceConfig,
    ILBSubsettingConfig,
    IntraNodeVisibilityConfig,
    IPAllocationPolicy,
    IPv6AccessType,
    Jwk,
    K8sBetaAPIConfig,
    KubernetesDashboard,
    LegacyAbac,
    LinuxNodeConfig,
    ListClustersRequest,
    ListClustersResponse,
    ListNodePoolsRequest,
    ListNodePoolsResponse,
    ListOperationsRequest,
    ListOperationsResponse,
    ListUsableSubnetworksRequest,
    ListUsableSubnetworksResponse,
    LocalNvmeSsdBlockConfig,
    LoggingComponentConfig,
    LoggingConfig,
    LoggingVariantConfig,
    MaintenanceExclusionOptions,
    MaintenancePolicy,
    MaintenanceWindow,
    ManagedPrometheusConfig,
    MasterAuth,
    MasterAuthorizedNetworksConfig,
    MaxPodsConstraint,
    MeshCertificates,
    MonitoringComponentConfig,
    MonitoringConfig,
    NetworkConfig,
    NetworkPolicy,
    NetworkPolicyConfig,
    NetworkTags,
    NodeConfig,
    NodeConfigDefaults,
    NodeKubeletConfig,
    NodeLabels,
    NodeManagement,
    NodeNetworkConfig,
    NodePool,
    NodePoolAutoConfig,
    NodePoolAutoscaling,
    NodePoolDefaults,
    NodePoolLoggingConfig,
    NodePoolUpdateStrategy,
    NodeTaint,
    NodeTaints,
    NotificationConfig,
    Operation,
    OperationProgress,
    PodCIDROverprovisionConfig,
    PrivateClusterConfig,
    PrivateClusterMasterGlobalAccessConfig,
    PrivateIPv6GoogleAccess,
    RecurringTimeWindow,
    ReleaseChannel,
    ReservationAffinity,
    ResourceLabels,
    ResourceLimit,
    ResourceUsageExportConfig,
    RollbackNodePoolUpgradeRequest,
    SandboxConfig,
    SecurityBulletinEvent,
    SecurityPostureConfig,
    ServerConfig,
    ServiceExternalIPsConfig,
    SetAddonsConfigRequest,
    SetLabelsRequest,
    SetLegacyAbacRequest,
    SetLocationsRequest,
    SetLoggingServiceRequest,
    SetMaintenancePolicyRequest,
    SetMasterAuthRequest,
    SetMonitoringServiceRequest,
    SetNetworkPolicyRequest,
    SetNodePoolAutoscalingRequest,
    SetNodePoolManagementRequest,
    SetNodePoolSizeRequest,
    ShieldedInstanceConfig,
    ShieldedNodes,
    SoleTenantConfig,
    StackType,
    StartIPRotationRequest,
    StatusCondition,
    TimeWindow,
    UpdateClusterRequest,
    UpdateMasterRequest,
    UpdateNodePoolRequest,
    UpgradeAvailableEvent,
    UpgradeEvent,
    UpgradeResourceType,
    UsableSubnetwork,
    UsableSubnetworkSecondaryRange,
    VerticalPodAutoscaling,
    VirtualNIC,
    WindowsNodeConfig,
    WorkloadIdentityConfig,
    WorkloadMetadataConfig,
    WorkloadPolicyConfig,
)

__all__ = (
    "ClusterManagerAsyncClient",
    "AcceleratorConfig",
    "AdditionalPodRangesConfig",
    "AddonsConfig",
    "AdvancedMachineFeatures",
    "AuthenticatorGroupsConfig",
    "AutoUpgradeOptions",
    "Autopilot",
    "AutopilotCompatibilityIssue",
    "AutoprovisioningNodePoolDefaults",
    "BestEffortProvisioning",
    "BinaryAuthorization",
    "BlueGreenSettings",
    "CancelOperationRequest",
    "CheckAutopilotCompatibilityRequest",
    "CheckAutopilotCompatibilityResponse",
    "ClientCertificateConfig",
    "CloudRunConfig",
    "Cluster",
    "ClusterAutoscaling",
    "ClusterManagerClient",
    "ClusterUpdate",
    "CompleteIPRotationRequest",
    "CompleteNodePoolUpgradeRequest",
    "ConfidentialNodes",
    "ConfigConnectorConfig",
    "CostManagementConfig",
    "CreateClusterRequest",
    "CreateNodePoolRequest",
    "DNSConfig",
    "DailyMaintenanceWindow",
    "DatabaseEncryption",
    "DatapathProvider",
    "DefaultSnatStatus",
    "DeleteClusterRequest",
    "DeleteNodePoolRequest",
    "DnsCacheConfig",
    "EphemeralStorageLocalSsdConfig",
    "FastSocket",
    "Fleet",
    "GPUDriverInstallationConfig",
    "GPUSharingConfig",
    "GatewayAPIConfig",
    "GcePersistentDiskCsiDriverConfig",
    "GcfsConfig",
    "GcpFilestoreCsiDriverConfig",
    "GetClusterRequest",
    "GetJSONWebKeysRequest",
    "GetJSONWebKeysResponse",
    "GetNodePoolRequest",
    "GetOpenIDConfigRequest",
    "GetOpenIDConfigResponse",
    "GetOperationRequest",
    "GetServerConfigRequest",
    "GkeBackupAgentConfig",
    "HorizontalPodAutoscaling",
    "HttpLoadBalancing",
    "ILBSubsettingConfig",
    "IPAllocationPolicy",
    "IPv6AccessType",
    "IdentityServiceConfig",
    "IntraNodeVisibilityConfig",
    "Jwk",
    "K8sBetaAPIConfig",
    "KubernetesDashboard",
    "LegacyAbac",
    "LinuxNodeConfig",
    "ListClustersRequest",
    "ListClustersResponse",
    "ListNodePoolsRequest",
    "ListNodePoolsResponse",
    "ListOperationsRequest",
    "ListOperationsResponse",
    "ListUsableSubnetworksRequest",
    "ListUsableSubnetworksResponse",
    "LocalNvmeSsdBlockConfig",
    "LoggingComponentConfig",
    "LoggingConfig",
    "LoggingVariantConfig",
    "MaintenanceExclusionOptions",
    "MaintenancePolicy",
    "MaintenanceWindow",
    "ManagedPrometheusConfig",
    "MasterAuth",
    "MasterAuthorizedNetworksConfig",
    "MaxPodsConstraint",
    "MeshCertificates",
    "MonitoringComponentConfig",
    "MonitoringConfig",
    "NetworkConfig",
    "NetworkPolicy",
    "NetworkPolicyConfig",
    "NetworkTags",
    "NodeConfig",
    "NodeConfigDefaults",
    "NodeKubeletConfig",
    "NodeLabels",
    "NodeManagement",
    "NodeNetworkConfig",
    "NodePool",
    "NodePoolAutoConfig",
    "NodePoolAutoscaling",
    "NodePoolDefaults",
    "NodePoolLoggingConfig",
    "NodePoolUpdateStrategy",
    "NodeTaint",
    "NodeTaints",
    "NotificationConfig",
    "Operation",
    "OperationProgress",
    "PodCIDROverprovisionConfig",
    "PrivateClusterConfig",
    "PrivateClusterMasterGlobalAccessConfig",
    "PrivateIPv6GoogleAccess",
    "RecurringTimeWindow",
    "ReleaseChannel",
    "ReservationAffinity",
    "ResourceLabels",
    "ResourceLimit",
    "ResourceUsageExportConfig",
    "RollbackNodePoolUpgradeRequest",
    "SandboxConfig",
    "SecurityBulletinEvent",
    "SecurityPostureConfig",
    "ServerConfig",
    "ServiceExternalIPsConfig",
    "SetAddonsConfigRequest",
    "SetLabelsRequest",
    "SetLegacyAbacRequest",
    "SetLocationsRequest",
    "SetLoggingServiceRequest",
    "SetMaintenancePolicyRequest",
    "SetMasterAuthRequest",
    "SetMonitoringServiceRequest",
    "SetNetworkPolicyRequest",
    "SetNodePoolAutoscalingRequest",
    "SetNodePoolManagementRequest",
    "SetNodePoolSizeRequest",
    "ShieldedInstanceConfig",
    "ShieldedNodes",
    "SoleTenantConfig",
    "StackType",
    "StartIPRotationRequest",
    "StatusCondition",
    "TimeWindow",
    "UpdateClusterRequest",
    "UpdateMasterRequest",
    "UpdateNodePoolRequest",
    "UpgradeAvailableEvent",
    "UpgradeEvent",
    "UpgradeResourceType",
    "UsableSubnetwork",
    "UsableSubnetworkSecondaryRange",
    "VerticalPodAutoscaling",
    "VirtualNIC",
    "WindowsNodeConfig",
    "WorkloadIdentityConfig",
    "WorkloadMetadataConfig",
    "WorkloadPolicyConfig",
)
