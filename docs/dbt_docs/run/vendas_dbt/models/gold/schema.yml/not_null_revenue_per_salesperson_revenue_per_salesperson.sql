select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select revenue_per_salesperson
from "crmdatabase_92cf"."public"."revenue_per_salesperson"
where revenue_per_salesperson is null



      
    ) dbt_internal_test