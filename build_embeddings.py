# Run once on your laptop: python build_embeddings.py  -> creates embeddings.npy
import app  # importing app builds and saves embeddings.npy
print("Saved", app.EMB.shape)
