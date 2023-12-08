#!/usr/bin/env python3
# coding=utf-8
#

import sys

import inkex
from inkex import PathElement
from inkex.localization import inkex_gettext as _

def draw_line(x1, y1, x2, y2, parent):
    """Draw an SVG line"""
    line = parent.add(PathElement())
    line.style = {"stroke": "#000000", "stroke-width": 5, "fill": "none"}
    line.path = "M {},{} L {},{}".format(x1, y1, x2, y2)


class Triangle(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--r", type=int, default=1, help="Количество раппортов")
        pars.add_argument("--r_h", type=float, default=100.0, help="Высота раппорта (px)")
        pars.add_argument("--r_w", type=float, default=100.0, help="Ширина раппорта (px)")

    def effect(self):
        tri = self.svg.get_current_layer()
        offset = self.svg.namedview.center
        X = 0
        for i in range (1, self.options.r + 1):
            height = self.options.r_h  # высота
            width = self.options.r_w  # ширина
            
            if i % 2 == 1:
                draw_line(X, 0, X + width, 0, tri)
                draw_line(X, 0, X, height, tri)
                draw_line(X, height, X + width, height, tri)

                draw_line(X + 0.5 * width, height / 4, X + width, height / 4, tri)
                draw_line(X + 0.5 * width, height / 4, X + 0.5 * width, height * 3 / 4, tri)
                draw_line(X + 0.5 * width, height * 3 / 4, X + width, height * 3 / 4, tri)

                draw_line(X + width, height / 3, X + width, height * 2 / 3 , tri)

            else:
                draw_line(X, 0, X + width, 0, tri)
                draw_line(X + width, 0, X + width, height, tri)
                draw_line(X, height, X + width, height, tri)

                draw_line(X + 0.5 * width, height / 4, X, height / 4, tri)
                draw_line(X + 0.5 * width, height / 4, X + 0.5 * width, height * 3 / 4, tri)
                draw_line(X + 0.5 * width, height * 3 / 4, X, height * 3 / 4, tri)

                draw_line(X, height / 3, X, height * 2 / 3 , tri)
            
            X = X + self.options.r_w + (self.options.r_w // 10)


if __name__ == "__main__":
    Triangle().run()
