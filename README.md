# Фонд оценочных средств по дисциплине «Основы искусственных нейронных сетей»

Направление 09.03.02 «Информационные системы и технологии», 2 курс, 4 семестр, 2 ЗЕТ / 72 часа, форма промежуточной аттестации — зачёт с оценкой.

Репозиторий содержит рабочий программу дисциплины (РПД) и фонд оценочных средств (ФОС), построенный на основе компетентностно-ролевой модели (КРМ) версии 3.0.

---

## 1. О дисциплине

**Цель** — овладение основными методами искусственного интеллекта, навыками разработки моделей искусственных нейронных сетей (ИНС) и подходами к их обучению.

**Состав:** 10 лекций + 10 практических работ + 2 кейс-задачи.

**Компетенции КРМ:** MF-1 (индикатор MF-1.2, уровень С) и DL-1 (индикаторы DL-1.1, DL-1.2, DL-1.3, DL-1.4, DL-1.12, уровень Б). **Якорная «выходная» роль — TADS**; рост к ML Engineer, Data Analyst, ML Researcher обеспечивается в постреквизитах.

Подробнее — в [`docs/rpd.md`](docs/rpd.md).

## 2. Модель измерения

Связка результатов обучения с КРМ и оценочными средствами. Полная машиночитаемая матрица — в [`data/role-competency-matrix.csv`](data/role-competency-matrix.csv); каталог компетенций — в [`data/competency-catalog.csv`](data/competency-catalog.csv).

| Модуль / КИМ | Компетенция | Индикатор | Уровень | Дескриптор (кратко) | Форма контроля | КИМ | Ресурсы |
| --- | --- | --- | --- | --- | --- | --- | --- |
| M1 / ПР 1 | MF-1 | MF-1.2 | С | Матричные операции на Python | Текущая | [КИМ-01](M1-fundamentals-of-ann/kim-01-matrix-algebra.md) | [numpy](resources/software/python-libs/README.md) |
| M1 / ПР 2 | DL-1 | DL-1.2, DL-1.1 | Б | Построение MLP, подготовка к обучению | Текущая | [КИМ-02](M1-fundamentals-of-ann/kim-02-mlp-prep.md) | numpy |
| M1 / ПР 3 | DL-1 | DL-1.1 | Б | Обучение ИНС (backprop) | Текущая | [КИМ-03](M1-fundamentals-of-ann/kim-03-training.md) | numpy, matplotlib |
| M1 / ПР 4 | DL-1, MF-1 | DL-1.1, MF-1.2 | Б, С | Диагностика переобучения, ROC-AUC | Текущая | [КИМ-04](M1-fundamentals-of-ann/kim-04-overfitting-validation.md) | scikit-learn |
| M2 / ПР 5 (+ Кейс 1) | DL-1, MF-1 | DL-1.2, MF-1.2 | Б, С | Метрики многоклассовой классификации | Текущая | [КИМ-05](M2-complex-models/kim-05-classification-metrics.md) | [MNIST](resources/datasets/README.md) |
| M2 / ПР 6 | DL-1 | DL-1.1 | Б | Mini-batch GD, Latency/Throughput | Текущая | [КИМ-06](M2-complex-models/kim-06-minibatch-gd.md) | PyTorch |
| M2 / ПР 7 | DL-1 | DL-1.1 | Б | Регуляризация | Текущая | [КИМ-07](M2-complex-models/kim-07-regularization.md) | PyTorch |
| M2 / ПР 8 | DL-1 | DL-1.1 | Б | Стабилизация градиентов | Текущая | [КИМ-08](M2-complex-models/kim-08-gradient-stabilization.md) | PyTorch |
| M2 / ПР 9 | DL-1 | DL-1.1 | Б | Алгоритмы оптимизации | Текущая | [КИМ-09](M2-complex-models/kim-09-optimizers.md) | PyTorch |
| M2 / ПР 10 (+ Кейс 2) | DL-1 | **DL-1.3, DL-1.4, DL-1.12** | Б | CNN + transfer learning (ResNet-18) | Текущая | [КИМ-10](M2-complex-models/kim-10-cnn.md) | torchvision |
| Project / Кейс 1 | DL-1 | DL-1.2, DL-1.1 | Б | MLP для многоклассовой классификации | Защита ПР 5 | [КИМ-01](Project/kim-01-mlp-multiclass.md) | [Default…](resources/datasets/README.md) |
| Project / Кейс 2 | DL-1 | **DL-1.3, DL-1.4, DL-1.12** | Б | CNN для распознавания образов | Защита ПР 10 | [КИМ-02](Project/kim-02-cnn-recognition.md) | [PlantVillage](resources/datasets/README.md) |
| Exam | MF-1, DL-1 | MF-1.2; DL-1.1–.4, .12 | С, Б | Итоговая проверка | Промежуточная | [КИМ-01](Exam/kim-01-grade-test.md) | [test-banks](resources/test-banks/README.md) |

## 3. Контрольно-измерительные материалы

| Группа | Расположение |
| --- | --- |
| Модуль 1 (ПР 1–4) | [`M1-fundamentals-of-ann/`](M1-fundamentals-of-ann/README.md) |
| Модуль 2 (ПР 5–10) | [`M2-complex-models/`](M2-complex-models/README.md) |
| Кейс-задачи (Project) | [`Project/`](Project/README.md) |
| Зачёт (Exam) | [`Exam/`](Exam/README.md) |

Каждый КИМ содержит: назначение и формируемые результаты, привязку к КРМ, цель, условия проведения, материалы и ресурсы, пошаговое задание, формат сдачи, критерии и шкалу, правила использования генеративного ИИ, вопросы для защиты.

## 4. Итоговая оценка

Применяется балльно-рейтинговая система (БРС), максимум 100 баллов.

| Составляющая | Баллы |
| --- | --- |
| Защита 8 практических работ (ПР 1–8, каждая до 10 баллов по 10-балльной рубрике) | 80 |
| Кейс-задачи (входят в состав ПР 5 и ПР 10) | в составе ПР |
| Посещение аудиторных занятий (10/46 ≈ 0,22 балла/час; 16 ч Л + 30 ч ПЗ = 46 ч; потолок 10) | 10 |
| Доклад на конференции по ИИ (опционально) | 10 |
| **Итого** | **100** |

> Состав «8 практических работ с защитой» = **ПР 1–8**. Десять учебных тем детализируют содержание; две кейс-задачи выносятся на защиту ПР 5 и ПР 10. Каждая ПР и кейс-задача оценивается по 10-балльной рубрике (уровни 10/8/6/4/0–3).

### Согласование шкал

- **Рубрика каждой ПР/кейса** — 10-балльная с уровнями **10 / 8 / 6 / 4 / 0–3** (это и есть «до 10 баллов за ПР» в БРС).
- **Итог** — БРС на 100 баллов с переводом в 5-балльную шкалу зачёта с оценкой.
- Обоснование выбора шкалы и портреты уровней по ролям — в [`docs/role-portraits.md`](docs/role-portraits.md) и [`methodical-guidelines/teachers-assessment/`](methodical-guidelines/teachers-assessment/README.md).

| Оценка зачёта | Баллы БРС |
| --- | --- |
| Неудовлетворительно | 0–59 |
| Удовлетворительно | 60–69 |
| Хорошо | 70–84 |
| Отлично | 85–100 |

Зачёт с оценкой получают обучающиеся, набравшие **не менее 60 баллов**. Набравшие менее 60 баллов при выполнении всех практических работ пишут итоговую зачётную работу ([`Exam/`](Exam/README.md)).

## 5. Методические материалы

- Обучающимся — [`methodical-guidelines/students/`](methodical-guidelines/students/README.md).
- Преподавателям (оценивание) — [`methodical-guidelines/teachers-assessment/`](methodical-guidelines/teachers-assessment/README.md).
- Преподавателям (ресурсы) — [`methodical-guidelines/teachers-resources/`](methodical-guidelines/teachers-resources/README.md).

## 5а. Исполняемая часть

- **Окружение** — [`requirements.txt`](requirements.txt) (Python 3.10+); настройка и воспроизводимость — [`docs/reproducibility.md`](docs/reproducibility.md).
- **Стартовые ноутбуки** для всех ПР и кейсов — в `attachments/` модулей: [ПР 1–4](M1-fundamentals-of-ann/attachments/), [ПР 5–10](M2-complex-models/attachments/), [кейсы](Project/attachments/).
- **Загрузка датасетов** — [`scripts/download_data.py`](scripts/download_data.py) (MNIST, CIFAR-10, SVHN, UCI Credit; инструкция по PlantVillage — в `--help`).
- **Smoke-тесты окружения** — `pytest tests/` (~1 минута, CPU): проверяют версии пакетов, воспроизводимость seed и работоспособность минимальных MLP/CNN.
- **Проверка ссылок и структуры** — `python scripts/check_links.py`: внутренние ссылки и якоря во всех Markdown и ноутбуках, пары КИМ/рубрика, обязательные разделы КИМ, шкала рубрик, согласованность БРС. Автоматически запускается в CI (`.github/workflows/check.yml`) на каждый push и pull request.

## 6. Структура репозитория

```
fundamentals-of-ann/
├── README.md                  (этот файл)
├── LICENSE.md
├── .gitignore
├── requirements.txt           (окружение Python)
├── scripts/                   (загрузка датасетов, проверка ссылок и структуры)
├── tests/                     (smoke-тесты окружения)
├── docs/                      (РПД, портреты уровней, воспроизводимость)
├── M1-fundamentals-of-ann/    (ПР 1–4 + рубрики + стартовые ноутбуки)
├── M2-complex-models/         (ПР 5–10 + рубрики + стартовые ноутбуки)
├── Project/                   (2 кейс-задачи + стартовые ноутбуки)
├── Exam/                      (зачёт с оценкой)
├── methodical-guidelines/     (students, teachers-assessment, teachers-resources)
├── resources/                 (datasets, papers, textbooks, software, test-banks, …)
├── data/                      (krm-v3.0.xlsx + csv)
├── team/
└── other/
```

## 7. Порядок заполнения и сопровождения

1. Изучить [`docs/rpd.md`](docs/rpd.md) и целевые роли КРМ.
2. Сверить коды компетенций/индикаторов с [`data/krm-v3.0.xlsx`](data/krm-v3.0.xlsx).
3. Проверить модель измерения (раздел 2) и матрицу [`data/role-competency-matrix.csv`](data/role-competency-matrix.csv).

## 8. Учёт замечаний экспертного бюро

В настоящей версии учтены замечания из «Защита РПД»:

- **DL-1.4** (а не DL-1.12) — основной индикатор темы CNN / ПР 10 / Кейс-задачи 2; **DL-1.12** — только для transfer learning.
- **DL-1.4 убран** из темы «Метрики классификации» (ПР 5).
- Баланс ПЗ: Раздел 1 = 8 ч; Раздел 2 = 22 ч; всего ПЗ = 30 ч (4 ч практической подготовки).
- Указаны целевая аудитория, роли КРМ (TADS — якорная), ожидаемые уровни (MF-1.2 — С; DL-1.x — Б) и входные/выходные уровни пререквизитов.
- Добавлена матрица «КИМ ↔ индикатор ↔ роль».

## 9. Команда

Состав и вклад участников — в [`team/README.md`](team/README.md).

## 10. Лицензия

CC BY 4.0 — см. [`LICENSE.md`](LICENSE.md). © ФГБОУ ВО РГАУ – МСХА им. К.А. Тимирязева, кафедра статистики и кибернетики, 2026.
