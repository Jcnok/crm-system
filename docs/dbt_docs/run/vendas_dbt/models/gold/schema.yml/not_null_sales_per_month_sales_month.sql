select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select sales_month
from "crmdatabase_92cf"."public"."sales_per_month"
where sales_month is null



      
    ) dbt_internal_test