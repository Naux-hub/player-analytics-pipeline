with orders as (
    select * from {{ ref('stg_orders') }}
),
customers as (
    select * from {{ ref('stg_customers') }}
),
items as (
    select * from {{ ref('stg_items') }}
),
final as (
    select
        o.order_id,
        o.customer_id,
        c.customer_unique_id, -- <--- DETTA ÄR NYCKELN!
        o.order_status,
        o.purchased_at,
        c.city,
        c.state,
        i.price,
        i.shipping_cost,
        i.price + i.shipping_cost as total_order_value
    from orders o
    left join customers c on o.customer_id = c.customer_id
    left join items i on o.order_id = i.order_id
)
select * from final