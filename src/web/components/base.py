from typing import Any


class DashAppBaseComponent:

    def render(self) -> Any:
        """
        Render component apps
        """
        raise NotImplementedError()
