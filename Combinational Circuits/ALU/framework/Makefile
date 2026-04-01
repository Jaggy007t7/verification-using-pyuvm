TOPLEVEL_LANG := verilog

PWD := $(shell pwd)

SIM ?= verilator

EXTRA_ARGS += --trace --trace-structs
WARNING_ARGS += -Wno-TIMESCALEMOD -Wno-WIDTH -Wno-UNOPT

export PYTHONPATH := $(PWD)/../model:$(PYTHONPATH)

ifeq ($(TOPLEVEL_LANG),verilog)
VERILOG_SOURCES := $(PWD)/../hdl/alu.v
else ifeq ($(TOPLEVEL_LANG),vhdl)
VHDL_SOURCES := $(PWD)/../hdl/alu.v
else
$(error A valid value (verilog or vhdl) was not provided for TOPLEVEL_LANG=$(TOPLEVEL_LANG))
endif

TOPLEVEL := alu
MODULE := alu_testbench

include $(shell cocotb-config --makefiles)/Makefile.sim

