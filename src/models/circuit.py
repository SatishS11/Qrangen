import qiskit

# def Circuit():
    # return h() * measure()

class AnyCircuit:
    def __init__(self, nqubits=None, nbits=None):
        if nqubits is None:
            self.qr = None
            self.cr = None
            self.U = qiskit.QuantumCircuit()
        else:
            self.qr = qiskit.QuantumRegister(nqubits)
            if nbits is None:
                nbits = nqubits
            self.cr = qiskit.ClassicalRegister(nbits)
            self.U = qiskit.QuantumCircuit(self.qr, self.cr)

    def __str__(self):
        return str(self.U)

    def __mul__(self, circ):
        result = AnyCircuit()
        result.U = self.U + circ.U
        return result

    def __matmul__(self, circ):
        result = AnyCircuit()
        result.U.add_register(self.qr)
        result.U.add_register(self.cr)
        result.U.add_register(circ.qr)
        result.U.add_register(circ.cr)
        result.U = circ.U + self.U
        return result
    def to_qiskit(self):
        return self.U

def h(iqubit=0, nqubits=1):
    result = AnyCircuit(nqubits)
    result.U.h(result.qr[iqubit])
    return result

def x(iqubit=0, nqubits=1):
    result = AnyCircuit(nqubits)
    result.U.x(result.qr[iqubit])
    return result

def y(iqubit=0, nqubits=1):
    result = AnyCircuit(nqubits)
    result.U.y(result.qr[iqubit])
    return result

def z(iqubit=0, nqubits=1):
    result = AnyCircuit(nqubits)
    result.U.z(result.qr[iqubit])
    return result

def measure(iqubit=0, ibit=None, nqubits=1):
    if ibit == None:
        ibit = iqubit
    result = AnyCircuit(nqubits)
    result.U.measure(result.qr[iqubit], result.cr[ibit])
    return result

Circuit = h

# if __name__ == "__main__":
    # print(Circuit())
