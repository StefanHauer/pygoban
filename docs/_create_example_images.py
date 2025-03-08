import pygoban
from pygoban import GobanMaker
import os

base_path = os.path.join(
    os.path.dirname(pygoban.__file__), "docs", "img"
)

g = GobanMaker(size=9)
g.create_svg_file(os.path.join(base_path, "goban_9x9.svg"))

g = GobanMaker(size=(8,5))
g.create_svg_file(os.path.join(base_path, "goban_8x5.svg"))

g = GobanMaker(
    size=(9,9),
    border_spacing=(28.,28.),
    x_annotation="latin_letters",
    y_annotation="arabic_numerals",
    font_size=8,
    font_face="Microsoft YaHei"
)
g.create_svg_file(os.path.join(base_path, "goban_9x9_annotated.svg"))

g = GobanMaker(
      size=(9,9),
      star_point_diameter=6,
      star_point_pos=2
)
g.create_svg_file(os.path.join(base_path, "goban_9x9_spm_at_2.svg"))

star_point_pos = [
    (2,2), (3,4)
]
g = GobanMaker(
      size=(9,9),
      star_point_diameter=6,
      star_point_pos=star_point_pos
)
g.create_svg_file(os.path.join(base_path, "goban_9x9_two_spm.svg"))

g = GobanMaker(
    size=(9,9),
    star_point_pos=3,
    star_point_diameter=10
)
g.create_svg_file(os.path.join(base_path, "goban_9x9_spm10mm.svg"))
