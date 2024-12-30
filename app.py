from flask import Flask, render_template,request

car_list = [
    {"id": 1, "name": "Toyota"},
    {"id": 2, "name": "Honda"},
    {"id": 3, "name": "BMW"},
    {"id": 4, "name": "Audi"}]

app = Flask(__name__)
# CRUD

# R -  READ
@app.route("/")
def cars():
    return render_template("index.html",cars=car_list)


# C - Create
@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else: #POST
        
        # when working with form
        # title = request.form['title']
        # print(title)
        # description = request.form['description']

        # when sending with axios (json)

        data = request.get_json()
        title = data.get('title')
        print(title)
        car_list.append({"id": len(car_list), "name": title},)
        return render_template("index.html",cars=car_list)
    
if __name__ == "__main__":
    app.run(debug=True)