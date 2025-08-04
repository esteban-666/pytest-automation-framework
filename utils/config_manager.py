"""
Configuration manager for the automation framework.
"""
import os
import yaml
import json
from pathlib import Path
from typing import Dict, Any, Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class ConfigManager:
    """Manages configuration for different environments and test settings."""
    
    def __init__(self, config_dir: str = "config"):
        self.config_dir = Path(config_dir)
        self.config_dir.mkdir(exist_ok=True)
        self._config = None
        self._load_config()
    
    def _load_config(self):
        """Load configuration from files and environment variables."""
        # Default configuration
        default_config = {
            "web": {
                "base_url": "http://localhost:3000",
                "implicit_wait": 10,
                "explicit_wait": 20,
                "page_load_timeout": 30,
                "window_size": {"width": 1920, "height": 1080}
            },
            "api": {
                "base_url": "http://localhost:8000",
                "timeout": 30,
                "headers": {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                }
            },
            "database": {
                "url": "sqlite:///test.db",
                "pool_size": 10,
                "max_overflow": 20
            },
            "browser": {
                "name": "chrome",
                "headless": True,
                "download_path": "./downloads",
                "user_agent": None
            },
            "mobile": {
                "platform": "Android",
                "device_name": "Pixel_4_API_30",
                "app_path": None
            },
            "reporting": {
                "html_report": True,
                "json_report": True,
                "xml_report": True,
                "screenshot_on_failure": True,
                "video_recording": False
            },
            "parallel": {
                "enabled": True,
                "workers": "auto",
                "max_workers": 4
            },
            "retry": {
                "enabled": True,
                "max_retries": 2,
                "retry_delay": 1
            },
            "logging": {
                "level": "INFO",
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "file": "logs/test.log"
            }
        }
        
        # Load environment-specific configuration
        env = os.getenv("TEST_ENV", "staging")
        env_config_file = self.config_dir / f"{env}.yaml"
        
        if env_config_file.exists():
            with open(env_config_file, 'r') as f:
                env_config = yaml.safe_load(f) or {}
                self._merge_config(default_config, env_config)
        
        # Override with environment variables
        self._override_with_env_vars(default_config)
        
        self._config = default_config
    
    def _merge_config(self, base_config: Dict, override_config: Dict):
        """Recursively merge configuration dictionaries."""
        for key, value in override_config.items():
            if key in base_config and isinstance(base_config[key], dict) and isinstance(value, dict):
                self._merge_config(base_config[key], value)
            else:
                base_config[key] = value
    
    def _override_with_env_vars(self, config: Dict):
        """Override configuration with environment variables."""
        env_mappings = {
            "WEB_BASE_URL": ("web", "base_url"),
            "API_BASE_URL": ("api", "base_url"),
            "DATABASE_URL": ("database", "url"),
            "BROWSER_NAME": ("browser", "name"),
            "BROWSER_HEADLESS": ("browser", "headless"),
            "IMPLICIT_WAIT": ("web", "implicit_wait"),
            "EXPLICIT_WAIT": ("web", "explicit_wait"),
            "PAGE_LOAD_TIMEOUT": ("web", "page_load_timeout"),
            "API_TIMEOUT": ("api", "timeout"),
            "LOG_LEVEL": ("logging", "level"),
            "PARALLEL_WORKERS": ("parallel", "workers"),
            "RETRY_COUNT": ("retry", "max_retries"),
            "SCREENSHOT_ON_FAILURE": ("reporting", "screenshot_on_failure"),
            "VIDEO_RECORDING": ("reporting", "video_recording")
        }
        
        for env_var, config_path in env_mappings.items():
            env_value = os.getenv(env_var)
            if env_value is not None:
                # Navigate to the nested config location
                current = config
                for key in config_path[:-1]:
                    current = current[key]
                
                # Convert string values to appropriate types
                if env_value.lower() in ('true', 'false'):
                    env_value = env_value.lower() == 'true'
                elif env_value.isdigit():
                    env_value = int(env_value)
                
                current[config_path[-1]] = env_value
    
    def get_config(self) -> Dict[str, Any]:
        """Get the complete configuration."""
        return self._config
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a specific configuration value using dot notation."""
        keys = key.split('.')
        value = self._config
        
        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default
    
    def set(self, key: str, value: Any):
        """Set a configuration value using dot notation."""
        keys = key.split('.')
        current = self._config
        
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        current[keys[-1]] = value
    
    def save_config(self, filename: str = None):
        """Save current configuration to a file."""
        if filename is None:
            env = os.getenv("TEST_ENV", "staging")
            filename = self.config_dir / f"{env}_current.yaml"
        
        with open(filename, 'w') as f:
            yaml.dump(self._config, f, default_flow_style=False, indent=2)
    
    def reload_config(self):
        """Reload configuration from files."""
        self._load_config()
    
    def get_environment_config(self, env: str) -> Dict[str, Any]:
        """Get configuration for a specific environment."""
        env_config_file = self.config_dir / f"{env}.yaml"
        
        if env_config_file.exists():
            with open(env_config_file, 'r') as f:
                return yaml.safe_load(f) or {}
        
        return {}
    
    def create_environment_config(self, env: str, config: Dict[str, Any]):
        """Create a new environment configuration file."""
        env_config_file = self.config_dir / f"{env}.yaml"
        
        with open(env_config_file, 'w') as f:
            yaml.dump(config, f, default_flow_style=False, indent=2)
    
    def validate_config(self) -> bool:
        """Validate the current configuration."""
        required_keys = [
            "web.base_url",
            "api.base_url",
            "browser.name"
        ]
        
        for key in required_keys:
            if self.get(key) is None:
                raise ValueError(f"Missing required configuration: {key}")
        
        return True


# Global configuration instance
config_manager = ConfigManager() 