import sqlite3
import flask
import json

app = flask.Flask(__name__)


def get_by_index(index):
    with sqlite3.connect("animal.db") as connect:
        connect.row_factory = sqlite3.Row
        result = connect.execute(f"""
                                  SELECT `index`, age_upon_outcome , animal_type , color1, color2
                                  from animals 
                                  left join animal_type
                                  left join color as color1 
                                  left join color as color2 
                                  where `index` = {index}
                                  """).fetchone()

        return dict(result)


@app.get('/<itemid>/')
def response(itemid):
    return app.response_class(response=json.dumps(get_by_index(itemid), ensure_ascii=False),
                              status=200,
                              mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)

sql = 'INSERT Into color(color) values'

for color in ['orange', 'blue ', 'white', 'black', 'brown', 'brown ', 'seal', 'Breed Specific', 'blue', 'cream ', 'chocolate', 'orange ', 'silver', 'flame', 'cream', 'lynx', 'seal ', 'lilac', 'buff', 'blue cream', 'black ', 'silver lynx', 'gray', 'gray ', 'yellow', 'apricot', 'lynx ', 'chocolate ', 'silver ', 'lilac ', 'brown tiger', 'black tiger', 'tan', 'orange tiger', 'flame ', 'silver lynx ', 'sable', 'pink', 'brown merle', 'fawn']:
    sql+= f"('{color}'),"

sql=sql[:-1]

print(sql)


with sqlite3.connect("animal.db") as connection:
    connection.row_factory = sqlite3.Row
    result = connection.execute('''
                                select *
                                from color c
                                ''').fetchall()

    for i in result:
        value = dict(i)
        connection.execute(f'''
        update my_table
        set color1 = {value['id']}
        where color1 = {value['color']}
        ''')

