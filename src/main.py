from fastapi import FastAPI
import os

app = FastAPI(debug=os.getenv("DEBUG"))
