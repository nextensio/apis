# swagger_client.DefaultApi

All URIs are relative to *https://server.nextensio.net:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_admin_group**](DefaultApi.md#add_admin_group) | **POST** /tenant/{tenant-id}/add/admgroups/{group} | add an admin groups to a tenant
[**add_attr_set**](DefaultApi.md#add_attr_set) | **POST** /tenant/{tenant-id}/add/attrset | define a new attribute
[**add_bundle**](DefaultApi.md#add_bundle) | **POST** /tenant/{tenant-id}/add/bundle | Add bundle.
[**add_bundle_attr**](DefaultApi.md#add_bundle_attr) | **POST** /tenant/{tenant-id}/add/bundleattr | add tenant bundle attrs
[**add_certs**](DefaultApi.md#add_certs) | **POST** /global/add/cert | add certificate
[**add_clientid**](DefaultApi.md#add_clientid) | **POST** /global/add/clientid | Add a new clientID for a new nextensio App
[**add_cluster_handler**](DefaultApi.md#add_cluster_handler) | **POST** /tenant/{tenant-id}/add/tenantcluster | add gateway cluster to tenant
[**add_gateway**](DefaultApi.md#add_gateway) | **POST** /global/add/gateway | add a gateway
[**add_host_attr**](DefaultApi.md#add_host_attr) | **POST** /tenant/{tenant-id}/add/hostattr | add tenant host attrs
[**add_idp_handler**](DefaultApi.md#add_idp_handler) | **POST** /tenant/{tenant-id}/add/idp | add identity provider to tenant
[**add_keep_alive**](DefaultApi.md#add_keep_alive) | **POST** /global/add/keepaliverequest | Send keepalive from device to controller
[**add_mgd_tenant**](DefaultApi.md#add_mgd_tenant) | **POST** /tenant/{tenant-id}/add/tenantmsp/{mgdtenant} | assign a managed tenant to a MSP tenant
[**add_policy_handler**](DefaultApi.md#add_policy_handler) | **POST** /tenant/{tenant-id}/add/policy | add policy
[**add_stats_rule_handler**](DefaultApi.md#add_stats_rule_handler) | **POST** /tenant/{tenant-id}/add/statsrule | add stats rule
[**add_tenant**](DefaultApi.md#add_tenant) | **POST** /global/add/tenant | add basic info for a tenant
[**add_trace_req**](DefaultApi.md#add_trace_req) | **POST** /tenant/{tenant-id}/add/tracereq | add trace request
[**add_trace_rule_handler**](DefaultApi.md#add_trace_rule_handler) | **POST** /tenant/{tenant-id}/add/tracereqrule | add trace rule
[**add_user**](DefaultApi.md#add_user) | **POST** /tenant/{tenant-id}/add/user | add user
[**add_user_attr**](DefaultApi.md#add_user_attr) | **POST** /tenant/{tenant-id}/add/userattr/single/{userid} | add tenant user attrs
[**add_user_attr_multiple**](DefaultApi.md#add_user_attr_multiple) | **POST** /tenant/{tenant-id}/add/userattr/multiple | add tenant user attrs for multiple users
[**add_user_key**](DefaultApi.md#add_user_key) | **POST** /tenant/{tenant-id}/add/userkey | add API key
[**addbundle_rule_handler**](DefaultApi.md#addbundle_rule_handler) | **POST** /tenant/{tenant-id}/add/bundlerule | add bundle rule
[**addhost_rule_handler**](DefaultApi.md#addhost_rule_handler) | **POST** /tenant/{tenant-id}/add/hostrule | add host rule
[**del_admin_group**](DefaultApi.md#del_admin_group) | **GET** /tenant/{tenant-id}/del/admgroups/{group} | delete an admin group from a tenant
[**del_attr_set**](DefaultApi.md#del_attr_set) | **POST** /tenant/{tenant-id}/del/attrset | delete an existing attribute
[**del_bundle**](DefaultApi.md#del_bundle) | **GET** /tenant/{tenant-id}/del/bundle/{bid} | del bundle from the tenant
[**del_bundle_rule**](DefaultApi.md#del_bundle_rule) | **GET** /tenant/{tenant-id}/del/bundlerule/{bid}/{rid}/{group} | delete bundle rule
[**del_cert**](DefaultApi.md#del_cert) | **GET** /global/del/cert/{certid} | delete a certificate
[**del_gateway**](DefaultApi.md#del_gateway) | **GET** /global/del/gateway/{name} | delete an unused nextensio gateway
[**del_host_attr**](DefaultApi.md#del_host_attr) | **GET** /tenant/{tenant-id}/del/hostattr/{host} | delete host attrs
[**del_host_rule**](DefaultApi.md#del_host_rule) | **GET** /tenant/{tenant-id}/del/hostrule/{host}/{rid}/{group} | delete host rule
[**del_idp_handler**](DefaultApi.md#del_idp_handler) | **GET** /tenant/{tenant-id}/del/idp/{idp} | delete an IDP
[**del_mgd_tenant**](DefaultApi.md#del_mgd_tenant) | **GET** /tenant/{tenant-id}/del/tenantmsp/{mgdtenant} | remove a managed tenant from a MSP tenant
[**del_onboard_logs**](DefaultApi.md#del_onboard_logs) | **GET** /tenant/{tenant-id}/del/onboardlog/{userid} | delete onboard logs for a particluar user
[**del_policy**](DefaultApi.md#del_policy) | **GET** /tenant/{tenant-id}/del/policy/{policyid} | delete policy
[**del_stats_rule**](DefaultApi.md#del_stats_rule) | **GET** /tenant/{tenant-id}/del/statsrule/{group} | delete stats rule
[**del_tenant**](DefaultApi.md#del_tenant) | **GET** /global/del/tenant/{tenant-id} | delete a tenant
[**del_tenant_cluster**](DefaultApi.md#del_tenant_cluster) | **GET** /tenant/{tenant-id}/del/tenantcluster/{gateway} | delete host attrs
[**del_trace_req**](DefaultApi.md#del_trace_req) | **GET** /tenant/{tenant-id}/del/tracereqrule/{rid}/{group} | delete trace request
[**del_user**](DefaultApi.md#del_user) | **GET** /tenant/{tenant-id}/del/user/{userid} | delete a user
[**del_user_key**](DefaultApi.md#del_user_key) | **GET** /tenant/{tenant-id}/del/userkey/{key} | delete API key
[**get_admin_for_groups**](DefaultApi.md#get_admin_for_groups) | **GET** /tenant/{tenant-id}/get/groupadms/{group} | get all admins of a tenant group
[**get_admin_groups**](DefaultApi.md#get_admin_groups) | **GET** /tenant/{tenant-id}/get/alladmgroups | get all admin groups of a tenant
[**get_all_bundle_attr**](DefaultApi.md#get_all_bundle_attr) | **GET** /tenant/{tenant-id}/get/allbundleattr | get all bundle attrs
[**get_all_bundle_rules**](DefaultApi.md#get_all_bundle_rules) | **GET** /tenant/{tenant-id}/get/bundlerules/{bid} | get all bundle rules in a tenant
[**get_all_bundles**](DefaultApi.md#get_all_bundles) | **GET** /tenant/{tenant-id}/get/allbundles | get all bundles
[**get_all_certs**](DefaultApi.md#get_all_certs) | **GET** /global/get/allcerts | get all certificates
[**get_all_host_attr**](DefaultApi.md#get_all_host_attr) | **GET** /tenant/{tenant-id}/get/allhostattr | get all host attrs
[**get_all_host_rules**](DefaultApi.md#get_all_host_rules) | **GET** /tenant/{tenant-id}/get/hostrules/{host} | get all host rules in a tenant
[**get_all_idps**](DefaultApi.md#get_all_idps) | **GET** /tenant/{tenant-id}/get/allidps | get all IDPs for a tenant
[**get_all_policies**](DefaultApi.md#get_all_policies) | **GET** /tenant/{tenant-id}/get/allpolicies | get all policies in a tenant
[**get_all_stats_rules**](DefaultApi.md#get_all_stats_rules) | **GET** /tenant/{tenant-id}/get/statsrule | get all stats rules in a tenant
[**get_all_tenant_cluster**](DefaultApi.md#get_all_tenant_cluster) | **GET** /tenant/{tenant-id}/get/alltenantclusters | get all clusters assigned for a tenant
[**get_all_trace_reqs**](DefaultApi.md#get_all_trace_reqs) | **GET** /tenant/{tenant-id}/get/alltracereq | get info about all trace requests
[**get_all_trace_rules**](DefaultApi.md#get_all_trace_rules) | **GET** /tenant/{tenant-id}/get/tracereqrules/{traceid} | get all trace rules in a tenant
[**get_all_user_attr**](DefaultApi.md#get_all_user_attr) | **GET** /tenant/{tenant-id}/get/alluserattr | get all user attrs
[**get_all_users**](DefaultApi.md#get_all_users) | **GET** /tenant/{tenant-id}/get/allusers | get all the users of a tenant
[**get_attr_collection_hdr**](DefaultApi.md#get_attr_collection_hdr) | **GET** /tenant/{tenant-id}/get/attrhdr/{type} | get the header of an attributes collection for a tenant
[**get_bundle**](DefaultApi.md#get_bundle) | **GET** /tenant/{tenant-id}/get/bundle/{bid} | get bundle info of a tenant
[**get_bundle_attr**](DefaultApi.md#get_bundle_attr) | **GET** /tenant/{tenant-id}/get/bundleattr/{bid} | get bundle attrs
[**get_bundle_status**](DefaultApi.md#get_bundle_status) | **GET** /tenant/{tenant-id}/get/bundlestatus/{bid} | get the status of every instance of a specific AppGroup extender for a tenant
[**get_cert**](DefaultApi.md#get_cert) | **GET** /global/get/cert/{certid} | get a certificate
[**get_client_id**](DefaultApi.md#get_client_id) | **GET** /noauth/clientid/{key} | get the clientid providing the proper key/password
[**get_gateways**](DefaultApi.md#get_gateways) | **GET** /global/get/allgateways | lists all gateways
[**get_host_attr**](DefaultApi.md#get_host_attr) | **GET** /tenant/{tenant-id}/get/hostattr/{host} | get host attrs
[**get_mgd_tenant**](DefaultApi.md#get_mgd_tenant) | **GET** /tenant/{tenant-id}/get/mgdtenants | get all tenant
[**get_policy**](DefaultApi.md#get_policy) | **GET** /tenant/{tenant-id}/get/policy/{policyid} | get policy given the policyid
[**get_tenant**](DefaultApi.md#get_tenant) | **GET** /tenant/{tenant-id}/get/tenant | get a tenant
[**get_tenant_cluster**](DefaultApi.md#get_tenant_cluster) | **GET** /tenant/{tenant-id}/get/tenantcluster/{gateway} | get the  gateway information (nextensio internal) for a gateway assined to a tenant
[**get_tenant_gateways**](DefaultApi.md#get_tenant_gateways) | **GET** /tenant/{tenant-id}/get/allgateways | lists all gateways allocated for a tenant
[**get_tenants**](DefaultApi.md#get_tenants) | **GET** /global/get/alltenants | get all tenant
[**get_trace_req**](DefaultApi.md#get_trace_req) | **GET** /tenant/{tenant-id}/get/tracereq/{traceid} | get info about a trace request
[**get_trace_requests_hdr**](DefaultApi.md#get_trace_requests_hdr) | **GET** /tenant/{tenant-id}/get/tracereqhdr | get the header of a trace requests collection for a tenant
[**get_user**](DefaultApi.md#get_user) | **GET** /tenant/{tenant-id}/get/user/{userid} | get a user
[**get_user_admin_role**](DefaultApi.md#get_user_admin_role) | **GET** /tenant/{tenant-id}/get/user/adminrole/{userid} | get the admin role of a user
[**get_user_attr**](DefaultApi.md#get_user_attr) | **GET** /tenant/{tenant-id}/get/userattr/{user-id} | get user attrs
[**get_user_keys**](DefaultApi.md#get_user_keys) | **GET** /tenant/{tenant-id}/get/alluserkeys | get all the API keys in the tenant
[**get_user_onboard_log**](DefaultApi.md#get_user_onboard_log) | **GET** /tenant/{tenant-id}/get/onboardlog/{userid} | get a user&#x27;s onboarding info
[**get_user_status**](DefaultApi.md#get_user_status) | **GET** /tenant/{tenant-id}/get/userstatus/{userid} | get details about user devices and their status
[**modify_tenant**](DefaultApi.md#modify_tenant) | **POST** /tenant/{tenant-id}/add/tenant | add or modify a tenant
[**onboard**](DefaultApi.md#onboard) | **GET** /global/get/onboard | onboard a nextensio extender
[**signup**](DefaultApi.md#signup) | **POST** /noauth/signup | allows a user to signup
[**upd_tenant_type**](DefaultApi.md#upd_tenant_type) | **POST** /tenant/{tenant-id}/add/tenanttype/{type} | change the type of a tenant
[**upd_user_role**](DefaultApi.md#upd_user_role) | **POST** /tenant/{tenant-id}/add/user/adminrole/{userid}/{role} | assign a new role for a user

# **add_admin_group**
> PostResponse add_admin_group(x_nextensio_group, tenant_id, group)

add an admin groups to a tenant

allows an user to add an admin groups to a tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
group = 'group_example' # str | provide group ID

try:
    # add an admin groups to a tenant
    api_response = api_instance.add_admin_group(x_nextensio_group, tenant_id, group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_admin_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **group** | **str**| provide group ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_attr_set**
> PostResponse add_attr_set(body, x_nextensio_group, tenant_id)

define a new attribute

allows any admin to add a new attribute. The attribute can be for a user, an App, or an AppGroup.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.AttrSetStruct() # AttrSetStruct | provide details of attribute to be added
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # define a new attribute
    api_response = api_instance.add_attr_set(body, x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_attr_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttrSetStruct**](AttrSetStruct.md)| provide details of attribute to be added | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_bundle**
> PostResponse add_bundle(body, x_nextensio_group, tenant_id)

Add bundle.

Add bundle to the specified tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.BundleStruct() # BundleStruct | provide tenant info
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provie tenant ID

try:
    # Add bundle.
    api_response = api_instance.add_bundle(body, x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BundleStruct**](BundleStruct.md)| provide tenant info | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provie tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_bundle_attr**
> PostResponse add_bundle_attr(body, x_nextensio_group, tenant_id)

add tenant bundle attrs

Add attributes to the bundle of a tenant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, object) | provide bundle attributes to be added/updated
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # add tenant bundle attrs
    api_response = api_instance.add_bundle_attr(body, x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_bundle_attr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)| provide bundle attributes to be added/updated | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_certs**
> PostResponse add_certs(body, x_nextensio_group)

add certificate

allows a user to add a Nextensio Certificate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.CertStruct() # CertStruct | provide info about certificate
x_nextensio_group = 'x_nextensio_group_example' # str | 

try:
    # add certificate
    api_response = api_instance.add_certs(body, x_nextensio_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_certs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CertStruct**](CertStruct.md)| provide info about certificate | 
 **x_nextensio_group** | **str**|  | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_clientid**
> PostResponse add_clientid(body, x_nextensio_group)

Add a new clientID for a new nextensio App

Add new clientID for new nextensio App

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddClientID() # AddClientID | provide details of attribute to be added
x_nextensio_group = 'x_nextensio_group_example' # str | 

try:
    # Add a new clientID for a new nextensio App
    api_response = api_instance.add_clientid(body, x_nextensio_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_clientid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddClientID**](AddClientID.md)| provide details of attribute to be added | 
 **x_nextensio_group** | **str**|  | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_cluster_handler**
> PostResponse add_cluster_handler(body, x_nextensio_group, tenant_id)

add gateway cluster to tenant

add gateway cluster to tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.TenantCluster() # TenantCluster | 
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # add gateway cluster to tenant
    api_response = api_instance.add_cluster_handler(body, x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_cluster_handler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TenantCluster**](TenantCluster.md)|  | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_gateway**
> PostResponse add_gateway(body, x_nextensio_group)

add a gateway

allows a user to add a new gateway or update an existing one

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.GatewayStruct() # GatewayStruct | provide info about gateway
x_nextensio_group = 'x_nextensio_group_example' # str | 

try:
    # add a gateway
    api_response = api_instance.add_gateway(body, x_nextensio_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayStruct**](GatewayStruct.md)| provide info about gateway | 
 **x_nextensio_group** | **str**|  | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_host_attr**
> PostResponse add_host_attr(body, x_nextensio_group, tenant_id)

add tenant host attrs

Add attributes to the host in a tenant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, object) | provide host attributes to be added/updated
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # add tenant host attrs
    api_response = api_instance.add_host_attr(body, x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_host_attr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)| provide host attributes to be added/updated | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_idp_handler**
> PostResponse add_idp_handler(body, x_nextensio_group, tenant_id)

add identity provider to tenant

add identity provider to tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddIDP() # AddIDP | 
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # add identity provider to tenant
    api_response = api_instance.add_idp_handler(body, x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_idp_handler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddIDP**](AddIDP.md)|  | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_keep_alive**
> add_keep_alive(body, x_nextensio_group)

Send keepalive from device to controller

Send keepalive from user device to nextensio controller

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.KeepaliveReq() # KeepaliveReq | provide details of attribute to be added
x_nextensio_group = 'x_nextensio_group_example' # str | 

try:
    # Send keepalive from device to controller
    api_instance.add_keep_alive(body, x_nextensio_group)
except ApiException as e:
    print("Exception when calling DefaultApi->add_keep_alive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KeepaliveReq**](KeepaliveReq.md)| provide details of attribute to be added | 
 **x_nextensio_group** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_mgd_tenant**
> PostResponse add_mgd_tenant(x_nextensio_group, tenant_id, mgdtenant)

assign a managed tenant to a MSP tenant

allows a superadmin to assign a managed tenant to a MSP tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
mgdtenant = 'mgdtenant_example' # str | provide ID of a managed tenant

try:
    # assign a managed tenant to a MSP tenant
    api_response = api_instance.add_mgd_tenant(x_nextensio_group, tenant_id, mgdtenant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_mgd_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **mgdtenant** | **str**| provide ID of a managed tenant | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_policy_handler**
> PostResponse add_policy_handler(body, x_nextensio_group, tenant_id)

add policy

add policy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddPolicy() # AddPolicy | 
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # add policy
    api_response = api_instance.add_policy_handler(body, x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_policy_handler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddPolicy**](AddPolicy.md)|  | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_stats_rule_handler**
> PostResponse add_stats_rule_handler(body, x_nextensio_group, tenant_id)

add stats rule

add stats rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.StatsRule() # StatsRule | 
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # add stats rule
    api_response = api_instance.add_stats_rule_handler(body, x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_stats_rule_handler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatsRule**](StatsRule.md)|  | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_tenant**
> PostResponse add_tenant(body, x_nextensio_group)

add basic info for a tenant

allows a superuser or an MSP to add a new tenant or update an existing one

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.TenantUpdate() # TenantUpdate | provide info about tenant
x_nextensio_group = 'x_nextensio_group_example' # str | 

try:
    # add basic info for a tenant
    api_response = api_instance.add_tenant(body, x_nextensio_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TenantUpdate**](TenantUpdate.md)| provide info about tenant | 
 **x_nextensio_group** | **str**|  | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_trace_req**
> PostResponse add_trace_req(body, x_nextensio_group, tenant_id)

add trace request

add trace request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, object) | need "traceid" as a mandatory key
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # add trace request
    api_response = api_instance.add_trace_req(body, x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_trace_req: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)| need &quot;traceid&quot; as a mandatory key | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_trace_rule_handler**
> PostResponse add_trace_rule_handler(body, x_nextensio_group, tenant_id)

add trace rule

add trace rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.TraceRule() # TraceRule | 
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # add trace rule
    api_response = api_instance.add_trace_rule_handler(body, x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_trace_rule_handler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TraceRule**](TraceRule.md)|  | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user**
> PostResponse add_user(body, x_nextensio_group, tenant_id)

add user

allows an admin to add a user to the specified tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserAdd() # UserAdd | provide info about user
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # add user
    api_response = api_instance.add_user(body, x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAdd**](UserAdd.md)| provide info about user | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_attr**
> PostResponse add_user_attr(body, x_nextensio_group, tenant_id, userid)

add tenant user attrs

Add attributes to the user of a tenant.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = NULL # dict(str, object) | provide user attributes to be added/updated
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
userid = 'userid_example' # str | provide User ID

try:
    # add tenant user attrs
    api_response = api_instance.add_user_attr(body, x_nextensio_group, tenant_id, userid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_user_attr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**dict(str, object)**](dict.md)| provide user attributes to be added/updated | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **userid** | **str**| provide User ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_attr_multiple**
> PostResponse add_user_attr_multiple(body, x_nextensio_group, tenant_id)

add tenant user attrs for multiple users

add tenant user attrs for multiple users

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = NULL # list[object] | provide user attributes to be added/updated
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # add tenant user attrs for multiple users
    api_response = api_instance.add_user_attr_multiple(body, x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_user_attr_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[object]**](object.md)| provide user attributes to be added/updated | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user_key**
> UserKeyResponse add_user_key(body, x_nextensio_group, tenant_id)

add API key

add API key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserKey() # UserKey | 
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # add API key
    api_response = api_instance.add_user_key(body, x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add_user_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserKey**](UserKey.md)|  | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**UserKeyResponse**](UserKeyResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addbundle_rule_handler**
> PostResponse addbundle_rule_handler(body, x_nextensio_group, tenant_id)

add bundle rule

add bundle rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.BundleRule() # BundleRule | 
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # add bundle rule
    api_response = api_instance.addbundle_rule_handler(body, x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->addbundle_rule_handler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BundleRule**](BundleRule.md)|  | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **addhost_rule_handler**
> PostResponse addhost_rule_handler(body, x_nextensio_group, tenant_id)

add host rule

add host rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.HostRule() # HostRule | 
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # add host rule
    api_response = api_instance.addhost_rule_handler(body, x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->addhost_rule_handler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostRule**](HostRule.md)|  | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_admin_group**
> PostResponse del_admin_group(x_nextensio_group, tenant_id, group)

delete an admin group from a tenant

allows an user to delete an admin group from a tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
group = 'group_example' # str | provide group ID

try:
    # delete an admin group from a tenant
    api_response = api_instance.del_admin_group(x_nextensio_group, tenant_id, group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->del_admin_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **group** | **str**| provide group ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_attr_set**
> PostResponse del_attr_set(body, x_nextensio_group, tenant_id)

delete an existing attribute

allows any admin to delete an existing attribute. The attribute can be for a user, an App, or an AppGroup.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.AttrSetStruct() # AttrSetStruct | provide details of attribute to be deleted
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # delete an existing attribute
    api_response = api_instance.del_attr_set(body, x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->del_attr_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttrSetStruct**](AttrSetStruct.md)| provide details of attribute to be deleted | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_bundle**
> str del_bundle(x_nextensio_group, tenant_id, bid)

del bundle from the tenant

Delete the bundle from the specified tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provie tenant ID
bid = 'bid_example' # str | provie bundle ID

try:
    # del bundle from the tenant
    api_response = api_instance.del_bundle(x_nextensio_group, tenant_id, bid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->del_bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provie tenant ID | 
 **bid** | **str**| provie bundle ID | 

### Return type

**str**

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_bundle_rule**
> del_bundle_rule(x_nextensio_group, tenant_id, bid, rid, group)

delete bundle rule

delete bundle rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
bid = 'bid_example' # str | bundle id
rid = 'rid_example' # str | rule id
group = 'group_example' # str | group id

try:
    # delete bundle rule
    api_instance.del_bundle_rule(x_nextensio_group, tenant_id, bid, rid, group)
except ApiException as e:
    print("Exception when calling DefaultApi->del_bundle_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **bid** | **str**| bundle id | 
 **rid** | **str**| rule id | 
 **group** | **str**| group id | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_cert**
> str del_cert(x_nextensio_group, certid)

delete a certificate

allows a user to delete a Nextensio Certificate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
certid = 'certid_example' # str | Certificate ID

try:
    # delete a certificate
    api_response = api_instance.del_cert(x_nextensio_group, certid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->del_cert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **certid** | **str**| Certificate ID | 

### Return type

**str**

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_gateway**
> str del_gateway(x_nextensio_group, name)

delete an unused nextensio gateway

allows a nextensio admin to delete a an unused Nextensio Gateway

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
name = 'name_example' # str | Gateway name

try:
    # delete an unused nextensio gateway
    api_response = api_instance.del_gateway(x_nextensio_group, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->del_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **name** | **str**| Gateway name | 

### Return type

**str**

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_host_attr**
> del_host_attr(x_nextensio_group, tenant_id, host)

delete host attrs

Delete host attributes defined by the admins.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
host = 'host_example' # str | provide host name

try:
    # delete host attrs
    api_instance.del_host_attr(x_nextensio_group, tenant_id, host)
except ApiException as e:
    print("Exception when calling DefaultApi->del_host_attr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **host** | **str**| provide host name | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_host_rule**
> del_host_rule(x_nextensio_group, tenant_id, host, rid, group)

delete host rule

delete host rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
host = 'host_example' # str | host id
rid = 'rid_example' # str | rule id
group = 'group_example' # str | group id

try:
    # delete host rule
    api_instance.del_host_rule(x_nextensio_group, tenant_id, host, rid, group)
except ApiException as e:
    print("Exception when calling DefaultApi->del_host_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **host** | **str**| host id | 
 **rid** | **str**| rule id | 
 **group** | **str**| group id | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_idp_handler**
> PostResponse del_idp_handler(x_nextensio_group, tenant_id, idp)

delete an IDP

delete a tenant's IDP

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
idp = 'idp_example' # str | provide tenant ID

try:
    # delete an IDP
    api_response = api_instance.del_idp_handler(x_nextensio_group, tenant_id, idp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->del_idp_handler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **idp** | **str**| provide tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_mgd_tenant**
> PostResponse del_mgd_tenant(x_nextensio_group, tenant_id, mgdtenant)

remove a managed tenant from a MSP tenant

allows a superadmin to delete a managed tenant from a MSP tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
mgdtenant = 'mgdtenant_example' # str | provide ID of a managed tenant

try:
    # remove a managed tenant from a MSP tenant
    api_response = api_instance.del_mgd_tenant(x_nextensio_group, tenant_id, mgdtenant)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->del_mgd_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **mgdtenant** | **str**| provide ID of a managed tenant | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_onboard_logs**
> del_onboard_logs(x_nextensio_group, tenant_id, userid)

delete onboard logs for a particluar user

delete onboard logs for a particluar user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
userid = 'userid_example' # str | user id

try:
    # delete onboard logs for a particluar user
    api_instance.del_onboard_logs(x_nextensio_group, tenant_id, userid)
except ApiException as e:
    print("Exception when calling DefaultApi->del_onboard_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **userid** | **str**| user id | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_policy**
> del_policy(x_nextensio_group, tenant_id, policyid)

delete policy

delete policy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
policyid = 'policyid_example' # str | policy id

try:
    # delete policy
    api_instance.del_policy(x_nextensio_group, tenant_id, policyid)
except ApiException as e:
    print("Exception when calling DefaultApi->del_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **policyid** | **str**| policy id | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_stats_rule**
> del_stats_rule(x_nextensio_group, tenant_id, group)

delete stats rule

delete stats rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
group = 'group_example' # str | group id

try:
    # delete stats rule
    api_instance.del_stats_rule(x_nextensio_group, tenant_id, group)
except ApiException as e:
    print("Exception when calling DefaultApi->del_stats_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **group** | **str**| group id | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_tenant**
> PostResponse del_tenant(x_nextensio_group, tenant_id)

delete a tenant

allows a user to delete an existing tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # delete a tenant
    api_response = api_instance.del_tenant(x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->del_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_tenant_cluster**
> del_tenant_cluster(x_nextensio_group, tenant_id, gateway)

delete host attrs

Delete tenant cluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
gateway = 'gateway_example' # str | gateway name like gatewaydosfo3.nextensio.net

try:
    # delete host attrs
    api_instance.del_tenant_cluster(x_nextensio_group, tenant_id, gateway)
except ApiException as e:
    print("Exception when calling DefaultApi->del_tenant_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **gateway** | **str**| gateway name like gatewaydosfo3.nextensio.net | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_trace_req**
> del_trace_req(x_nextensio_group, tenant_id, rid, group)

delete trace request

delete trace request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
rid = 'rid_example' # str | rule id
group = 'group_example' # str | group id

try:
    # delete trace request
    api_instance.del_trace_req(x_nextensio_group, tenant_id, rid, group)
except ApiException as e:
    print("Exception when calling DefaultApi->del_trace_req: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **rid** | **str**| rule id | 
 **group** | **str**| group id | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_user**
> str del_user(x_nextensio_group, tenant_id, userid)

delete a user

allows an admin to delete an existing user from the tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
userid = 'userid_example' # str | provide user ID

try:
    # delete a user
    api_response = api_instance.del_user(x_nextensio_group, tenant_id, userid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->del_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **userid** | **str**| provide user ID | 

### Return type

**str**

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_user_key**
> del_user_key(x_nextensio_group, tenant_id, key)

delete API key

delete API key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
key = 'key_example' # str | key name

try:
    # delete API key
    api_instance.del_user_key(x_nextensio_group, tenant_id, key)
except ApiException as e:
    print("Exception when calling DefaultApi->del_user_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **key** | **str**| key name | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_for_groups**
> AdmGroupsDetails get_admin_for_groups(x_nextensio_group, tenant_id, group)

get all admins of a tenant group

allows an user to retrieve all available admin of a tenant group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
group = 'group_example' # str | provide group name

try:
    # get all admins of a tenant group
    api_response = api_instance.get_admin_for_groups(x_nextensio_group, tenant_id, group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_admin_for_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **group** | **str**| provide group name | 

### Return type

[**AdmGroupsDetails**](AdmGroupsDetails.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_groups**
> AdmGroupsArray get_admin_groups(x_nextensio_group, tenant_id)

get all admin groups of a tenant

allows an user to retrieve all available admin groups of a tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # get all admin groups of a tenant
    api_response = api_instance.get_admin_groups(x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_admin_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**AdmGroupsArray**](AdmGroupsArray.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_bundle_attr**
> BundleAttrMultiple get_all_bundle_attr(x_nextensio_group, tenant_id)

get all bundle attrs

Retrieve all bundle attributes defined by the admins.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # get all bundle attrs
    api_response = api_instance.get_all_bundle_attr(x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_bundle_attr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**BundleAttrMultiple**](BundleAttrMultiple.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_bundle_rules**
> AllBundleRules get_all_bundle_rules(x_nextensio_group, tenant_id, bid)

get all bundle rules in a tenant

get all bundle rules in a tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
bid = 'bid_example' # str | bundle ID

try:
    # get all bundle rules in a tenant
    api_response = api_instance.get_all_bundle_rules(x_nextensio_group, tenant_id, bid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_bundle_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **bid** | **str**| bundle ID | 

### Return type

[**AllBundleRules**](AllBundleRules.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_bundles**
> AllBundles get_all_bundles(x_nextensio_group, tenant_id)

get all bundles

Retrieve all bundles.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provie tenant ID

try:
    # get all bundles
    api_response = api_instance.get_all_bundles(x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_bundles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provie tenant ID | 

### Return type

[**AllBundles**](AllBundles.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_certs**
> AllCerts get_all_certs(x_nextensio_group)

get all certificates

allows a user to get a Nextensio Certificate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 

try:
    # get all certificates
    api_response = api_instance.get_all_certs(x_nextensio_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_certs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 

### Return type

[**AllCerts**](AllCerts.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_host_attr**
> HostAttrMultiple get_all_host_attr(x_nextensio_group, tenant_id)

get all host attrs

Retrieve all host attributes defined by the admins.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # get all host attrs
    api_response = api_instance.get_all_host_attr(x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_host_attr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**HostAttrMultiple**](HostAttrMultiple.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_host_rules**
> AllHostRules get_all_host_rules(x_nextensio_group, tenant_id, host)

get all host rules in a tenant

get all host rules in a tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
host = 'host_example' # str | host ID

try:
    # get all host rules in a tenant
    api_response = api_instance.get_all_host_rules(x_nextensio_group, tenant_id, host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_host_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **host** | **str**| host ID | 

### Return type

[**AllHostRules**](AllHostRules.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_idps**
> IdpStruct get_all_idps(x_nextensio_group, tenant_id)

get all IDPs for a tenant

allows a tenant user to retrieve all IDPs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # get all IDPs for a tenant
    api_response = api_instance.get_all_idps(x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_idps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**IdpStruct**](IdpStruct.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_policies**
> GetAllPolicies get_all_policies(x_nextensio_group, tenant_id)

get all policies in a tenant

get all policies in a tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # get all policies in a tenant
    api_response = api_instance.get_all_policies(x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**GetAllPolicies**](GetAllPolicies.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_stats_rules**
> AllStatsRules get_all_stats_rules(x_nextensio_group, tenant_id)

get all stats rules in a tenant

get all stats rules in a tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # get all stats rules in a tenant
    api_response = api_instance.get_all_stats_rules(x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_stats_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**AllStatsRules**](AllStatsRules.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_tenant_cluster**
> AllTenantclusters get_all_tenant_cluster(x_nextensio_group, tenant_id)

get all clusters assigned for a tenant

allows to retrieve info of all clusters assigned to a tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # get all clusters assigned for a tenant
    api_response = api_instance.get_all_tenant_cluster(x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_tenant_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**AllTenantclusters**](AllTenantclusters.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_trace_reqs**
> AllTraceReqDetails get_all_trace_reqs(x_nextensio_group, tenant_id)

get info about all trace requests

retrieves info about all trace requests for the Trace policy. The trace requests specify the criteria to be used to trace one or more matching flows.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # get info about all trace requests
    api_response = api_instance.get_all_trace_reqs(x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_trace_reqs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**AllTraceReqDetails**](AllTraceReqDetails.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_trace_rules**
> AllTraceRules get_all_trace_rules(x_nextensio_group, tenant_id, traceid)

get all trace rules in a tenant

get all trace rules in a tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
traceid = 'traceid_example' # str | trace ID

try:
    # get all trace rules in a tenant
    api_response = api_instance.get_all_trace_rules(x_nextensio_group, tenant_id, traceid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_trace_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **traceid** | **str**| trace ID | 

### Return type

[**AllTraceRules**](AllTraceRules.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_user_attr**
> UserAttrMultiple get_all_user_attr(x_nextensio_group, tenant_id)

get all user attrs

Retrieve all user attributes defined by the admins.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # get all user attrs
    api_response = api_instance.get_all_user_attr(x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_user_attr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**UserAttrMultiple**](UserAttrMultiple.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users**
> AllUserDetails get_all_users(x_nextensio_group, tenant_id)

get all the users of a tenant

allows an admin to get details of all users of a tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # get all the users of a tenant
    api_response = api_instance.get_all_users(x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**AllUserDetails**](AllUserDetails.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attr_collection_hdr**
> DataHdr get_attr_collection_hdr(x_nextensio_group, tenant_id, type)

get the header of an attributes collection for a tenant

allows a user to retrieve the header doc for an attributes collection. This collection may have a list of all the Users, Apps, or Appgroups with their attributes. The header doc provides info such as version, who last changed the collection and when.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
type = 'type_example' # str | provide attribute collection type. Value can be Users, AppGroups, or Apps.

try:
    # get the header of an attributes collection for a tenant
    api_response = api_instance.get_attr_collection_hdr(x_nextensio_group, tenant_id, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_attr_collection_hdr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **type** | **str**| provide attribute collection type. Value can be Users, AppGroups, or Apps. | 

### Return type

[**DataHdr**](DataHdr.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle**
> GetBundleStruct get_bundle(x_nextensio_group, tenant_id, bid)

get bundle info of a tenant

Retrieve bundle info.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provie tenant ID
bid = 'bid_example' # str | provie bundle ID

try:
    # get bundle info of a tenant
    api_response = api_instance.get_bundle(x_nextensio_group, tenant_id, bid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provie tenant ID | 
 **bid** | **str**| provie bundle ID | 

### Return type

[**GetBundleStruct**](GetBundleStruct.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_attr**
> BundleAttrSingle get_bundle_attr(x_nextensio_group, tenant_id, bid)

get bundle attrs

Retrieve bundle attributes defined by the admins.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
bid = 'bid_example' # str | provide bundle ID

try:
    # get bundle attrs
    api_response = api_instance.get_bundle_attr(x_nextensio_group, tenant_id, bid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_bundle_attr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **bid** | **str**| provide bundle ID | 

### Return type

[**BundleAttrSingle**](BundleAttrSingle.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_status**
> BundleStatus get_bundle_status(x_nextensio_group, tenant_id, bid)

get the status of every instance of a specific AppGroup extender for a tenant

allows a user to retrieve the status of all instances of an AppGroup extender based on the extender ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
bid = 'bid_example' # str | provide AppGroup extender unique ID.

try:
    # get the status of every instance of a specific AppGroup extender for a tenant
    api_response = api_instance.get_bundle_status(x_nextensio_group, tenant_id, bid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_bundle_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **bid** | **str**| provide AppGroup extender unique ID. | 

### Return type

[**BundleStatus**](BundleStatus.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cert**
> CertStructWithResult get_cert(x_nextensio_group, certid)

get a certificate

allows a user to get a Nextensio Certificate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
certid = 'certid_example' # str | Certificate ID

try:
    # get a certificate
    api_response = api_instance.get_cert(x_nextensio_group, certid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **certid** | **str**| Certificate ID | 

### Return type

[**CertStructWithResult**](CertStructWithResult.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_id**
> ClientID get_client_id(x_nextensio_group, key)

get the clientid providing the proper key/password

ask for the IDP clientID for nextensio app, key/password protected.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
key = 'key_example' # str | key/password.

try:
    # get the clientid providing the proper key/password
    api_response = api_instance.get_client_id(x_nextensio_group, key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_client_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **key** | **str**| key/password. | 

### Return type

[**ClientID**](ClientID.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gateways**
> AllGateways get_gateways(x_nextensio_group)

lists all gateways

allows a user to retrieve all gateways available

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 

try:
    # lists all gateways
    api_response = api_instance.get_gateways(x_nextensio_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_gateways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 

### Return type

[**AllGateways**](AllGateways.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_attr**
> HostAttrSingle get_host_attr(x_nextensio_group, tenant_id, host)

get host attrs

Retrieve host attributes defined by the admins.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
host = 'host_example' # str | provide host name

try:
    # get host attrs
    api_response = api_instance.get_host_attr(x_nextensio_group, tenant_id, host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_host_attr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **host** | **str**| provide host name | 

### Return type

[**HostAttrSingle**](HostAttrSingle.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mgd_tenant**
> TenantDetails get_mgd_tenant(tenant_id, x_nextensio_group)

get all tenant

allows a user to get details of an existing tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | provide tenant ID
x_nextensio_group = 'x_nextensio_group_example' # str | 

try:
    # get all tenant
    api_response = api_instance.get_mgd_tenant(tenant_id, x_nextensio_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_mgd_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| provide tenant ID | 
 **x_nextensio_group** | **str**|  | 

### Return type

[**TenantDetails**](TenantDetails.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> GetPolicyStruct get_policy(x_nextensio_group, tenant_id, policyid)

get policy given the policyid

get policy given the policyid

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
policyid = 'policyid_example' # str | trace id

try:
    # get policy given the policyid
    api_response = api_instance.get_policy(x_nextensio_group, tenant_id, policyid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **policyid** | **str**| trace id | 

### Return type

[**GetPolicyStruct**](GetPolicyStruct.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant**
> Tenant get_tenant(tenant_id, x_nextensio_group)

get a tenant

allows a user to get details of an existing tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | provide tenant ID
x_nextensio_group = 'x_nextensio_group_example' # str | 

try:
    # get a tenant
    api_response = api_instance.get_tenant(tenant_id, x_nextensio_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| provide tenant ID | 
 **x_nextensio_group** | **str**|  | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_cluster**
> GetTenantcluster get_tenant_cluster(x_nextensio_group, tenant_id, gateway)

get the  gateway information (nextensio internal) for a gateway assined to a tenant

allows to retrieve a tenants gateway internal information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
gateway = 'gateway_example' # str | provide gateway name

try:
    # get the  gateway information (nextensio internal) for a gateway assined to a tenant
    api_response = api_instance.get_tenant_cluster(x_nextensio_group, tenant_id, gateway)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_tenant_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **gateway** | **str**| provide gateway name | 

### Return type

[**GetTenantcluster**](GetTenantcluster.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_gateways**
> AllGateways get_tenant_gateways(x_nextensio_group, tenant_id)

lists all gateways allocated for a tenant

allows a tenant user to retrieve all gateways allocated to the tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # lists all gateways allocated for a tenant
    api_response = api_instance.get_tenant_gateways(x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_tenant_gateways: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**AllGateways**](AllGateways.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenants**
> TenantDetails get_tenants(x_nextensio_group)

get all tenant

allows a user to retrieve all existing tenants

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 

try:
    # get all tenant
    api_response = api_instance.get_tenants(x_nextensio_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_tenants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 

### Return type

[**TenantDetails**](TenantDetails.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trace_req**
> TraceReqDetails get_trace_req(x_nextensio_group, tenant_id, traceid)

get info about a trace request

retrieves info about a trace request for the Trace policy. The trace request specifies the criteria to be used to trace one or more matching flows.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
traceid = 'traceid_example' # str | provide trace id, which is any user defined ID for a trace request

try:
    # get info about a trace request
    api_response = api_instance.get_trace_req(x_nextensio_group, tenant_id, traceid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_trace_req: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **traceid** | **str**| provide trace id, which is any user defined ID for a trace request | 

### Return type

[**TraceReqDetails**](TraceReqDetails.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trace_requests_hdr**
> DataHdr get_trace_requests_hdr(x_nextensio_group, tenant_id)

get the header of a trace requests collection for a tenant

allows a user to retrieve the header doc for a trace requests collection. The header doc provides info such as version, who last changed the collection and when.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # get the header of a trace requests collection for a tenant
    api_response = api_instance.get_trace_requests_hdr(x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_trace_requests_hdr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**DataHdr**](DataHdr.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserDetails get_user(x_nextensio_group, tenant_id, userid)

get a user

allows an admin to get details of an existing user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
userid = 'userid_example' # str | provide user ID

try:
    # get a user
    api_response = api_instance.get_user(x_nextensio_group, tenant_id, userid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **userid** | **str**| provide user ID | 

### Return type

[**UserDetails**](UserDetails.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_admin_role**
> Adminrole get_user_admin_role(x_nextensio_group, tenant_id, userid)

get the admin role of a user

allows to retrieve a user's admin role

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
userid = 'userid_example' # str | provide userid

try:
    # get the admin role of a user
    api_response = api_instance.get_user_admin_role(x_nextensio_group, tenant_id, userid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_admin_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **userid** | **str**| provide userid | 

### Return type

[**Adminrole**](Adminrole.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_attr**
> UserAttrSingle get_user_attr(x_nextensio_group, tenant_id, user_id)

get user attrs

Retrieve user attributes defined by the admins.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
user_id = 'user_id_example' # str | provide User ID

try:
    # get user attrs
    api_response = api_instance.get_user_attr(x_nextensio_group, tenant_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_attr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **user_id** | **str**| provide User ID | 

### Return type

[**UserAttrSingle**](UserAttrSingle.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_keys**
> UserKeys get_user_keys(x_nextensio_group, tenant_id)

get all the API keys in the tenant

get all the API keys in the tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID

try:
    # get all the API keys in the tenant
    api_response = api_instance.get_user_keys(x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 

### Return type

[**UserKeys**](UserKeys.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_onboard_log**
> OnboardLogDetails get_user_onboard_log(x_nextensio_group, tenant_id, userid)

get a user's onboarding info

retrieves info about a user's last attempt to onboard to a Nextensio gateway

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
userid = 'userid_example' # str | provide user id

try:
    # get a user's onboarding info
    api_response = api_instance.get_user_onboard_log(x_nextensio_group, tenant_id, userid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_onboard_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **userid** | **str**| provide user id | 

### Return type

[**OnboardLogDetails**](OnboardLogDetails.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_status**
> UserStatus get_user_status(x_nextensio_group, tenant_id, userid)

get details about user devices and their status

allows an admin to get status of an existing user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
userid = 'userid_example' # str | provide user ID

try:
    # get details about user devices and their status
    api_response = api_instance.get_user_status(x_nextensio_group, tenant_id, userid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **userid** | **str**| provide user ID | 

### Return type

[**UserStatus**](UserStatus.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_tenant**
> PostResponse modify_tenant(body, x_nextensio_group, tenant_id)

add or modify a tenant

allows a tenant admin / MSP to modify certain parameters of an existing tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.TenantUpdate() # TenantUpdate | provide tenant info
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | tenant ID

try:
    # add or modify a tenant
    api_response = api_instance.modify_tenant(body, x_nextensio_group, tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->modify_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TenantUpdate**](TenantUpdate.md)| provide tenant info | 
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| tenant ID | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **onboard**
> OnboardResult onboard(x_nextensio_group)

onboard a nextensio extender

Onboard Nextensio extender running on a user device and return a set of parameters so that they can connect to a Nextensio gateway

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 

try:
    # onboard a nextensio extender
    api_response = api_instance.onboard(x_nextensio_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->onboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 

### Return type

[**OnboardResult**](OnboardResult.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signup**
> PostResponse signup(body)

allows a user to signup

allows a new user to signup as an admin on behalf of a new tenant. Create a new tenant with one user, the user signing up, and create default policies and everything needed to get the tenant going.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.SignupDetails() # SignupDetails | provide name of tenant and email id of user signing up

try:
    # allows a user to signup
    api_response = api_instance.signup(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->signup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SignupDetails**](SignupDetails.md)| provide name of tenant and email id of user signing up | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upd_tenant_type**
> PostResponse upd_tenant_type(x_nextensio_group, tenant_id, type)

change the type of a tenant

allows a superadmin to change the type of a tenant

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
type = 'type_example' # str | provide type of tenant - self-managed, MSP-managed or MSP

try:
    # change the type of a tenant
    api_response = api_instance.upd_tenant_type(x_nextensio_group, tenant_id, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->upd_tenant_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **type** | **str**| provide type of tenant - self-managed, MSP-managed or MSP | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upd_user_role**
> PostResponse upd_user_role(x_nextensio_group, tenant_id, userid, role)

assign a new role for a user

allows a superadmin or tenant admin to assign a user to a new role. The new role may be that of a tenant or group admin or that of a regular user. For eg., a regular user can be made a group admin or an overall admin or vice-versa, or a group admin can be made an overall admin or vice-versa.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = swagger_client.Configuration()
configuration.api_key['X-Nextensio-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Nextensio-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_nextensio_group = 'x_nextensio_group_example' # str | 
tenant_id = 'tenant_id_example' # str | provide tenant ID
userid = 'userid_example' # str | provide ID of user
role = 'role_example' # str | provide new role. Valid values are regular, admin, or groupname-admin

try:
    # assign a new role for a user
    api_response = api_instance.upd_user_role(x_nextensio_group, tenant_id, userid, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->upd_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_nextensio_group** | **str**|  | 
 **tenant_id** | **str**| provide tenant ID | 
 **userid** | **str**| provide ID of user | 
 **role** | **str**| provide new role. Valid values are regular, admin, or groupname-admin | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

