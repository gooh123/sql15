import sqlite3
import flask
import json
 
app = flask.Flask(__name__)


def get_by_index(index):
    with sqlite3.connect("animal.db") as connect:
        connect.row_factory = sqlite3.Row
        result = connect.execute(f'''SELECT "index", age_upon_outcome , animal_type , color, color2
                            from animals mt
                            join animal_type
                            join color
                            join color2
                            where "index" = {index}''').fetchone()

        return dict(result) 
 
@app.get('/<itemid>/')
def response(itemid):
    return app.response_class(response=json.dumps(get_by_index(itemid), ensure_ascii=False),
                              status=200,
                              mimetype='application/json'
                              )


if __name__ == '__main__':
    app.run(debug=True)

sql = 'INSERT Into color(color) values'

for color in ['orange', 'blue', 'white', 'black', 'brown', 'seal']:
    sql+= f"('{color}')"

sql=sql[:-1]

print(sql)

