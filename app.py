from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from calculate import calculaterBETA

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("main.html")

global file_readx, fx_content, a, b, c, d, e, f, g, h

# @app.route('/sendparameter1')
# def sendparameter():
#     a = request.args.get('a', type=float)
#     b = request.args.get('b', type=float)
#     c = request.args.get('c', type=float)
#     d = request.args.get('d', type=float)
#     e = request.args.get('e', type=float)
#     f = request.args.get('f', type=float)
#     g = request.args.get('g', type=float)
#     h = request.args.get('h', type=float)
#     print("param1 is: ", a)
#     print("param2 is: ", b)
#     print("param3 is: ", c)
#     print("param4 is: ", d)
#     print("param5 is: ", e)
#     print("param6 is: ", f)
#     print("param7 is: ", g)
#     print("param8 is: ", h)
#     return jsonify(
#         resulta=['Parameter1', 'Parameter2', 'Parameter3', 'Parameter4', 'Parameter5', 'Parameter6', 'Parameter7',
#                  'Parameter8'], resultb=[a, b, c, d, e, f, g, h])

@app.route('/single-file-upload', methods=['POST'])
def upload_file():
    fx = request.files['singlefiles']
    fx.save(os.path.join(app.root_path, 'uploaded_single_file', secure_filename(fx.filename)))
    errors = {}
    success = False

    with open(os.path.join(app.root_path, 'uploaded_single_file', secure_filename(fx.filename)), 'r') as file:
        fx_content = file.read()
        success = True
    print(fx_content, type(fx_content).__name__)


    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        resp = jsonify(resultsingle=fx_content)
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp


@app.route('/multiple-files-string-upload', methods=['POST'])
def upload_file_string():
    if 'files[]' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    d = float(request.form['d'])
    e = float(request.form['e'])
    f = float(request.form['f'])
    g = float(request.form['g'])
    h = float(request.form['h'])
    print("param1 is: ", a)
    print("param2 is: ", b)
    print("param3 is: ", c)
    print("param4 is: ", d)
    print("param5 is: ", e)
    print("param6 is: ", f)
    print("param7 is: ", g)
    print("param8 is: ", h)

    files = request.files.getlist('files[]')
    errors = {}
    success = False

    file_readx=""
    num: int = 0

    for file_read in files:
        file_read.save(os.path.join(app.root_path, 'uploaded_files', secure_filename(file_read.filename)))
        with open(os.path.join(app.root_path, 'uploaded_files', secure_filename(file_read.filename)), 'r') as file:
            file_content = file.read()
            print(file_content, type(file_content).__name__)
        file_readx=file_readx+"File No. "+str((num+1))+": \n"+file_content+"\n"
        num=num+1
        success = True
    print(file_readx)

    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        resp = jsonify(
            resultparamname=['Parameter1', 'Parameter2', 'Parameter3', 'Parameter4', 'Parameter5', 'Parameter6', 'Parameter7',
                     'Parameter8'], resultparamval=[a, b, c, d, e, f, g, h], resultmulti=file_readx)
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp


@app.route('/run-script', methods=['POST'])
def run_script():

    avar = float(request.form['senda'])
    bvar = float(request.form['sendb'])
    cvar = float(request.form['sendc'])
    dvar = float(request.form['sendd'])
    evar = float(request.form['sende'])
    fvar = float(request.form['sendf'])
    gvar = float(request.form['sendg'])
    hvar = float(request.form['sendh'])
    print("sent param1 is: ", avar)
    print("sent param2 is: ", bvar)
    print("sent param3 is: ", cvar)
    print("sent param4 is: ", dvar)
    print("sent param5 is: ", evar)
    print("sent param6 is: ", fvar)
    print("sent param7 is: ", gvar)
    print("sent param8 is: ", hvar)
    multistrvar=str(request.form['sendmultistr'])
    singlestrvar = str(request.form['sendsinglestr'])
    print("sent multistrvar is: \n", multistrvar)
    print("sent singlestrvar is: \n", singlestrvar)

    resp = jsonify(result="success")
    resp.status_code = 201
    return resp



# @app.route("/sendparameter", methods=["POST"])
# def sendParameter():
# global firstp, secondp, thirdp
# firstp = float(request.form["params"])
# secondp=float(request.form["paramf"])
##print("second parameter: ", secondp)
# thirdp= (request.form["filef"])
# print("first parameter: ", firstp)
# print("second parameter: ", secondp)
##print("Third parameter: ", thirdp)
# f = request.files['filef']
# f.save(os.path.join(app.root_path, 'uploaded_files', secure_filename(f.filename)))
# print ('file uploaded successfully')
# calculaterBETA(firstp, secondp)
# return redirect(request.referrer)

# @app.route("/<varb>/")
# def usecase(varb):
#    return f"Hello {varb}"

# @app.route("/admin")
# def admin():
#    return redirect(url_for("usecase", varb="admin!"))

if __name__ == '__main__':
    app.run(debug=True)
