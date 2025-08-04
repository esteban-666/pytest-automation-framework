# Pytest Automation Framework

A comprehensive test automation framework built with pytest, designed for web and API testing with support for parallel execution, reporting, and CI/CD integration.

## 🚀 Features

- **Multi-layer testing**: Unit, E2E, and API tests
- **Page Object Model**: Organized page objects for web testing
- **Parallel execution**: Run tests in parallel for faster execution
- **Comprehensive reporting**: HTML reports with coverage
- **Configuration management**: Environment-specific configurations
- **Fixture management**: Reusable test fixtures
- **Data-driven testing**: Support for parameterized tests
- **CI/CD ready**: GitHub Actions integration

## 📁 Project Structure

```
pytest-automation-framework/
├── config/                 # Configuration files
├── conftest.py            # Pytest configuration and fixtures
├── pages/                 # Page Object Model classes
├── pytest.ini            # Pytest configuration
├── requirements.txt       # Python dependencies
├── setup.py              # Package setup
├── run_tests.py          # Local test runner script
├── reports/              # Test reports
├── tests/                # Test files
│   ├── api/              # API tests
│   ├── e2e/              # End-to-end tests
│   └── unit/             # Unit tests
└── utils/                # Utility functions
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd pytest-automation-framework
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Quick Start

### Running Tests Locally

**Option 1: Using the test runner script (Recommended)**
```bash
python run_tests.py
```

**Option 2: Using pytest directly**
```bash
# Run all tests
pytest

# Run specific test category
pytest tests/unit/
pytest tests/e2e/
pytest tests/api/

# Run with specific markers
pytest -m "smoke"
pytest -m "regression"

# Run in parallel
pytest -n auto

# Run with verbose output
pytest -v

# Run and generate HTML report
pytest --html=reports/report.html
```

### Configuration

The framework supports multiple environments. Set the environment variable:

```bash
export TEST_ENV=local  # Options: local, staging, prod
```

## 📝 Writing Tests

### Unit Tests Example

```python
# tests/unit/test_math.py
import pytest
from utils.calculator import Calculator

class TestCalculator:
    def testAdd(self):
        calc = Calculator()
        assert calc.add(2, 3) == 5
    
    def testSubtract(self):
        calc = Calculator()
        assert calc.subtract(5, 3) == 2
```

### E2E Tests Example

```python
# tests/e2e/test_ui.py
import pytest
from pages.demoqa_pages import DemoQAMainPage

class TestUI:
    def testDemoqaForm(self, driver):
        demoqa = DemoQAMainPage(driver)
        driver.get("https://demoqa.com/")
        # Test implementation
```

### API Tests Example

```python
# tests/api/test_api.py
import pytest
from utils.api_client import APIClient

class TestAPI:
    def testAllRestMethods(self):
        client = APIClient(base_url="https://httpbin.org")
        response = client.get("/get")
        assert response.status_code == 200
```

## 🔧 Configuration

### Environment Configuration

Create environment-specific config files in `config/`:

```yaml
# config/local.yaml
base_url: "https://demoqa.com"
api_base_url: "https://jsonplaceholder.typicode.com"
browser: "chrome"
headless: false
```

### Pytest Configuration

The `pytest.ini` file contains framework-specific settings:

```ini
[tool:pytest]
minversion = 6.0
addopts = -ra -q --strict-markers
testpaths = tests
markers =
    smoke: marks tests as smoke tests
    regression: marks tests as regression tests
    slow: marks tests as slow running
```

## 📊 Reporting

The framework generates comprehensive reports:

- **HTML Reports**: Visual reports with charts and details
- **Coverage Reports**: Code coverage analysis
- **Screenshots**: Automatic screenshots on test failures

Reports are saved in the `reports/` directory.

## 🏷️ Test Markers

Use markers to categorize and run specific test groups:

```python
@pytest.mark.smoke
def testCriticalFlow():
    pass

@pytest.mark.regression
def testComprehensiveFeature():
    pass

@pytest.mark.slow
def testPerformance():
    pass
```

## 🔄 CI/CD Integration

### GitHub Actions

The framework includes a GitHub Actions workflow that:

- Runs tests on multiple Python versions (3.9, 3.10, 3.11)
- Executes unit, API, and E2E tests
- Generates and uploads test reports
- Performs code quality checks (Black, isort, flake8)

Workflow file: `.github/workflows/test.yml`

## 🧪 Test Examples

### Unit Tests
- **Math Operations**: Calculator functionality testing
- **Parameterized Tests**: Multiple input validation
- **Exception Testing**: Error handling validation

### API Tests
- **REST Methods**: GET, POST, PUT, PATCH, DELETE
- **Data Validation**: Response structure validation
- **Error Handling**: HTTP status code validation

### E2E Tests
- **DemoQA**: Form submission, drag & drop
- **The Internet**: Login, checkboxes, alerts
- **Page Object Model**: Organized web interactions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Write tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For questions and support:
- Create an issue in the repository
- Check the test examples in the `tests/` directory
- Review the configuration files
