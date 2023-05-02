from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)



if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)
    

"""
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNfdG9rZW4iLCJleHAiOjE2ODM2NDk0NzIsImlhdCI6MTY4MzA0NDY3Miwic3ViIjoiNSJ9.Pxt6-TfUDIk-WNtE8T52oMCTmuyXpUBiL9Cj70X9B7Q
Tipo: bearer

Token2: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNfdG9rZW4iLCJleHAiOjE2ODM2NTM2MjYsImlhdCI6MTY4MzA0ODgyNiwic3ViIjoiMiJ9.Y0GWw_oXFnvRXhyO__roPeigKxsDC8DeyNC4r3pZ7hw
Tipo: bearer

"""