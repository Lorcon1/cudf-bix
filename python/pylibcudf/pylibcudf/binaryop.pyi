# Copyright (c) 2024, NVIDIA CORPORATION.

from enum import IntEnum

from pylibcudf.column import Column
from pylibcudf.scalar import Scalar
from pylibcudf.types import DataType

class BinaryOperator(IntEnum):
    ADD = ...
    SUB = ...
    MUL = ...
    DIV = ...
    TRUE_DIV = ...
    FLOOR_DIV = ...
    MOD = ...
    PMOD = ...
    PYMOD = ...
    POW = ...
    INT_POW = ...
    LOG_BASE = ...
    ATAN2 = ...
    SHIFT_LEFT = ...
    SHIFT_RIGHT = ...
    SHIFT_RIGHT_UNSIGNED = ...
    BITWISE_AND = ...
    BITWISE_OR = ...
    BITWISE_XOR = ...
    LOGICAL_AND = ...
    LOGICAL_OR = ...
    EQUAL = ...
    NOT_EQUAL = ...
    LESS = ...
    GREATER = ...
    LESS_EQUAL = ...
    GREATER_EQUAL = ...
    NULL_EQUALS = ...
    NULL_MAX = ...
    NULL_MIN = ...
    NULL_NOT_EQUALS = ...
    GENERIC_BINARY = ...
    NULL_LOGICAL_AND = ...
    NULL_LOGICAL_OR = ...
    INVALID_BINARY = ...

def binary_operation(
    lhs: Column | Scalar,
    rhs: Column | Scalar,
    op: BinaryOperator,
    output_type: DataType,
) -> Column: ...
def is_supported_operation(
    out: DataType, lhs: DataType, rhs: DataType, op: BinaryOperator
) -> bool: ...
