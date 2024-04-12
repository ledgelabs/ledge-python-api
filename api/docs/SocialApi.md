# ledge_python_sdk.SocialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connect_social**](SocialApi.md#connect_social) | **POST** /social/connect-social | 
[**create_wallet_connection**](SocialApi.md#create_wallet_connection) | **GET** /social/connect-wallet | 
[**get_connected_social**](SocialApi.md#get_connected_social) | **GET** /social/connected-social | 
[**get_connected_socials**](SocialApi.md#get_connected_socials) | **GET** /social/connected-socials | 
[**get_profile**](SocialApi.md#get_profile) | **GET** /social/profile | 
[**remove_connected_social**](SocialApi.md#remove_connected_social) | **DELETE** /social/connected-social | 


# **connect_social**
> ConnectedSocial connect_social(token, quest_schedule_id=quest_schedule_id, goal_id=goal_id)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.connected_social import ConnectedSocial
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
    api_instance = ledge_python_sdk.SocialApi(api_client)
    token = 'token_example' # str | 
    quest_schedule_id = 'quest_schedule_id_example' # str |  (optional)
    goal_id = 'goal_id_example' # str |  (optional)

    try:
        api_response = api_instance.connect_social(token, quest_schedule_id=quest_schedule_id, goal_id=goal_id)
        print("The response of SocialApi->connect_social:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialApi->connect_social: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **quest_schedule_id** | **str**|  | [optional] 
 **goal_id** | **str**|  | [optional] 

### Return type

[**ConnectedSocial**](ConnectedSocial.md)

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

# **create_wallet_connection**
> Dict[str, object] create_wallet_connection(wallet_id)



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
    api_instance = ledge_python_sdk.SocialApi(api_client)
    wallet_id = 'wallet_id_example' # str | 

    try:
        api_response = api_instance.create_wallet_connection(wallet_id)
        print("The response of SocialApi->create_wallet_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialApi->create_wallet_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **get_connected_social**
> UserConnection get_connected_social(social_id=social_id, user_id=user_id, connection_type=connection_type)



Requires at least socialId or userId AND connectionType

### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.connection_type import ConnectionType
from ledge_python_sdk.models.user_connection import UserConnection
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
    api_instance = ledge_python_sdk.SocialApi(api_client)
    social_id = 'social_id_example' # str |  (optional)
    user_id = 'user_id_example' # str |  (optional)
    connection_type = ledge_python_sdk.ConnectionType() # ConnectionType |  (optional)

    try:
        api_response = api_instance.get_connected_social(social_id=social_id, user_id=user_id, connection_type=connection_type)
        print("The response of SocialApi->get_connected_social:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialApi->get_connected_social: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_id** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **connection_type** | [**ConnectionType**](.md)|  | [optional] 

### Return type

[**UserConnection**](UserConnection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | a UserConnection or null if not found |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connected_socials**
> List[UserConnection] get_connected_socials(id=id, connection_types=connection_types)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.connection_type import ConnectionType
from ledge_python_sdk.models.user_connection import UserConnection
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
    api_instance = ledge_python_sdk.SocialApi(api_client)
    id = 'id_example' # str |  (optional)
    connection_types = [ledge_python_sdk.ConnectionType()] # List[ConnectionType] |  (optional)

    try:
        api_response = api_instance.get_connected_socials(id=id, connection_types=connection_types)
        print("The response of SocialApi->get_connected_socials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialApi->get_connected_socials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **connection_types** | [**List[ConnectionType]**](ConnectionType.md)|  | [optional] 

### Return type

[**List[UserConnection]**](UserConnection.md)

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

# **get_profile**
> GetProfile200Response get_profile(token)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.get_profile200_response import GetProfile200Response
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
    api_instance = ledge_python_sdk.SocialApi(api_client)
    token = 'token_example' # str | 

    try:
        api_response = api_instance.get_profile(token)
        print("The response of SocialApi->get_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialApi->get_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**GetProfile200Response**](GetProfile200Response.md)

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

# **remove_connected_social**
> UserConnection remove_connected_social(social_id=social_id, user_id=user_id, connection_type=connection_type, user_connection_id=user_connection_id)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.connection_type import ConnectionType
from ledge_python_sdk.models.user_connection import UserConnection
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
    api_instance = ledge_python_sdk.SocialApi(api_client)
    social_id = 'social_id_example' # str |  (optional)
    user_id = 'user_id_example' # str |  (optional)
    connection_type = ledge_python_sdk.ConnectionType() # ConnectionType |  (optional)
    user_connection_id = 'user_connection_id_example' # str |  (optional)

    try:
        api_response = api_instance.remove_connected_social(social_id=social_id, user_id=user_id, connection_type=connection_type, user_connection_id=user_connection_id)
        print("The response of SocialApi->remove_connected_social:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SocialApi->remove_connected_social: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_id** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **connection_type** | [**ConnectionType**](.md)|  | [optional] 
 **user_connection_id** | **str**|  | [optional] 

### Return type

[**UserConnection**](UserConnection.md)

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

