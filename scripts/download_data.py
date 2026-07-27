#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Загрузка наборов данных для практических работ и кейсов.

Использование:
    python scripts/download_data.py            # малые CSV MNIST (ПР 5) + torchvision MNIST
    python scripts/download_data.py --full     # + полные CSV MNIST (~110 МБ)
    python scripts/download_data.py --vision   # + CIFAR-10 и SVHN (ПР 6, 10)
    python scripts/download_data.py --uci      # + Default of Credit Card Clients (Кейс 1)
    python scripts/download_data.py --all      # всё сразу

Данные сохраняются в каталог data/ в корне репозитория (внесён в .gitignore).

PlantVillage (Кейс 2) не имеет стабильной прямой ссылки: скачайте набор
со страницы https://www.kaggle.com/datasets/emmarex/plantdisease (или зеркала,
указанного преподавателем) и распакуйте в data/plantvillage/ так, чтобы
каждому классу соответствовал подкаталог с изображениями (формат ImageFolder).
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

SMALL_MNIST = {
    "mnist_train_100.csv": "https://raw.githubusercontent.com/makeyourownneuralnetwork/makeyourownneuralnetwork/master/mnist_dataset/mnist_train_100.csv",
    "mnist_test_10.csv": "https://raw.githubusercontent.com/makeyourownneuralnetwork/makeyourownneuralnetwork/master/mnist_dataset/mnist_test_10.csv",
}
FULL_MNIST = {
    "mnist_train.csv": "https://pjreddie.com/media/files/mnist_train.csv",
    "mnist_test.csv": "https://pjreddie.com/media/files/mnist_test.csv",
}
UCI_CREDIT = {
    "default_of_credit_card_clients.xls": "https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls",
}


def fetch(url: str, dest: Path) -> None:
    import requests

    if dest.exists():
        print(f"  [пропуск] {dest.relative_to(ROOT)} уже существует")
        return
    print(f"  [загрузка] {url}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    dest.write_bytes(resp.content)
    print(f"  [готово]   {dest.relative_to(ROOT)} ({len(resp.content) / 1e6:.1f} МБ)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--full", action="store_true", help="полные CSV MNIST (~110 МБ)")
    parser.add_argument("--vision", action="store_true", help="CIFAR-10 и SVHN через torchvision")
    parser.add_argument("--uci", action="store_true", help="Default of Credit Card Clients (Кейс 1)")
    parser.add_argument("--all", action="store_true", help="загрузить всё")
    args = parser.parse_args()
    if args.all:
        args.full = args.vision = args.uci = True

    print("MNIST (малые CSV для ПР 5):")
    for name, url in SMALL_MNIST.items():
        fetch(url, DATA / "mnist" / name)

    if args.full:
        print("MNIST (полные CSV):")
        for name, url in FULL_MNIST.items():
            fetch(url, DATA / "mnist" / name)

    print("MNIST (torchvision, для ПР 6–10):")
    from torchvision import datasets

    datasets.MNIST(root=DATA / "torchvision", train=True, download=True)
    datasets.MNIST(root=DATA / "torchvision", train=False, download=True)

    if args.vision:
        print("CIFAR-10 и SVHN (torchvision):")
        datasets.CIFAR10(root=DATA / "torchvision", train=True, download=True)
        datasets.CIFAR10(root=DATA / "torchvision", train=False, download=True)
        datasets.SVHN(root=DATA / "torchvision" / "svhn", split="train", download=True)
        datasets.SVHN(root=DATA / "torchvision" / "svhn", split="test", download=True)

    if args.uci:
        print("UCI Default of Credit Card Clients (Кейс 1):")
        for name, url in UCI_CREDIT.items():
            fetch(url, DATA / "uci_credit" / name)

    print("\nГотово. PlantVillage (Кейс 2) загружается вручную — см. --help.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
