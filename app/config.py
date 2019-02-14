"""Config module."""


class BaseConfig:
    """Base class of configurations."""
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(BaseConfig):
    """Test configs."""

    TESTING = True


class DevelopmentConfig(BaseConfig):
    """Development configs."""

    TESTING = False


def get_config(config_name):
    configs = {
        'test': TestConfig,
        'development': DevelopmentConfig,
    }
    return configs[config_name]
