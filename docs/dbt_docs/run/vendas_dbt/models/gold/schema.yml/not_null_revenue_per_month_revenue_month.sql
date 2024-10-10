select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select revenue_month
from "crmdatabase_92cf"."public"."revenue_per_month"
where revenue_month is null



      
    ) dbt_internal_test