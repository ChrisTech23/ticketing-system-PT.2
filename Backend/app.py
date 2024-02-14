from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Example in-memory database (replace with your actual database setup)
tickets = [
    {"id": 1, "title": "Ticket 1", "description": "This is ticket 1", "status": "Open"},
    {"id": 2, "title": "Ticket 2", "description": "This is ticket 2", "status": "Open"},
]

# Route to fetch all tickets
@app.route('/tickets/id', methods=['GET'])
def get_tickets():
    return jsonify(tickets)

# Route to create a new ticket
@app.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.json
    new_ticket = {
        "id": data["id"],
        "title": data["title"],
        "description": data["description"],
        "status": "Open"
    }
    tickets.append(new_ticket)
    return jsonify(new_ticket), 201

# Route to update a ticket's status
@app.route('/update/<id>', methods=['PUT'])
def update_ticket_status(id):
    # Function implementation
    for ticket in tickets:
        if ticket["id"] == id:
            ticket["status"] = request.json["status"]
            return jsonify(ticket)
    return jsonify({"error": "Ticket not found"}), 404

# Route to delete a ticket
@app.route('/tickets/<int:id>/delete', methods=['DELETE'])
def delete_ticket(id):
    for ticket in tickets:
        if ticket["id"] == id:
            tickets.remove(ticket)
            return jsonify({"message": "Ticket deleted"})
    return jsonify({"error": "Ticket not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
