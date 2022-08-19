# Implemented Boolean logic gates, namely:
# and, or, nand, nor, xor, not

class LogicGate:
    def __init__(self, label):
        self.label = label
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        return int(input(f"Enter pin A input for gate {self.get_label()}: "))

    def get_pin_b(self):
        return int(input(f"Enter pin B input for gate {self.get_label()}: "))

class UnaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pin = None

    def get_pin(self):
        return int(input(f"Enter pin input for gate {self.get_label()}: "))

class AndGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        return int(a and b)

class NandGate(AndGate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        return int(not super().perform_gate_logic())

class OrGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        return int(a or b)

class NorGate(OrGate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        return int(not super().perform_gate_logic())

class XorGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = bool(self.get_pin_a())
        b = bool(self.get_pin_b())
        return int(a ^ b)

class NotGate(UnaryGate):
    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        pin = self.get_pin()
        return int(not pin)
