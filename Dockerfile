FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY scripts/ ./scripts/

# Por defecto ejecuta el de Postgres, puedes cambiarlo
CMD ["sh", "-c", "python scripts/ingesta_library.py && python scripts/ingesta_prestamos.py && python scripts/ingesta_usuarios.py"]
