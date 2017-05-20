def add_null_column(self, frame):
    self.log.info('Running add_null_column')
    frame['null_column'] = None
    return frame