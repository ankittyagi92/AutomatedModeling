def add_null_column(self, frame):
    self.log.info('Running add_null_column')
    frame = frame.withColumn('null_column', frame.DEDUCTIBLE)
    return frame