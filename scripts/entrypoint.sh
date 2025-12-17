#!/usr/bin/env sh
set -eu

echo "=== Sante Plus container boot ==="
python -V || true

# Hard thread caps (in addition to Dockerfile ENV) to reduce segfault risk on constrained CPUs
export OMP_NUM_THREADS="${OMP_NUM_THREADS:-1}"
export MKL_NUM_THREADS="${MKL_NUM_THREADS:-1}"
export OPENBLAS_NUM_THREADS="${OPENBLAS_NUM_THREADS:-1}"
export NUMEXPR_NUM_THREADS="${NUMEXPR_NUM_THREADS:-1}"
export VECLIB_MAXIMUM_THREADS="${VECLIB_MAXIMUM_THREADS:-1}"

echo "=== Smoke test: import tensorflow ==="
python - <<'PY'
import os
print("TF_CPP_MIN_LOG_LEVEL=", os.environ.get("TF_CPP_MIN_LOG_LEVEL"))
print("TF_ENABLE_ONEDNN_OPTS=", os.environ.get("TF_ENABLE_ONEDNN_OPTS"))
print("TF_DISABLE_MKL=", os.environ.get("TF_DISABLE_MKL"))
print("OMP_NUM_THREADS=", os.environ.get("OMP_NUM_THREADS"))
print("MKL_NUM_THREADS=", os.environ.get("MKL_NUM_THREADS"))
print("OPENBLAS_NUM_THREADS=", os.environ.get("OPENBLAS_NUM_THREADS"))

import tensorflow as tf
print("TensorFlow:", tf.__version__)
print("Has tf.keras.saving:", hasattr(tf.keras, "saving"))
PY

echo "=== Starting Streamlit ==="
exec streamlit run app.py \
  --server.port="${PORT:-8080}" \
  --server.address="0.0.0.0" \
  --server.headless=true


