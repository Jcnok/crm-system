select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select average_products_per_sale
from "crmdatabase_92cf"."public"."average_products_per_sale"
where average_products_per_sale is null



      
    ) dbt_internal_test