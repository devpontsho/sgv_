__author__ = 'Pontsho Maseko'
__version__ = 1.0
__all__ = ['create_svg', 'write_svg']


def create_svg(data):

    """Create svg from data given.
    :param data: Dictionary with instructions to build svg.
    :return: None.
    """

    # Code
    svg_code = '<svg height="{Height}" width="{Width}">{Code}\n</svg>'

    # Objects to draws
    code = ''
    for key in data['draws']:
        
        # Dic
        dic = data['draws'][key]

        tags = ''
        for tag in dic:
            
            # Create style
            if tag == 'style':
                
                # Tag
                style_tag =  'style="'

                # For every style
                for style in dic['style']:
                    style_tag += '{Key}:{Value};'.format(Key=style, Value=dic['style'][style])

                # Add style tag to end
                tags += ' {}"'.format(style_tag)

            # Else other tags
            else:
                tags += ' {Key}="{Value}"'.format(Key=tag, Value=dic[tag])

        # Append to code
        code += '\n\t<{Key}{Tags} />'.format(Key = key, Tags=tags)

    # Add to the svg_code
    svg_code = svg_code.format(Height=data['height'], Width=data['width'], Code=code)

    # Write svg
    write_svg(svg_code, data['output'])


def write_svg(data, output=''):

    """Write out svg
    :param data: The svg code.
    :return: None.
    """

    with open(output, 'w') as f:
        f.write(data)

    print('SVG : {}'.format(output))