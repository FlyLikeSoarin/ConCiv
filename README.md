## Console Civilization


### Задание по предмету "Технологии програмирования"
### Репозиторий Вихрева Евгения, 797 группа


### Игровая модель

Это упрощённая, портированная в консоль sid meier's civilization.
Игра проходит на поле состоящем из квадратных тайлов, на этих клетка
при помощи поселенцев можно строить города, которые в свою очередь
могут строить боевых юнитов и поселенцев. Победа достигается захватов
всех городов на карте.


### 1 часть задания

Как часть первого задания будут созданы классы "City", "Unit" и "Fraction"

Эти классы содержат в себе ту часть игры где создаются новые объекты

Проще говоря, Фракция может создавать города, города могут создавать юнитов этой Фракции,
а юнит(поселенец) будет в будующем просить у поставить город в определённом месте


### 2 часть задания

    ...


### 3 часть задания

    ...


### Текущее состояние проекта:

    Реализована часть игры в который происходит генерация объектов.
    ConCiv_exec в данный момент Содержит тесты, показывающие работоспособность
    написанной части, но в будующем этот файл будет запускать всю игру.

    Все игровые объекты ("City", "Unit"), будут управляться из внешнего класса игрового мира