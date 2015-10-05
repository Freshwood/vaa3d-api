from flask import jsonify, request

from . import api
from ..models.task import Task
from ..schemas.task import task_schema, tasks_schema


@api.route('/tasks', methods=['GET'])
def get_tasks():
    return "hello, world!"


@api.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    return "hello, " + str(id)


@api.route('/tasks', methods=['POST'])
def create_task():
    pass


@api.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    pass


@api.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    pass
