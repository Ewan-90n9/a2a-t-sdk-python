from __future__ import annotations

import importlib
import sys
from pathlib import Path
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"

if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


class ModuleLayoutTest(unittest.TestCase):
    def test_legacy_exception_and_result_modules_are_removed(self) -> None:
        removed_modules = [
            "a2a_t.negotiation.common.exceptions",
            "a2a_t.server.prompt_compliance.result",
            "a2a_t.prompt.task_rendering.exceptions",
        ]

        for module_name in removed_modules:
            with self.subTest(module_name=module_name):
                with self.assertRaises(ModuleNotFoundError):
                    importlib.import_module(module_name)


if __name__ == "__main__":
    unittest.main()
