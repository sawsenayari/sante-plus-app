FROM python:3.11-bullseye

WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers de requirements
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application
COPY . .

# Variables d'environnement pour éviter les segfaults TensorFlow
ENV PYTHONUNBUFFERED=1
ENV TF_CPP_MIN_LOG_LEVEL=3
ENV TF_ENABLE_ONEDNN_OPTS=0
ENV TF_DISABLE_MKL=1
ENV OMP_NUM_THREADS=1
ENV MKL_NUM_THREADS=1
ENV OPENBLAS_NUM_THREADS=1
ENV NUMEXPR_NUM_THREADS=1
ENV VECLIB_MAXIMUM_THREADS=1

# Exposer le port (Render utilise $PORT)
EXPOSE 8080

# Entrypoint avec smoke-test TensorFlow (utile pour diagnostiquer les segfaults 139 sur Render)
CMD ["sh", "scripts/entrypoint.sh"]

