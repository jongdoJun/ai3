from dataclasses import dataclass
@dataclass
class Entity:
    context:str
    fname:str
    target:str

    @property
    def context(self)->str: return self._context

    @property
    def fname(self)->str : return self._fname

    @property
    def target(self) -> str: return self._target

    @context.setter
    def context(self, context) : self._context = context

    @fname.setter
    def fname(self, fname) : self._fname = fname

    @target.setter
    def target(self, target) : self._target = target