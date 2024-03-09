FROM continuumio/miniconda3

WORKDIR /home/app

RUN apt-get update
RUN apt-get install nano unzip
RUN apt install curl -y

COPY requirements.txt /home/app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/app/

# Run the Streamlit app
CMD streamlit run --server.port $PORT streamlit.py

ENTRYPOINT ["python", "train.py"]