#!/usr/bin/env python
# coding=utf-8

import torch
from torch.autograd import Function


class quantize_tensor(Function):
    def __init__(self, int_bits, frac_bits):
        self.int_bits = int_bits
        self.frac_bits = frac_bits
    def forward(self, tensor, int_bits, frac_bits):
        x.data[x.data>=2**int_bits-1] = 2**int_bits-1
        x.data[x.data<=-2**int_bits] = -2**int_bits
        x.data = torch.round(x*pow(2, frac_bits))
        x.data = torch.div(x, pow(2, frac_bits))
        return x


