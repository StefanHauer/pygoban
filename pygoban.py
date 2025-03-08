"""GobanMaker class to create scalable vector graphics files of Go boards.."""

import string
import math
import cairo
import cn2an

class GobanMaker:
    """Class to create svg files of Go boards using the cairo library.
    
    Attributes
    ----------
    size : tuple of two int, default=(9,9)
        Number of vertical and horizontal lines that make up the grid.
    line_widths : tuple of two float, default=(1.,2.)
        Line widths of the grid (thinner lines), and the border of the grid (thicker lines), both
        in mm.
    line_spacing : tuple of two float, default=(22., 23.7)
        Spacing between vertical and horizontal lines of the grid in mm.
    border_spacing : tuple of two float, default=(11.,12.)
        Spacing of the border in mm, i.e., the space outside the grid.
    star_point_diameter : float, default=4
        Diameter of the star point markers in mm.
    star_point_pos : list of tuples, default='auto'
        Grid points where to put star point markers. If 'auto', will try to put them in the
        3 $\times$ 3 corners on the center of the sides, and in the center, where possible.
    x_annotation : [None, 'arabic_numerals', 'chinese_numerals', 'latin_letters'], default=None
        Annotation style for the vertical grid lines.
    y_annotation : [None, 'arabic_numerals', 'chinese_numerals', 'latin_letters'], default=None
        Annotation style for the horizontal grid lines.
    font_face : str, default='Microsoft YaHei'
        Font face to use for the annotation of the vertical and horizontal grid lines.
    font_size : float, default=8
        Font size to use for the annotation of the vertical and horizontal grid lines.
    
    Examples
    --------

    >>> g = GobanMaker(
    ...    size=13
    ... )
    >>> g.create_svg_file('test.svg')

    >>> g = GobanMaker(
    ...    size=(9,5)
    ... )
    >>> g.create_svg_file('test.svg')
    """

    def __init__(
            self, *, size=(9,9),
            line_widths=(1.,2.),
            line_spacing=(22., 23.7),
            border_spacing=(11.,12.),
            star_point_diameter=4.,
            star_point_pos="auto",
            x_annotation=None,
            y_annotation=None,
            font_face="Microsoft YaHei",
            font_size=8
        ):
        self.set_board_size(size)
        self.set_line_widths(line_widths)
        self.set_line_spacing(line_spacing)
        self.set_border_spacing(border_spacing)
        self.set_grid_annotation_style(
            x_annotation=x_annotation,
            y_annotation=y_annotation
        )
        self.set_star_point_settings(star_point_pos, star_point_diameter)
        self.set_font_face(font_face)
        self.set_font_size(font_size)

    def set_board_size(self, size):
        """Set the size of the Go board.
        
        Parameters
        ----------
        size : int or tuple of ints
            Number of vertical and horizontal lines that make up the grid.

        Examples
        --------

        >>> g = GobanMaker()
        >>> g.set_board_size(9)
        >>> g.create_svg_file('test.svg')

        >>> g = GobanMaker()
        >>> g.set_board_size((13,12))
        >>> g.create_svg_file('test.svg')
        """
        if isinstance(size, int):
            size = (size,size)
        elif isinstance(size, tuple):
            if len(size)!=2:
                raise ValueError("Board size must be two-dimensional.")
            if not isinstance(size[0], int) or not isinstance(size[1], int):
                raise ValueError("Parameter size must be a tuple of integers.")
        else:
            raise ValueError("Parameter size may only be an int or a tuple.")
        self.size=size

    def set_line_widths(self, line_widths):
        """Set the line widths for the grid, and the border of the grid in mm.
        
        Parameters
        ----------
        line_widths : tuple of floats
            Line thickness in mm for the thinner grid lines and the thicker lines of the
            grid border.

        Examples
        --------

        >>> g = GobanMaker()
        >>> g.set_line_widths((1,2))
        >>> g.create_svg_file('test.svg')
        """
        line_widths = (min(line_widths), max(line_widths))
        self.line_widths=line_widths

    def set_star_point_settings(self, star_point_pos=None, star_point_diameter=None):
        """Set the settings of the star point markers.
        
        Parameters
        ----------
        star_point_pos : int, tuple or 'auto'.
            If set to 'auto', will create star points on the 4x4, center and
            4xcenter grid intersections. If an int n is specified, will put the
            star points on the nxn , center and nxcenter grid intersections.
            If a list of tuples is specified will create the point on only those
            points.
        star_point_diameter : float
            Diameter of the star point marker in mm.

        Examples
        --------

        >>> g = GobanMaker()
        >>> g.set_star_point_settings(star_point_pos=2)
        >>> g.create_svg_file('test.svg')

        >>> g.set_star_point_settings(star_point_pos=[(9,9)])
        >>> g.create_svg_file('test.svg')
        """
        if star_point_pos is not None:
            self.star_point_pos = star_point_pos
        if star_point_diameter is not None:
            self.star_point_diameter = star_point_diameter

    def set_line_spacing(self, line_spacing):
        """Set the distance between horizontal and vertical lines in mm.
        
        Parameters
        ----------
        line_spacing : float or tuple of two floats
            Spacing between grids in mm.

        >>> g = GobanMaker()
        >>> g.set_line_spacing((22.,23.))
        >>> g.create_svg_file('test.svg')
        """
        if isinstance(line_spacing, float):
            line_spacing = (line_spacing, line_spacing)
        elif isinstance(line_spacing, tuple):
            if len(line_spacing)!=2:
                raise ValueError("Parameter line_spacing must be a tuple of two values")
            if not isinstance(line_spacing[0], float) or not isinstance(line_spacing[1], float):
                raise ValueError("Parameter line_spacing must be a tuple of integers.")
        else:
            raise ValueError("Parameter line_spacing may only be a float or a tuple.")
        self.line_spacing=line_spacing

    def set_border_spacing(self, border_spacing):
        """Set the size of the border in mm.
        
        Parameters
        ----------
        border_spacing : float or tuple of two floats
            Spacing of border in mm.

        >>> g = GobanMaker()
        >>> g.set_border_spacing((28.,28.))
        >>> g.create_svg_file('test.svg')
        """
        if isinstance(border_spacing, float):
            border_spacing = (border_spacing, border_spacing)
        elif isinstance(border_spacing, tuple):
            if len(border_spacing)!=2:
                raise ValueError("Parameter border_spacing must be a tuple of two values")
            if not isinstance(border_spacing[0], float) or not isinstance(border_spacing[1], float):
                raise ValueError("Parameter border_spacing must be a tuple of integers.")
        else:
            raise ValueError("Parameter border_spacing may only be a float or a tuple.")
        self.border_spacing = border_spacing

    def set_grid_annotation_style(self, x_annotation=None, y_annotation=None, ):
        """Set the type of annotation for the x and the y grid, so either none,
        annotation with Arabic numerals, Chinese numerals, or Latin letters.
        
        Parameters
        ----------
        x_annotation : [None, "arabic_numerals", "chinese_numerals", "latin_letters"]
            Annotation of the x-axis, i.e., the player facing sides of the board.
        y_annotation : [None, "arabic_numerals", "chinese_numerals", "latin_letters"]
            Annotation of the y-axis, i.e., the left/right sides of the board.

        >>> g = GobanMaker()
        >>> g.set_grid_annotation_style(
        ...     x_annotation='arabic_numerals',
        ...     y_annotation='latin_letters'
        ... )
        >>> g.create_svg_file('test.svg')
        """
        legal_values = [None, "arabic_numerals", "chinese_numerals", "latin_letters"]
        if x_annotation in legal_values:
            self.x_annotation=x_annotation
        else:
            raise ValueError(f"Annotation must be one of {', '.join(legal_values)}.")
        if y_annotation in legal_values:
            self.y_annotation=y_annotation
        else:
            raise ValueError(f"Annotation must be one of {', '.join(legal_values)}.")

    def set_font_face(self, font_face):
        """Set font face.

        Parameters
        ----------
        font_face : str
            Name of the font to use.
        """
        self.font_face=font_face

    def set_font_size(self, font_size):
        """Set font size.
        
        Parameters
        ----------
        font_size : float
            Font size to use.

        >>> g = GobanMaker(
        ...     x_annotation="latin_letters"
        ... )
        >>> g.set_font_size(10)
        >>> g.create_svg_file('test.svg')
        """
        self.font_size=font_size

    def create_svg_file(self, file_path):
        """Make an svg file of the Go board according to the specified settings.
        
        Parameters
        ----------
        file_path : str
            Save path of the created svg file.    
        """
        board_width, board_height = self._get_board_dimensions()
        with cairo.SVGSurface(file_path, board_width, board_height) as surface:
            surface.set_document_unit(cairo.SVG_UNIT_MM)
            context = cairo.Context(surface)

            self._draw_grid(context)
            self._draw_star_points(context)
            self._draw_annotations(context)
            self._draw_border(context)

    def _get_board_dimensions(self):
        """Get the dimensions of the board in mm.
        
        Returns
        -------
        board_size : tuple of float
            Board width, and board height in mm.
        """
        board_size = (
            (self.size[0]-1)*self.line_spacing[0] + 2*self.border_spacing[0],
            (self.size[1]-1)*self.line_spacing[1] + 2*self.border_spacing[1]
        )
        return board_size

    def _draw_grid(self, context):
        """Draw the grid of the Go board.
        
        Parameters
        ----------
        context : cairo.Context
        """
        context.set_line_cap(cairo.LINE_CAP_ROUND)

        y_lower_border = self.border_spacing[1]
        y_upper_border = self.border_spacing[1] + (self.size[1]-1)*self.line_spacing[1]
        for vertical_lines in range(self.size[0]):
            x_pos = self.border_spacing[0] + vertical_lines*self.line_spacing[0]
            if vertical_lines in [0, self.size[0]-1]:
                current_line_width = self.line_widths[1]
            else:
                current_line_width = self.line_widths[0]
            context.set_line_width(current_line_width)
            context.move_to(x_pos,y_lower_border)
            context.line_to(x_pos,y_upper_border)
            context.stroke()

        x_lower_border = self.border_spacing[0]
        x_upper_border = self.border_spacing[0] + (self.size[0]-1)*self.line_spacing[0]
        for horizontal_lines in range(self.size[1]):
            y_pos = self.border_spacing[1] + horizontal_lines*self.line_spacing[1]
            if horizontal_lines in [0, self.size[1]-1]:
                current_line_width = self.line_widths[1]
            else:
                current_line_width = self.line_widths[0]
            context.set_line_width(current_line_width)
            context.move_to(x_lower_border, y_pos)
            context.line_to(x_upper_border, y_pos)
            context.stroke()

    def _draw_star_points(self, context):
        """Draw the dots at the grid intersections.
        
        Parameters
        ----------
        context : cairo.Context
        """
        context.set_line_cap(cairo.LINE_CAP_ROUND)

        if self.star_point_pos == "auto":
            star_point_pos = self._get_auto_star_point_pos()
        else:
            star_point_pos = self.star_point_pos

        for x_grid_pos, y_grid_pos in star_point_pos:
            x_pos = self.border_spacing[0] + self.line_spacing[0]*(x_grid_pos-1)
            y_pos = self.border_spacing[1] + self.line_spacing[1]*(y_grid_pos-1)
            context.set_line_width(4)
            context.move_to(x_pos, y_pos)
            context.line_to(x_pos, y_pos)
            context.stroke()

    def _get_auto_star_point_pos(self):
        """Automatically get the grid positions of the star point markers.
        Will do so on the (3,3) points (if possible), in the centerpoint (if possible),
        and on the centers of the sides (if possible).
        
        Returns
        -------
        star_point_pos : list of tuples
            List of tuples specifying the star points on the grid.
        """
        star_point_pos = []
        if self.size[0]>=3 and self.size[1]>=3:
            star_point_pos += [
                (3,3),
                (3, self.size[1]-2),
                (self.size[0]-2,3),
                (self.size[0]-2, self.size[1]-2)
            ]
            if self.size[0]%2!=0 and self.size[1]%2!=0:
                star_point_pos += [
                    (
                        (self.size[0]-1)/2 +1, (self.size[1]-1)/2 +1
                    )
                ]
            if self.size[0]%2!=0:
                x_middle_pos = (self.size[0]-1)/2 +1
                star_point_pos += [
                    (x_middle_pos,3),
                    (x_middle_pos, self.size[1]-2),
                ]
            if self.size[1]%2!=0:
                y_middle_pos = (self.size[1]-1)/2 +1
                star_point_pos += [
                    (3, y_middle_pos),
                    (self.size[1]-2, y_middle_pos),
                ]


        return star_point_pos

    def _draw_annotations(self, context):
        """Draw the annotations of the grid lines.
        
        Parameters
        ----------
        context : cairo.Context
        """
        context.select_font_face(self.font_face)
        context.set_font_size(self.font_size)

        center_factor = 0.3

        if self.x_annotation is not None:
            y_lower_border = self.border_spacing[1]*center_factor
            y_upper_border = (
                self.border_spacing[1]*(2-center_factor)
                + (self.size[1]-1)*self.line_spacing[1]
            )

            for vertical_lines in range(self.size[0]):
                s = self._get_annotation_string(vertical_lines, self.x_annotation)
                x_pos = self.border_spacing[0] + vertical_lines*self.line_spacing[0]

                pos = (x_pos,y_lower_border)
                self._add_text(context, s, pos, theta=math.pi)

                pos = (x_pos,y_upper_border)
                self._add_text(context, s, pos, theta=0)

        if self.y_annotation is not None:
            x_lower_border = self.border_spacing[0]*center_factor
            x_upper_border = (
                self.border_spacing[0]*(2-center_factor)
                + (self.size[0]-1)*self.line_spacing[0]
            )

            for horizontal_lines in range(self.size[1]):
                s = self._get_annotation_string(self.size[1]-horizontal_lines-1, self.y_annotation)
                y_pos = self.border_spacing[1] + horizontal_lines*self.line_spacing[1]

                pos = (x_lower_border, y_pos)
                self._add_text(context, s, pos)

                pos = (x_upper_border, y_pos)
                self._add_text(context, s, pos, theta=math.pi)

    @staticmethod
    def _get_annotation_string(index, annotation_style):
        """Return the string to annotate a grid line based on the line index
        and the annotation style.

        Parameters
        ----------
        index : int
            Index of the grid line
        annotation_style : str
            Name of the annotation style. Either 'arabic_numerals', 'latin_letters',
            or 'chinese_numerals'.
        
        Returns
        -------
        my_string : str
            String for the specified index.
        """
        if annotation_style == "arabic_numerals":
            my_string =  str(int(index+1))
        elif annotation_style == "latin_letters":
            my_string =  string.ascii_uppercase.replace("I", "")[index]
        elif annotation_style == "chinese_numerals":
            my_string =  cn2an.an2cn(index+1)
        else:
            raise ValueError(f"Unknown annotation style '{annotation_style}' specified.")
        return my_string

    @staticmethod
    def _add_text(context, my_text, pos, theta = 0.0):
        """Add rotatable text on the board, for instance, to annotate the grid.

        Parameters
        ----------
        context : cairo.Context
        my_text : str
            Text to put on the board.
        pos : tuple
            Position of the string in mm on the board
        theta : float
            Rotation in radians

        Notes:
        -----
        Shamelessly stolen from Stack Overflow:
        https://stackoverflow.com/questions/8463271/rotate-text-around-its-center-in-pycairo
        """
        context.save()

        fheight = context.font_extents()[2]
        x_off = context.text_extents(my_text)[0]
        tw = context.text_extents(my_text)[2]
        nx = -tw/2.0-x_off
        ny = fheight/3

        context.translate(pos[0], pos[1])
        context.rotate(theta)
        context.translate(nx, ny)
        context.move_to(0,0)
        context.show_text(my_text)
        context.restore()

    def _draw_border(self, context):
        """Draw the border of the board (not of the grid).
        
        Parameters
        ----------
        context : cairo.Context

        Notes
        -----
        The code for how to make a rectangle with rounded boarders I
        took from here: https://www.geeksforgeeks.org/pycairo-drawing-the-roundrect/
        """
        line_width = self.line_widths[1]
        x = line_width/2
        y = line_width/2
        width, height= self._get_board_dimensions()
        width -= line_width
        height -= line_width
        r = self.line_spacing[0]/3
        context.set_line_width(line_width)
        context.set_source_rgb(0, 0, 0)
        context.move_to(x, y+r)
        context.arc(x+r, y+r, r,
                    math.pi, 3*math.pi/2)

        context.arc(x+width-r, y+r, r,
                    3*math.pi/2, 0)

        context.arc(x+width-r, y+height-r,
                    r, 0, math.pi/2)

        context.arc(x+r, y+height-r, r,
                    math.pi/2, math.pi)

        context.close_path()
        context.stroke()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
