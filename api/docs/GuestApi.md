# ledge_python_sdk.GuestApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_referral_code**](GuestApi.md#validate_referral_code) | **GET** /guest | 


# **validate_referral_code**
> str validate_referral_code(referral_code)



### Example


```python
import ledge_python_sdk
from ledge_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ledge_python_sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ledge_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ledge_python_sdk.GuestApi(api_client)
    referral_code = 'referral_code_example' # str | 

    try:
        api_response = api_instance.validate_referral_code(referral_code)
        print("The response of GuestApi->validate_referral_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestApi->validate_referral_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **referral_code** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

