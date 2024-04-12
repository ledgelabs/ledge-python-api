# ledge_python_sdk.InventoryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_avatar**](InventoryApi.md#get_avatar) | **POST** /inventory/avatar | 
[**get_inventory**](InventoryApi.md#get_inventory) | **GET** /inventory | 
[**get_item_count**](InventoryApi.md#get_item_count) | **GET** /inventory/itemCount | 
[**get_leaderboard**](InventoryApi.md#get_leaderboard) | **GET** /inventory/leaderboard | 
[**get_product_id_count**](InventoryApi.md#get_product_id_count) | **GET** /inventory/products/{productId} | 
[**get_spin_case**](InventoryApi.md#get_spin_case) | **GET** /inventory/SpinCase | 
[**get_user_avatar**](InventoryApi.md#get_user_avatar) | **POST** /inventory/avatar/{userId} | 
[**get_user_item_count**](InventoryApi.md#get_user_item_count) | **GET** /inventory/users/{userId} | 
[**update_inventory**](InventoryApi.md#update_inventory) | **PATCH** /inventory | 
[**update_profile**](InventoryApi.md#update_profile) | **POST** /inventory/update-profile | 


# **get_avatar**
> UserInventoryDetailed get_avatar(user_id=user_id)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.user_inventory_detailed import UserInventoryDetailed
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.InventoryApi(api_client)
    user_id = 'user_id_example' # str |  (optional)

    try:
        api_response = api_instance.get_avatar(user_id=user_id)
        print("The response of InventoryApi->get_avatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional] 

### Return type

[**UserInventoryDetailed**](UserInventoryDetailed.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory**
> List[UserInventoryDetailed] get_inventory(product_types, is_default=is_default, is_seen=is_seen, user_id=user_id)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.product_type import ProductType
from ledge_python_sdk.models.user_inventory_detailed import UserInventoryDetailed
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.InventoryApi(api_client)
    product_types = [ledge_python_sdk.ProductType()] # List[ProductType] | 
    is_default = True # bool |  (optional)
    is_seen = True # bool |  (optional)
    user_id = 'user_id_example' # str |  (optional)

    try:
        api_response = api_instance.get_inventory(product_types, is_default=is_default, is_seen=is_seen, user_id=user_id)
        print("The response of InventoryApi->get_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_types** | [**List[ProductType]**](ProductType.md)|  | 
 **is_default** | **bool**|  | [optional] 
 **is_seen** | **bool**|  | [optional] 
 **user_id** | **str**|  | [optional] 

### Return type

[**List[UserInventoryDetailed]**](UserInventoryDetailed.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_count**
> float get_item_count(product_types)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.product_type import ProductType
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.InventoryApi(api_client)
    product_types = [ledge_python_sdk.ProductType()] # List[ProductType] | 

    try:
        api_response = api_instance.get_item_count(product_types)
        print("The response of InventoryApi->get_item_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_item_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_types** | [**List[ProductType]**](ProductType.md)|  | 

### Return type

**float**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leaderboard**
> List[UserInventoryDetailed] get_leaderboard(product_types)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.product_type import ProductType
from ledge_python_sdk.models.user_inventory_detailed import UserInventoryDetailed
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.InventoryApi(api_client)
    product_types = [ledge_python_sdk.ProductType()] # List[ProductType] | 

    try:
        api_response = api_instance.get_leaderboard(product_types)
        print("The response of InventoryApi->get_leaderboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_leaderboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_types** | [**List[ProductType]**](ProductType.md)|  | 

### Return type

[**List[UserInventoryDetailed]**](UserInventoryDetailed.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_id_count**
> float get_product_id_count(product_id)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.InventoryApi(api_client)
    product_id = 'product_id_example' # str | 

    try:
        api_response = api_instance.get_product_id_count(product_id)
        print("The response of InventoryApi->get_product_id_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_product_id_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 

### Return type

**float**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spin_case**
> List[UserSpinDetailed] get_spin_case(spin_type)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.product_type import ProductType
from ledge_python_sdk.models.user_spin_detailed import UserSpinDetailed
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.InventoryApi(api_client)
    spin_type = ledge_python_sdk.ProductType() # ProductType | 

    try:
        api_response = api_instance.get_spin_case(spin_type)
        print("The response of InventoryApi->get_spin_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_spin_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spin_type** | [**ProductType**](.md)|  | 

### Return type

[**List[UserSpinDetailed]**](UserSpinDetailed.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_avatar**
> UserInventoryDetailed get_user_avatar(user_id)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.user_inventory_detailed import UserInventoryDetailed
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.InventoryApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        api_response = api_instance.get_user_avatar(user_id)
        print("The response of InventoryApi->get_user_avatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_user_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserInventoryDetailed**](UserInventoryDetailed.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_item_count**
> float get_user_item_count(user_id, product_types)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.product_type import ProductType
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.InventoryApi(api_client)
    user_id = 'user_id_example' # str | 
    product_types = [ledge_python_sdk.ProductType()] # List[ProductType] | 

    try:
        api_response = api_instance.get_user_item_count(user_id, product_types)
        print("The response of InventoryApi->get_user_item_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_user_item_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **product_types** | [**List[ProductType]**](ProductType.md)|  | 

### Return type

**float**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inventory**
> UserInventory update_inventory(inventory_id, user_inventory)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.user_inventory import UserInventory
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.InventoryApi(api_client)
    inventory_id = 'inventory_id_example' # str | 
    user_inventory = ledge_python_sdk.UserInventory() # UserInventory | 

    try:
        api_response = api_instance.update_inventory(inventory_id, user_inventory)
        print("The response of InventoryApi->update_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->update_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_id** | **str**|  | 
 **user_inventory** | [**UserInventory**](UserInventory.md)|  | 

### Return type

[**UserInventory**](UserInventory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> UserInventory update_profile(update_profile_request)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.update_profile_request import UpdateProfileRequest
from ledge_python_sdk.models.user_inventory import UserInventory
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.InventoryApi(api_client)
    update_profile_request = ledge_python_sdk.UpdateProfileRequest() # UpdateProfileRequest | 

    try:
        api_response = api_instance.update_profile(update_profile_request)
        print("The response of InventoryApi->update_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->update_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_profile_request** | [**UpdateProfileRequest**](UpdateProfileRequest.md)|  | 

### Return type

[**UserInventory**](UserInventory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

