# Rosette API Text Embeddings Visualization Sample Code
A simple Python script for transforming a corpus of documents in text vectors suitable for visualization in .tsv format. It uses the [Rosette API](https://developer.rosette.com/)'s `/text-embedding` endpoint and the [BBC News Corpus](http://mlg.ucd.ie/datasets/bbc.html). Note that the corpus is only free for research purposes.

## Getting started
1. Clone the repo and open the files in your favorite text editor/python IDE.
2. In `visualize-embeddings.py`, replace 'MY_ROSAPI_KEY' with your [Rosette API key](https://developer.rosette.com/admin/applications) and save.
3. Run `visualize-embeddings.py` via your python IDE or command line:
  `$ python test_embeddings.py`

You'll see that the script parses the raw text files of the corpus into a list of documents. Each document consist of 3 fields:
  * category
  * headline
  * content
  
The script then creates two files:
  * embeddings.tsv: a TSV file where each line contains the text vector for a document's content field.
  * metadata.tsv: a TSV file where each line contains a document's metadata (i.e. category and headline).

To visualize the embeddings, load them into Google TensorFlow's [Embedding Projector](http://projector.tensorflow.org/). Turn on color coding by category to really see the vectors in action. You can see our projection [at this link](http://projector.tensorflow.org/?config=https://gist.githubusercontent.com/hillelt/bd4fad5280eefba4d2d8875e87f0eabb/raw/0672efa576a6fd5c14ec93ed86a2b9326a35c3bf/projector_config.json).

## Customize for your data
Try replacing the BBC News corpus with your own data. And if you find anything interesting, we'd love to hear about it! Find us at community@rosette.com.

