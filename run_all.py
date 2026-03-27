#!/usr/bin/env python
"""
Scars Watch Campaign - Combined Service Launcher

This script starts both Flask and Streamlit services in separate processes.
Works on Windows, macOS, and Linux.
"""

import subprocess
import sys
import os
import signal
import time
from pathlib import Path

# Configuration
FLASK_PORT = int(os.environ.get('FLASK_PORT', 5000))
STREAMLIT_PORT = int(os.environ.get('STREAMLIT_PORT', 8501))
FLASK_HOST = os.environ.get('FLASK_HOST', '0.0.0.0')

# Colors for terminal output
class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header(text):
    """Print formatted header"""
    print(f"{Colors.BLUE}{Colors.BOLD}{text}{Colors.END}")

def print_success(text):
    """Print success message"""
    print(f"{Colors.GREEN}✓ {text}{Colors.END}")

def print_warning(text):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠ {text}{Colors.END}")

def print_error(text):
    """Print error message"""
    print(f"{Colors.RED}✗ {text}{Colors.END}")

def print_info(text):
    """Print info message"""
    print(f"{Colors.BLUE}ℹ {text}{Colors.END}")

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import flask
        import streamlit
        return True
    except ImportError:
        return False

def install_dependencies():
    """Install required dependencies"""
    print_info("Installing dependencies...")
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-e', '.'],
                   capture_output=True)
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'],
                   capture_output=True)
    print_success("Dependencies installed")

def main():
    """Main launcher function"""
    print()
    print_header("=" * 60)
    print_header("  Scars Watch Campaign - Service Launcher")
    print_header("=" * 60)
    print()

    # Check dependencies
    if not check_dependencies():
        print_warning("Some dependencies are missing")
        install_dependencies()

    # Print configuration
    print_info(f"Flask will run on:     http://localhost:{FLASK_PORT}")
    print_info(f"Streamlit will run on: http://localhost:{STREAMLIT_PORT}")
    print()

    # Prepare environment variables
    env = os.environ.copy()
    env['FLASK_HOST'] = FLASK_HOST
    env['FLASK_PORT'] = str(FLASK_PORT)
    env['FLASK_DEBUG'] = '1'

    # Store process references
    processes = []

    try:
        # Start Flask
        print_info("Starting Flask app...")
        flask_process = subprocess.Popen(
            [sys.executable, 'app.py'],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        processes.append(('Flask', flask_process))
        print_success(f"Flask started (PID: {flask_process.pid})")

        # Give Flask a moment to start
        time.sleep(2)

        # Start Streamlit
        print_info("Starting Streamlit app...")
        streamlit_process = subprocess.Popen(
            [sys.executable, '-m', 'streamlit', 'run', 'fluff_generator.py',
             '--server.port', str(STREAMLIT_PORT), '--server.headless', 'false'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        processes.append(('Streamlit', streamlit_process))
        print_success(f"Streamlit started (PID: {streamlit_process.pid})")

        print()
        print_header("=" * 60)
        print_success("Both services are running!")
        print()
        print_info(f"📍 Map Interface:     http://localhost:{FLASK_PORT}")
        print_info(f"📍 Fluff Generator:   http://localhost:{STREAMLIT_PORT}")
        print()
        print_warning("Press Ctrl+C to stop both services")
        print_header("=" * 60)
        print()

        # Read output from both processes
        while True:
            for name, process in processes:
                if process.poll() is not None:
                    print_error(f"{name} process has ended")
                    returncode = process.returncode
                    stdout, stderr = process.communicate()
                    if stderr:
                        print(f"  Error output: {stderr[:200]}")
            time.sleep(1)

    except KeyboardInterrupt:
        print()
        print_warning("Shutdown signal received")

    finally:
        # Cleanup - terminate all processes
        print_info("Shutting down services...")
        for name, process in processes:
            try:
                process.terminate()
                process.wait(timeout=5)
                print_success(f"{name} stopped")
            except subprocess.TimeoutExpired:
                process.kill()
                print_success(f"{name} force stopped")

        print_success("All services stopped")
        print()

if __name__ == '__main__':
    main()
