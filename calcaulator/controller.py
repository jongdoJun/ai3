from calcaulator.model import Model
from calcaulator.service import Service
from calcaulator.tensor_service import TensorService
class Controller:
    def exec(self, num1, num2, opcode):
        model = Model()
        model.num1 = num1
        model.num2 = num2
        model.opcode = opcode
        service = Service(model)
        if opcode == '+':
            result = service.add()
        if opcode == '-':
            result = service.subract()
        if opcode == '*':
            result = service.multiply()
        if opcode == '/':
            result = service.divide()
        return result
    def tensorExec(self,num1,num2,opcode):
        model = Model()
        model.num1 = num1
        model.num2 = num2
        model.opcode = opcode
        service = TensorService(model)
        if opcode == '+':
            result = service.add()
        if opcode == '-':
            result = service.subract()
        if opcode == '*':
            result = service.multiply()
        if opcode == '/':
            result = service.divide()
        return result