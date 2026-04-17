import abc from ABC

class Observer(ABC):
  @abstractmethod
  def update(self, message):
    pass
