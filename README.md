# Mammo-Find
An LLM-based Web Visualization tool for Mammogram dataset recommendations 

## To run the code, follow the instructions below

### You will need Python 3.11.7

### You will need Ollama installed in your pc and have some LLMs downloaded

### First clone the git repository
git clone https://github.com/RaiyanJahangir/Mammo-Find.git

### Go to the root directory and then open the command prompt
py -3.11 -m venv myenv  //You may need python 3.11 installed on your pc along with other versions.

### To activate the virtual environment:
myenv\Scripts\activate

### To install all the necessary packages and libraries
pip install -r requirements.txt

### Now run the Graph_Generator.ipynb

### After running the notebook, check index.html to see the generated graph

### Then start the Flaskk Server by running app.py
This code activates the flask server and connects the LLM to the web interface for chatting.
