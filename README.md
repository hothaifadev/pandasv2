# Pandas ai

>the pandas ai is a tool that allows you to interact with your data using natural language queries. It uses OpenAI's GPT-3 model to generate SQL queries based on your input.

## How it works
* connect database for this tool and analyze data using Open ai
* optimize the reports using this tool
* generate the SQL queries using this tool (prompt automatically)

fgmm database is not clean and we have issue  when pandas ai generate the code it will be generate the queries 
for example i founded 

- table invoice_deials the pandas ai generate the code 
```sql
SELECT * FROM invoice_details -- correct spelling
```
- status column in all tables
```sql
SELECT * FROM invoice_details WHERE status = 'completed' -- in fgmm status columns its boolean (true/false)
```


## Fix issues

we have two options
1. resolve database and clean the data
2. resolve pandas ai code generation but for now i don't know how to do that (no clear pandasai documentation)



## About Project

- Generate reports using postgresql Database
- Generate reports using prompt
- save prompt and optimize it using openai prompt (beta)