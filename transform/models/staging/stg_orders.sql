select
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp as purchased_at,
    order_approved_at as approved_at
from {{ source('ecom_raw', 'raw_orders') }}