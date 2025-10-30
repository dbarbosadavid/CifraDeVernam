

# API - Cifra de Vernam

Documentação disponível em https://cifradevernan.vercel.app/docs

## Este projeto se trata de uma API com dois endpoints:

* /cifrar (permite a codificação de um texto através de uma chave utilizando a Cifra de Vernam, com método XOR)

* /decifrar (permite a decodificação de um texto através da chave usada na codificação, com método XOR)

# Linguagens/Bibliotecas usadas

* Python 3.13
* FastAPI
* PyDantic
* uvicorn

# Como rodar

* Instalar Python 3.13 ou superior
* Clonar o repositório
* Instalar as Bibliotecas: 

```
    py -m pip install fastapi pydantic uvicorn
```

* Executar comando para rodar o servidor:
```
    py -m uvicorn app:app --reload
```

#### A API já estará rodando, para acessar a documentação e testar os endpints:

* No navgeador, basta acessar:
```
    127.0.0.1:8000/docs
```

# Projeto elaborado para fins acadêmicos