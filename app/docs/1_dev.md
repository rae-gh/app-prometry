# Create dev environment
python3 -m venv .env-promapp

# Load dev environment
source .env-promapp/bin/activate
(deactivate to exit venv)
pip install --upgrade pip

pip install -r requirements.txt --upgrade

# run app
streamlit run app/Home.py

# distribute to streamlit
This will be automatically distributed to streamlit on push to main  
https://share.streamlit.io/
