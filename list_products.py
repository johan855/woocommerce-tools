
from woocommerce import API


def get_list(pages):
    key = 'consumer_key'
    secret = 'consumer_secret'
    url = 'url'
    wcapi = API(
        url=url,
        consumer_key=key,
        consumer_secret=secret,
        wp_api=True
    )

    response = ''
    list_of_products = []
    pages = 10

    for x in range(0, pages):
        response = wcapi.get("products?page={0}".format(x)).json()
        for product in response['products']:
            list_of_products.append(product['id'])
    return list_of_products
