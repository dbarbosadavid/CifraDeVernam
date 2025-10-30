from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI(
    title="Cifra de Vernam: API", 
    openapi_url="/cifra-de-vernam",
    description="Esta API cifra e decifra textos com a Cifra de Vernam, usando XOR entre o texto e a chave fornecida."
    )

class Cifrar(BaseModel):
    texto_puro: str
    chave: str

class Decifrar(BaseModel):
    texto_cifrado: str
    chave: str

class TextoCifrado(BaseModel):
    texto_cifrado: str

class TextoDecifrado(BaseModel):
    texto_decifrado: str

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"mensagem": f"ERRO! {exc.detail}"},
    )

@app.post("/cifrar", 
          summary="Cifra o texto informado com a Cifra de Vernam",
          description="Serve para cifrar um texto com a Cifra de Vernam. O usuário deve informar o texto e uma chave.",
          response_model=TextoCifrado)
def cifrar(cifrar: Cifrar):
    texto_puro = cifrar.texto_puro
    chave = cifrar.chave
    verificar(texto_puro, chave)

    return texto_xor(texto_puro, chave)

@app.post("/decifrar", 
          summary="Decifra o texto com a Cifra de Vernan", 
          description="Serve para decifrar um texto cifrado com a Cifra de Vernan. O usuário deve fornecer o texto cifrado e a chave utilizada na cifragem.",
          response_model=TextoDecifrado,
          response_description="Texto decifrado!")
def decifrar(decifrar: Decifrar):
    texto_cifrado = decifrar.texto_cifrado
    chave = decifrar.chave
    verificar(texto_cifrado, chave)

    return texto_xor(texto_cifrado, chave)


def verificar(
        texto: str,
        chave: str
):
    if len(texto) < 3 or len(chave) < 3:
        raise HTTPException(status_code=406, detail="Texto/Chave devem ter pelo menos 3 caracteres")
    elif texto == chave:
        raise HTTPException(status_code=406, detail="Texto e Chave não podem ser iguais")

    iguais = True

    for i in range(len(texto)):
        index = i % len(chave)
        if texto[i] != chave[index]:
            iguais = False

    if iguais:
        raise HTTPException(status_code=406, detail="Texto e Chave não podem ser iguais quando concatenados")

def texto_xor(
        texto: str,
        chave: str,
):
    texto_xor = ''

    for i in range(len(texto)):
        binario_cifrado = ''
        index = i % len(chave)
        binario_texto = bin(ord(texto[i]))
        binario_chave = bin(ord(chave[index]))

        for j in range(len(binario_texto)):
            if j < 4:
                binario_cifrado += binario_texto[j]
            else:
                if binario_texto[j] == binario_chave[j]:
                    binario_cifrado += '0'
                else:
                    binario_cifrado += '1'

        decimal_value = int(binario_cifrado, 2)
        character = chr(decimal_value)
        texto_xor += character

    response = TextoCifrado(texto_cifrado=texto_xor)

    return response