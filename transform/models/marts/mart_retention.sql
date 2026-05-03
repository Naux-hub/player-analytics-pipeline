with orders as (
    select * from {{ ref('fct_orders') }}
),
player_journey as (
    select
        customer_unique_id,
        purchased_at,
        -- Nu mäter vi ordningen baserat på den UNIKA spelaren
        row_number() over (partition by customer_unique_id order by purchased_at) as session_number,
        min(purchased_at) over (partition by customer_unique_id) as first_login_at
    from orders
),
retention_stats as (
    select
        customer_unique_id,
        first_login_at,
        purchased_at as return_visit_at,
        date_diff('day', cast(first_login_at as timestamp), cast(purchased_at as timestamp)) as days_to_return
    from player_journey
    where session_number > 1 -- Vi vill bara se de som kommit tillbaka minst en gång
)
select * from retention_stats