class ResourceNotFoundException(Exception):
    def __init__(self, resource_id, resource=None):
        self.resource = resource
        self.resource_id = resource_id


class SubjectNotFoundException(ResourceNotFoundException):
    def __init__(self, subject: str = None):
        self.resource = "Subject"
        self.resource_id = subject


class CurriculaNotFoundException(ResourceNotFoundException):
    def __init__(self, curricula: str = None):
        self.resource = "Curricula"
        self.resource_id = curricula


class AcademicRecordNotFoundException(ResourceNotFoundException):
    def __init__(self, academic_record: str = None):
        self.resource = "Academic Record"
        self.resource_id = academic_record


class ReceiptNotFoundException(ResourceNotFoundException):
    def __init__(self, receipt: str = None):
        self.resource = "Receipt"
        self.resource_id = receipt


class ResourceAlreadyExistsException(Exception):
    def __init__(self, resource_id, resource=None):
        self.resource = resource
        self.resource_id = resource_id


class SubjectAlreadyExistsException(ResourceAlreadyExistsException):
    def __init__(self, subject: str = None):
        self.resource = "Subject"
        self.resource_id = subject


class CurriculaAlreadyExistsException(ResourceAlreadyExistsException):
    def __init__(self, curricula: str = None):
        self.resource = "Curricula"
        self.resource_id = curricula


class AcademicRecordAlreadyExistsException(ResourceAlreadyExistsException):
    def __init__(self, academic_record: str = None):
        self.resource = "Academic Record"
        self.resource_id = academic_record


class ReceiptAlreadyExistsException(ResourceAlreadyExistsException):
    def __init__(self, receipt: str = None):
        self.resource = "Receipt"
        self.resource_id = receipt
