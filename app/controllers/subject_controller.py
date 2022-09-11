from flask import request

from app.entities.subject_entity import SubjectEntity


class SubjectController:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_subject_by_id(self, subject: SubjectEntity):
        """"Get subject by subject id"""
        try:
            todo_id = request.args.get(subject.code)
            if todo_id:
                return self.db_session.document(todo_id).get()
            else:
                return [doc.to_dict() for doc in self.db_session.stream()]

        except Exception as e:
            return f"An error Occurred: {e}"

    def create_subject(self, new_subject: SubjectEntity):
        """"Create new subject"""
        try:
            todo_id = request.args.get(new_subject.code)
            if todo_id:
                return self.db_session.document(todo_id).set(request.json)
        except Exception as e:
            return f"An error Occurred: {e}"
