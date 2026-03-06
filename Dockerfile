FROM python:3.10-slim

# Create a non-root user (Required by Hugging Face Spaces)
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

# Copy requirements and install them
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files and give ownership to our user
COPY --chown=user . .

# Ensure the start script is executable
RUN chmod +x start.sh

# Expose the required ports
EXPOSE 7860
EXPOSE 5005
EXPOSE 5055

# Tell Flask/Gunicorn to run on port 7860
ENV PORT=7860

CMD ["./start.sh"]