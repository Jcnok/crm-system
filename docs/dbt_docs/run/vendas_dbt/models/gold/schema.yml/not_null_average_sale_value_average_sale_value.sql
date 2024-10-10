select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select average_sale_value
from "crmdatabase_92cf"."public"."average_sale_value"
where average_sale_value is null



      
    ) dbt_internal_test