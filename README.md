# Vending-Machine
- This is vending machine app built via Django (Python).
- Simple operations include product selection, payment and validation.

# Prerequisite
### Docker
- https://www.docker.com/products/docker-desktop/

# Related screenshot

### Product selection
- URL: http://localhost:8000/vending/v1/
- Selection of all product list.
> ![alt text](static_global/readme/product_select.png)

### Payment checkout
- URL: http://localhost:8000/vending/checkout/
- Payment checkout page for multiple payment method.
> ![alt text](static_global/readme/checkout.png)
> ![alt text](static_global/readme/checkout_card.png)

### Payment result
- URL: http://localhost:8000/vending/pay/
- Payment validation and result.
> ![alt text](static_global/readme/pay_result.png)

### Block direct access
- Block all direct access to intermediate page.
> ![alt text](static_global/readme/403.png)

### [Validation] Item price
- Validate actual price of item from global values.
> ![alt text](static_global/readme/not_found.png)

### [Validation] Cash amount
- Validate cash amount inserted by buyer.
> ![alt text](static_global/readme/cash_amt.png)
> ![alt text](static_global/readme/cash_amt2.png)

