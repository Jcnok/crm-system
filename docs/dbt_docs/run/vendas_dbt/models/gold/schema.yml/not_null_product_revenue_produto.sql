select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select produto
from "crmdatabase_92cf"."public"."product_revenue"
where produto is null



      
    ) dbt_internal_test