select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select average_ticket
from "crmdatabase_92cf"."public"."average_ticket"
where average_ticket is null



      
    ) dbt_internal_test