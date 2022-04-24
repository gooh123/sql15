import sqlite3
import flask
import json

app = flask.Flask(__name__)


def get_by_index(index):
    with sqlite3.connect("animal.db") as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(f'''SELECT *
                            from animals a
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
