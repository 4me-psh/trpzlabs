from abc import ABC, abstractmethod


class Recommendations(ABC):

    @abstractmethod
    def recommend(self):
        pass

#інтерфейс рекомендацій