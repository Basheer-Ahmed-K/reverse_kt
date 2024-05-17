# Databricks notebook source
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType, MapType
from pyspark.sql.functions import explode, explode_outer, posexplode, posexplode_outer

# COMMAND ----------

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("emails", ArrayType(StringType(), True), True),
])

data = [
    (1, 'Basheer', ['basheer@gmail.com', 'basheer@diggibyte.com']),
    (2, 'ahmed', []),
    (3, 'logesh', ['logesh@gmail.com']),
]

# COMMAND ----------

df = spark.createDataFrame(data, schema)
display(df)

# COMMAND ----------

explode_df = df.withColumn('email', explode('emails')).drop('emails')
display(explode_df)

# COMMAND ----------

explode_outer_df = df.withColumn("email", explode_outer("emails")).drop("emails")
display(explode_outer_df)

# COMMAND ----------

posexplode_df = df.select("*",posexplode("emails")).drop("emails")
display(posexplode_df)

# COMMAND ----------

posexplode_outer_df = df.select("*", posexplode_outer("emails")).drop("emails")
display(posexplode_outer_df)

# COMMAND ----------

from pyspark.sql.functions import from_json, to_json

json_data = '{"name": "John", "age": 30}'

schema = "name STRING, age INT"
# schema = MapType(StringType(),StringType())

df_json = spark.createDataFrame([(json_data,)], ["json"])
display(df_json)
df_parsed = df_json.select(from_json("json", schema).alias("data"))
display(df_parsed)

# COMMAND ----------

# Convert struct to JSON
df_to_json = df_parsed.select(to_json("data").alias("json"))
display(df_to_json)
