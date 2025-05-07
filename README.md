# Accounts API

API de ejemplo que forma parte de una Prueba de Concepto (PoC) de autenticación segura entre microservicios de Banco Futuro usando JWT firmados con AWS KMS.

---

## 🚀 ¿Qué hace?

Expone un único endpoint `/balance` (GET) que devuelve el saldo disponible de una cuenta simulada, **autenticando previamente** con un token JWT firmado por la API que consume.

---

## 🧱 Rol en la PoC

- Esta API **representa el sistema contable** de una entidad financiera.
- Verifica tokens firmados con AWS KMS antes de responder.
- Es llamada internamente por otras APIs (como `transactions`) para consultar el saldo antes de procesar acciones sensibles.

---

## 🔧 Requisitos

- Python 3.8+
- AWS SDK (`boto3`)
- Flask
- PyJWT
- Acceso al Secret Manager de AWS y a la clave de KMS correspondiente

---

## ⚙️ Variables de entorno necesarias

| Variable         | Descripción                                                |
|------------------|------------------------------------------------------------|
| `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` | Credenciales temporales o fijas para usar Secrets Manager y KMS |
| (opcional) `AWS_SESSION_TOKEN`               | Si usás credenciales temporales, requeridas también |
| `AWS_DEFAULT_REGION`                         | Región donde se encuentran los secretos y claves (ej: `us-east-1`) |

---

## 🛠 Cómo levantar la API

```bash
pip install -r requirements.txt
export FLASK_APP=accounts_api.py
flask run --host=0.0.0.0 --port=5001
```

---

## 🔐 Seguridad

Se usa el SDK de `bank_auth_sdk` para verificar los tokens JWT.

El SDK se encuentra en el repo de [bank-auth-sdk](https://github.com/arq-apps/bank_auth_sdk).
Para instalar el SDK se debe hacer con el comando:

```bash
pip install git+https://github.com/arq-apps/bank_auth_sdk.git
```

El header de la request debe ser:

```
Authorization: Bearer <token>
```
El token debe estar firmado con una clave autorizada (definida en el Secret Manager).



## 🧪 Ejemplo de request

```bash
{
  "status": "success",
  "api": "accounts",
  "balance": {
    "currency": "ARS",
    "available": 132500.5,
    "last_updated": "2025-05-06T21:15:00Z"
  }
}
```




