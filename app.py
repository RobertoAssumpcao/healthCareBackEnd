from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from model import Session, Glicose
from sqlalchemy.exc import IntegrityError
from schemas.errorSchema import ErrorSchema
from schemas.glicoseSchema import GlicoseSchemaRemove, GlicoseListSchemaResponse, GlicoseSchemaRequest, list_glicoses

info = Info(title="Health care", version="1.0.0")
app = OpenAPI(__name__, info = info)
CORS(app)

swagger_tag = Tag(name="Swagger", description="Swagger endpoints")
glicose_tag = Tag(name="Glicose", description="Glicose endpoints")

@app.get('/', tags=[swagger_tag])
def home():
    """
    A rota padrão leva você às opções de documentação do endpoint.
    """
    return redirect('/openapi')

@app.post('/glicose', tags=[glicose_tag], 
          responses =
          {
              "200": GlicoseListSchemaResponse, "400": ErrorSchema, "409": ErrorSchema, "500": ErrorSchema
          })
def add_glicose(form: GlicoseSchemaRequest):
    """
    endpoint usado para adicionar uma nova glicose e retorna a lista das que já foram registradas.
    """

    glicose = Glicose(
        nome= form.nome,
        glicose= form.glicose
    )

    try:
        session = Session()
        session.add(glicose)
        session.commit()

        glicoses = session.query(Glicose).all()

        session.close()

        if not glicoses:
            return {"message": "Glucoses not found"}, 404
        else:
            return list_glicoses(glicoses), 200
    except IntegrityError as ex:
        {"message": "Glicose já registrada no banco de dados"}, 409
    except Exception as ex:
        {"message": "não foi possível salvar"}, 500
    

@app.get('/glicoses', tags=[glicose_tag], 
         responses = 
         {
             "200": GlicoseListSchemaResponse, "404": ErrorSchema, "500": ErrorSchema
         })
def get_all_glicoses():
    """
    endpoint usado para listar todas as glicoses registradas.
    """
    try:
        session = Session()
        glicoses = session.query(Glicose).all()
        
        session.close()

        if not glicoses:
            return {"message": "Glucoses not found"}, 404
        else:
            return list_glicoses(glicoses), 200
    except Exception as ex:
        return {"message": ex}, 500

@app.delete('/glicose', tags=[glicose_tag],
            responses={"200": GlicoseListSchemaResponse, "404": ErrorSchema, "500": ErrorSchema})
def del_glicose(query: GlicoseSchemaRemove):
    """Deleta um registro de glicose
    Retorna uma lista de glicoses.
    """

    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Glicose).filter(Glicose.id == query.id).delete()
    session.commit()

    glicoses = session.query(Glicose).all()

    session.close()

    try:
        if count:
            return list_glicoses(glicoses), 200
        else:
            return {"mesage": "Glicose não encontrado."}, 404
    except Exception as ex:
        return {"message": ex}, 500