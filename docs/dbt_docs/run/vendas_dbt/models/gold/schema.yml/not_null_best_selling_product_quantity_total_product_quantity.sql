select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select total_product_quantity
from "crmdatabase_92cf"."public"."best_selling_product_quantity"
where total_product_quantity is null



      
    ) dbt_internal_test