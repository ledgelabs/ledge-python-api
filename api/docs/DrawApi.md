# ledge_python_sdk.DrawApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_next_active_draw_schedule**](DrawApi.md#get_next_active_draw_schedule) | **GET** /draw/drawSchedule/active/{objectId} | 
[**get_previous_draw_schedules**](DrawApi.md#get_previous_draw_schedules) | **GET** /draw/drawSchedule/previous/{objectId} | 


# **get_next_active_draw_schedule**
> DrawScheduleDetailed get_next_active_draw_schedule(object_id)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.draw_schedule_detailed import DrawScheduleDetailed
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
    api_instance = ledge_python_sdk.DrawApi(api_client)
    object_id = 'object_id_example' # str | 

    try:
        api_response = api_instance.get_next_active_draw_schedule(object_id)
        print("The response of DrawApi->get_next_active_draw_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DrawApi->get_next_active_draw_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**|  | 

### Return type

[**DrawScheduleDetailed**](DrawScheduleDetailed.md)

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

# **get_previous_draw_schedules**
> List[ProcessedDrawSchedule] get_previous_draw_schedules(object_id)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.processed_draw_schedule import ProcessedDrawSchedule
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
    api_instance = ledge_python_sdk.DrawApi(api_client)
    object_id = 'object_id_example' # str | 

    try:
        api_response = api_instance.get_previous_draw_schedules(object_id)
        print("The response of DrawApi->get_previous_draw_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DrawApi->get_previous_draw_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**|  | 

### Return type

[**List[ProcessedDrawSchedule]**](ProcessedDrawSchedule.md)

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

