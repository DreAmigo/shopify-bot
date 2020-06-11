# Shopify Bot

A very simple Shopify Bot to self checkout using Python and Selenium.

## Installation

Download [chromedriver](https://chromedriver.chromium.org/) and save in the `checkout-shopify` folder.

## Usage

- Add your `user information` for the checkout.
- Change `domain` and `handle` details.
- Change `shoeSize` and `quantity`.

```
➜  checkout-shopify git:(master) ✗ python checkout-shopify.py
1. Added to the cart...
2. Selecting Shipping...
3. Filling up Payment...
4. Credit Card details ready...
5. Processing payment...

            Order #1026
          
('Checkout total: ', 26.51839303970337, 'seconds.')
```

## Information
The script was tested in the [Culture Kings](https://www.culturekings.com.au) store therefore you might need to change a few details depending on the Shopify Store.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)