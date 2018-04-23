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

Так как в цивилизации не может быть отрядов и объединений во второй части задания я реализовал класс карты "Map", который содержит информацию о карте, и выполняет запросы юнитов на действия. 

Кроме этого был реализован класс "Battle1v1" который является фасадом для управления дуэльной игрой. В нём реализованно общение между двумя сущьностями класса "Fraction" и классом "Map".

Фасад Battle1v1 инкапсулирует логику дуэльной игры и позволяет с лёгкостью управлять ею. 

Компоновщик не был неализован по той причине, что в цивилизации не может быть отрядов состоящих из нескольких юнитов, никакой иерархии не наблюдается

Единственное место где я мог использовать декоратор - создание разных видов тайлов, но и этот случай не подходил ведь в подклассах я не добавляю дополнительный фунционал а просто переопределяю некоторые поля

Так как все интерфейсы друг к другу подходят, адаптер тоже не пригодился


### 3 часть задания

    ...


### Текущее состояние проекта:

    Реализована часть игры в который происходит генерация объектов.
    ConCiv_exec в данный момент Содержит тесты, показывающие работоспособность
    написанной части, но в будующем этот файл будет запускать всю игру.

    Все игровые объекты ("City", "Unit"), будут управляться из внешнего класса игрового мира
