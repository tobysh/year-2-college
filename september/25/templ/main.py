from flask import Flask, render_template, abort
import os
app = Flask(__name__)

shopname = "shopmore"
pages = []
for page in os.listdir("./templates"):
    pages.append(page.split(".")[0])
print(pages)
@app.route("/<page>")
def show(page):
    if page in pages:
        return render_template(f"{page}.html", shopname=shopname, pagename=page)
    else:
        abort(404)

@app.errorhandler(404)
def page_not_found():
    return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True)