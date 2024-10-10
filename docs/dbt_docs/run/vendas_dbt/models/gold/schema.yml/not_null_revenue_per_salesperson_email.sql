select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select email
from "crmdatabase_92cf"."public"."revenue_per_salesperson"
where email is null



      
    ) dbt_internal_test