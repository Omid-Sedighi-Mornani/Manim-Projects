from manim import *
from Library.list_utils import ExtendedVGroup, ExtendedMathTex


class Boxes(VMobject):
    def __init__(
        self,
        row_buff: float = 0.15,
        column_buff: float = 0.15,
        show_labels=False,
        *args,
        **kwargs,
    ):
        width = kwargs.pop("width", 2)
        height = kwargs.pop("height", 2)
        side_length = kwargs.pop("side_length", 1)
        buff = kwargs.pop("buff", None)
        super().__init__(*args, **kwargs)

        if buff:
            row_buff = column_buff = buff

        box = Square(side_length=side_length, *args, **kwargs)

        self.box_group = ExtendedVGroup(
            *[
                ExtendedVGroup(*[box.copy() for _ in range(width)]).arrange(
                    RIGHT, buff=column_buff
                )
                for _ in range(height)
            ]
        ).arrange(DOWN, buff=row_buff)

        self.label_width = ExtendedMathTex(width, color=kwargs.get("color", WHITE))

        self.label_height = ExtendedMathTex(height, color=kwargs.get("color", WHITE))

        self.add(self.box_group)

        if show_labels:
            self.add_labels()

    def __getitem__(self, key):

        if isinstance(key, tuple) and len(key) == 2:
            row_idx, col_idx = key

            if isinstance(row_idx, slice) and isinstance(col_idx, slice):
                # 2D-Slice: VGroup aller angesprochenen Zellen
                return ExtendedVGroup(
                    *[cell for row in self.box_group[row_idx] for cell in row[col_idx]]
                )
            elif isinstance(row_idx, slice):
                # Ganze Spalte (vertikal): z. B. boxes[:, 0]
                return ExtendedVGroup(
                    *[row[col_idx] for row in self.box_group[row_idx]]
                )
            elif isinstance(col_idx, slice):
                # Ganze Zeile (horizontal): z. B. boxes[1, :]
                return ExtendedVGroup(*self.box_group[row_idx][col_idx])
            else:
                # Einzelnes Feld: z. B. boxes[1, 2]
                return self.box_group[row_idx][col_idx]

        # Zugriff mit nur einem Index (z. B. boxes[1])
        return self.box_group[key]

    def add_labels(self):
        self.label_width.next_to(self.box_group, direction=DOWN)
        self.label_height.next_to(self.box_group, direction=LEFT)
        self.add(self.label_height, self.label_width)

    def remove_labels(self):
        self.remove(self.label_height, self.label_width)

    def show_labels(self, *args, **kwargs):
        self.add_labels()
        return FadeIn(self.label_height, self.label_width, *args, **kwargs)

    def hide_labels(self, *args, **kwargs):
        self.remove_labels()
        return FadeOut(self.label_height, self.label_width, *args, **kwargs)
