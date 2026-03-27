from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
def test_patch_order_by_id():
    # First, create an order
    order_data = {
        "pet_id": 0
    }
    
    create_response = api_helpers.post_api_data("/store/order", order_data)
    assert create_response.status_code == 201, f"Failed to create order: {create_response.text}"
    
    order = create_response.json()
    order_id = order['id']
    
    # Now test the PATCH request
    update_data = {
        "status": "sold"
    }
    
    patch_response = api_helpers.patch_api_data(f"/store/order/{order_id}", update_data)
    
    # Validate the response code
    assert patch_response.status_code == 200
    
    # Validate the response message
    response_data = patch_response.json()
    assert response_data['message'] == "Order and pet status updated successfully"
    assert_that(response_data['message'], contains_string("Order and pet status updated successfully"))
