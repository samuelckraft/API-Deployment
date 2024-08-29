from flask import Flask, request, jsonify


app = Flask(__name__)

sums = []

@app.route('/sum', methods=["POST"])
def sum():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2
    sums.append(result)

    return jsonify({'result': result})

@app.route('/sum/result/<int>', methods=['GET'])
def get_sums(int):
    answer = ''
    for sum in sums:
        if sum <= int:
            answer + sum + ', '

    return answer


if __name__ == '__main__':
    app.run(debug=True)