from anomalib.data import MVTec
from anomalib.models import Patchcore
from anomalib.engine import Engine
import streamlit as st

st.header("作成中")

datamodule = MVTec()
model = Patchcore()
engine = Engine()

engine.fit(datamodule=datamodule, model=model)

# Assuming the datamodule, model and engine is initialized from the previous step,
# a prediction via a checkpoint file can be performed as follows:
predictions = engine.predict(
    datamodule=datamodule,
    model=model
)

print(predictions)