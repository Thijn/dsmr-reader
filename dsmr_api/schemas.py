from rest_framework.schemas.openapi import AutoSchema


class DsmrReaderSchema(AutoSchema):
    operation_mapping = None

    def __init__(self, **operation_mapping):
        super().__init__()
        self.operation_mapping = operation_mapping

    def _get_operation_id(self, path, method):
        return self.operation_mapping[method.lower()]
