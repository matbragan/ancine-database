{{
    config(
        materialized = 'table',
    )
}}

select *
from {{ source('ancine', 'obras_crt') }}
limit 5