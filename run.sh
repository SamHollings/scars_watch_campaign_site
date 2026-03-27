#!/bin/bash

# Scars Watch Campaign - Combined Launcher
# This script starts both Flask and Streamlit in separate processes

set -e

echo "🚀 Starting Scars Watch Campaign..."
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
FLASK_PORT=${FLASK_PORT:-5000}
STREAMLIT_PORT=${STREAMLIT_PORT:-8501}
FLASK_HOST=${FLASK_HOST:-0.0.0.0}

echo -e "${BLUE}Configuration:${NC}"
echo "  Flask: http://localhost:$FLASK_PORT"
echo "  Streamlit: http://localhost:$STREAMLIT_PORT"
echo ""

# Check if dependencies are installed
if ! command -v flask &> /dev/null; then
    echo -e "${YELLOW}⚠️  Flask not found. Installing dependencies...${NC}"
    pip install -e . > /dev/null
    pip install -r requirements.txt > /dev/null
fi

# Start Flask in the background
echo -e "${GREEN}▶ Starting Flask app...${NC}"
FLASK_HOST=$FLASK_HOST FLASK_PORT=$FLASK_PORT python app.py &
FLASK_PID=$!
echo "  Flask PID: $FLASK_PID"

# Give Flask a moment to start
sleep 2

# Start Streamlit in the background
echo -e "${GREEN}▶ Starting Streamlit app...${NC}"
streamlit run fluff_generator.py --server.port $STREAMLIT_PORT --server.headless true &
STREAMLIT_PID=$!
echo "  Streamlit PID: $STREAMLIT_PID"

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✓ Both services are running!${NC}"
echo ""
echo "  📍 Map Interface:     http://localhost:$FLASK_PORT"
echo "  📍 Fluff Generator:   http://localhost:$STREAMLIT_PORT"
echo ""
echo -e "${YELLOW}Press Ctrl+C to stop both services${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Function to cleanup on exit
cleanup() {
    echo ""
    echo -e "${YELLOW}Shutting down services...${NC}"
    kill $FLASK_PID 2>/dev/null || true
    kill $STREAMLIT_PID 2>/dev/null || true
    echo -e "${GREEN}✓ Services stopped${NC}"
}

# Set up trap to catch Ctrl+C
trap cleanup EXIT INT TERM

# Wait for both processes
wait
