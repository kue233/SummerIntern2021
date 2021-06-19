from flask import Flask,render_template,redirect,session,make_response,jsonify,request
from GraphFunc import CreateGraph

app = Flask(__name__)
app.debug=True


@app.route("/index",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        ticker = request.form.get('ticker')
        CreateGraph().createGraphs(ticker)
        print(request.form.get('ticker'))
        if request.form.get('back')=='back':
            return render_template('yfIndex.html')
        return render_template('yfIndex_result.html',ticker=ticker)
    print(request.method)
    return render_template('yfIndex.html')


if __name__ =='__main__':
    app.run()