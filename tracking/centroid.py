from .abstract import AbstractPizzaTracker
from video import Video

class CentroidTracker(AbstractPizzaTracker):
    def identify(self, metadata):
        """
        Metodo identifica pizzas unicas en la metadata

        Recibe un DataFrame de formato

        frame, x1, y1, x2, y2

        Y retorna un DataFrame de formato

        frame, label, x1, y1, x2, y2
        """
        video = Video(metadata)
        video.track(window=50)
        return video.to_df()
