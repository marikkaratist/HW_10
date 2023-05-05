from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")
def page_index():

    candidates = utils.get_all()
    page_content = utils.build_preformatted_list(candidates)

    return page_content


@app.route("/candidates/<int:pk>")
def page_candidate(pk):

    candidate = utils.get_by_pk(pk)
    candidates = [candidate]
    page_content = f"<img src='{candidate['picture']}'>"
    page_content += utils.build_preformatted_list(candidates)

    return page_content


@app.route("/skills/<skill_name>")
def page_skill(skill_name):

    candidates = utils.get_by_skill(skill_name)
    page_content = utils.build_preformatted_list(candidates)

    return page_content


app.run()
