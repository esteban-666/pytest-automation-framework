"""
API client for making HTTP requests and API testing.
"""
import json
import time
from typing import Dict, Any, Optional, Union
import requests
try:
    import httpx
    HTTPX_AVAILABLE = True
except ImportError:
    HTTPX_AVAILABLE = False
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from utils.logger import logger


class APIClient:
    """HTTP client for API testing with retry logic and logging."""
    
    def __init__(self, base_url: str = "", timeout: int = 30, max_retries: int = 3):
        """
        Initialize API client.
        
        Args:
            base_url: Base URL for API requests
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        
        # Configure retry strategy
        retry_strategy = Retry(
            total=max_retries,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST", "PUT", "DELETE", "PATCH"],
            backoff_factor=1
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        
        # Default headers
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Pytest-Automation-Framework/1.0"
        })
        
        logger.info(f"API client initialized with base URL: {base_url}")
    
    def _build_url(self, endpoint: str) -> str:
        """Build full URL from endpoint."""
        if endpoint.startswith('http'):
            return endpoint
        return f"{self.base_url}/{endpoint.lstrip('/')}"
    
    def _log_request(self, method: str, url: str, headers: dict = None, data: Any = None):
        """Log request details."""
        logger.info(f"🌐 API Request: {method} {url}")
        if headers:
            logger.debug(f"Headers: {headers}")
        if data:
            logger.debug(f"Data: {data}")
    
    def _log_response(self, response: requests.Response, duration: float):
        """Log response details."""
        status_code = response.status_code
        if 200 <= status_code < 300:
            logger.info(f"✅ API Response: {status_code}")
        else:
            logger.error(f"❌ API Response: {status_code}")
        
        logger.info(f"⏱️ API call duration: {duration:.2f} seconds")
        
        try:
            response_data = response.json()
            logger.debug(f"Response data: {response_data}")
        except json.JSONDecodeError:
            logger.debug(f"Response text: {response.text[:500]}...")
    
    def request(
        self,
        method: str,
        endpoint: str,
        headers: Dict[str, str] = None,
        data: Any = None,
        json_data: Dict[str, Any] = None,
        params: Dict[str, Any] = None,
        files: Dict[str, Any] = None,
        timeout: int = None
    ) -> requests.Response:
        """
        Make an HTTP request.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            endpoint: API endpoint
            headers: Request headers
            data: Request data
            json_data: JSON data for request body
            params: Query parameters
            files: Files to upload
            timeout: Request timeout
        
        Returns:
            Response object
        """
        url = self._build_url(endpoint)
        timeout = timeout or self.timeout
        
        # Prepare request data
        request_data = {}
        if headers:
            request_data['headers'] = headers
        if data:
            request_data['data'] = data
        if json_data:
            request_data['json'] = json_data
        if params:
            request_data['params'] = params
        if files:
            request_data['files'] = files
        
        # Log request
        self._log_request(method, url, headers, data or json_data)
        
        # Make request
        start_time = time.time()
        try:
            response = self.session.request(
                method=method.upper(),
                url=url,
                timeout=timeout,
                **request_data
            )
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {str(e)}")
            raise
        
        # Log response
        duration = time.time() - start_time
        self._log_response(response, duration)
        
        return response
    
    def get(self, endpoint: str, params: Dict[str, Any] = None, headers: Dict[str, str] = None) -> requests.Response:
        """Make a GET request."""
        return self.request("GET", endpoint, params=params, headers=headers)
    
    def post(self, endpoint: str, data: Any = None, json_data: Dict[str, Any] = None, headers: Dict[str, str] = None) -> requests.Response:
        """Make a POST request."""
        return self.request("POST", endpoint, data=data, json_data=json_data, headers=headers)
    
    def put(self, endpoint: str, data: Any = None, json_data: Dict[str, Any] = None, headers: Dict[str, str] = None) -> requests.Response:
        """Make a PUT request."""
        return self.request("PUT", endpoint, data=data, json_data=json_data, headers=headers)
    
    def patch(self, endpoint: str, data: Any = None, json_data: Dict[str, Any] = None, headers: Dict[str, str] = None) -> requests.Response:
        """Make a PATCH request."""
        return self.request("PATCH", endpoint, data=data, json_data=json_data, headers=headers)
    
    def delete(self, endpoint: str, headers: Dict[str, str] = None) -> requests.Response:
        """Make a DELETE request."""
        return self.request("DELETE", endpoint, headers=headers)
    
    def head(self, endpoint: str, headers: Dict[str, str] = None) -> requests.Response:
        """Make a HEAD request."""
        return self.request("HEAD", endpoint, headers=headers)
    
    def options(self, endpoint: str, headers: Dict[str, str] = None) -> requests.Response:
        """Make an OPTIONS request."""
        return self.request("OPTIONS", endpoint, headers=headers)
    
    def upload_file(self, endpoint: str, file_path: str, field_name: str = "file", headers: Dict[str, str] = None) -> requests.Response:
        """
        Upload a file.
        
        Args:
            endpoint: API endpoint
            file_path: Path to file to upload
            field_name: Form field name for the file
            headers: Request headers
        
        Returns:
            Response object
        """
        with open(file_path, 'rb') as f:
            files = {field_name: f}
            return self.post(endpoint, files=files, headers=headers)
    
    def download_file(self, endpoint: str, file_path: str, headers: Dict[str, str] = None) -> str:
        """
        Download a file.
        
        Args:
            endpoint: API endpoint
            file_path: Path to save the file
            headers: Request headers
        
        Returns:
            Path to downloaded file
        """
        response = self.get(endpoint, headers=headers)
        response.raise_for_status()
        
        with open(file_path, 'wb') as f:
            f.write(response.content)
        
        logger.info(f"File downloaded: {file_path}")
        return file_path
    
    def set_auth(self, auth_type: str, **kwargs):
        """
        Set authentication for requests.
        
        Args:
            auth_type: Type of authentication (basic, bearer, token, oauth)
            **kwargs: Authentication parameters
        """
        if auth_type.lower() == "basic":
            from requests.auth import HTTPBasicAuth
            auth = HTTPBasicAuth(kwargs.get('username'), kwargs.get('password'))
            self.session.auth = auth
        elif auth_type.lower() == "bearer":
            token = kwargs.get('token')
            self.session.headers.update({"Authorization": f"Bearer {token}"})
        elif auth_type.lower() == "token":
            token = kwargs.get('token')
            self.session.headers.update({"Authorization": f"Token {token}"})
        elif auth_type.lower() == "oauth":
            from requests_oauthlib import OAuth1
            auth = OAuth1(
                kwargs.get('client_key'),
                kwargs.get('client_secret'),
                kwargs.get('resource_owner_key'),
                kwargs.get('resource_owner_secret')
            )
            self.session.auth = auth
        
        logger.info(f"Authentication set: {auth_type}")
    
    def add_header(self, key: str, value: str):
        """Add a header to all requests."""
        self.session.headers.update({key: value})
        logger.info(f"Header added: {key}={value}")
    
    def remove_header(self, key: str):
        """Remove a header from all requests."""
        if key in self.session.headers:
            del self.session.headers[key]
            logger.info(f"Header removed: {key}")
    
    def clear_headers(self):
        """Clear all custom headers."""
        self.session.headers.clear()
        logger.info("All headers cleared")
    
    def get_headers(self) -> Dict[str, str]:
        """Get current headers."""
        return dict(self.session.headers)
    
    def set_timeout(self, timeout: int):
        """Set default timeout for requests."""
        self.timeout = timeout
        logger.info(f"Timeout set to {timeout} seconds")
    
    def validate_response(self, response: requests.Response, expected_status: int = 200) -> bool:
        """
        Validate response status code.
        
        Args:
            response: Response object
            expected_status: Expected status code
        
        Returns:
            True if status matches, False otherwise
        """
        if response.status_code == expected_status:
            logger.info(f"Response validation passed: {response.status_code}")
            return True
        else:
            logger.error(f"Response validation failed: expected {expected_status}, got {response.status_code}")
            return False
    
    def validate_json_schema(self, response: requests.Response, schema: Dict[str, Any]) -> bool:
        """
        Validate response against JSON schema.
        
        Args:
            response: Response object
            schema: JSON schema to validate against
        
        Returns:
            True if validation passes, False otherwise
        """
        try:
            from jsonschema import validate
            response_data = response.json()
            validate(instance=response_data, schema=schema)
            logger.info("JSON schema validation passed")
            return True
        except Exception as e:
            logger.error(f"JSON schema validation failed: {str(e)}")
            return False
    
    def wait_for_status(self, endpoint: str, expected_status: int = 200, max_wait: int = 60, interval: int = 5) -> bool:
        """
        Wait for endpoint to return expected status.
        
        Args:
            endpoint: API endpoint
            expected_status: Expected status code
            max_wait: Maximum wait time in seconds
            interval: Check interval in seconds
        
        Returns:
            True if status matches within timeout, False otherwise
        """
        start_time = time.time()
        
        while time.time() - start_time < max_wait:
            try:
                response = self.get(endpoint)
                if response.status_code == expected_status:
                    logger.info(f"Endpoint {endpoint} returned expected status {expected_status}")
                    return True
            except requests.exceptions.RequestException:
                pass
            
            logger.debug(f"Waiting for endpoint {endpoint} to return status {expected_status}")
            time.sleep(interval)
        
        logger.error(f"Endpoint {endpoint} did not return status {expected_status} within {max_wait} seconds")
        return False
    
    def health_check(self, endpoint: str = "health") -> bool:
        """
        Perform health check on API.
        
        Args:
            endpoint: Health check endpoint
        
        Returns:
            True if healthy, False otherwise
        """
        try:
            response = self.get(endpoint)
            is_healthy = response.status_code == 200
            logger.info(f"Health check {'passed' if is_healthy else 'failed'}: {response.status_code}")
            return is_healthy
        except requests.exceptions.RequestException as e:
            logger.error(f"Health check failed: {str(e)}")
            return False
    
    def close(self):
        """Close the session."""
        self.session.close()
        logger.info("API client session closed")
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


class AsyncAPIClient:
    """Async HTTP client for API testing."""
    
    def __init__(self, base_url: str = "", timeout: int = 30):
        """
        Initialize async API client.
        
        Args:
            base_url: Base URL for API requests
            timeout: Request timeout in seconds
        """
        if not HTTPX_AVAILABLE:
            raise ImportError("httpx is not installed. Install it with: pip install httpx")
        
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.client = httpx.AsyncClient(
            base_url=base_url,
            timeout=timeout,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "User-Agent": "Pytest-Automation-Framework/1.0"
            }
        )
        
        logger.info(f"Async API client initialized with base URL: {base_url}")
    
    async def request(
        self,
        method: str,
        endpoint: str,
        headers: Dict[str, str] = None,
        data: Any = None,
        json_data: Dict[str, Any] = None,
        params: Dict[str, Any] = None
    ) -> 'httpx.Response':
        """Make an async HTTP request."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        # Log request
        logger.info(f"🌐 Async API Request: {method} {url}")
        if headers:
            logger.debug(f"Headers: {headers}")
        if data or json_data:
            logger.debug(f"Data: {data or json_data}")
        
        # Make request
        start_time = time.time()
        try:
            response = await self.client.request(
                method=method.upper(),
                url=url,
                headers=headers,
                data=data,
                json=json_data,
                params=params
            )
        except httpx.RequestError as e:
            logger.error(f"Async request failed: {str(e)}")
            raise
        
        # Log response
        duration = time.time() - start_time
        status_code = response.status_code
        if 200 <= status_code < 300:
            logger.info(f"✅ Async API Response: {status_code}")
        else:
            logger.error(f"❌ Async API Response: {status_code}")
        
        logger.info(f"⏱️ Async API call duration: {duration:.2f} seconds")
        
        return response
    
    async def get(self, endpoint: str, params: Dict[str, Any] = None, headers: Dict[str, str] = None) -> 'httpx.Response':
        """Make an async GET request."""
        return await self.request("GET", endpoint, params=params, headers=headers)
    
    async def post(self, endpoint: str, data: Any = None, json_data: Dict[str, Any] = None, headers: Dict[str, str] = None) -> 'httpx.Response':
        """Make an async POST request."""
        return await self.request("POST", endpoint, data=data, json_data=json_data, headers=headers)
    
    async def put(self, endpoint: str, data: Any = None, json_data: Dict[str, Any] = None, headers: Dict[str, str] = None) -> 'httpx.Response':
        """Make an async PUT request."""
        return await self.request("PUT", endpoint, data=data, json_data=json_data, headers=headers)
    
    async def delete(self, endpoint: str, headers: Dict[str, str] = None) -> 'httpx.Response':
        """Make an async DELETE request."""
        return await self.request("DELETE", endpoint, headers=headers)
    
    async def close(self):
        """Close the async client."""
        await self.client.aclose()
        logger.info("Async API client closed")
    
    async def __aenter__(self):
        """Async context manager entry."""
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close() 