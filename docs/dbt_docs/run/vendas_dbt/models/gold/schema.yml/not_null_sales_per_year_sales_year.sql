select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select sales_year
from "crmdatabase_92cf"."public"."sales_per_year"
where sales_year is null



      
    ) dbt_internal_test