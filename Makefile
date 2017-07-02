#!/usr/bin/env bash
THIS_MAKEFILE := $(word $(words $(MAKEFILE_LIST)),$(MAKEFILE_LIST))
PROJECT_ROOT := $(realpath $(dir $(THIS_MAKEFILE)))

print-%: ; @echo $* = $($*)


