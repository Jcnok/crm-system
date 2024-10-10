select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select total_product_revenue
from "crmdatabase_92cf"."public"."best_selling_product_value"
where total_product_revenue is null



      
    ) dbt_internal_test