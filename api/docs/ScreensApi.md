# ledge_python_sdk.ScreensApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_banner**](ScreensApi.md#get_banner) | **GET** /screens/banner | 
[**get_screens**](ScreensApi.md#get_screens) | **GET** /screens | 


# **get_banner**
> Banner get_banner(game_id, title=title)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.banner import Banner
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
    api_instance = ledge_python_sdk.ScreensApi(api_client)
    game_id = 'game_id_example' # str | 
    title = 'title_example' # str |  (optional)

    try:
        api_response = api_instance.get_banner(game_id, title=title)
        print("The response of ScreensApi->get_banner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScreensApi->get_banner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**|  | 
 **title** | **str**|  | [optional] 

### Return type

[**Banner**](Banner.md)

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

# **get_screens**
> PaginatedScreenDetailed get_screens(name, page=page, limit=limit)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.paginated_screen_detailed import PaginatedScreenDetailed
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
    api_instance = ledge_python_sdk.ScreensApi(api_client)
    name = 'name_example' # str | 
    page = 0 # float |  (optional) (default to 0)
    limit = 10 # float |  (optional) (default to 10)

    try:
        api_response = api_instance.get_screens(name, page=page, limit=limit)
        print("The response of ScreensApi->get_screens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScreensApi->get_screens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] [default to 10]

### Return type

[**PaginatedScreenDetailed**](PaginatedScreenDetailed.md)

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

