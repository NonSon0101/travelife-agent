
FROM python:3.11-slim
WORKDIR /app

# Create a non-root user
RUN adduser --disabled-password --gecos "" myuser

# Change ownership of /app to myuser
RUN chown -R myuser:myuser /app

# Switch to the non-root user
USER myuser

# Set up environment variables - Start
ENV PATH="/home/myuser/.local/bin:$PATH"

ENV GOOGLE_GENAI_USE_VERTEXAI=1
ENV GOOGLE_CLOUD_PROJECT=metal-ring-456416-s1
ENV GOOGLE_CLOUD_LOCATION=us-central1

# Set up environment variables - End

# Install ADK - Start
RUN pip install google-adk
# Install ADK - End

# Copy agent - Start

COPY . /app/


# Copy agent - End

EXPOSE 8000

CMD ["python", "agent.py"]
