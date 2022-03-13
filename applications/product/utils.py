from .models import Sku
from livesettings.functions import config_value


def display_featured(num_to_display=None, random_display=None):
    """
    Used by the index generic view to choose how the featured products are displayed.
    Items can be displayed randomly or all in order
    """
    if num_to_display is None:
        num_to_display = config_value('PRODUCT', 'NUM_DISPLAY')
    if random_display is None:
        random_display = config_value('PRODUCT','RANDOM_FEATURED')

    q = Sku.objects.all()
    if not random_display:
        return q[:num_to_display]
    else:
        return q.order_by('?')[:num_to_display]