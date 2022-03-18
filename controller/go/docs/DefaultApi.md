# {{classname}}

All URIs are relative to *https://server.nextensio.net:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddAdminGroup**](DefaultApi.md#AddAdminGroup) | **Post** /tenant/{tenant-id}/add/admgroups/{group} | add an admin groups to a tenant
[**AddAttrSet**](DefaultApi.md#AddAttrSet) | **Post** /tenant/{tenant-id}/add/attrset | define a new attribute
[**AddBundle**](DefaultApi.md#AddBundle) | **Post** /tenant/{tenant-id}/add/bundle | Add bundle.
[**AddCerts**](DefaultApi.md#AddCerts) | **Post** /global/add/cert | add certificate
[**AddClientid**](DefaultApi.md#AddClientid) | **Post** /global/add/clientid | Add a new clientID for a new nextensio App
[**AddClusterHandler**](DefaultApi.md#AddClusterHandler) | **Post** /tenant/{tenant-id}/add/tenantcluster | add gateway cluster to tenant
[**AddGateway**](DefaultApi.md#AddGateway) | **Post** /global/add/gateway | add a gateway
[**AddIdpHandler**](DefaultApi.md#AddIdpHandler) | **Post** /tenant/{tenant-id}/add/idp | add identity provider to tenant
[**AddKeepAlive**](DefaultApi.md#AddKeepAlive) | **Post** /global/add/keepaliverequest | Send keepalive from device to controller
[**AddMgdTenant**](DefaultApi.md#AddMgdTenant) | **Post** /tenant/{tenant-id}/add/tenantmsp/{mgdtenant} | assign a managed tenant to a MSP tenant
[**AddPolicyHandler**](DefaultApi.md#AddPolicyHandler) | **Post** /tenant/{tenant-id}/add/policy | add policy
[**AddStatsRuleHandler**](DefaultApi.md#AddStatsRuleHandler) | **Post** /tenant/{tenant-id}/add/statsrule | add stats rule
[**AddTenant**](DefaultApi.md#AddTenant) | **Post** /global/add/tenant | add basic info for a tenant
[**AddTraceReq**](DefaultApi.md#AddTraceReq) | **Post** /tenant/{tenant-id}/add/tracereq | add trace request
[**AddTraceRuleHandler**](DefaultApi.md#AddTraceRuleHandler) | **Post** /tenant/{tenant-id}/add/tracereqrule | add trace rule
[**AddUser**](DefaultApi.md#AddUser) | **Post** /tenant/{tenant-id}/add/user | add user
[**AddUserAttr**](DefaultApi.md#AddUserAttr) | **Post** /tenant/{tenant-id}/add/userattr/single/{userid} | add tenant user attrs
[**AddUserAttrMultiple**](DefaultApi.md#AddUserAttrMultiple) | **Post** /tenant/{tenant-id}/add/userattr/multiple | add tenant user attrs for multiple users
[**AddUserKey**](DefaultApi.md#AddUserKey) | **Post** /tenant/{tenant-id}/add/userkey | add API key
[**AddbundleRuleHandler**](DefaultApi.md#AddbundleRuleHandler) | **Post** /tenant/{tenant-id}/add/bundlerule | add bundle rule
[**AddhostRuleHandler**](DefaultApi.md#AddhostRuleHandler) | **Post** /tenant/{tenant-id}/add/hostrule | add host rule
[**DelAdminGroup**](DefaultApi.md#DelAdminGroup) | **Get** /tenant/{tenant-id}/del/admgroups/{group} | delete an admin group from a tenant
[**DelAttrSet**](DefaultApi.md#DelAttrSet) | **Post** /tenant/{tenant-id}/del/attrset | delete an existing attribute
[**DelBundle**](DefaultApi.md#DelBundle) | **Get** /tenant/{tenant-id}/del/bundle/{bid} | del bundle from the tenant
[**DelBundleRule**](DefaultApi.md#DelBundleRule) | **Get** /tenant/{tenant-id}/del/bundlerule/{bid}/{rid}/{group} | delete bundle rule
[**DelCert**](DefaultApi.md#DelCert) | **Get** /global/del/cert/{certid} | delete a certificate
[**DelGateway**](DefaultApi.md#DelGateway) | **Get** /global/del/gateway/{name} | delete an unused nextensio gateway
[**DelHostAttr**](DefaultApi.md#DelHostAttr) | **Get** /tenant/{tenant-id}/del/hostattr/{host} | delete host attrs
[**DelHostRule**](DefaultApi.md#DelHostRule) | **Get** /tenant/{tenant-id}/del/hostrule/{host}/{rid}/{group} | delete host rule
[**DelIdpHandler**](DefaultApi.md#DelIdpHandler) | **Get** /tenant/{tenant-id}/del/idp/{idp} | delete an IDP
[**DelMgdTenant**](DefaultApi.md#DelMgdTenant) | **Get** /tenant/{tenant-id}/del/tenantmsp/{mgdtenant} | remove a managed tenant from a MSP tenant
[**DelOnboardLogs**](DefaultApi.md#DelOnboardLogs) | **Get** /tenant/{tenant-id}/del/onboardlog/{userid} | delete onboard logs for a particluar user
[**DelPolicy**](DefaultApi.md#DelPolicy) | **Get** /tenant/{tenant-id}/del/policy/{policyid} | delete policy
[**DelStatsRule**](DefaultApi.md#DelStatsRule) | **Get** /tenant/{tenant-id}/del/statsrule/{group} | delete stats rule
[**DelTenant**](DefaultApi.md#DelTenant) | **Get** /global/del/tenant/{tenant-id} | delete a tenant
[**DelTenantCluster**](DefaultApi.md#DelTenantCluster) | **Get** /tenant/{tenant-id}/del/tenantcluster/{gateway} | delete host attrs
[**DelTraceReq**](DefaultApi.md#DelTraceReq) | **Get** /tenant/{tenant-id}/del/tracereqrule/{rid}/{group} | delete trace request
[**DelUser**](DefaultApi.md#DelUser) | **Get** /tenant/{tenant-id}/del/user/{userid} | delete a user
[**DelUserKey**](DefaultApi.md#DelUserKey) | **Get** /tenant/{tenant-id}/del/userkey/{key} | delete API key
[**GetAdminForGroups**](DefaultApi.md#GetAdminForGroups) | **Get** /tenant/{tenant-id}/get/groupadms/{group} | get all admins of a tenant group
[**GetAdminGroups**](DefaultApi.md#GetAdminGroups) | **Get** /tenant/{tenant-id}/get/alladmgroups | get all admin groups of a tenant
[**GetAllBundleAttr**](DefaultApi.md#GetAllBundleAttr) | **Get** /tenant/{tenant-id}/get/allbundleattr | get all bundle attrs
[**GetAllBundleRules**](DefaultApi.md#GetAllBundleRules) | **Get** /tenant/{tenant-id}/get/bundlerules/{bid} | get all bundle rules in a tenant
[**GetAllBundles**](DefaultApi.md#GetAllBundles) | **Get** /tenant/{tenant-id}/get/allbundles | get all bundles
[**GetAllCerts**](DefaultApi.md#GetAllCerts) | **Get** /global/get/allcerts | get all certificates
[**GetAllHostAttr**](DefaultApi.md#GetAllHostAttr) | **Get** /tenant/{tenant-id}/get/allhostattr | get all host attrs
[**GetAllHostRules**](DefaultApi.md#GetAllHostRules) | **Get** /tenant/{tenant-id}/get/hostrules/{host} | get all host rules in a tenant
[**GetAllIdps**](DefaultApi.md#GetAllIdps) | **Get** /tenant/{tenant-id}/get/allidps | get all IDPs for a tenant
[**GetAllPolicies**](DefaultApi.md#GetAllPolicies) | **Get** /tenant/{tenant-id}/get/allpolicies | get all policies in a tenant
[**GetAllStatsRules**](DefaultApi.md#GetAllStatsRules) | **Get** /tenant/{tenant-id}/get/statsrule | get all stats rules in a tenant
[**GetAllTenantCluster**](DefaultApi.md#GetAllTenantCluster) | **Get** /tenant/{tenant-id}/get/alltenantclusters | get all clusters assigned for a tenant
[**GetAllTraceReqs**](DefaultApi.md#GetAllTraceReqs) | **Get** /tenant/{tenant-id}/get/alltracereq | get info about all trace requests
[**GetAllTraceRules**](DefaultApi.md#GetAllTraceRules) | **Get** /tenant/{tenant-id}/get/tracereqrules/{traceid} | get all trace rules in a tenant
[**GetAllUserAttr**](DefaultApi.md#GetAllUserAttr) | **Get** /tenant/{tenant-id}/get/alluserattr | get all user attrs
[**GetAllUsers**](DefaultApi.md#GetAllUsers) | **Get** /tenant/{tenant-id}/get/allusers | get all the users of a tenant
[**GetAttrCollectionHdr**](DefaultApi.md#GetAttrCollectionHdr) | **Get** /tenant/{tenant-id}/get/attrhdr/{type} | get the header of an attributes collection for a tenant
[**GetBundle**](DefaultApi.md#GetBundle) | **Get** /tenant/{tenant-id}/get/bundle/{bid} | get bundle info of a tenant
[**GetBundleAttr**](DefaultApi.md#GetBundleAttr) | **Get** /tenant/{tenant-id}/get/bundleattr/{bid} | get bundle attrs
[**GetBundleStatus**](DefaultApi.md#GetBundleStatus) | **Get** /tenant/{tenant-id}/get/bundlestatus/{bid} | get the status of every instance of a specific AppGroup extender for a tenant
[**GetCert**](DefaultApi.md#GetCert) | **Get** /global/get/cert/{certid} | get a certificate
[**GetClientId**](DefaultApi.md#GetClientId) | **Get** /noauth/clientid/{key} | get the clientid providing the proper key/password
[**GetGateways**](DefaultApi.md#GetGateways) | **Get** /global/get/allgateways | lists all gateways
[**GetHostAttr**](DefaultApi.md#GetHostAttr) | **Get** /tenant/{tenant-id}/get/hostattr/{host} | get host attrs
[**GetMgdTenant**](DefaultApi.md#GetMgdTenant) | **Get** /tenant/{tenant-id}/get/mgdtenants | get all tenant
[**GetPolicy**](DefaultApi.md#GetPolicy) | **Get** /tenant/{tenant-id}/get/policy/{policyid} | get policy given the policyid
[**GetTenant**](DefaultApi.md#GetTenant) | **Get** /tenant/{tenant-id}/get/tenant | get a tenant
[**GetTenantCluster**](DefaultApi.md#GetTenantCluster) | **Get** /tenant/{tenant-id}/get/tenantcluster/{gateway} | get the  gateway information (nextensio internal) for a gateway assined to a tenant
[**GetTenantGateways**](DefaultApi.md#GetTenantGateways) | **Get** /tenant/{tenant-id}/get/allgateways | lists all gateways allocated for a tenant
[**GetTenants**](DefaultApi.md#GetTenants) | **Get** /global/get/alltenants | get all tenant
[**GetTraceReq**](DefaultApi.md#GetTraceReq) | **Get** /tenant/{tenant-id}/get/tracereq/{traceid} | get info about a trace request
[**GetTraceRequestsHdr**](DefaultApi.md#GetTraceRequestsHdr) | **Get** /tenant/{tenant-id}/get/tracereqhdr | get the header of a trace requests collection for a tenant
[**GetUser**](DefaultApi.md#GetUser) | **Get** /tenant/{tenant-id}/get/user/{userid} | get a user
[**GetUserAdminRole**](DefaultApi.md#GetUserAdminRole) | **Get** /tenant/{tenant-id}/get/user/adminrole/{userid} | get the admin role of a user
[**GetUserAttr**](DefaultApi.md#GetUserAttr) | **Get** /tenant/{tenant-id}/get/userattr/{user-id} | get user attrs
[**GetUserKeys**](DefaultApi.md#GetUserKeys) | **Get** /tenant/{tenant-id}/get/alluserkeys | get all the API keys in the tenant
[**GetUserOnboardLog**](DefaultApi.md#GetUserOnboardLog) | **Get** /tenant/{tenant-id}/get/onboardlog/{userid} | get a user&#x27;s onboarding info
[**GetUserStatus**](DefaultApi.md#GetUserStatus) | **Get** /tenant/{tenant-id}/get/userstatus/{userid} | get details about user devices and their status
[**ModifyTenant**](DefaultApi.md#ModifyTenant) | **Post** /tenant/{tenant-id}/add/tenant | add or modify a tenant
[**Onboard**](DefaultApi.md#Onboard) | **Get** /global/get/onboard | onboard a nextensio extender
[**Signup**](DefaultApi.md#Signup) | **Post** /noauth/signup | allows a user to signup
[**UpdTenantType**](DefaultApi.md#UpdTenantType) | **Post** /tenant/{tenant-id}/add/tenanttype/{type} | change the type of a tenant
[**UpdUserRole**](DefaultApi.md#UpdUserRole) | **Post** /tenant/{tenant-id}/add/user/adminrole/{userid}/{role} | assign a new role for a user

# **AddAdminGroup**
> PostResponse AddAdminGroup(ctx, xNextensioGroup, tenantId, group)
add an admin groups to a tenant

allows an user to add an admin groups to a tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **group** | **string**| provide group ID | 

### Return type

[**PostResponse**](postResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddAttrSet**
> PostResponse AddAttrSet(ctx, body, xNextensioGroup, tenantId)
define a new attribute

allows any admin to add a new attribute. The attribute can be for a user, an App, or an AppGroup.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**AttrSetStruct**](AttrSetStruct.md)| provide details of attribute to be added | 
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

[**PostResponse**](postResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddBundle**
> AddBundle(ctx, body, xNextensioGroup, tenantId)
Add bundle.

Add bundle to the specified tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**BundleStruct**](BundleStruct.md)| provide tenant info | 
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provie tenant ID | 

### Return type

 (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddCerts**
> PostResponse AddCerts(ctx, body, xNextensioGroup)
add certificate

allows a user to add a Nextensio Certificate

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**CertStruct**](CertStruct.md)| provide info about certificate | 
  **xNextensioGroup** | **string**|  | 

### Return type

[**PostResponse**](postResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddClientid**
> PostResponse AddClientid(ctx, body, xNextensioGroup)
Add a new clientID for a new nextensio App

Add new clientID for new nextensio App

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**AddClientId**](AddClientId.md)| provide details of attribute to be added | 
  **xNextensioGroup** | **string**|  | 

### Return type

[**PostResponse**](postResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddClusterHandler**
> string AddClusterHandler(ctx, xNextensioGroup, tenantId, optional)
add gateway cluster to tenant

add gateway cluster to tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
 **optional** | ***DefaultApiAddClusterHandlerOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a DefaultApiAddClusterHandlerOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**optional.Interface of TenantCluster**](TenantCluster.md)|  | 

### Return type

**string**

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddGateway**
> PostResponse AddGateway(ctx, body, xNextensioGroup)
add a gateway

allows a user to add a new gateway or update an existing one

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**GatewayStruct**](GatewayStruct.md)| provide info about gateway | 
  **xNextensioGroup** | **string**|  | 

### Return type

[**PostResponse**](postResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddIdpHandler**
> string AddIdpHandler(ctx, xNextensioGroup, tenantId, optional)
add identity provider to tenant

add identity provider to tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
 **optional** | ***DefaultApiAddIdpHandlerOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a DefaultApiAddIdpHandlerOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**optional.Interface of AddIdp**](AddIdp.md)|  | 

### Return type

**string**

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddKeepAlive**
> AddKeepAlive(ctx, body, xNextensioGroup)
Send keepalive from device to controller

Send keepalive from user device to nextensio controller

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**KeepaliveReq**](KeepaliveReq.md)| provide details of attribute to be added | 
  **xNextensioGroup** | **string**|  | 

### Return type

 (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddMgdTenant**
> PostResponse AddMgdTenant(ctx, xNextensioGroup, tenantId, mgdtenant)
assign a managed tenant to a MSP tenant

allows a superadmin to assign a managed tenant to a MSP tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **mgdtenant** | **string**| provide ID of a managed tenant | 

### Return type

[**PostResponse**](postResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddPolicyHandler**
> AddPolicyHandler(ctx, xNextensioGroup, tenantId, optional)
add policy

add policy

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
 **optional** | ***DefaultApiAddPolicyHandlerOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a DefaultApiAddPolicyHandlerOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**optional.Interface of AddPolicy**](AddPolicy.md)|  | 

### Return type

 (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddStatsRuleHandler**
> AddStatsRuleHandler(ctx, xNextensioGroup, tenantId, optional)
add stats rule

add stats rule

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
 **optional** | ***DefaultApiAddStatsRuleHandlerOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a DefaultApiAddStatsRuleHandlerOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**optional.Interface of StatsRule**](StatsRule.md)|  | 

### Return type

 (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddTenant**
> PostResponse AddTenant(ctx, body, xNextensioGroup)
add basic info for a tenant

allows a superuser or an MSP to add a new tenant or update an existing one

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**TenantUpdate**](TenantUpdate.md)| provide info about tenant | 
  **xNextensioGroup** | **string**|  | 

### Return type

[**PostResponse**](postResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddTraceReq**
> string AddTraceReq(ctx, body, xNextensioGroup, tenantId)
add trace request

add trace request

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**map[string]string**](map.md)| need &quot;traceid&quot; as a mandatory key | 
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

**string**

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddTraceRuleHandler**
> AddTraceRuleHandler(ctx, xNextensioGroup, tenantId, optional)
add trace rule

add trace rule

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
 **optional** | ***DefaultApiAddTraceRuleHandlerOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a DefaultApiAddTraceRuleHandlerOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**optional.Interface of TraceRule**](TraceRule.md)|  | 

### Return type

 (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddUser**
> PostResponse AddUser(ctx, body, xNextensioGroup, tenantId)
add user

allows an admin to add a user to the specified tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**UserAdd**](UserAdd.md)| provide info about user | 
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

[**PostResponse**](postResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddUserAttr**
> string AddUserAttr(ctx, body, xNextensioGroup, tenantId, userid)
add tenant user attrs

Add attributes to the user of a tenant.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**map[string]string**](map.md)| provide user attributes to be added/updated | 
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **userid** | **string**| provide User ID | 

### Return type

**string**

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddUserAttrMultiple**
> string AddUserAttrMultiple(ctx, body, xNextensioGroup, tenantId)
add tenant user attrs for multiple users

add tenant user attrs for multiple users

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**[]interface{}**](interface{}.md)| provide user attributes to be added/updated | 
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

**string**

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddUserKey**
> UserKeyResponse AddUserKey(ctx, xNextensioGroup, tenantId, optional)
add API key

add API key

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
 **optional** | ***DefaultApiAddUserKeyOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a DefaultApiAddUserKeyOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**optional.Interface of UserKey**](UserKey.md)|  | 

### Return type

[**UserKeyResponse**](userKeyResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddbundleRuleHandler**
> AddbundleRuleHandler(ctx, xNextensioGroup, tenantId, optional)
add bundle rule

add bundle rule

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
 **optional** | ***DefaultApiAddbundleRuleHandlerOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a DefaultApiAddbundleRuleHandlerOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**optional.Interface of BundleRule**](BundleRule.md)|  | 

### Return type

 (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **AddhostRuleHandler**
> AddhostRuleHandler(ctx, xNextensioGroup, tenantId, optional)
add host rule

add host rule

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
 **optional** | ***DefaultApiAddhostRuleHandlerOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a DefaultApiAddhostRuleHandlerOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**optional.Interface of HostRule**](HostRule.md)|  | 

### Return type

 (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelAdminGroup**
> PostResponse DelAdminGroup(ctx, xNextensioGroup, tenantId, group)
delete an admin group from a tenant

allows an user to delete an admin group from a tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **group** | **string**| provide group ID | 

### Return type

[**PostResponse**](postResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelAttrSet**
> PostResponse DelAttrSet(ctx, body, xNextensioGroup, tenantId)
delete an existing attribute

allows any admin to delete an existing attribute. The attribute can be for a user, an App, or an AppGroup.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**AttrSetStruct**](AttrSetStruct.md)| provide details of attribute to be deleted | 
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

[**PostResponse**](postResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelBundle**
> string DelBundle(ctx, xNextensioGroup, tenantId, bid)
del bundle from the tenant

Delete the bundle from the specified tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provie tenant ID | 
  **bid** | **string**| provie bundle ID | 

### Return type

**string**

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelBundleRule**
> DelBundleRule(ctx, xNextensioGroup, tenantId, bid, rid, group)
delete bundle rule

delete bundle rule

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **bid** | **string**| bundle id | 
  **rid** | **string**| rule id | 
  **group** | **string**| group id | 

### Return type

 (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelCert**
> string DelCert(ctx, xNextensioGroup, certid)
delete a certificate

allows a user to delete a Nextensio Certificate

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **certid** | **string**| Certificate ID | 

### Return type

**string**

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelGateway**
> string DelGateway(ctx, xNextensioGroup, name)
delete an unused nextensio gateway

allows a nextensio admin to delete a an unused Nextensio Gateway

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **name** | **string**| Gateway name | 

### Return type

**string**

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelHostAttr**
> DelHostAttr(ctx, xNextensioGroup, tenantId, host)
delete host attrs

Delete host attributes defined by the admins.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **host** | **string**| provide host name | 

### Return type

 (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelHostRule**
> DelHostRule(ctx, xNextensioGroup, tenantId, host, rid, group)
delete host rule

delete host rule

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **host** | **string**| host id | 
  **rid** | **string**| rule id | 
  **group** | **string**| group id | 

### Return type

 (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelIdpHandler**
> PostResponse DelIdpHandler(ctx, xNextensioGroup, tenantId, idp)
delete an IDP

delete a tenant's IDP

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **idp** | **string**| provide tenant ID | 

### Return type

[**PostResponse**](postResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelMgdTenant**
> PostResponse DelMgdTenant(ctx, xNextensioGroup, tenantId, mgdtenant)
remove a managed tenant from a MSP tenant

allows a superadmin to delete a managed tenant from a MSP tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **mgdtenant** | **string**| provide ID of a managed tenant | 

### Return type

[**PostResponse**](postResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelOnboardLogs**
> DelOnboardLogs(ctx, xNextensioGroup, tenantId, userid)
delete onboard logs for a particluar user

delete onboard logs for a particluar user

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **userid** | **string**| user id | 

### Return type

 (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelPolicy**
> DelPolicy(ctx, xNextensioGroup, tenantId, policyid)
delete policy

delete policy

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **policyid** | **string**| policy id | 

### Return type

 (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelStatsRule**
> DelStatsRule(ctx, xNextensioGroup, tenantId, group)
delete stats rule

delete stats rule

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **group** | **string**| group id | 

### Return type

 (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelTenant**
> PostResponse DelTenant(ctx, xNextensioGroup, tenantId)
delete a tenant

allows a user to delete an existing tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

[**PostResponse**](postResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelTenantCluster**
> DelTenantCluster(ctx, xNextensioGroup, tenantId, gateway)
delete host attrs

Delete tenant cluster.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **gateway** | **string**| gateway name like gatewaydosfo3.nextensio.net | 

### Return type

 (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelTraceReq**
> DelTraceReq(ctx, xNextensioGroup, tenantId, rid, group)
delete trace request

delete trace request

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **rid** | **string**| rule id | 
  **group** | **string**| group id | 

### Return type

 (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelUser**
> string DelUser(ctx, xNextensioGroup, tenantId, userid)
delete a user

allows an admin to delete an existing user from the tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **userid** | **string**| provide user ID | 

### Return type

**string**

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DelUserKey**
> DelUserKey(ctx, xNextensioGroup, tenantId, key)
delete API key

delete API key

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **key** | **string**| key name | 

### Return type

 (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAdminForGroups**
> AdmGroupsDetails GetAdminForGroups(ctx, xNextensioGroup, tenantId, group)
get all admins of a tenant group

allows an user to retrieve all available admin of a tenant group

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **group** | **string**| provide group name | 

### Return type

[**AdmGroupsDetails**](admGroupsDetails.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAdminGroups**
> []AdmGroupsDetails GetAdminGroups(ctx, xNextensioGroup, tenantId)
get all admin groups of a tenant

allows an user to retrieve all available admin groups of a tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

[**[]AdmGroupsDetails**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAllBundleAttr**
> []AttrStruct GetAllBundleAttr(ctx, xNextensioGroup, tenantId)
get all bundle attrs

Retrieve all bundle attributes defined by the admins.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

[**[]AttrStruct**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAllBundleRules**
> []BundleRule GetAllBundleRules(ctx, xNextensioGroup, tenantId, bid)
get all bundle rules in a tenant

get all bundle rules in a tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **bid** | **string**| bundle ID | 

### Return type

[**[]BundleRule**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAllBundles**
> []BundleStruct GetAllBundles(ctx, xNextensioGroup, tenantId)
get all bundles

Retrieve all bundles.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provie tenant ID | 

### Return type

[**[]BundleStruct**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAllCerts**
> []CertStruct GetAllCerts(ctx, xNextensioGroup)
get all certificates

allows a user to get a Nextensio Certificate

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 

### Return type

[**[]CertStruct**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAllHostAttr**
> []AttrStruct GetAllHostAttr(ctx, xNextensioGroup, tenantId)
get all host attrs

Retrieve all host attributes defined by the admins.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

[**[]AttrStruct**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAllHostRules**
> []HostRule GetAllHostRules(ctx, xNextensioGroup, tenantId, host)
get all host rules in a tenant

get all host rules in a tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **host** | **string**| host ID | 

### Return type

[**[]HostRule**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAllIdps**
> IdpStruct GetAllIdps(ctx, xNextensioGroup, tenantId)
get all IDPs for a tenant

allows a tenant user to retrieve all IDPs

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

[**IdpStruct**](idpStruct.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAllPolicies**
> []PolicyStruct GetAllPolicies(ctx, xNextensioGroup, tenantId)
get all policies in a tenant

get all policies in a tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

[**[]PolicyStruct**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAllStatsRules**
> []TraceRule GetAllStatsRules(ctx, xNextensioGroup, tenantId)
get all stats rules in a tenant

get all stats rules in a tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

[**[]TraceRule**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAllTenantCluster**
> Tenantcluster GetAllTenantCluster(ctx, xNextensioGroup, tenantId)
get all clusters assigned for a tenant

allows to retrieve info of all clusters assigned to a tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

[**Tenantcluster**](tenantcluster.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAllTraceReqs**
> []TraceReq GetAllTraceReqs(ctx, xNextensioGroup, tenantId)
get info about all trace requests

retrieves info about all trace requests for the Trace policy. The trace requests specify the criteria to be used to trace one or more matching flows.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

[**[]TraceReq**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAllTraceRules**
> []TraceRule GetAllTraceRules(ctx, xNextensioGroup, tenantId, traceid)
get all trace rules in a tenant

get all trace rules in a tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **traceid** | **string**| trace ID | 

### Return type

[**[]TraceRule**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAllUserAttr**
> []AttrStruct GetAllUserAttr(ctx, xNextensioGroup, tenantId)
get all user attrs

Retrieve all user attributes defined by the admins.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

[**[]AttrStruct**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAllUsers**
> []UserDetails GetAllUsers(ctx, xNextensioGroup, tenantId)
get all the users of a tenant

allows an admin to get details of all users of a tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

[**[]UserDetails**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAttrCollectionHdr**
> DataHdr GetAttrCollectionHdr(ctx, xNextensioGroup, tenantId, type_)
get the header of an attributes collection for a tenant

allows a user to retrieve the header doc for an attributes collection. This collection may have a list of all the Users, Apps, or Appgroups with their attributes. The header doc provides info such as version, who last changed the collection and when.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **type_** | **string**| provide attribute collection type. Value can be Users, AppGroups, or Apps. | 

### Return type

[**DataHdr**](dataHdr.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetBundle**
> BundleStruct GetBundle(ctx, xNextensioGroup, tenantId, bid)
get bundle info of a tenant

Retrieve bundle info.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provie tenant ID | 
  **bid** | **string**| provie bundle ID | 

### Return type

[**BundleStruct**](bundleStruct.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetBundleAttr**
> AttrStruct GetBundleAttr(ctx, xNextensioGroup, tenantId, bid)
get bundle attrs

Retrieve bundle attributes defined by the admins.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **bid** | **string**| provide bundle ID | 

### Return type

[**AttrStruct**](attrStruct.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetBundleStatus**
> []BundleStatusStruct GetBundleStatus(ctx, xNextensioGroup, tenantId, bid)
get the status of every instance of a specific AppGroup extender for a tenant

allows a user to retrieve the status of all instances of an AppGroup extender based on the extender ID

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **bid** | **string**| provide AppGroup extender unique ID. | 

### Return type

[**[]BundleStatusStruct**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetCert**
> CertStructWithResult GetCert(ctx, xNextensioGroup, certid)
get a certificate

allows a user to get a Nextensio Certificate

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **certid** | **string**| Certificate ID | 

### Return type

[**CertStructWithResult**](certStructWithResult.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetClientId**
> ClientId GetClientId(ctx, xNextensioGroup, key)
get the clientid providing the proper key/password

ask for the IDP clientID for nextensio app, key/password protected.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **key** | **string**| key/password. | 

### Return type

[**ClientId**](clientID.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetGateways**
> []GatewayStruct GetGateways(ctx, xNextensioGroup)
lists all gateways

allows a user to retrieve all gateways available

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 

### Return type

[**[]GatewayStruct**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetHostAttr**
> AttrStruct GetHostAttr(ctx, xNextensioGroup, tenantId, host)
get host attrs

Retrieve host attributes defined by the admins.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **host** | **string**| provide host name | 

### Return type

[**AttrStruct**](attrStruct.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetMgdTenant**
> []Tenant GetMgdTenant(ctx, tenantId, xNextensioGroup)
get all tenant

allows a user to get details of an existing tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **tenantId** | **string**| provide tenant ID | 
  **xNextensioGroup** | **string**|  | 

### Return type

[**[]Tenant**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetPolicy**
> GetPolicyStruct GetPolicy(ctx, xNextensioGroup, tenantId, policyid)
get policy given the policyid

get policy given the policyid

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **policyid** | **string**| trace id | 

### Return type

[**GetPolicyStruct**](getPolicyStruct.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetTenant**
> Tenant GetTenant(ctx, tenantId, xNextensioGroup)
get a tenant

allows a user to get details of an existing tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **tenantId** | **string**| provide tenant ID | 
  **xNextensioGroup** | **string**|  | 

### Return type

[**Tenant**](tenant.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetTenantCluster**
> Tenantcluster GetTenantCluster(ctx, xNextensioGroup, tenantId, gateway)
get the  gateway information (nextensio internal) for a gateway assined to a tenant

allows to retrieve a tenants gateway internal information

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **gateway** | **string**| provide gateway name | 

### Return type

[**Tenantcluster**](tenantcluster.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetTenantGateways**
> []GatewayStruct GetTenantGateways(ctx, xNextensioGroup, tenantId)
lists all gateways allocated for a tenant

allows a tenant user to retrieve all gateways allocated to the tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

[**[]GatewayStruct**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetTenants**
> []Tenant GetTenants(ctx, xNextensioGroup)
get all tenant

allows a user to retrieve all existing tenants

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 

### Return type

[**[]Tenant**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetTraceReq**
> TraceReqDetails GetTraceReq(ctx, xNextensioGroup, tenantId, traceid)
get info about a trace request

retrieves info about a trace request for the Trace policy. The trace request specifies the criteria to be used to trace one or more matching flows.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **traceid** | **string**| provide trace id, which is any user defined ID for a trace request | 

### Return type

[**TraceReqDetails**](TraceReqDetails.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetTraceRequestsHdr**
> DataHdr GetTraceRequestsHdr(ctx, xNextensioGroup, tenantId)
get the header of a trace requests collection for a tenant

allows a user to retrieve the header doc for a trace requests collection. The header doc provides info such as version, who last changed the collection and when.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

[**DataHdr**](dataHdr.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetUser**
> UserDetails GetUser(ctx, xNextensioGroup, tenantId, userid)
get a user

allows an admin to get details of an existing user

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **userid** | **string**| provide user ID | 

### Return type

[**UserDetails**](userDetails.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetUserAdminRole**
> Adminrole GetUserAdminRole(ctx, xNextensioGroup, tenantId, userid)
get the admin role of a user

allows to retrieve a user's admin role

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **userid** | **string**| provide userid | 

### Return type

[**Adminrole**](adminrole.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetUserAttr**
> AttrStruct GetUserAttr(ctx, xNextensioGroup, tenantId, userId)
get user attrs

Retrieve user attributes defined by the admins.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **userId** | **string**| provide User ID | 

### Return type

[**AttrStruct**](attrStruct.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetUserKeys**
> UserKeys GetUserKeys(ctx, xNextensioGroup, tenantId)
get all the API keys in the tenant

get all the API keys in the tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 

### Return type

[**UserKeys**](userKeys.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetUserOnboardLog**
> OnboardLogDetails GetUserOnboardLog(ctx, xNextensioGroup, tenantId, userid)
get a user's onboarding info

retrieves info about a user's last attempt to onboard to a Nextensio gateway

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **userid** | **string**| provide user id | 

### Return type

[**OnboardLogDetails**](onboardLogDetails.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetUserStatus**
> []UserStatusStruct GetUserStatus(ctx, xNextensioGroup, tenantId, userid)
get details about user devices and their status

allows an admin to get status of an existing user

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **userid** | **string**| provide user ID | 

### Return type

[**[]UserStatusStruct**](array.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ModifyTenant**
> PostResponse ModifyTenant(ctx, body, xNextensioGroup, tenantId)
add or modify a tenant

allows a tenant admin / MSP to modify certain parameters of an existing tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**TenantUpdate**](TenantUpdate.md)| provide tenant info | 
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| tenant ID | 

### Return type

[**PostResponse**](postResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Onboard**
> OnboardResult Onboard(ctx, xNextensioGroup)
onboard a nextensio extender

Onboard Nextensio extender running on a user device and return a set of parameters so that they can connect to a Nextensio gateway

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 

### Return type

[**OnboardResult**](OnboardResult.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Signup**
> PostResponse Signup(ctx, body)
allows a user to signup

allows a new user to signup as an admin on behalf of a new tenant. Create a new tenant with one user, the user signing up, and create default policies and everything needed to get the tenant going.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**SignupDetails**](SignupDetails.md)| provide name of tenant and email id of user signing up | 

### Return type

[**PostResponse**](postResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdTenantType**
> PostResponse UpdTenantType(ctx, xNextensioGroup, tenantId, type_)
change the type of a tenant

allows a superadmin to change the type of a tenant

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **type_** | **string**| provide type of tenant - self-managed, MSP-managed or MSP | 

### Return type

[**PostResponse**](postResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdUserRole**
> PostResponse UpdUserRole(ctx, xNextensioGroup, tenantId, userid, role)
assign a new role for a user

allows a superadmin or tenant admin to assign a user to a new role. The new role may be that of a tenant or group admin or that of a regular user. For eg., a regular user can be made a group admin or an overall admin or vice-versa, or a group admin can be made an overall admin or vice-versa.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **xNextensioGroup** | **string**|  | 
  **tenantId** | **string**| provide tenant ID | 
  **userid** | **string**| provide ID of user | 
  **role** | **string**| provide new role. Valid values are regular, admin, or groupname-admin | 

### Return type

[**PostResponse**](postResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

