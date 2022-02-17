# Copyright (C) 2018-2022 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""Factory functions for all ngraph ops."""
from functools import partial
from typing import Callable, Iterable, List, Optional, Set, Union

import numpy as np
from ngraph.impl import Node, Shape
from ngraph.impl.op import Constant, Parameter
from ngraph.opset_utils import _get_node_factory
from ngraph.utils.decorators import binary_op, nameable_op, unary_op
from ngraph.utils.input_validation import (
    assert_list_of_ints,
    check_valid_attributes,
    is_non_negative_value,
    is_positive_value,
)
from ngraph.utils.node_factory import NodeFactory
from ngraph.utils.tensor_iterator_types import (
    GraphBody,
    TensorIteratorSliceInputDesc,
    TensorIteratorMergedInputDesc,
    TensorIteratorInvariantInputDesc,
    TensorIteratorBodyOutputDesc,
    TensorIteratorConcatOutputDesc,
)
from ngraph.utils.types import (
    NodeInput,
    NumericData,
    NumericType,
    ScalarData,
    TensorShape,
    as_node,
    as_nodes,
    get_dtype,
    get_element_type,
    get_element_type_str,
    make_constant_node,
)

_get_node_factory_opset7 = partial(_get_node_factory, "opset7")


# -------------------------------------------- ops ------------------------------------------------


@nameable_op
def einsum(
        inputs: List[Node],
        equation: str
) -> Node:
    """Return a node which performs Einsum operation.

    :param inputs: The list of input nodes
    :param equation: Einsum equation
    :return: The new node performing Einsum operation on the inputs
    """
    attributes = {
        "equation": equation
    }

    return _get_node_factory_opset7().create("Einsum", as_nodes(*inputs), attributes)


@nameable_op
def gelu(
        data: Node,
        approximation_mode: str,
        name: Optional[str] = None,
) -> Node:
    """Return a node which performs Gelu activation function.

    :param data: The node with data tensor.
    :param approximation_mode: defines which approximation to use ('tanh' or 'erf')
    :param name: Optional output node name.
    :return: The new node performing a Gelu activation with the input tensor.
    """
    inputs = as_nodes(data)

    attributes = {
        "approximation_mode": approximation_mode
    }

    return _get_node_factory_opset7().create("Gelu", inputs, attributes)


@nameable_op
def roll(
        data: NodeInput,
        shift: NodeInput,
        axes: NodeInput,
) -> Node:
    """Return a node which performs Roll operation.

    :param data: The node with data tensor.
    :param shift: The node with the tensor with numbers of places by which elements are shifted.
    :param axes: The node with the tensor with axes along which elements are shifted.
    :return: The new node performing a Roll operation on the input tensor.
    """
    inputs = as_nodes(data, shift, axes)

    return _get_node_factory_opset7().create("Roll", inputs)


@nameable_op
def gather(
        data: NodeInput,
        indices: NodeInput,
        axis: NodeInput,
        batch_dims: Optional[int] = 0,
) -> Node:
    """Return a node which performs Gather.

    :param data:         N-D tensor with data for gathering
    :param indices:      N-D tensor with indices by which data is gathered
    :param axis:         axis along which elements are gathered
    :param batch_dims:   number of batch dimensions
    :return:             The new node which performs Gather
    """
    inputs = as_nodes(data, indices, axis)
    attributes = {
        "batch_dims": batch_dims
    }
    return _get_node_factory_opset7().create("Gather", inputs, attributes)


def dft(
        data: NodeInput,
        axes: NodeInput,
        signal_size: Optional[NodeInput] = None,
) -> Node:
    """Return a node which performs DFT operation.

    :param data: Tensor with transformed data.
    :param axes: Tensor with axes to transform.
    :param signal_size: Tensor specifying signal size with respect to axes from the input 'axes'.
    :return: The new node which performs DFT operation on the input data tensor.
    """
    if signal_size is None:
        inputs = as_nodes(data, axes)
    else:
        inputs = as_nodes(data, axes, signal_size)

    return _get_node_factory_opset7().create("DFT", inputs)


@nameable_op
def idft(
        data: NodeInput,
        axes: NodeInput,
        signal_size: Optional[NodeInput] = None,
) -> Node:
    """Return a node which performs IDFT operation.

    :param data: Tensor with transformed data.
    :param axes: Tensor with axes to transform.
    :param signal_size: Tensor specifying signal size with respect to axes from the input 'axes'.
    :return: The new node which performs IDFT operation on the input data tensor.
    """
    if signal_size is None:
        inputs = as_nodes(data, axes)
    else:
        inputs = as_nodes(data, axes, signal_size)

    return _get_node_factory_opset7().create("IDFT", inputs)
