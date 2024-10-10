select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select revenue_year
from "crmdatabase_92cf"."public"."revenue_per_year"
where revenue_year is null



      
    ) dbt_internal_test