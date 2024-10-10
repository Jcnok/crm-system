select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select product_revenue
from "crmdatabase_92cf"."public"."product_revenue"
where product_revenue is null



      
    ) dbt_internal_test