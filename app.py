
import psycopg2
from flask import Flask, request, render_template, jsonify


app = Flask(__name__, static_url_path="")

@app.route('/')
def index():
    """Return the main page."""
    return render_template('index.html')


@app.route('/store_to_db', methods=['GET', 'POST'])
def store_to_db():
    """Return a random prediction."""
    data = request.json
    conn = psycopg2.connect('dbname=diarydb')
    cur = conn.cursor()
    query = f"""
    INSERT INTO diary ( date, entry) VALUES
    ({"'" + data['user_input1'].replace("'", "")+ "'"},
     {"'"+ data['user_input2'].replace("'", "")+"'"});
    """
    cur.execute(query)
    conn.commit()
    return jsonify('diary entry saved')

