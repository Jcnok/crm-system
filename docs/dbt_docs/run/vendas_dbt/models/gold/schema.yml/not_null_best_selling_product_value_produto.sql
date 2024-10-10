select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select produto
from "crmdatabase_92cf"."public"."best_selling_product_value"
where produto is null



      
    ) dbt_internal_test