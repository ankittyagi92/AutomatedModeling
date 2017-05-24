from pyspark import SparkConf

def build_spark_config(spark_config, log):
    conf = SparkConf()
    conf_dict = {
        "spark.executor.memory": spark_config.executor_memory
    }
    if spark_config.dynamicAllocation_enabled:
        temp_dict = {
            "spark.dynamicAllocation.enabled": spark_config.dynamicAllocation_enabled,
            "spark.dynamicAllocation.initialExecutors": spark_config.dynamicAllocation_initialExecutors,
            "spark.dynamicAllocation.executoIdleTimeout": spark_config.dynamicAllocation_executoIdleTimeout,
            "spark.dynamicAllocation.minExecutors": spark_config.dynamicAllocation_minExecutors,
            "spark.dynamicAllocation.maxExecutors": spark_config.dynamicAllocation_maxExecutors
        }
    else:
        temp_dict = {
            "spark.executor.instances": spark_config.executor_instances
        }
    conf_dict.update(temp_dict)
    for spark_key, value in conf_dict.items():
        log.info("Setting spark config param: %s to %s" %(spark_key, value))
        conf.set(spark_key, value)
    return conf