# Contributing to Pytest Automation Framework

Thank you for your interest in contributing to the Pytest Automation Framework! This document provides guidelines for contributing to this project.

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 📝 Development Guidelines

### Code Style
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add comprehensive docstrings
- Keep functions small and focused

### Testing
- Write tests for new features
- Ensure all tests pass before submitting
- Add detailed logging to test steps
- Use descriptive test names in camelCase

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, etc.)
- Keep messages under 50 characters for the subject line

## 🧪 Running Tests

### Local Testing
```bash
# Run all tests
python run_tests.py

# Run specific test types
pytest tests/unit/ -v
pytest tests/api/ -v
pytest tests/e2e/ -v

# Run with coverage
pytest --cov=utils --cov-report=html
```

### Code Quality Checks
```bash
# Format code
black .
isort .

# Lint code
flake8 .

# Type checking (if using mypy)
mypy .
```

## 📋 Pull Request Process

1. **Create a feature branch** from `main`
2. **Make your changes** following the guidelines above
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Submit a pull request** with a clear description

### Pull Request Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Test improvement

## Testing
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Documentation updated

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
```

## 🐛 Reporting Issues

When reporting issues, please include:
- **Description** of the problem
- **Steps to reproduce**
- **Expected vs actual behavior**
- **Environment details** (OS, Python version, etc.)
- **Screenshots/logs** if applicable

## 📚 Additional Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Page Object Model](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)

## 🤝 Code of Conduct

- Be respectful and inclusive
- Help others learn and grow
- Provide constructive feedback
- Follow the project's coding standards

Thank you for contributing! 🎉 