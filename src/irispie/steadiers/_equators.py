"""
Steady equator
"""


#[

from __future__ import annotations

import numpy as _np
from typing import (Callable, Protocol, )
from collections.abc import (Iterable, )

from datapie import wrongdoings as _wd

from ..equators import plain as _plain
from ..equations import Equation
from ..quantities import Quantity

#]


class SteadyEquatorProtocol:
    """
    """
    #[
    def eval(
        self,
        steady_array: _np.ndarray,
    ) -> _np.ndarray:
        ...
    #]


class SteadyEquator:
    """
    """
    #[

    def __init__(
        self,
        equations: Iterable[Equation],
        *,
        context: dict[str, Callable] | None = None,
    ) -> None:
        r"""
        """
        self._equator = _plain.PlainEquator(equations, context=context, )
        self._equations = tuple(equations)

    def eval(
        self,
        steady_array: _np.ndarray,
        column_offset: int,
    ) -> _np.ndarray:
        ...

    def _report_details_on_nonfinites(self, eval_array: _np.ndarray, ) -> str:
        details = []
        indexes = _np.where(~_np.isfinite(eval_array, ))[0]
        equations_to_report = tuple(self._equations[i].human for i in indexes)
        details.extend(self._equations[i].human for i in indexes)
        return details

    #]


class FlatSteadyEquator(SteadyEquator, ):
    """
    """
    #[

    def eval(
        self,
        steady_array: _np.ndarray,
        column_offset: int,
    ) -> _np.ndarray:
        r"""
        """
        time_zero = self._equator.eval(steady_array, column_offset, )
        if not _np.isfinite(time_zero).all():
            error_message = ["Non-finite values in these equations when evaluating steady state", ]
            error_message.extend(self._report_details_on_nonfinites(time_zero, ), )
            raise ValueError(_wd.prepare_message(error_message, ), )
        return time_zero

    #]


class NonflatSteadyEquator(SteadyEquator, ):
    """
    """
    #[

    # Assigned in the evaluator
    NONFLAT_STEADY_SHIFT = ...

    def eval(
        self,
        steady_array: _np.ndarray,
        column_offset: int,
    ) -> _np.ndarray:
        """
        """
        time_zero = self._equator.eval(steady_array, column_offset, )
        if not _np.isfinite(time_zero).all():
            error_message = ["Non-finite values in these equations when evaluating steady state at time t+0", ]
            error_message.extend(self._report_details_on_nonfinites(time_zero, ), )
            raise ValueError(_wd.prepare_message(error_message, ), )
        time_k = self._equator.eval(steady_array, column_offset + self.NONFLAT_STEADY_SHIFT, )
        if not _np.isfinite(time_k).all():
            error_message = ["Non-finite values in these equations when evaluating steady state at time t+k", ]
            error_message.extend(self._report_details_on_nonfinites(time_k, ), )
            raise ValueError(_wd.prepare_message(error_message, ), )
        return _np.hstack((time_zero, time_k, ))

    #]


