from storage import Storage

class ElasticSearchStorage(Storage):
    def __init__(self, config_dict):
        self.db = config_dict['database']
        self.host = config_dict['host']
        self.port = config_dict['port']
        self.username = config_dict['username']
        self.password = config_dict['password']
        self.index = config_dict['index']
        self.doc_type = config_dict['doc_type']

    def store(self, task):
        return 'Task ID'

    def get_task(self, task_id):
        return {1: {'task': 'data'}}

    def get_report(self, report_id):
        return {1: {'report': 'data'}}

    def delete(self, task_id):
        return {'Message': 'deleted'}
