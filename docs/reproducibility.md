# Настройка окружения и воспроизводимость

## 1. Установка окружения

Требуется Python **3.10+**.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Проверка окружения (~1 минута, CPU):

```bash
pytest tests/
```

Все тесты должны проходить. Если тест падает — окружение установлено неверно; типовые причины: устаревший Python, конфликт версий numpy/torch, отсутствие пакета из `requirements.txt`.

## 2. Загрузка данных

```bash
python scripts/download_data.py          # минимум для ПР 5–6
python scripts/download_data.py --all    # все наборы (кроме PlantVillage)
```

PlantVillage (Кейс 2) загружается вручную — инструкция в `python scripts/download_data.py --help`. Загруженные данные попадают в `data/` и не коммитятся (см. `.gitignore`).

## 3. CPU или GPU

| Работы | CPU | GPU |
| --- | --- | --- |
| ПР 1–9, Кейс 1 | достаточно | не требуется |
| ПР 10, Кейс 2 | выполнимо (обучение CNN на MNIST — минуты; transfer learning ResNet-18 на подвыборке — до ~20 минут) | рекомендуется |

Код в стартовых ноутбуках выбирает устройство автоматически:

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
```

При отсутствии GPU допустимо уменьшить объём данных (подвыборка) и число эпох — качество моделей при этом обсуждается на защите с поправкой на ограничение.

## 4. Фиксация случайности

Базовый seed курса — `30 + номер варианта`. В начале каждого ноутбука:

```python
VARIANT = ...            # номер варианта
SEED = 30 + VARIANT
import random, numpy as np, torch
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)
```

Замечания:

- полная битовая воспроизводимость между CPU и GPU (и между версиями PyTorch) не гарантируется — допускаются малые расхождения метрик; выводы работы от них зависеть не должны;
- для `DataLoader` с `num_workers > 0` дополнительно передавайте `generator=torch.Generator().manual_seed(SEED)`;
- фиксируйте seed **один раз в начале** ноутбука, а не перед каждой ячейкой.

## 5. Стартовые ноутбуки

Заготовки для всех работ лежат в `attachments/` соответствующих модулей:

- `M1-fundamentals-of-ann/attachments/` — ПР 1–4;
- `M2-complex-models/attachments/` — ПР 5–10;
- `Project/attachments/` — кейсы 1–2.

Ноутбук — это каркас (структура, проверки окружения, подсказки), а не решение: все `TODO` заполняются самостоятельно в соответствии с КИМ и правилами использования генеративного ИИ.
