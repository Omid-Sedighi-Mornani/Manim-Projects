from manim import Group, VGroup, MathTex
from typing import List
from operator import itemgetter


class ExtendingGroupClass:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def __getitem__(self, value):
        self_list = self.split()
        GroupClass = self.get_group_class()
        if isinstance(value, slice):
            return GroupClass(*self_list.__getitem__(value))

        if isinstance(value, list) or isinstance(value, tuple):
            return GroupClass(*[self_list.__getitem__(i) for i in value])

        return self_list.__getitem__(value)


class ExtendedGroup(ExtendingGroupClass, Group):
    pass


class ExtendedVGroup(ExtendingGroupClass, VGroup):
    pass


class ExtendedMathTex(ExtendingGroupClass, MathTex):
    pass
