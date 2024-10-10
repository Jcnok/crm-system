select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select sales_per_salesperson
from "crmdatabase_92cf"."public"."sales_per_salesperson"
where sales_per_salesperson is null



      
    ) dbt_internal_test