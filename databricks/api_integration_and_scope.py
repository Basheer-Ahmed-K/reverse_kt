# Databricks notebook source
import requests

# COMMAND ----------

# DBTITLE 1,GET REQUEST
response = requests.get("https://reqres.in/api/users?page=2")
display(response.json())

# COMMAND ----------

# DBTITLE 1,POST REQUEST
post_res = requests.post("https://reqres.in/api/users", 
    {
        "name": "morpheus",
        "job": "leader"
    })
print(post_res.json())

# COMMAND ----------

jdbc_token = dbutils.secrets.get("JdbcSecretScope", "JdbcTonen")

for char in jdbc_token:
    print(char, end=" ")

# COMMAND ----------

print(jdbc_token)
