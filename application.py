from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/application-form")
def index_page():
    """Show an index page."""

    first_name = request.form.get(firstname)
    last_name = request.form.get(lastname)
    job_choice = request.form.get(jobchoice) 
    salary = request.form.get(salary)
    
    return """
        <!DOCTYPE html>
        <html>
            <body>Thank you %s %s, for applying to be a %s. Your minimum salary is %d dollars.
            </body>
        </html>
       """%(first_name, last_name, job_choice, salary)

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

