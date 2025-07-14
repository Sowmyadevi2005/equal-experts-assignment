#-----------------------------------------------------------------
#STAGE 1: Test the application using pytest and ruun security 
#         checks using bandit
#------------------------------------------------------------------
FROM python:3.9-slim as test

# Make /app dir as WORKDIR
WORKDIR /app

# COPY requiremens.txt
COPY requirements.txt .

# Install packages  secified in requirements.txt
RUN pip install --no-cache-dir  -r requirements.txt

# COPY all the code
COPY . .

# Install Bandit for security scanning
RUN pip install pytest bandit

# Run pytest to execute the test cases
RUN pytest --disable-warnings

# Run Bandit to scan the Python code for vulnerabilities
# This will scan all Python files in the /app directory
RUN bandit -r . -ll || true

#-----------------------------------------------------------------
#STAGE 2: Build and run the Application  
#------------------------------------------------------------------

FROM python:3.9-slim as build

# Make /app dir as WORKDIR
WORKDIR /app

# COPY requiremens.txt
COPY requirements.txt .

# Install packages  secified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# COPY all the Source code from src folder
COPY src/* src/

# COPY main.py
COPY main.py .

# Expose the PORT
EXPOSE 8080

# Run the application
CMD ["python","main.py"]