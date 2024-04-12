# ledge_python_sdk.CaseRewardApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_case**](CaseRewardApi.md#get_case) | **GET** /caseReward/case | 
[**get_case_reward**](CaseRewardApi.md#get_case_reward) | **GET** /caseReward/case-reward | 
[**get_cases**](CaseRewardApi.md#get_cases) | **GET** /caseReward | 
[**update_cases_to_seen**](CaseRewardApi.md#update_cases_to_seen) | **POST** /caseReward/update-cases-to-seen | 


# **get_case**
> CaseRewardDetailed get_case(game_id=game_id, product_id=product_id, opened=opened, order_by_created_at=order_by_created_at)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.case_reward_detailed import CaseRewardDetailed
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
    api_instance = ledge_python_sdk.CaseRewardApi(api_client)
    game_id = 'game_id_example' # str |  (optional)
    product_id = 'product_id_example' # str |  (optional)
    opened = True # bool |  (optional)
    order_by_created_at = 'order_by_created_at_example' # str |  (optional)

    try:
        api_response = api_instance.get_case(game_id=game_id, product_id=product_id, opened=opened, order_by_created_at=order_by_created_at)
        print("The response of CaseRewardApi->get_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseRewardApi->get_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**|  | [optional] 
 **product_id** | **str**|  | [optional] 
 **opened** | **bool**|  | [optional] 
 **order_by_created_at** | **str**|  | [optional] 

### Return type

[**CaseRewardDetailed**](CaseRewardDetailed.md)

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

# **get_case_reward**
> ProductSwap get_case_reward(case_id)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.product_swap import ProductSwap
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
    api_instance = ledge_python_sdk.CaseRewardApi(api_client)
    case_id = 'case_id_example' # str | 

    try:
        api_response = api_instance.get_case_reward(case_id)
        print("The response of CaseRewardApi->get_case_reward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseRewardApi->get_case_reward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 

### Return type

[**ProductSwap**](ProductSwap.md)

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

# **get_cases**
> PaginatedCaseRewardDetailed get_cases(game_id=game_id, product_type=product_type, opened=opened, seen=seen, page=page, limit=limit)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.paginated_case_reward_detailed import PaginatedCaseRewardDetailed
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
    api_instance = ledge_python_sdk.CaseRewardApi(api_client)
    game_id = 'game_id_example' # str |  (optional)
    product_type = [ledge_python_sdk.ProductType()] # List[ProductType] |  (optional)
    opened = True # bool |  (optional)
    seen = True # bool |  (optional)
    page = 0 # float |  (optional) (default to 0)
    limit = 10 # float |  (optional) (default to 10)

    try:
        api_response = api_instance.get_cases(game_id=game_id, product_type=product_type, opened=opened, seen=seen, page=page, limit=limit)
        print("The response of CaseRewardApi->get_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseRewardApi->get_cases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**|  | [optional] 
 **product_type** | [**List[ProductType]**](ProductType.md)|  | [optional] 
 **opened** | **bool**|  | [optional] 
 **seen** | **bool**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] [default to 10]

### Return type

[**PaginatedCaseRewardDetailed**](PaginatedCaseRewardDetailed.md)

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

# **update_cases_to_seen**
> update_cases_to_seen()



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
    api_instance = ledge_python_sdk.CaseRewardApi(api_client)

    try:
        api_instance.update_cases_to_seen()
    except Exception as e:
        print("Exception when calling CaseRewardApi->update_cases_to_seen: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

