# Parent exception if a resource doesn't exist
class ResourceNotFoundException(Exception):
    def __init__(self, resource_id, resource=None):
        self.resource = resource
        self.resource_id = resource_id


class SubjectNotFoundException(ResourceNotFoundException):
    def __init__(self, subject: str = None):
        self.subject = subject
        self.resource = "SubjectEntity"
        self.resource_id = "subject"


class CurriculaNotFoundException(ResourceNotFoundException):
    def __init__(self, curricula: str = None):
        self.curricula = curricula
        self.resource = "CurriculaEntity"
        self.resource_id = "curricula"


# Parent exception if a resource already exists
class ResourceAlreadyExistsException(Exception):
    def __init__(self, resource_id, resource=None):
        self.resource = resource
        self.resource_id = resource_id


class SubjectAlreadyExistsException(ResourceAlreadyExistsException):
    def __init__(self, subject: str = None):
        self.subject = subject
        self.resource = "SubjectEntity"
        self.resource_id = "subject"


class CurriculaAlreadyExistsException(ResourceAlreadyExistsException):
    def __init__(self, curricula: str = None):
        self.curricula = curricula
        self.resource = "CurriculaEntity"
        self.resource_id = "curricula"
