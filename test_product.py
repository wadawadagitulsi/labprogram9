from product import product_info

def test_product_info():
    result = product_info(101, "Laptop", 2, 45000)

    expected = "Product ID: 101\nName: Laptop\nQuantity: 2\nPrice: 45000"

    assert result == expected
    
