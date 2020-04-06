from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
   return render_template('hw4pre.html')

@app.route('/orders', methods=['post'])

def write_orders():
    name_receive = request.form['name_give']
    qty_receive = request.form['qty_give']
    addr_receive = request.form['addr_give']
    phone_receive = request.form['addr_give']
    order = {
        'name': name_receive,
        'qty': qty_receive,
        'addr': addr_receive,
        'phone': phone_receive
    }

    db.orders.insert_one(order)

    return jsonify({'result':'success', 'msg':'주문이 성공적으로 완료되었습니다.'})


@app.route('/orders')
def find_orders():

    orders = list(db.orders.find({}, {'_id':0}))
    return jsonify({'result': 'success', 'msg':'주문을 조회하였습니다.', 'reviews':orders})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)