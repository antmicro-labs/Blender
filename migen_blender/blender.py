from migen import *

class Rgb(Module):
    def __init__(self):
        self.dma_1 = dma_1 = Signal(8)
        self.dma_2 = dma_2 = Signal(8)
        self.result = result = Signal(8)
        self.comb += result.eq(dma_1*dma_2)

class MyTop(Module):
    def __init__(self):
        self.image_1 = image_1 = Array(Array(Signal(8) for a in range(4)) for b in range(4))
        self.image_2 = image_2 = Array(Array(Signal(8) for a in range(4)) for b in range(4))
        self.inp_1 = inp_1 = Signal(8)
        self.inp_2 = inp_2 = Signal(8)
        #declare the module
        multiply = Rgb()
        #add the module to our submodules list
        self.submodules += multiply
        #assign this res is the same as the one of the submodules
        self.res = multiply.result

        #out.eq(my_2d_array[x][y])
        #the adder takes our input and add 3
        self.comb += [
            multiply.dma_1.eq(inp_1),
            multiply.dma_2.eq(inp_2)
            ]
        for x in range(4):
            for y in range(4):
                image_1[x][y].eq(2)
                image_2[x][y].eq(2)

def rbg_multiply(dut):
    for x in range(4):
        for y in range(4):
            yield dut.image_1[x][y].eq(2)
            yield dut.image_2[x][y].eq(2)
            #yield dut.inp_1.eq(dut.image_1[x][y])
            #yield dut.inp_1.eq(dut.image_1[x][y])
            print("{} {} {} {}".format(x, y, (yield dut.image_1[x][y]), (yield dut.image_2[x][y])))

dut = MyTop()
run_simulation(dut, rbg_multiply(dut), vcd_name="result_rgb.vcd")