import abc


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(abc.ABC, Hero):
    def __init__(self, base):
        super().__init__()
        self.base = base

    @abc.abstractmethod
    def get_positive_effects(self):
        return self.positive_effects

    @abc.abstractmethod
    def get_negative_effects(self):
        return self.negative_effects

    @abc.abstractmethod
    def get_stats(self):
        return self.stats


class AbstractNegative(AbstractEffect):
    @abc.abstractmethod
    def get_negative_effects(self):
        return self.base.negative_effects.copy()

    @abc.abstractmethod
    def get_stats(self):
        return self.base.stats.copy()

    def get_positive_effects(self):
        return self.base.get_positive_effects()


class AbstractPositive(AbstractEffect):
    @abc.abstractmethod
    def get_positive_effects(self):
        return self.base.positive_effects.copy()

    @abc.abstractmethod
    def get_stats(self):
        return self.base.stats.copy()

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class Berserk(AbstractPositive):
    def __init__(self, base):
        super().__init__(base)

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats["Strength"] += 7
        self.stats["Endurance"] += 7
        self.stats["Agility"] += 7
        self.stats["Luck"] += 7
        self.stats["Perception"] -= 3
        self.stats["Charisma"] -= 3
        self.stats["Intelligence"] -= 3
        self.stats["HP"] += 50
        return self.stats

    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        self.positive_effects.append("Berserk")
        return self.positive_effects


class Blessing(AbstractPositive):
    def __init__(self, base):
        super().__init__(base)

    def get_stats(self):
        self.stats = self.base.get_stats()
        for i in self.stats:
            if len(i) != 2:
                self.stats[i] += 2
        return self.stats

    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        self.positive_effects.append("Blessing")
        return self.positive_effects


class Weakness(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats["Strength"] -= 4
        self.stats["Endurance"] -= 4
        self.stats["Agility"] -= 4
        return self.stats

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append("Weakness")
        return self.negative_effects


class EvilEye(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats["Luck"] -= 10
        return self.stats

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append("EvilEye")
        return self.negative_effects

class Curse(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)

    def get_stats(self):
        self.stats = self.base.get_stats()
        for i in self.stats:
            if len(i) != 2:
                self.stats[i] -= 2
        return self.stats

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append("Curse")
        return self.negative_effects