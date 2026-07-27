# -*- coding: utf-8 -*-
"""Smoke-тесты окружения: pytest tests/

Проверяют, что окружение из requirements.txt пригодно для выполнения
всех практических работ курса. Выполняются на CPU за ~1 минуту.
"""
import random

import numpy as np


def test_python_version():
    import sys

    assert sys.version_info >= (3, 10), "Требуется Python 3.10+"


def test_imports():
    import matplotlib  # noqa: F401
    import pandas  # noqa: F401
    import sklearn  # noqa: F401
    import torch  # noqa: F401
    import torchvision  # noqa: F401


def test_numpy_seed_reproducibility():
    a = np.random.default_rng(31).integers(0, 10, size=(10, 10))
    b = np.random.default_rng(31).integers(0, 10, size=(10, 10))
    assert (a == b).all()


def test_torch_seed_reproducibility():
    import torch

    torch.manual_seed(31)
    a = torch.randn(4, 4)
    torch.manual_seed(31)
    b = torch.randn(4, 4)
    assert torch.equal(a, b)


def test_global_seed_helper():
    """Тот же приём фиксации seed, что в стартовых ноутбуках."""
    import torch

    seed = 31
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    assert random.random() == random.Random(seed).random()
