FROM python:3.9-slim

FROM streamlit/streamlit:latest

# Install Chromium and Chromium driver
RUN apt-get update && apt-get install -y \
    chromium-browser \
    chromium-chromedriver

# Copy the requirements file to the container
COPY requirements.txt /app/requirements.txt

# Install the required packages
RUN pip install -r /app/requirements.txt

# Copy the app code to the container
COPY . /app

# Set the working directory
WORKDIR /app

# Expose the Streamlit port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "streamlit_app.py"]
