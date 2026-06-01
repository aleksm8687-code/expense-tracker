# Как выложить проект на GitHub

## Вариант через терминал

1. Создайте на GitHub новый пустой публичный репозиторий, например:

```text
expense-tracker
```

Важно: не добавляйте README, .gitignore и License через GitHub, потому что они уже есть в проекте.

2. В терминале откройте папку проекта:

```bash
cd expense-tracker
```

3. Подключите ваш GitHub-репозиторий:

```bash
git remote add origin https://github.com/ВАШ_ЛОГИН/expense-tracker.git
```

4. Отправьте основную ветку:

```bash
git push -u origin main
```

5. Отправьте учебные ветки:

```bash
git push -u origin feature/add-expense
```

```bash
git push -u origin feature/list-and-stats
```

```bash
git push -u origin feature/delete-expense
```

```bash
git push -u origin feature/tests
```

```bash
git push -u origin feature/date-validation
```

## Как сделать Issue и Pull Request

1. На GitHub откройте вкладку `Issues`.
2. Создайте первую задачу:

```text
Добавить проверку формата даты
```

3. Откройте вкладку `Pull requests`.
4. Нажмите `New pull request`.
5. Выберите:

```text
base: main
compare: feature/date-validation
```

6. В описании Pull Request напишите:

```text
Closes #1
```

Если номер Issue не `#1`, укажите свой номер, например `Closes #2`.

7. Нажмите `Create pull request`.
8. Нажмите `Merge pull request`.

После слияния Pull Request задача в Issues должна перейти в `Closed`.

## Команда для скрина графа коммитов

```bash
git log --oneline --graph --all
```
