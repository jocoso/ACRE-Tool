import logging
from abc import ABC, abstractmethod
import unittest


# Setting logging up...
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[logging.StreamHandler()]
    )


setup_logging()
logger = logging.getLogger(__name__)


class SceneModule(ABC):
    """Abstract base class for scene modules."""

    # Core Methods
    @abstractmethod
    def start(self):
        """Start the scene."""
        pass

    @abstractmethod
    def stop(self):
        """Stop the scene."""
        pass

    @abstractmethod
    def in_progress(self):
        """Determine if the scene is in progress."""
        pass

    @abstractmethod
    def kill_condition_met(self):
        """Determine if the scene's kill condition is met."""
        pass

    # Helpers
    def load_resources(self):
        """Optional: Load resources required by the scene."""
        pass 

    def unload_resources(self):
        """Optional: Unload resources."""
        pass

    def on_enter(self):
        """Optional: Define behaviour when entering the scene."""
        pass

    def on_exit(self):
        """Optional: Define behaviour when exiting the scene."""
        pass

    def transition_to_next(self):
        """Optional: Handle transition to the next scene."""
        pass


class SceneModuleImp(SceneModule):
    """Example implementation of SceneModule."""

    def start(self):
        logger.info("SceneModuleImp started.")

    def stop(self):
        logger.info("SceneModuleImp stopped.")

    def in_progress(self):
        return False

    def kill_condition_met(self):
        return False


class TestSceneModule(unittest.TestCase):
    """Test suite for SceneModule implementations."""
        
    def test_can_instantiate_implementation(self):
        """Ensure SceneModuleImp can be instantiated without errors."""
        try:
            instance = SceneModuleImp()
            self.assertIsInstance(instance, SceneModule)
        except Exception as e:
            self.fail(f"Instantiation failed with exception: {e}")


if __name__ == '__main__':
    unittest.main()
