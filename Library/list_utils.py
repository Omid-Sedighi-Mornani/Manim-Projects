from manim import *
import re
import itertools as it


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
    def get_group_class(self):
        return ExtendedVGroup


class ExtendedMathTex(ExtendingGroupClass, MathTex):

    def _break_up_by_substrings(self):
        """
        Reorganize existing submobjects one layer
        deeper based on the structure of tex_strings (as a list
        of tex_strings)
        """
        new_submobjects = []
        curr_index = 0
        for tex_string in self.tex_strings:
            sub_tex_mob = ExtendedSingleStringMathTex(
                tex_string,
                tex_environment=self.tex_environment,
                tex_template=self.tex_template,
            )
            num_submobs = len(sub_tex_mob.submobjects)
            new_index = (
                curr_index + num_submobs + len("".join(self.arg_separator.split()))
            )
            if num_submobs == 0:
                last_submob_index = min(curr_index, len(self.submobjects) - 1)
                sub_tex_mob.move_to(self.submobjects[last_submob_index], RIGHT)
            else:
                sub_tex_mob.submobjects = self.submobjects[curr_index:new_index]
            new_submobjects.append(sub_tex_mob)
            curr_index = new_index
        self.submobjects = new_submobjects
        return self


class ExtendedText(ExtendingGroupClass, Text):
    pass


class ExtendedSingleStringMathTex(ExtendingGroupClass, SingleStringMathTex):
    pass
