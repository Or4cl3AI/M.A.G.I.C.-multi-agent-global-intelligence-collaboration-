## user_interface.py
from flask import Flask, request, jsonify
from memory_module import MemoryModule

class UserInterface:
    def __init__(self, task: str = None):
        self.task = task
        self.memory_module = MemoryModule()
        self.app = Flask(__name__)

        @self.app.route('/task', methods=['POST'])
        def input_task():
            self.task = request.json.get('task')
            return jsonify({'message': 'Task input successful'}), 200

        @self.app.route('/progress', methods=['GET'])
        def monitor_progress():
            # Placeholder for progress monitoring implementation
            progress = "Progress data"
            return jsonify({'progress': progress}), 200

        @self.app.route('/feedback', methods=['POST'])
        def provide_feedback():
            feedback = request.json.get('feedback')
            self.memory_module.store_information(feedback)
            return jsonify({'message': 'Feedback received'}), 200

    def run(self, host: str = '0.0.0.0', port: int = 5000):
        self.app.run(host=host, port=port)
