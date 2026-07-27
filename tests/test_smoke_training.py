# -*- coding: utf-8 -*-
"""Smoke-тесты обучения: минимальные MLP и CNN действительно обучаются.

Эталонные проверки для ПР 4, 7 (MLP) и ПР 10 (CNN): на синтетических данных
loss должен убывать, размерности выходов — совпадать с ожидаемыми.
"""
import numpy as np
import torch
import torch.nn as nn

SEED = 31


def _make_blobs(n=256, n_features=8, n_classes=2):
    from sklearn.datasets import make_classification

    X, y = make_classification(
        n_samples=n, n_features=n_features, n_informative=n_features // 2,
        n_classes=n_classes, random_state=SEED,
    )
    return torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.long)


def test_mlp_trains_loss_decreases():
    torch.manual_seed(SEED)
    X, y = _make_blobs()
    model = nn.Sequential(nn.Linear(8, 16), nn.ReLU(), nn.Linear(16, 2))
    opt = torch.optim.Adam(model.parameters(), lr=1e-2)
    loss_fn = nn.CrossEntropyLoss()

    first_loss = last_loss = None
    for _ in range(30):
        opt.zero_grad()
        loss = loss_fn(model(X), y)
        loss.backward()
        opt.step()
        last_loss = loss.item()
        if first_loss is None:
            first_loss = last_loss

    assert last_loss < first_loss * 0.7, (
        f"Loss не убывает: {first_loss:.4f} → {last_loss:.4f}"
    )


def test_cnn_forward_shapes():
    """Каркас CNN из ПР 10: 2 свёрточных слоя + классификатор, вход 28×28."""
    torch.manual_seed(SEED)
    model = nn.Sequential(
        nn.Conv2d(1, 8, kernel_size=3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
        nn.Conv2d(8, 16, kernel_size=3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
        nn.Flatten(), nn.Linear(16 * 7 * 7, 10),
    )
    x = torch.randn(4, 1, 28, 28)
    out = model(x)
    assert out.shape == (4, 10)


def test_manual_backprop_matches_autograd():
    """Идея ПР 3/9: ручной градиент совпадает с autograd для линейного слоя."""
    torch.manual_seed(SEED)
    X = torch.randn(16, 4)
    y = torch.randn(16, 1)
    W = torch.randn(4, 1, requires_grad=True)

    pred = X @ W
    loss = ((pred - y) ** 2).mean()
    loss.backward()

    manual_grad = 2 * X.T @ (X @ W.detach() - y) / len(X)
    assert torch.allclose(W.grad, manual_grad, atol=1e-5)


def test_numpy_sigmoid_stable():
    """Сигмоида из ПР 2 не должна переполняться на больших аргументах."""
    x = np.array([-500.0, 0.0, 500.0])
    with np.errstate(over="raise"):
        s = 1.0 / (1.0 + np.exp(-np.clip(x, -60, 60)))
    assert s[0] < 1e-20 and abs(s[1] - 0.5) < 1e-12 and s[2] > 1 - 1e-12
