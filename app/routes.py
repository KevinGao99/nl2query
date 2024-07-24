from flask import request, jsonify, render_template
from app import create_app
from nl2query import MongoQuery

app = create_app()

keys = ['_id', 'index', 'ClusterID', 'Income', 'MaritalStatus', 'Name', 'Gender', 'Age', 'HouseholdSize', 'EducationLevel', 'Address', 'County', 'ZipCode', 'State', 'Country']
queryfier = MongoQuery('T5', collection_keys=keys, collection_name='Customer_Profile')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    user_query = data['query']
    
    try:
        query_result = queryfier.generate_query(user_query)
        return jsonify(query_result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
