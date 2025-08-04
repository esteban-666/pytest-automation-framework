#!/usr/bin/env python3
"""
Simple script to run tests locally.
"""
import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and print the result."""
    print(f"\n{'='*50}")
    print(f"Running: {description}")
    print(f"Command: {command}")
    print(f"{'='*50}")
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.stdout:
        print("STDOUT:")
        print(result.stdout)
    
    if result.stderr:
        print("STDERR:")
        print(result.stderr)
    
    print(f"Exit code: {result.returncode}")
    return result.returncode == 0

def main():
    """Main function to run tests."""
    print("🚀 Pytest Automation Framework - Local Test Runner")
    print("=" * 60)
    
    # Check if virtual environment is activated
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Warning: Virtual environment not detected. Consider activating it first.")
        print("   Run: source venv/bin/activate")
    
    # Create necessary directories
    os.makedirs("reports", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    
    success = True
    
    # Run unit tests
    success &= run_command(
        "pytest tests/unit/ -v --cov=utils --cov-report=html:reports/coverage --cov-report=term-missing",
        "Unit Tests with Coverage"
    )
    
    # Run API tests
    success &= run_command(
        "pytest tests/api/ -v --html=reports/api-report.html --self-contained-html",
        "API Tests"
    )
    
    # Run E2E tests (only if unit and API tests pass)
    if success:
        success &= run_command(
            "pytest tests/e2e/ -v --html=reports/e2e-report.html --self-contained-html",
            "E2E Tests"
        )
    else:
        print("\n⚠️  Skipping E2E tests due to previous failures")
    
    # Run linting
    print("\n🔍 Running Code Quality Checks...")
    run_command("black --check .", "Black Code Formatting Check")
    run_command("isort --check-only .", "Import Sorting Check")
    run_command("flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics", "Flake8 Linting")
    
    print("\n" + "=" * 60)
    if success:
        print("✅ All tests completed successfully!")
        print("📊 Reports generated in the 'reports' directory")
    else:
        print("❌ Some tests failed. Check the output above for details.")
        sys.exit(1)

if __name__ == "__main__":
    main() 