from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from model import Session, Glucose
from sqlalchemy.exc import IntegrityError
from schemas.errorSchema import ErrorSchema
from schemas.glucoseSchema import GlicoseSchemaRemove, GlucoseListSchemaResponse, GlucoseSchemaRequest, list_glucoses

info = Info(title="Health care", version="1.0.0")
app = OpenAPI(__name__, info = info)
CORS(app)

swagger_tag = Tag(name="Swagger", description="Swagger related endpoints")
glucose_tag = Tag(name="Glucose", description="Glucose related endpoints")

@app.get('/', tags=[swagger_tag])
def home():
    """
    The default route takes you to the endpoint documentation options.
    """
    return redirect('/openapi')

@app.post('/glucose', tags=[glucose_tag], 
          responses =
          {
              "200": GlucoseListSchemaResponse, "400": ErrorSchema, "409": ErrorSchema, "500": ErrorSchema
          })
def add_glucose(form: GlucoseSchemaRequest):
    """
    endpoint used to add a new glucose and returns the list of those that have already been registered.
    """

    glucose = Glucose(
        name= form.name,
        glucose= form.glucose
    )

    try:
        session = Session()
        session.add(glucose)
        session.commit()

        glucoses = session.query(Glucose).all()

        session.close()

        if not glucoses:
            return {"message": "Glucoses not found"}, 404
        else:
            return list_glucoses(glucoses), 200
    except IntegrityError as ex:
        return {"message": "Glucose already registered in the database"}, 409
    except Exception as ex:
        return {"message": "could not save"}, 500
    

@app.get('/glucoses', tags=[glucose_tag], 
         responses = 
         {
             "200": GlucoseListSchemaResponse, "404": ErrorSchema, "500": ErrorSchema
         })
def get_all_glucoses():
    """
    endpoint used to list all recorded glucoses.
    """
    try:
        session = Session()
        glucoses = session.query(Glucose).all()
        
        session.close()

        if not glucoses:
            return {"message": "Glucoses not found"}, 404
        else:
            return list_glucoses(glucoses), 200
    except Exception as ex:
        return {"message": ex}, 500

@app.delete('/glucose', tags=[glucose_tag],
            responses={"200": GlucoseListSchemaResponse, "404": ErrorSchema, "500": ErrorSchema})
def del_glicose(query: GlicoseSchemaRemove):
    """Deleta um registro de glicose
    Retorna uma lista de glicoses.
    """

    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Glucose).filter(Glucose.id == query.id).delete()
    session.commit()

    glucoses = session.query(Glucose).all()

    session.close()

    try:
        if count:
            return list_glucoses(glucoses), 200
        else:
            return {"mesage": "Glicose não encontrado."}, 404
    except Exception as ex:
        return {"message": ex}, 500