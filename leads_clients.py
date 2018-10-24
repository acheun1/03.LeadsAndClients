#Assignment: Leads and Clients
#2018 10 09
#Cheung Anthony

# You should pull appropriate information from the database to generate the table and the graph.  Once you retrieve all the information for 'all time', then allow the user to change the reporting date range by adjusting the two dates on the top right.  This assignment can be a bit difficult but teaches a lot of great lessons that could save you lots of time later when you're working on real complex projects.

from flask import Flask, render_template, redirect, request, session, flash

from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key='as43df46asd3f4as4'

@app.route('/')
def index():
    mysql = connectToMySQL('leads_clients')
    # report = mysql.query_db("SELECT * FROM reporting")
    report = mysql.query_db("SELECT customer_name,cnt AS count FROM reporting group by customer_name")
    cnt=len(report)
    return render_template('index.html',front_report=report,loopcnt=cnt)

# @app.route('/update_records', methods=['POST'])
# def update():
#     mysql = connectToMySQL('cr')
#     insert_query="INSERT INTO user (name_first, name_last, occupation, created_at, updated_at) VALUES (%(name_first)s, %(name_last)s, %(occupation)s, NOW(), NOW());"
#     record = {
#                 'name_first':request.form['q1'],
#                 'name_last':request.form['q2'],
#                 'occupation':request.form['q3'],
#             }
#     new_record_id=mysql.query_db(insert_query, record)
#     return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
