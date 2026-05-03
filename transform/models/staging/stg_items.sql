select
    order_id,
    order_item_id as item_number,
    product_id,
    price,
    freight_value as shipping_cost
from {{ source('ecom_raw', 'raw_items') }}