"""
Setup script for pytest automation framework.
"""
from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    """Read README.md file."""
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Pytest Automation Framework"

# Read requirements
def read_requirements():
    """Read requirements.txt file."""
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="pytest-automation-framework",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive test automation framework built with pytest",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pytest-automation-framework",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Framework :: Pytest",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "black>=23.0.0",
            "flake8>=6.0.0",
            "isort>=5.12.0",
        ],
    },
    include_package_data=True,
    package_data={
        "pytest_automation_framework": [
            "config/*.yaml",
            "config/*.yml",
        ],
    },
    keywords=[
        "pytest",
        "automation",
        "testing",
        "selenium",
        "api",
        "webdriver",
        "test-framework",
        "page-object-model",
    ],
    project_urls={
        "Bug Reports": "https://github.com/yourusername/pytest-automation-framework/issues",
        "Source": "https://github.com/yourusername/pytest-automation-framework",
    },
    zip_safe=False,
)
