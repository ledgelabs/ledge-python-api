# ledge_python_sdk.ProductApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_products**](ProductApi.md#get_products) | **GET** /product | 
[**get_swappable_product**](ProductApi.md#get_swappable_product) | **GET** /product/swap-product/{productId} | 
[**get_swappable_products**](ProductApi.md#get_swappable_products) | **GET** /product/swappable-products | 


# **get_products**
> List[Product] get_products(product_types=product_types)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.product import Product
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
    api_instance = ledge_python_sdk.ProductApi(api_client)
    product_types = [ledge_python_sdk.ProductType()] # List[ProductType] |  (optional)

    try:
        api_response = api_instance.get_products(product_types=product_types)
        print("The response of ProductApi->get_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->get_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_types** | [**List[ProductType]**](ProductType.md)|  | [optional] 

### Return type

[**List[Product]**](Product.md)

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

# **get_swappable_product**
> Product get_swappable_product(product_id)



### Example

* Api Key Authentication (api_key):

```python
import ledge_python_sdk
from ledge_python_sdk.models.product import Product
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
    api_instance = ledge_python_sdk.ProductApi(api_client)
    product_id = 'product_id_example' # str | 

    try:
        api_response = api_instance.get_swappable_product(product_id)
        print("The response of ProductApi->get_swappable_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->get_swappable_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 

### Return type

[**Product**](Product.md)

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

# **get_swappable_products**
> List[ProductSwap] get_swappable_products(product_id, order_qty_by=order_qty_by, order_chance_by=order_chance_by)



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
    api_instance = ledge_python_sdk.ProductApi(api_client)
    product_id = 'product_id_example' # str | 
    order_qty_by = 'order_qty_by_example' # str |  (optional)
    order_chance_by = 'order_chance_by_example' # str |  (optional)

    try:
        api_response = api_instance.get_swappable_products(product_id, order_qty_by=order_qty_by, order_chance_by=order_chance_by)
        print("The response of ProductApi->get_swappable_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductApi->get_swappable_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 
 **order_qty_by** | **str**|  | [optional] 
 **order_chance_by** | **str**|  | [optional] 

### Return type

[**List[ProductSwap]**](ProductSwap.md)

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

