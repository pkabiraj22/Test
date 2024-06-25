from pyspark.sql import *


if __name__ == "__main__":
    spark = SparkSession().builder \
            .appName('My App') \
            .master("local[0]") \
            .getOrCreate()
    

    data = spark.read \
            .format() \
            .``





    spark.stop()

