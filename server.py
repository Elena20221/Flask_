from flask import Flask,request, jsonify
from flask.views import MethodView
from db import Session,Advertisement
from schema import validate_create_adv
from errors import  HttpError


app= Flask('app')

@app.errorhandler(HttpError)
def error_handler(error: HttpError):
    http_response = jsonify({'message': error.message})
    http_response.status_code = error.status_code
    return http_response


class AdView(MethodView):
    def get(self, id_ad: int):
        with Session() as session:
            ad = session.query(Advertisement).filter(Advertisement.id == id_ad).first()
            return jsonify({
                'id': ad.id,
                'title': ad.title,
                'owner': ad.owner,
                'description': ad.description,
                'created_at': ad.created_at,
            })

    def post(self):
        json_data = validate_create_adv(request.json)
        with Session() as session:
            new_ad = Advertisement(**json_data)
            session.add(new_ad)
            session.commit()
            return jsonify({
                  'id': new_ad.id,
                  'title': new_ad.title,
                  'owner': new_ad.owner,
                  'description': new_ad.description,
                  'created_at': new_ad.created_at
                }
            )

    def delete(self, id_ad: str):
        json_data = validate_create_adv(request.json)
        with Session() as session:
            ad = session.query(Advertisement).filter(Advertisement.id == id_ad).first()
            session.delete(ad)
            session.commit()
            return jsonify({
                'status': 'success'
            })


app.add_url_rule('/advertisements/<int:id_ad>/', view_func=AdView.as_view('advertisements_get'), methods=['DELETE', 'GET'])
app.add_url_rule('/advertisements', view_func=AdView.as_view('advertisements'), methods=['POST'])


app.run(port=5000)
