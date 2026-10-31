# Target application.
TARGET := deriv_example

# C compiler.
C_COMPILER = gcc

# C compiler flags.
C_FLAGS := -Wall -Werror -std=c11

# Source files.
SRC_FILES := main.c

# Build and run target by default.
default: build run

# Build the target.
build:
	@$(C_COMPILER) $(SRC_FILES) -o $(TARGET) $(C_FLAGS)

# Run the target.
run:
	@./$(TARGET)

# Clean the target.
clean:
	@rm -f $(TARGET)

.PHONY: default build run clean
