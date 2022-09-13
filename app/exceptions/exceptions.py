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
