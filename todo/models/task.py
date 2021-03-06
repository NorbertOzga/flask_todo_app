from marshmallow import fields

from todo.extension import database, marshmallow
from todo.validators.common import cannot_be_empty
from todo.validators.task import is_in_allowed_priority_range


class Task(database.Model):
    __tablename__ = 'tasks'

    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer,
                              database.ForeignKey(
                                  'users.id',
                                  ondelete='CASCADE'
                              ),
                              nullable=False)
    title = database.Column(database.String, nullable=False)
    description = database.Column(database.String, nullable=True)
    priority = database.Column(database.Integer, nullable=False)
    add_time = database.Column(database.DateTime, nullable=False)
    active = database.Column(database.Boolean, default=True)


class TaskSchema(marshmallow.Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(validate=[cannot_be_empty])
    title = fields.String(validate=[cannot_be_empty])
    description = fields.String()
    priority = fields.Integer(validate=[is_in_allowed_priority_range])
    add_time = fields.DateTime(dump_only=True)
    active = fields.Boolean(default=True)


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
