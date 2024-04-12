# ledge_python_sdk.TransactionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_transactions**](TransactionApi.md#get_all_transactions) | **GET** /transaction | 


# **get_all_transactions**
> PaginatedTransactionDetailed get_all_transactions(sell_product_type=sell_product_type, sell_product_id=sell_product_id, page=page, limit=limit)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.paginated_transaction_detailed import PaginatedTransactionDetailed
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
    api_instance = ledge_python_sdk.TransactionApi(api_client)
    sell_product_type = [ledge_python_sdk.ProductType()] # List[ProductType] |  (optional)
    sell_product_id = 'sell_product_id_example' # str |  (optional)
    page = 0 # float |  (optional) (default to 0)
    limit = 10 # float |  (optional) (default to 10)

    try:
        api_response = api_instance.get_all_transactions(sell_product_type=sell_product_type, sell_product_id=sell_product_id, page=page, limit=limit)
        print("The response of TransactionApi->get_all_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionApi->get_all_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sell_product_type** | [**List[ProductType]**](ProductType.md)|  | [optional] 
 **sell_product_id** | **str**|  | [optional] 
 **page** | **float**|  | [optional] [default to 0]
 **limit** | **float**|  | [optional] [default to 10]

### Return type

[**PaginatedTransactionDetailed**](PaginatedTransactionDetailed.md)

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

