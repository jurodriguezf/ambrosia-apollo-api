class SubjectNotFoundException(Exception):
    def __init__(self, subject: str = None, message="Subject not found"):
        self.subject = subject
        self.message = message
        super().__init__(self.message)


class SubjectAlreadyExistsException(Exception):
    def __init__(self, subject: str = None, message="Subject already exists"):
        self.subject = subject
        self.message = message
        super().__init__(self.message)


class CurriculaNotFoundException(Exception):
    def __init__(self, curricula: str = None, message="Curricula not found"):
        self.curricula = curricula
        self.message = message
        super().__init__(self.message)


class CurriculaAlreadyExistsException(Exception):
    def __init__(self, curricula: str = None, message="Curricula already exists"):
        self.curricula = curricula
        self.message = message
        super().__init__(self.message)
