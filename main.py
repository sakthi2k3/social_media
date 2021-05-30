from flask import Flask, render_template,request
import  requests
from script import create_table,data_entry,fech_data
create_table()

app=Flask(
    __name__,
    template_folder="client/template",
    static_folder="client/static",

)



@app.route('/' , methods=['GET','POST'])
def start():
    if request.method =='GET':
        data=fech_data()
        return render_template('index.html',people=data)

    else:
        dis={}
        dis["name"]=request.form['name']
        dis["post"]=request.form['post']
        data_entry(dis["name"],dis["post"])
        data=fech_data()
        return render_template('index.html',people=data)



if __name__ == "__main__":
    app.run(debug=True)
    