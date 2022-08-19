# STUPID BIG IN HERE SOMEWHERE
# DEBUG
from Connector import Connector

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

    def __repr__(self):
        return f"BinaryGate(pin_a: {self.pin_a}, pin_b: {self.pin_b})"

    def get_pin_a(self):
        if self.pin_a != None:
            return self.pin_a.get_from().get_output()
        else:
            return int(input(f"Once Enter pin A input for gate {self.get_label()}: "))

    def get_pin_b(self):
        if self.pin_b != None:
            return self.pin_b.get_from().get_output()
        else:
            return int(input(f"Twice Enter pin B input for gate {self.get_label()}: "))

    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        elif self.pin_b == None:
            self.pin_b = source
        else:
            raise RuntimeError("Error: no empty pins")

class UnaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pin = None

    def get_pin(self):
        if self.pin != None:
            return self.pin.get_from().get_output()
        return int(input(f"Enter pin input for gate {self.get_label()}: "))

    def set_next_pin(self, source):
        if self.pin != None:
            raise RuntimeError("Error: no empty pins")
        self.pin = source

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

def main():
    g1 = AndGate("G1")
    g2 = XorGate("G2")
    g2.pin_a = g1.get_pin_a()
    g2.pin_b = g1.get_pin_b()

    output_from = g1.get_output()
    output_to = g2.get_output()
    print(f"C: {output_from}, S: {output_to}" )

main()