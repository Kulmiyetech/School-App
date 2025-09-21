from flask import Flask, render_template, redirect, request, url_for
from supabase import create_client, client
url ='https://jmmfhogtdpldhqwmhdgd.supabase.co'
key ='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptbWZob2d0ZHBsZGhxd21oZGdkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTg0NjMwNzMsImV4cCI6MjA3NDAzOTA3M30.GlzML887SKKK4hrIXPIyxRrhrfvXP1o9CpWKKtXF46I'
supabase: client = create_client(url, key)
app= Flask(__name__)


@app.route('/')
def index():
    data = supabase.table('students').select('*').execute()
    students = data.data
    return render_template('index.html', students= students)


@app.route('/add_student', methods= ['POST'])
def add_student():
    name = request.form['name']
    faculty = request.form['faculty']
    semester = request.form['semester']
    supabase.table('students').insert({
        'name': name, 
        'faculty': faculty,
        'semester':semester

    }).execute()
    return redirect('/')

@app.route('/delete_student/<int:id>')
def delete_student(id):
    supabase.table('students').delete().eq('id', id).execute()
    return redirect('/')

@app.route('/edit_student/<int:id>')
def edit_student(id):
    student = supabase.table('students').select('*').eq('id', id).single().execute().data
    return render_template('edit.html', student= student)


@app.route('/update_student/<int:id>', methods = ['POST'])
def update_student(id):
    name = request.form['name']
    faculty = request.form['faculty']
    semester = request.form['semester']
    supabase.table('students').update({
        'name': name,
        'faculty': faculty,
        'semester': semester
    }).eq('id', id).execute()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
